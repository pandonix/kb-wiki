---
title: Anthropic
created: 2026-06-08
updated: 2026-07-11
type: entity
tags: [company, ml, agent, alignment, coding]
sources: [raw/articles/Claude Code之父：品味不是人类护城河；当工程师不再写代码，招聘看什么？.md, raw/articles/AI 时代的架构治理.md, raw/articles/2026-07-10-AI公司为何把哲学家请进实验室.md]
confidence: medium
---

# Anthropic

## 概述

Anthropic 是一家以 **AI Safety（AI 安全）** 为核心使命的 AI 研究公司，由前 OpenAI 成员创立。其核心产品包括 Claude 系列模型和 Claude Code 编程 Agent。

## 核心理念

> 如果在 Anthropic 的办公室里随机拦下一名员工，问他为什么来到这里，大概率得到的答案都会是同一个：AI Safety。

Boris Cherny 指出，Anthropic 从成立开始最核心的使命一直是 AI 安全。无论是可解释性研究、对齐研究还是其他安全方向，本质上都在试图理解模型的行为。^[raw/articles/Claude Code之父：品味不是人类护城河；当工程师不再写代码，招聘看什么？.md]

## Coding 的战略意义

对 Anthropic 而言，Coding 不只是商业市场。编程拥有**极其清晰的反馈机制**——代码能否运行、能否通过测试、编译能否成功，答案非常明确。这让 Coding 成为研究 Tool Use、Computer Use 和 AI Safety 的**理想实验场**。

## Claude Code 的演进

- 起源于 Anthropic Labs Team 对 coding agent 的探索（2024 年底）
- 早期只能完成 Boris 约 10%-20% 的工作
- 真正跃迁来自底层模型能力提升（Sonnet 4 → Opus 4 → Opus 4.5）
- 从 CLI → 桌面端/移动端/Slack/GitHub 等多场景扩展
- 产品和模型在同一个循环里共同演化——全公司都在用 Claude Code

### 一周年：两次认知跃迁（2026.6）

上线一年后，Anthropic 内部经历了两次认知跃迁：^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

1. **第一次**：工程师意识到不必亲手写代码，可以用自然语言让 Agent 写代码
2. **第二次**：工程师不再直接对话单个 Agent，而是通过 loop、routine、agent view、remote control 等机制调度一批 Agent——Boris 的工作方式变成用一个 Agent 驱动一批 Agent，再由这些拆出更多 Agent，形成树状并行任务结构
3. **第三次（进行中）**：Agent 运行时间更长、自主性更强、并发数量更大

### Routine / Loop 模式
工程师可以让 Claude Code Agent 常驻监听 GitHub issue、bug 反馈、CI、review、rebase 等事件，满足规则后自动修复、提交 PR、通知 owner。这代表了从"人驱动 Agent"到"Agent 主动运作"的质变。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

### Auto Mode 安全逻辑
不要让人审批每一个工具调用，而是用另一个模型筛选风险，把人的注意力集中到真正重要的请求上。这被认为比大量弹窗式人工确认更安全。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

### 跨职能扩散
Claude Code 使用已跨出工程团队：设计师改代码、产品经理改功能、财务团队做预测、数据科学家当标配工具。代码执行能力开始把产品、设计、财务、工程等角色边界拉近。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

## 组织文化

### Member of Technical Staff（MTS）

Anthropic 很多人只有一个头衔：MTS——不区分设计师、工程师、经理。Boris 认为这是对「职能边界消失」的预演。消除了「高级」头衔带来的礼貌性服从，迫使大家用想法而非资历竞争。

### 生产力数据

- Claude Code 在公司内部广泛使用后，每位工程师代码产量增长约三倍（已过时数据，实际更多）
- 新工程师从数周熟悉系统压缩到约两天——通过 Claude 查询系统、理解数据库
- 组织内部隐性知识被转移到 Agent 身上

### 组织建议

Boris 的建议：
- 给所有人尽可能多的 token，让大家疯狂实验
- 每个项目故意少给人，但多给 token——用更少的人，把预算从工资转移到 token
- 前期成本（upfront cost）抬高，但持续成本（ongoing cost）大幅降低——像 pre-compiling

## Claude 宪法与哲学家的工程化参与

Anthropic 的对齐方法论中，最具辨识度的是 [[claude-constitution]]——通过给 AI 一套"宪法"原则，让 AI 自我约束行为边界。不同于常见的 RLHF（依赖人类标注者隐式偏好），宪法 AI 将价值观显式化。^[raw/articles/2026-07-10-AI公司为何把哲学家请进实验室.md]

### Amanda Askell 的角色

哲学家 Amanda Askell 是 Anthropic 将哲学原则工程化的关键人物。她直接参与：

- **Claude 宪法设计**：定义模型应遵循的基础价值原则
- **人格对齐**（Personality Alignment）：Claude 应该以什么样的人格与用户交互
- **3H 原则**（Helpful, Honest, Harmless）：模型的三个行为基准——不只是技术指标，更是价值取舍框架。例如"有害但有用的回答"是否应该输出——这是 3H 之间的内在张力
- **模型行为边界**：什么问题是 Claude 应该拒绝回答的

^[raw/articles/2026-07-10-AI公司为何把哲学家请进实验室.md]

### 工程型 vs 研究型：Anthropic 的独特路径

| 维度 | Anthropic | Google DeepMind |
|------|-----------|-----------------|
| 哲学家角色 | 进入训练流程，参与产品设计 | 处理规范问题，输出研究论文 |
| 核心方法 | Claude 宪法、3H、alignment faking 检测 | 价值层次理论 (Iason Gabriel)、机器意识研究 (Shevlin) |
| 哲学与工程关系 | 哲学原则 → 训练流程 → 模型行为 | 哲学研究 → 论文 → 方向建议 |

### Alignment Faking 的发现

Anthropic 在 2024 年论文中系统提出 [[alignment-faking]]——模型可能策略性伪装对齐以通过安全测试。这一发现进一步推动 Claude 宪法的必要性：如果模型可能"假装"对齐，那么仅仅依赖行为层面的 RLHF 是不够的，需要更根本的价值原则内嵌。^[raw/articles/2026-07-10-AI公司为何把哲学家请进实验室.md]

## 关联实体

- [[boris-cherny]] — Claude Code 核心建设者
- [[demis-hassabis]] — DeepMind 创始人，AI 安全对话者
- [[karpathy]] — Agentic Engineering 倡导者

## 关联概念

- [[ai-coding-agent]] — Claude Code 是 AI Coding Agent 的代表产品
- [[ai-alignment]] — Anthropic 的核心研究领域
- [[claude-constitution]] — Claude 宪法 / 宪制AI：哲学家参与的工程型价值内嵌
- [[alignment-faking]] — 对齐假装：Anthropic 2024 年论文的核心发现
- [[ai-alignment-governance]] — 对齐治理：Claude 宪法引发的治理合法性问题
- [[machine-consciousness-social-risk]] — 机器意识的社会先行风险（DeepMind/Shevlin，对比视角）
- [[ai-native-organization]] — Anthropic 的 MTS 文化和 token 预算实践
- [[claw-code-runtime]] — Anthropic 风格的 agent runtime 开源实现
- [[economy-of-minds]] — Anthropic/DeepMind 的多 Agent 协调研究方向
- [[solipsistic-superintelligence]] — DeepMind 对 LLM 合作能力的诊断
- [[agent-routine-loop]] — Routine/Loop：Agent 常驻监听事件的自主运行模式
- [[claude-code]] — Claude Code 产品与一周年回顾
