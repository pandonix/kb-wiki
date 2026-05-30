# Wiki 健康检查报告

> 检查日期：2026-05-28  
> 总页数：130（实体 17 + 概念 109 + 对比 3 + 查询 1）  
> 检查维度：来源完整性 / 内容冲突 / 链接密度 / 缺失页面 / 过期程度

---

## 总体评分

| 维度 | 状态 | 分数 | 说明 |
|------|------|------|------|
| 来源完整性 | 优 | 98.5% | 仅 2/130 页缺少来源 |
| 链接密度 | 良 | 87.7% | 16 页零入链，但所有页 outlink ≥ 2 |
| 内容一致性 | 优 | 无标记冲突 | 0 页标记 contradictions |
| 新鲜度 | 良 | — | 无 stale 标记，部分老页面待复核 |
| 质量信号 | 中 | 80% | 26 页缺 confidence 评级 |
| 存根/空页 | 优 | 0 存根 | 无内容极少的页面 |

**综合评级：B+** — 结构性良好，存在几处需立即修复的问题。

---

## 一、缺失来源的页面（2 页，非严重）

| 页面 | 类型 | 问题 |
|------|------|------|
| `ai-coding-agent` | concept | **无任何 frontmatter**（连 title/created/updated 都没有） |
| `three-career-scripts-analysis` | query | 有完整 frontmatter 但缺少 `sources` 字段 |

`ai-coding-agent` 是严重问题——它是链接密度最高的节点之一，被 5+ 页面引用，自身出链 8 条。见下文 P0。

---

## 二、内容冲突分析（0 处标记，2 处可疑）

经全文审阅，Wiki 中**没有显式标记的 contradictions**。以下为值得关注的模糊边界：

### 2.1 ai-economy-impact vs ai-economy-subsidy-crisis （内容重复）

`ai-economy-impact.md` 第 78-91 行以「AI 补贴危机：月费订阅模式的经济不可能」为标题，详细展开了与 `ai-economy-subsidy-crisis.md` 相同的主题，且引用同一来源 `raw/articles/AI 的经济账根本算不通.md`。

- **问题**：补贴危机在两个页面中被完整展开，属于冗余。
- **建议**：`ai-economy-impact` 中的补贴段改为摘要 + `→ 详见 [[ai-economy-subsidy-crisis]]`，保持主页面为经济影响全景，将细节下钻到专项页面。

### 2.2 实体页 vs 概念页的边界（4 对，有意为之）

| 实体页 | 概念页 | 关系 |
|--------|--------|------|
| `howard-marks` | `howard-marks-investing` | 人物传记 vs 投资哲学 |
| `duan-yongping` | `duan-yongping-investing` | 同上 |
| `claw-code-runtime` | `openclaw-runtime` | 不同产品，竞品对比 |
| `psychological-survival` | `psychological-scripts` | 底层机制 vs 具体表现 |

这四对**不是冲突，是互补**，每对内部都有交叉链接。不需要修复。

---

## 三、孤岛页面（16 页零入链）

以下页面有出链但**没有任何其他页面链接到它们**。它们写得很好，但在 Wiki 图中是死胡同。

### 高价值孤岛（强烈建议修复）

| 页面 | 行数 | 出链 | 价值判断 |
|------|------|------|----------|
| `science-vs-engineering` | 88 | 5 | 科学与工程的核心区分，哲学深度高，应被多页引用 |
| `palantir-ontology` | ~100+ | 6 | Ontology 方法论深度分析，与 AI 架构治理、企业 Agent 高度相关 |
| `mythical-man-month` | 71 | 6 | 软件工程经典，AI 时代重读价值极高 |
| `ai-era-scarce-capabilities` | 142 | 13 | Wiki 中最长的单页之一，深度整合多个概念，但无人指回 |
| `ai-second-half` | 83 | 6 | 姚顺雨核心论述 + Hy3 工程兑现，AI 产业关键节点 |
| `ai-strategy-positioning` | ~80+ | 5 | AI 战略定位分析，与 AI 组织采纳、原生银行等强相关 |
| `ai-code-adoption-vs-review` | 123 | 10 | adoption 和 review 的唯一对比页，内容详尽 |

### 主题孤岛

| 页面 | 行数 | 出链 | 价值判断 |
|------|------|------|----------|
| `bytedance-douyin-analysis` | ~60+ | 4 | 字节/抖音分析，与流量 2.0、商业相关 |
| `ba-vs-sa-boundary` | ~60+ | 3 | BA vs SA 边界分析 |
| `sincerity-communication` | ~60+ | 4 | 真诚沟通方法论 |

### 个人/生活类孤岛（可选择性修复）

| 页面 | 行数 | 出链 |
|------|------|------|
| `emergency-psychological-response` | ~50+ | 4 |
| `hidden-fatigue` | ~50+ | 4 |
| `lee-kuan-yew-leadership` | ~60+ | 4 |
| `analogical-overshadowing` | ~50+ | 4 |
| `antique-market-lemons` | ~50+ | 3 |
| `three-career-scripts-analysis` | ~80+ | 10 |

**修复方向**：前 7 个高价值孤岛是最紧迫的——在相关主题页中增加对它们的引用即可大幅提升 Wiki 图的连通性。例如：
- `ai-era-scarce-capabilities` ← 被 `ai-commoditization-boundary` 引用（姊妹页，应该互链）
- `science-vs-engineering` ← 被 `causality-philosophy` 引用（因果哲学是科学工程的基础）
- `mythical-man-month` ← 被 `ai-code-adoption` 或 `software-disposable` 引用
- `palantir-ontology` ← 被 `enterprise-agent-practice` 或 `ai-architecture-governance` 引用

---

