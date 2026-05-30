---
title: Expression-Substance 框架：AI 的边界与人的不可替代性
created: 2026-05-30
updated: 2026-05-30
type: concept
tags: [philosophy, ml, agent, thought, writing, coding]
confidence: high
sources:
  - concepts/ai-alignment.md
  - concepts/ai-writing-flavor.md
  - concepts/ai-commoditization-boundary.md
  - concepts/harness-engineering.md
  - concepts/ai-code-review.md
  - concepts/big-v-prose-writing.md
  - concepts/outsourcing-thinking-ai.md
  - queries/wechat-moat-ai-era.md
  - queries/ai-writing-literary-mistake.md
---

# Expression-Substance 框架：AI 的边界与人的不可替代性

## 核心定义

**Expression-Substance 框架** 是一个跨领域的人机协作模型：AI 在 Expression（表达/执行）层拥有压倒性优势，但在 Intent（意图）和 Substance（实质/真实材料）层存在结构性缺陷。AI 能否产生价值，不取决于它有多强，而取决于**人是否守住了 Intent 和 Substance 这两端**。

> AI 做加速器，不讓 AI 做方向盘。—— [[ai-alignment]]

## 三层模型

| 层次 | 定义 | AI 能力 | 人的角色 | 外包风险 |
|------|------|---------|---------|---------|
| **Intent**（意图） | 为什么做、为谁做、做到什么程度 | 不能自发产生，只能被赋予 | 终极决策者 | 外包 = 在写/做别人的东西 |
| **Substance**（实质） | 真实材料、具体经验、独特立场 | 无生命出处，只能重组已有 | 唯一供给者 | 外包 = 产出没有根基 |
| **Expression**（表达） | 编码、润色、生成、执行 | 碾压级优势 | 导演/审查者 | 外包 = 本来就该外包 |

### 为什么这个分层成立

Intelligence as a Service 时代的核心不对称：

1. **AI 消灭的是复制成本，不是稀缺性本身**（[[desire-scarcity-migration]]）。Expression 的本质是「复制和重组已有的表达模式」——这是 AI 最擅长的。但 Intent（「我想说什么」）和 Substance（「我真的经历过什么」）是不可复制的。

2. **细节可以外包，理解不能外包**（[[harness-engineering]] 中 Karpathy 的判断）。AI 可以生成看起来完美的输出，但它不理解输出的含义——它只能预测「下一个最可能的 token」，不能判断「这个 token 对不对」。

3. **AI 能完成任务，不能承担责任**（[[ai-commoditization-boundary]]）。任何涉及「出了问题谁负责」的场景，责任必须由人承载。Intent 层是责任的起点：谁设定的目标，谁就对结果负责。

## 跨领域对应

框架的价值在于它跨软件工程、文学写作、组织管理等多领域成立：

### 软件工程

| 层次 | 含义 | 范例 |
|------|------|------|
| Intent | 架构设计、需求定义、判断标准 | Karpathy：「人负责设环境、定意图、建反馈」[[harness-engineering]] |
| Substance | 业务逻辑、组织上下文、历史约束 | AI 缺少「默认上下文」→ 采纳率仅 30% [[ai-code-adoption]] |
| Expression | 编写代码、生成测试、执行任务 | AI 可承担 80-90% 编码 [[ai-coding-agent]] |

**风险场景**：Vibe Coding（全自动开发）——Intent 和 Substance 都不在人手里 → 代码存活率 44.3%，漏洞速率 9x [[copilot-learning]]。

**治理框架**：Adoption（注入 Substance）+ Review（守住 Intent）= 完整质量控制环 [[ai-code-adoption-vs-review]]。

### 文学写作

