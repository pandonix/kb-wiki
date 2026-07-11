---
title: Claude 宪法 / 宪制AI
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [alignment, ml, safety, company]
sources: [raw/articles/2026-07-10-AI公司为何把哲学家请进实验室.md]
confidence: medium
---

# Claude 宪法 / 宪制AI

## 核心定义

Claude 宪法（Claude Constitution / Constitutional AI）是 [[anthropic]] 的核心对齐方法论：通过给 AI 一套"宪法"原则，让 AI 在训练和推理中自我约束行为边界。与常见的 RLHF 不同，宪法的制定过程直接引入哲学家参与，使价值原则进入模型训练、微调和行为边界设计——而不是停留在品牌叙事层面。^[raw/articles/2026-07-10-AI公司为何把哲学家请进实验室.md]

## 哲学家如何参与

### Amanda Askell 的角色

Amanda Askell（哲学家）是 Anthropic 将哲学原则工程化的关键人物。她直接参与 Claude 宪法的设计，涉及：

- **人格对齐**（Personality Alignment）：Claude 应该以什么样的人格与用户交互
- **3H 原则**（Helpful, Honest, Harmless）：模型的三个行为基准，不只是技术指标，更是价值取舍框架
- **模型行为边界**：什么问题是 Claude 应该拒绝回答的，拒绝的边界如何定义

^[raw/articles/2026-07-10-AI公司为何把哲学家请进实验室.md]

### Anthropic vs DeepMind：工程型 vs 研究型

| 维度 | Anthropic | Google DeepMind |
|------|-----------|-----------------|
| 哲学家角色 | 进入训练流程和行为边界设计 | 处理规范性问题（研究型） |
| 核心输出 | Claude 宪法、人格对齐、alignment faking 检测 | 价值层次理论（Iason Gabriel）、机器意识研究（Shevlin） |
| 哲学与工程的关系 | 哲学原则 → 模型行为 → 产品体验 | 哲学研究 → 论文 → 指导方向 |
| 治理属性 | 工程型内嵌 | 研究型外挂 |

^[raw/articles/2026-07-10-AI公司为何把哲学家请进实验室.md]

关键区别：Anthropic 让哲学原则成为训练流程的一部分，DeepMind 让哲学作为独立研究层——两者的治理含义完全不同。前者让哲学家成为"产品设计师"（设计 AI 的价值观行为），后者让哲学家成为"顾问"（提出规范性问题）。

## 宪法 AI 的技术机制

结合 [[ai-alignment]] 中的 RLAIF / Constitutional AI 方法：

1. 制定一套原则（宪法）——由哲学家 + 工程师共同定义
2. 用宪法原则训练一个 critique 模型（AI 监督 AI）
3. 用 critique 模型的反馈进行 RL 微调
4. 模型在推理时遵循宪法原则进行自我约束

这不同于传统的 RLHF：RLHF 依赖人类标注者的偏好（隐式价值观），宪法 AI 将价值观显式化为一套可讨论、可修改、可审计的原则。^[raw/articles/2026-07-10-AI公司为何把哲学家请进实验室.md]

## 治理层面的意义

Claude 宪法的存在意味着 Anthropic 至少部分承认：**AI 的行为边界不应该完全由工程师定义。** 但它也引出 [[ai-alignment-governance]] 中的核心问题：这套宪法由谁制定？哲学家是内部员工，还是独立第三方？宪法可以被修改吗？谁有修改权？

## 相关概念

- [[anthropic]] — Anthropic 公司的安全使命与组织实践
- [[ai-alignment]] — AI 对齐的技术全景：Constitutional AI 是核心方法之一
- [[ai-alignment-governance]] — 治理合法性：Claude 宪法的"立法者"问题
- [[alignment-faking]] — Claude 宪法试图防范的模型行为之一
