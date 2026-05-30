#!/usr/bin/env python3
"""
Wiki Incremental Build — Delta Detector & Builder

Usage:
  python wiki-delta.py scan          # Show delta without building
  python wiki-delta.py build         # Scan + output build plan for changed files
  python wiki-delta.py mark-built    # Mark specific files as built (after manual ingest)
  python wiki-delta.py init          # Initialize manifest from current state
  python wiki-delta.py stats         # Show manifest stats

The manifest (.build-manifest.json) tracks:
  - sha256 of each raw file's body content
  - Whether it's been built into wiki pages
  - Which wiki pages reference it
  - Last ingest date

On each run:
  1. Scan all raw files, compute body sha256
  2. Compare against manifest
  3. Output: new files, changed files, deleted files, unchanged files
  4. For build: output actionable plan with affected wiki pages
"""

import os
import sys
import json
import hashlib
import re
from datetime import datetime

WIKI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(WIKI, "raw")
MANIFEST_PATH = os.path.join(WIKI, ".build-manifest.json")


def compute_body_sha256(filepath):
    """Compute sha256 of body only (after frontmatter), matching SCHEMA convention."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        parts = content.split("---", 2)
        if len(parts) >= 3:
            body = parts[2]
        else:
            body = content
        return hashlib.sha256(body.encode("utf-8")).hexdigest()
    except Exception as e:
        return f"ERROR:{e}"


def scan_raw_files():
    """Walk raw/ and return {relative_path: sha256}."""
    result = {}
    for root, dirs, files in os.walk(RAW_DIR):
        # Skip assets directory (images etc)
        if os.path.basename(root) == "assets":
            continue
        for fname in files:
            if fname.endswith(".md"):
                fpath = os.path.join(root, fname)
                rel = os.path.relpath(fpath, WIKI)
                sha = compute_body_sha256(fpath)
                result[rel] = sha
    return result


def get_wiki_sources_by_basename():
    """Build map: raw_basename -> [wiki_pages]."""
    source_map = {}
    for subdir in ["entities", "concepts", "comparisons", "queries"]:
        dirpath = os.path.join(WIKI, subdir)
        if not os.path.isdir(dirpath):
            continue
        for fname in os.listdir(dirpath):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read(5000)
            except:
                continue
            m = re.search(r'sources:\s*\[(.*?)\]', content, re.DOTALL)
            if m:
                sources_str = m.group(1)
                sources = [s.strip().strip('"\'') for s in sources_str.split(",") if s.strip()]
                wiki_page = os.path.join(subdir, fname)
                for src in sources:
                    basename = os.path.basename(src)
                    if basename not in source_map:
                        source_map[basename] = []
                    if wiki_page not in source_map[basename]:
                        source_map[basename].append(wiki_page)
    return source_map


def load_manifest():
    if os.path.exists(MANIFEST_PATH):
        with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"version": 2, "last_build": None, "total_raw": 0, "files": {}}


def save_manifest(manifest):
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)


def compute_delta(manifest, current_files):
    """Compare current state vs manifest, return delta dict."""
    existing = manifest.get("files", {})
    
    new_files = []
    changed_files = []
    unchanged_files = []
    deleted_files = []
    
    for path, sha in current_files.items():
        if path not in existing:
            new_files.append(path)
        elif existing[path].get("sha256") != sha:
            changed_files.append({
                "path": path,
                "old_sha": existing[path].get("sha256", "?"),
                "new_sha": sha,
                "wiki_pages": existing[path].get("wiki_pages", [])
            })
        else:
            unchanged_files.append(path)
    
    for path in existing:
        if path not in current_files:
            deleted_files.append({
                "path": path,
                "sha256": existing[path].get("sha256", "?"),
                "wiki_pages": existing[path].get("wiki_pages", [])
            })
    
    return {
        "new": sorted(new_files),
        "changed": sorted(changed_files, key=lambda x: x["path"]),
        "deleted": sorted(deleted_files, key=lambda x: x["path"]),
        "unchanged_count": len(unchanged_files),
        "total": len(current_files)
    }


def cmd_scan():
    """Show delta without side effects."""
    manifest = load_manifest()
    current = scan_raw_files()
    delta = compute_delta(manifest, current)
    
    print(f"=== Wiki Delta Scan ===")
    print(f"Total raw files: {delta['total']}")
    print(f"Unchanged: {delta['unchanged_count']}")
    print(f"New: {len(delta['new'])}")
    print(f"Changed: {len(delta['changed'])}")
    print(f"Deleted: {len(delta['deleted'])}")
    
    if delta["new"]:
        print(f"\n--- NEW (need ingest) ---")
        for f in delta["new"]:
            print(f"  + {f}")
    
    if delta["changed"]:
        print(f"\n--- CHANGED (need re-ingest) ---")
        for f in delta["changed"]:
            pages_str = ", ".join(f["wiki_pages"]) if f["wiki_pages"] else "none"
            print(f"  ~ {f['path']}")
            print(f"    affects: {pages_str}")
    
    if delta["deleted"]:
        print(f"\n--- DELETED (wiki pages may need update) ---")
        for f in delta["deleted"]:
            pages_str = ", ".join(f["wiki_pages"]) if f["wiki_pages"] else "none"
            print(f"  - {f['path']}")
            print(f"    affects: {pages_str}")
    
    # Estimate token savings
    total = delta["total"]
    to_process = len(delta["new"]) + len(delta["changed"])
    if total > 0:
        savings_pct = (1 - to_process / total) * 100
        print(f"\n--- Token Estimate ---")
        print(f"Full rebuild: {total} files")
        print(f"Incremental: {to_process} files ({savings_pct:.0f}% savings)")


def cmd_build():
    """Output build plan for agent to execute."""
    manifest = load_manifest()
    current = scan_raw_files()
    delta = compute_delta(manifest, current)
    source_map = get_wiki_sources_by_basename()
    
    to_ingest = []  # Files needing new wiki pages
    to_update = []  # Files whose wiki pages need updating
    
    # New files: need fresh ingest
    for path in delta["new"]:
        basename = os.path.basename(path)
        to_ingest.append({
            "raw_path": path,
            "existing_wiki_pages": source_map.get(basename, [])
        })
    
    # Changed files: their wiki pages need re-processing
    for f in delta["changed"]:
        to_update.append({
            "raw_path": f["path"],
            "wiki_pages": f["wiki_pages"],
            "old_sha": f["old_sha"],
            "new_sha": f["new_sha"]
        })
    
    # Deleted files: their wiki pages lose a source
    deleted_impact = []
    for f in delta["deleted"]:
        if f["wiki_pages"]:
            deleted_impact.append({
                "raw_path": f["path"],
                "wiki_pages": f["wiki_pages"]
            })
    
    plan = {
        "action": "incremental_build",
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "stats": {
            "total_raw": delta["total"],
            "unchanged": delta["unchanged_count"],
            "to_ingest": len(to_ingest),
            "to_update": len(to_update),
            "deleted_with_impact": len(deleted_impact)
        },
        "ingest": to_ingest,
        "update": to_update,
        "deleted": deleted_impact
    }
    
    print(json.dumps(plan, ensure_ascii=False, indent=2))


def cmd_init():
    """Initialize manifest from current state, marking all referenced files as built."""
    current = scan_raw_files()
    source_map = get_wiki_sources_by_basename()
    now = datetime.now().strftime("%Y-%m-%d")
    
    manifest = {
        "version": 2,
        "last_build": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "total_raw": len(current),
        "files": {}
    }
    
    for path, sha in current.items():
        basename = os.path.basename(path)
        wiki_pages = source_map.get(basename, [])
        manifest["files"][path] = {
            "sha256": sha,
            "built": len(wiki_pages) > 0,
            "wiki_pages": wiki_pages,
            "last_ingested": now if wiki_pages else None
        }
    
    save_manifest(manifest)
    built = sum(1 for v in manifest["files"].values() if v["built"])
    unbuilt = sum(1 for v in manifest["files"].values() if not v["built"])
    print(f"Manifest initialized: {MANIFEST_PATH}")
    print(f"Total: {len(current)} | Built: {built} | Unbuilt: {unbuilt}")


def cmd_mark_built():
    """Mark files as built. Reads paths from stdin or args."""
    if len(sys.argv) < 3:
        # Read from stdin
        print("Enter raw paths to mark as built (one per line, Ctrl-D to end):")
        paths = [line.strip() for line in sys.stdin if line.strip()]
    else:
        paths = sys.argv[2:]
    
    manifest = load_manifest()
    now = datetime.now().strftime("%Y-%m-%d")
    marked = 0
    
    for path in paths:
        if path in manifest.get("files", {}):
            manifest["files"][path]["built"] = True
            manifest["files"][path]["last_ingested"] = now
            marked += 1
        else:
            print(f"Warning: {path} not in manifest, skipping")
    
    if marked > 0:
        manifest["last_build"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        save_manifest(manifest)
        print(f"Marked {marked} files as built")
    else:
        print("No files marked")


def cmd_stats():
    """Show manifest statistics."""
    manifest = load_manifest()
    files = manifest.get("files", {})
    
    built = sum(1 for v in files.values() if v.get("built"))
    unbuilt = sum(1 for v in files.values() if not v.get("built"))
    total_wiki_refs = sum(len(v.get("wiki_pages", [])) for v in files.values())
    
    # Size estimate
    total_size = 0
    for path in files:
        fpath = os.path.join(WIKI, path)
        if os.path.exists(fpath):
            total_size += os.path.getsize(fpath)
    
    print(f"=== Wiki Manifest Stats ===")
    print(f"Last build: {manifest.get('last_build', 'never')}")
    print(f"Total raw files: {len(files)}")
    print(f"Built (has wiki pages): {built}")
    print(f"Unbuilt (no wiki pages): {unbuilt}")
    print(f"Total wiki page references: {total_wiki_refs}")
    print(f"Total raw content size: {total_size / 1024:.0f} KB")
    print(f"Manifest file: {MANIFEST_PATH}")


def cmd_update_manifest():
    """Re-scan and update manifest sha256 values without changing built status."""
    manifest = load_manifest()
    current = scan_raw_files()
    source_map = get_wiki_sources_by_basename()
    
    # Update sha256 for existing entries, add new ones, remove deleted
    new_manifest = {
        "version": 2,
        "last_build": manifest.get("last_build"),
        "total_raw": len(current),
        "files": {}
    }
    
    for path, sha in current.items():
        basename = os.path.basename(path)
        wiki_pages = source_map.get(basename, [])
        
        if path in manifest.get("files", {}):
            # Preserve existing metadata
            old = manifest["files"][path]
            new_manifest["files"][path] = {
                "sha256": sha,  # Update to current
                "built": old.get("built", False),
                "wiki_pages": wiki_pages if wiki_pages else old.get("wiki_pages", []),
                "last_ingested": old.get("last_ingested")
            }
        else:
            # New file not in manifest
            new_manifest["files"][path] = {
                "sha256": sha,
                "built": len(wiki_pages) > 0,
                "wiki_pages": wiki_pages,
                "last_ingested": None
            }
    
    save_manifest(new_manifest)
    print(f"Manifest updated. Total: {len(current)} files")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)
    
    cmd = sys.argv[1]
    if cmd == "scan":
        cmd_scan()
    elif cmd == "build":
        cmd_build()
    elif cmd == "init":
        cmd_init()
    elif cmd == "mark-built":
        cmd_mark_built()
    elif cmd == "stats":
        cmd_stats()
    elif cmd == "update-manifest":
        cmd_update_manifest()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)
