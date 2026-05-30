---
title: Claw Code Agent Runtime
created: 2026-05-18
updated: 2026-05-18
type: concept
tags: [ml, infra, coding, agent, tool]
sources: [raw/claw-code-runtime-analysis.md]
confidence: medium
---

# Claw Code Agent Runtime

## 核心定义

Claw Code 是一个开源 Rust 实现的 Agent harness（Anthropic 风格的 agent 执行框架）。其自我定位是 "humans set direction; claws perform the labor"——展示 clawhip / OmX / OmO 三件套协调下能跑出什么样的 harness。不是 Anthropic 官方闭源 Claude Code 本体，但理解原理对外推官方实现有参考价值。^[raw/claw-code-runtime-analysis.md]

## 主运行链路

1. **CLI 入口分发**：`parse_args` 区分一次性 prompt、交互式 REPL、slash command、本地命令（status/config/resume/skills/plugins）
2. **运行时装配**：`LiveCli` 把 system prompt、Session、GlobalToolRegistry、PermissionPolicy、plugin/MCP 状态、provider client 装配进 `ConversationRuntime`
3. **Run-turn 主循环**：LLM streaming → 解析 text/tool_use → hook + permission → 执行工具 → 写入 tool_result → 再次请求 LLM，直到模型不再输出 tool_use
4. **Context 组织**：system_prompt = Vec<String> + Session.messages = Vec<ConversationMessage>
5. **Agent 协同 = Tool 调用**：Agent 暴露为可调用工具，后台 `std::thread` 启动独立 `ConversationRuntime`

## 核心架构：ConversationRuntime

```
ConversationRuntime {
  session: Session,
  api_client: C,
  tool_executor: T,
  permission_policy: PermissionPolicy,
  system_prompt: Vec<String>,
  max_iterations: usize,
  hook_runner: HookRunner,
  usage_tracker: UsageTracker,
  auto_compaction_input_tokens_threshold: u32,  // 默认 100_000
}
```

每个 turn 结束后调用 `maybe_auto_compact`：input_tokens ≥ 100,000 时触发压缩。^[raw/claw-code-runtime-analysis.md]

## Context 组织

### System Prompt 十段模板

1. 身份 + output style
2. 通用系统行为约束
3. 任务执行规则
4. 工具/动作规范
5. `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` 分界标记
6. environment（Model family: Claude Opus 4.6、cwd、date、OS）
7. `render_project_context`（git status、git diff）
8. `render_instruction_files`（CLAUDE.md、.claw/CLAUDE.md，单文件上限 4000 字符，总上限 12000）
9. RuntimeConfig 摘要
10. append_sections（如 subagent 注入）

### Session Messages 模型

- MessageRole: System / User / Assistant / Tool
- ContentBlock: Text / ToolUse / ToolResult
- Session 同时支持 JSONL append 和完整 JSON 快照

### 自动压缩不变量

压缩时 `keep_from` 处的 ToolResult 如果第一个 block 是 tool result，边界会回退确保对应 ToolUse assistant message 同步保留——否则 OpenAI-compat provider 因孤立 tool 角色返回 400。^[raw/claw-code-runtime-analysis.md]

### Session Health Probe

压缩后下一个 turn 开头执行 non-destructive probe：用 `glob_search` 跑不可能匹配的 pattern（`*.health-check-probe-`），确认 tool_executor 仍可响应。失败则报错并提示 `/session new`。

## 工具体系

50 个 ToolSpec，分 8 类：文件/搜索、Shell/REPL、网络、工作流、Task/Worker、Team/Cron、LSP/MCP/远程、测试桩。^[raw/claw-code-runtime-analysis.md]

### 权限两级模型

| 层 | 内容 |
|---|---|
| Tool spec | `required_permission`：ReadOnly / WorkspaceWrite / DangerFullAccess |
| PermissionPolicy | active mode + allow/deny/ask rules + hook override + per-tool requirement |

授权优先级：deny rule → hook override → ask rule → allow rule/FullAccess mode → prompter → deny。

### Hook 三类

- `PreToolUse`：allow/deny/ask、改写 input、cancel、fail
- `PostToolUse`：成功后追加 messages、改判 error
- `PostToolUseFailure`：失败后追加诊断

## Agent 协同机制

将 `Agent` 暴露成 LLM 可调用的工具，由 LLM 决定何时调用，而非 harness 强制起多 agent。^[raw/claw-code-runtime-analysis.md]

执行过程：写入 `.clawd-agents/{id}.md` + manifest.json（status: running）→ `std::thread` 后台启动独立 ConversationRuntime → 受限工具白名单 + subagent system prompt → 无 prompter，不可交互式 ask user → 成功写 completed 状态。

子 agent 类型：explorer/plan/verify/general-purpose/claw-guide/statusline-setup。默认 max_iterations = 32。

## Provider 抽象

`ProviderClient` enum：Anthropic（Claude）、Xai（Grok）、OpenAi（GPT/通义/DashScope）。Prompt cache 仅 Anthropic 可用。

### Post-tool stall nudge

请求最后一条 message 是 ToolResult 时，带 stall timeout 的第一次流如果超时，自动重发完全相同的请求作为 "continuation nudge"，只重发一次。^[raw/claw-code-runtime-analysis.md]

## 与 OpenClaw 的关键差异

| 维度 | Claw Code | OpenClaw |
|------|-----------|----------|
| 语言 | Rust | TypeScript |
| Agent 协同 | Tool 调用 + 后台线程 | Gateway RPC 再入 + session 隔离 |
| 入口 | CLI 单一 | CLI + Gateway + Channel 多入口 |
| Context engine | 无（硬编码压缩逻辑） | 可插拔（legacy/插件 engine） |
| 压缩触发 | 单阈值（100K tokens） | 三类触发（overflow/timeout/手动） |
| 交付 | 终端输出 | Channel delivery（多平台） |

## 相关概念

- [[openclaw-runtime]] — OpenClaw Agent Runtime 分析
- [[ai-coding-agent]] — AI Coding Agent 工程方法论
- [[harness-engineering]] — 驾驭 Agent 的核心工程方法
- [[multi-agent-collaboration]] — 多 Agent 协作模式对比
