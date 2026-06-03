---
title: Harness Engineering
created: 2026-04-24
updated: 2026-05-29
type: concept
tags: [infra, agent, coding]
sources: [raw/articles/Harness工程与领导力.md, raw/articles/Codex的多Agent并行开发指南.md, raw/articles/从 iproduct 重构到 harness 方法论：为什么 V1 应先做最小真实闭环.md, raw/articles/Karpathy 最新访谈：Vibe Coding 只是开始，真正重要的是 Agentic Engineering.md, raw/articles/一文读懂Harness Engineering：从14篇工程文章中，寻找那个让AI不再离经叛道的壳｜Hao好聊趋势.md, raw/articles/2026-05-27-需要自进化的不是Agent而是Harness.md]
confidence: high
---

# Harness Engineering

## 核心定义

Harness Engineering（驾驭工程）不是"把模型调得更聪明"，而是把模型外面的整套系统设计好：包括状态管理、工具定义、提示编排、执行编排、反馈闭环和可执行约束。在 OpenAI 的描述里，工程师的角色是"人负责设环境、定意图、建反馈，agent 负责执行"。^[
Harness工程与领导力.md
]

## 2026 年 Harness 认识更新：自进化的 Harness

从 LobeHub 的实践来看，Harness 的下一步不是仅仅作为被动执行环境，而是主动的自我进化系统。模型变得更强后，构建在其上的产品体验未必同步提升，因为缺失了一环：**产品本身能否随模型迭代、用户使用而自动进化**。^[2026-05-27-需要自进化的不是Agent而是Harness.md]

### Harness 作为 Agent 的操作系统层
如果把模型看作 CPU，上下文窗口像 RAM，Agent Harness 就接近操作系统。它管理启动过程、上下文、工具、错误和生命周期。Agent 则是跑在这套运行时之上的应用逻辑。

### 自进化的四个优化维度
1. **上下文策略**：Context Window 是有限资源，系统需要知道哪些信息该进入上下文，哪些可以延后，哪些应该压缩
2. **工具编排**：工具 schema 怎么设计、什么时候调用、失败后是否重试，只能在真实任务里暴露
3. **错误认知**：系统必须知道什么会出错。每出现一种新的错误模式，都是 Harness 对自己边界的一次更新
4. **模型适配**：不同 provider 的 API、限流、错误格式和边界行为都不一样，适配层需要持续学习

### Tracing：自进化的前置条件
没有完整 execution snapshot，系统无法归因、比较和优化。行业当前困境是主流 agent framework 的 tracing 多是后加能力而非 runtime 的一等公民：
- **LangChain**：callback 可选，忘了注册就丢 trace
- **CrewAI**：事件丢失导致 trace 断裂
- **OpenAI Agents**：需要显式创建 trace，不自动传播
- **AG2**：middleware 可选安装，不装就零 tracing

LobeHub 的做法是将 Agent Runtime 做成状态机和单步执行模型，每个 step 天然成为 trace event。Trace 就像 Harness 的黑匣子——本身不解决问题，但让问题第一次变得可以回放、归因和比较。^[2026-05-27-需要自进化的不是Agent而是Harness.md]

## 核心三件事 + 三项放大器

### 核心三件事

**1. 共享上下文 / 知识事实源**

OpenAI 的做法不是塞超长说明书给 agent，而是把 `docs/`、架构说明、执行计划、质量文档、技术债都和代码一起版本化，`AGENTS.md` 只做"目录"。看不见的知识 = 不存在。^[
Harness工程与领导力.md
]

**2. 验证—反馈闭环**

LangChain 的实验证明：模型不变，只改 harness，成绩也能明显提升。最有效的抓手是 traces、自验证、verification/scoring，以及围绕失败模式的持续迭代。^[
Harness工程与领导力.md
]

**3. 架构边界 / 强约束**

OpenAI 明确强调：**enforce invariants, not micromanage implementations**。不要事无巨细规定怎么写，而是把边界、依赖方向、层次结构和必要校验做成机械可执行的规则。这样 agent 才能快，但不至于把系统写散。^[
Harness工程与领导力.md
]

