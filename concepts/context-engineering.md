---
title: 上下文工程
created: 2026-05-22
updated: 2026-05-22
type: concept
tags: [ml, agent, coding]
sources: [raw/articles/有效的 Context 工程（精读、万字梳理）.md]
confidence: medium
---

# Context Engineering（上下文工程）

上下文工程是 Prompt Engineering 在 AI Agent 时代的自然演进。目标是以尽可能少且必要的 tokens，最大化 LLM 生成结果，引导模型输出期望行为。

## Prompt 工程 vs Context 工程

| 维度 | Prompt 工程 | Context 工程 |
|------|------------|-------------|
| 关注点 | 单轮 AI 交互的生成质量 | 多轮推理过程中动态优化整个上下文信息配置 |
| 范围 | System prompt 编写 | System prompt + Tools + MCP + 外部数据 + Message History |
| 适用场景 | 单次对话、简单任务 | Agent 长时间自主运行 |

Prompt 仍是 Context 工程的子集与基础。Context 工程是为适应 AI Agent 架构日趋复杂健全的自然发展。

## Context Rot（上下文腐烂）

最大上下文窗口 ≠ 最佳注意力窗口。Context Rot 指长上下文导致 LLM 性能显著下降的现象。

Chroma 团队的实验揭示了三大因素：

1. **注意力稀释**：Context 输入越长，模型注意力被稀释
2. **语义距离**：问题与关键信息的语义相似度越低，模型越难匹配答案
3. **干扰放大**：关键信息与周围干扰内容的语义相似度越高，模型越难分辨

三个因素会相互放大。即使是 1M 上下文的 Gemini 2.5 Pro，在 tokens 量达 4 万左右时推理就开始变慢、质量下降。

反过来，控制 Context 长度、减少干扰项、提升问题与有效信息的相似度，即可提升 Agent 处理效果。

## 三类核心策略

### 一、从写好 System Prompt 开始

- **启发式引导**：足够灵活地为模型提供启发，既具体又能泛化
- **结构化提示**：使用 XML 标签或 Markdown 语法分割不同指导作用的提示词
- **先用聪明模型写最小化提示**：定义「有什么、做什么」而非「怎么做」
- **精选最小可行的 Agent 工具集**：工具应自包含、能被 LLM 充分理解、功能重叠少
- **谨慎使用 few-shot**：避免过度 few-shot 导致风格僵化

### 二、即时上下文（Just-in-Time Context）

让 Agent 像人一样「整体回忆 → 深入回顾 → 推理」。Agent 自主导航与检索信息，动态获取所需内容到上下文窗口。

如 Cursor 先翻阅 README.md 了解项目结构 → 到对应目录找代码。即使是每次检索获取的文件名、大小、创建时间，也有助于后续推理判断信息的相关性。

### 三、为超长程任务实现无限上下文

1. **压缩（Compaction）**：在上下文接近窗口限制时，有损压缩对话内容，保留核心决策与细节，丢弃冗余
2. **结构化笔记（Structured Note-taking）**：Agent 定期把重要记忆写入外部笔记文件，按需拉回上下文
3. **多智能体架构（Multi-Agents）**：分而治之，专门 Agent 专注于自己的任务与记忆空间，主 Agent 协调整体计划

可根据 Agent 应用类型灵活组合使用。

## Anthropic 的 Agentic Systems 分类

- **Workflow**：LLM 和工具通过代码预编排执行路径（Prompt Chaining、Routing、Parallelization、Orchestrator-Workers、Evaluator-Optimizer）
- **Agent**：LLM 在循环中自主使用工具，能理解复杂输入、推理规划、从错误中恢复

最小化设计原则：从简单提示与优秀模型开始，只有智能不足时才考虑调优工程。

## 相关概念

- [[ai-coding-agent]] — AI Coding Agent 工程方法论
- [[agent-memory]] — Agent 记忆系统
- [[agent-skills]] — Agent Skills
- Context Rot — 上下文腐烂现象（待深入研究）
- [[multi-agent-collaboration]] — 多 Agent 协作模式
- [[agent-routine-loop]] — Routine/Loop 模式下 Agent 自主检索上下文

## 方向转变：从塞上下文到给途径

Anthropic 内部观察到上下文工程的新方向：从"精心塞上下文"转向"给 Agent 获取上下文的途径"——减少微观管理，让模型自行拉取必要信息。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

这与此前的 Just-in-Time Context 策略一脉相承，但更进一步：不仅是"动态获取"，而是让 Agent 具备可追溯的上下文入口（如 `CLAUDE.md`、skill 文件、项目文档），自主决定何时及如何检索信息，而非由人微观管理全部背景。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]