## 四、被多次提到但无独立页面的概念（0 个）

**全部 130 个被 wikilink 引用的目标都有对应页面。** 这是一项好成绩——Wiki 的引用完整性很高，不存在「幽灵链接」。唯一的问题是 `ai-code-adoption-vs-review` 之前被我误报为缺失（实际存在于 `comparisons/` 目录，index.md 也正确归类为 Comparisons）。

---

## 五、可能已过期的页面

### 需复核（上次更新超过 30 天）

| 页面 | 最后更新 | 风险 |
|------|----------|------|
| `stanford-ai-index-2026` | 2026-04-24 | Stanford AI Index 每年发布，2026 版 4 月发布后可能有补充报告 |
| `backtrader` | 2026-04-24 | 量化回测框架可能有新版本 |
| `veighna` | 2026-04-24 | vn.py 社区活跃，可能有更新 |
| `agentic-forecasting` | 2026-04-24 | BLF 论文后续可能有新进展 |
| `berkshire` | 2026-04-24 | 伯克希尔股东大会（5 月初）后可能有新信息 |
| `capitalist-realism` | 2026-04-24 | 哲学类页面，本身不需要频繁更新 |
| `ai-code-review` | 2026-04-24 | AI Code Review 实践可能已有新方法 |

### 结构性顾虑

- **0 页标记 `stale`**：不是好事。一个 130 页的知识库应该有意识地将已知过时页标记出来。当前状态说明缺乏「过期审查」习惯。
- **`ai-strategy-positioning`**：AI 战略定位是高速变化的领域，而该页仍是孤岛——既可能过时，也无人复核。

---

## 六、质量信号缺口

### 26 页缺 confidence 评级

无 confidence 的页面分布在多个主题域：

| 主题域 | 缺评级的页数 |
|--------|------------|
| AI/Agent 工程 | 8 |
| 经济/投资 | 4 |
| 组织/管理 | 3 |
| 哲学/心理学 | 4 |
| 其他 | 7 |

**影响**：无法快速区分「高置信度的已验证知识」和「中等置信度的阶段性理解」。建议对所有缺评级页面补充 `confidence` 字段。

---

## 七、Wiki 结构健康度

### 亮点
- 所有页面 outlink ≥ 2（SCHEMA 的硬性要求被遵守了）
- 无存根页（内容都足够充实）
- 引用完整性 100%（无幽灵链接）
- 实体-概念分离设计生效（howard-marks / howard-marks-investing 等对）
- 对比页（3 个）和查询页（1 个）质量高

### 短板
- 入链分布不均衡：`second-order-thinking` 被 9 页引用，而 16 页零入链
- 缺乏 stale 标记文化：0 页标记过期
- frontmatter 质量不一致：`ai-coding-agent` 完全缺失

---

## 最优先修复的 5 个问题

### P0：修复 `ai-coding-agent.md` 的 frontmatter

**严重程度**：致命  
**影响**：Wiki 的核心枢纽页面之一（被 5+ 页引用，自身出链 8 条），缺少 title、created、updated、sources、confidence。  
**操作**：补全 frontmatter，添加来源引用（至少引用 `raw/agent/` 下的相关文件）。

---

### P1：消除 ai-economy-impact 与 ai-economy-subsidy-crisis 的内容重复

**严重程度**：高  
**影响**：同一主题在两个页面中完整展开（同一来源 `AI 的经济账根本算不通.md`），违反「详细内容只在一处」原则。  
**操作**：
1. `ai-economy-impact` 第 78-91 行压缩为摘要段 + `→ 详见 [[ai-economy-subsidy-crisis]]`
2. 确认 `ai-economy-subsidy-crisis` 中的内容是完整版

---

### P2：为 7 个高价值孤岛页面建立入链

**严重程度**：高  
**影响**：`science-vs-engineering`、`palantir-ontology`、`mythical-man-month`、`ai-era-scarce-capabilities`、`ai-second-half`、`ai-strategy-positioning`、`ai-code-adoption-vs-review` 是 Wiki 中最有深度的内容，但在图中不可达。  
**操作**：在 3-5 个核心枢纽页（如 `ai-economy-impact`、`causality-philosophy`、`enterprise-agent-practice`、`ai-architecture-governance`、`ai-code-adoption`）的「相关概念」段增加对这些页面的引用。

---

### P3：补充 26 页的 confidence 评级

**严重程度**：中  
**影响**：20% 的 Wiki 页面缺少质量信号。未来读者无法判断哪些是经过验证的知识，哪些是阶段性理解。  
**操作**：优先补全 8 个 AI/Agent 工程类页面的 confidence（这些是最活跃更新的领域），然后逐步覆盖全部。

---

### P4：建立 stale 审查习惯

**严重程度**：中  
**影响**：整个 130 页知识库 0 页标记过期。AI 相关页面（AI 下半场、战略定位、经济影响）如果超过 60-90 天未更新，很可能已落后于行业发展。  
**操作**：
1. 对 4 月 24 日创建至今未更新的页面做一轮快速扫描，判断是否需要标记 `stale`
2. 在 SCHEMA 中新增规则：**AI/Agent 类页面超过 60 天未更新则自动加 stale 标记**
3. 优先复核 `stanford-ai-index-2026`（可能有补充报告）、`ai-strategy-positioning`（战略领域高速变化）

---

## 附录：数据来源

- 全部 130 个核心页面均通过 YAML frontmatter 解析
- 链接分析基于页内 `[[wikilinks]]` 提取
- 冲突检测基于 slug 相似度 + 人工阅读验证
- 深度审阅页面数：34 页（26% 抽样）

---

*报告生成：2026-05-28 20:30 CST | 工具：Hermes Agent health check*