| 层次 | 含义 | 范例 |
|------|------|------|
| Intent | 立意、审美、为谁写、想达成什么 | 导演-演员模型中「导演」的角色 [[ai-alignment]] |
| Substance | 真实经历、具体细节、独特立场 | 「凌晨两点看错题本的细节」→ AI 味立刻下降 [[ai-writing-flavor]] |
| Expression | 语言组织、润色、多版本生成 | AI 擅长「像很多人都可能写出来的话」[[ai-writing-flavor]] |

**风险场景**：全面代写——不提供真实材料、不守住审美立场 → 作者缺席、文字被熨平、LLM 均值回归。

**治理框架**：给真实材料而非抽象话题 + 导演-演员协作模型。

### 社交平台护城河

| 层次 | 含义 | 范例 |
|------|------|------|
| Intent | 「我想和这个真实的人发生连接」 | 微信的四层关系链中第三四层 [[wechat-relationship-chain-value]] |
| Substance | 「对方真的是一个有意识的、可信任的人」 | AI 不能提供 co-presence（共同在场感）[[wechat-relationship-chain-value]] |
| Expression | 信息传递、工具服务 | AI 生态侵蚀公众号/小程序生态 |

**风险场景**：AI 替代社交的 Expression 层（信息分发），但无法触及 Intent/Substance 层（信任承载、身份建构）。

## 框架的通用判断公式

对于任何「AI 能不能替代 X」的问题，用三个问题拆解：

1. **Intent 归谁？** —— 谁设定目标、定义成功、为结果负责？如果这个角色是人，AI 就是加速器。
2. **Substance 从哪来？** —— 核心输入是人的真实经验/组织上下文/独特审美，还是公共领域可获取的信息？前者意味着人的不可替代。
3. **Expression 是否可分离？** —— 执行层是否能从意图和实质层干净地剥离？如果能，AI 在这里是最佳选择。

**如果三个问题里有两个以上指向「人不可或缺」，那么这个领域就不会被 AI 替代——但会被 AI 重塑。**

## 与「导演-演员」模型的关系

Expression-Substance 框架是 [[ai-alignment]] 中「导演-演员」模型的底层理论抽象：

- 「导演」= Intent 层 + Substance 层 —— 设定意图、决定审美、把控结局、提供真实材料
- 「演员」= Expression 层 —— 负责高难度表演、适应不同风格、不知疲倦重拍

框架比模型更抽象，因此更可迁移：软件工程的「架构守护者」、写作的「导演」、社交平台的「信任锚点」——三者是同一结构在不同领域的投影。

## 与「护城河精炼」的关系

Expression-Substance 框架为两次 Wiki 交叉分析提供了统一的底层解释：

- [[wechat-moat-ai-era]] 的结论：微信护城河被「精炼」——Expression 层（信息分发/服务发现）被侵蚀，Intent/Substance 层（信任承载/身份建构）被强化。
- [[ai-writing-literary-mistake]] 的结论：AI 写作不是文学史最大错误——Expression 层外包无害甚至有益，Intent/Substance 层外包才是灾难。

**核心洞察**：AI 对不同领域的冲击表面各异，但底层遵循同一规律——冲击 Expression 层，暴露 Substance 层的稀缺性。谁能在 Substance 层建立起不可替代的壁垒，谁就能在 AI 时代保持不可替代性。

## 相关概念

- [[ai-alignment]] — 导演-演员模型的理论来源
- [[ai-writing-flavor]] — AI 味的三层结构：Expression 层可以去掉 AI 味，Substance 层才能消灭它
- [[ai-commoditization-boundary]] — Expression-Substance 框架的经济学底座：商品化梯度
- [[harness-engineering]] — 软件工程中的 Expression-Substance 实践
- [[ai-code-review]] — 守住 Intent 的审计系统
- [[big-v-prose-writing]] — 散文写作中的 Substance（生命出处）论证
- [[outsourcing-thinking-ai]] — Intent 外包的危险
- [[desire-scarcity-migration]] — Substance 层稀缺性升值的底层机制
- [[wechat-relationship-chain-value]] — 社交平台中的 Expression-Substance 对应