### 三项放大器

**4. 可观测性与系统可读性**
UI、日志、指标、trace，最好都直接暴露给 agent。Agent 才能自己复现 bug、验证修复、理解行为。^[
Harness工程与领导力.md
]

**5. 自治执行 + 升级机制**
成熟 harness 不是全自动乱跑，而是"能自主就自主，需判断时再升级给人"。只有遇到需要判断的问题时才升级给人。^[
Harness工程与领导力.md
]

**6. 熵管理 / 持续清理**
Agent 会复制仓库里已有的模式，好的坏的都会复制。必须做持续"垃圾回收"：定期扫描偏差、更新质量评分、发起定向重构 PR。^[
Harness工程与领导力.md
]

## V1 优先原则：最小真实闭环

AI 时代，面对历史包袱重、路径依赖强、局部修补成本持续升高的旧项目，**重构往往比修补更合理**。

判断系统是否值得继续修补，看这些骨架是否失效：
- 任务入口是否清晰
- 状态和上下文是否可组织
- 边界是否明确
- 失败后是否可定位、可恢复
- 结果是否可验证
- 系统是否适合持续迭代优化

V1 应优先串行闭环，**不要过早并行**。过早进入多 worktree、多 contract、多角色并行，团队大量时间会花在 debug 协同复杂度上。更稳妥的顺序：先做 single-threaded truth path，再做 parallel orchestration。^[
从 iproduct 重构到 harness 方法论：为什么 V1 应先做最小真实闭环.md
]

## Harness 与领导力的深层类比

| Harness Engineering | 领导力 |
|---------------------|--------|
| 给地图，而不是给口号 | 定方向、建原则、沉淀共同语境 |
| 约束不变量，而不是微观实现 | 设边界，不微操 |
| 搭平台让 agent 能做好工作 | 搭环境、长能力，让团队持续产出 |
| 看 trace/eval/测试/验证 | 看节奏/复盘/指标/问题闭环 |
| 授权，但保留升级通道 | 自主推进，判断时升级 |
| 持续 garbage collection | 持续反熵、原则固化 |

**核心相通之处**：能不能把目标、边界、信息、反馈和纠偏机制设计到位，让系统在你不盯着的时候也持续做对事。^[
Harness工程与领导力.md
]

## Karpathy 的 Agentic Engineering 视角

Karpathy 将 Agentic Engineering 定义为一种工程纪律：如何设计、协调、监督一组 AI Agent，让它们在不牺牲质量、安全、可维护性的情况下加速开发。^[
Karpathy 最新访谈：Vibe Coding 只是开始，真正重要的是 Agentic Engineering.md
]

### Agent 是 "spiky entities"

Agent 能力很强但会犯错、有随机性、不稳定。工程师的工作不是盲目信任，而是把它们放进合适的流程：让它们生成方案、写代码、跑测试、互相检查，让系统有边界、有验证、有回滚。

### 人必须负责 spec（规格）

- 所有资金和用户状态必须绑定到内部唯一用户 ID，而不是外部邮箱
- Agent 没有真正理解身份、支付和资金归属的风险
- 人的角色：顶层设计、约束条件、判断标准
- "细节可以外包，理解不能外包"

### 面试应重构

不再给算法题，而是让候选人做大项目（如 Twitter clone），然后用多个 Agent 去攻击它，看系统能否经得住。

## 相关概念

- [[ai-coding-agent]] — AI Coding Agent 工程全景
- [[declarative-architecture]] — 声明式架构也是一种 harness 思想
- [[ai-software-form-evolution]] — 软件形态演进中 harness 的角色
- [[multi-agent-collaboration]] — 多 Agent 协作的 harness 设计
- [[context-engineering]] — 上下文工程是 harness 的关键子系统
- [[expression-substance-framework]] — Expression-Substance 框架：Harness 就是软件工程中的 Substance 层
- [[musk-algorithm]] — 马斯克五步工作法：先删再减再优化的工程哲学
- [[elon-musk]] — Elon Musk 人物页
