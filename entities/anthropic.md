---
title: Anthropic
created: 2026-06-08
updated: 2026-06-08
type: entity
tags: [company, ml, agent, alignment, coding]
sources: [raw/articles/Claude Code之父：品味不是人类护城河；当工程师不再写代码，招聘看什么？.md, raw/articles/AI 时代的架构治理.md]
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

## 关联实体

- [[boris-cherny]] — Claude Code 核心建设者
- [[demis-hassabis]] — DeepMind 创始人，AI 安全对话者
- [[karpathy]] — Agentic Engineering 倡导者

## 关联概念

- [[ai-coding-agent]] — Claude Code 是 AI Coding Agent 的代表产品
- [[ai-alignment]] — Anthropic 的核心研究领域
- [[ai-native-organization]] — Anthropic 的 MTS 文化和 token 预算实践
- [[claw-code-runtime]] — Anthropic 风格的 agent runtime 开源实现
- [[economy-of-minds]] — Anthropic/DeepMind 的多 Agent 协调研究方向
- [[solipsistic-superintelligence]] — DeepMind 对 LLM 合作能力的诊断
