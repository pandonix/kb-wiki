---
title: Boris Cherny
created: 2026-06-08
updated: 2026-06-08
type: entity
tags: [person, agent, coding, company]
sources: [raw/articles/Claude Code之父：品味不是人类护城河；当工程师不再写代码，招聘看什么？.md]
confidence: medium
---

# Boris Cherny

## 概述

Boris Cherny 是 Anthropic 的技术成员（Member of Technical Staff），Claude Code 的核心建设者之一。他曾就职于 Meta（Facebook），在 Anthropic Labs Team 主导 Claude Code 的从零构建。

## 关键观点

### 对 Claude Code 的定位

- Claude Code 不是单纯的编程工具，而是 Anthropic 用来**观察模型进入真实世界的实验平台** ^[raw/articles/Claude Code之父：品味不是人类护城河；当工程师不再写代码，招聘看什么？.md]
- 真正决定 Claude Code 上限的是底层模型能力提升（Sonnet 4 → Opus 4 → Opus 4.5），而非产品功能
- 他自己已有半年没有亲手写代码，工作变成写 Loops——程序替他向 Claude 下达指令

### 编程抽象层级上移

从穿孔纸带 → 汇编 → Fortran/Java/Python → prompt Claude → **写 Loops（程序持续调度多个 Claude 实例）**。人类只是再次提升了编程的抽象层级。

### 对品味（Taste）的看法

**不认为品味是人类护城河。** 每次他觉得自己在编程上有「特殊品味」（如不准用 class），最后都被证明是错的——模型直接写 class，代码也不差。他推演 3-6 个月后模型的大部分产品想法都会是好的。**最终剩下的只有价值观**——如何做对的事情，而不仅仅是把事情做对。

### 招聘与组织

- 最喜欢 **Generalist（通才）**：能跨用户、设计、数据、工程、业务，把想法变成结果
- 支持 **Member of Technical Staff** 头衔：消除层级暗示，让想法本身而非资历来竞争
- 建议创始人：**少招人，多给 token**——把预算从人的工资转移到 token 上
- 经验在 AI 时代不是线性累积，有时甚至是负债

## 关联实体

- [[anthropic]] — Boris 所在的 AI 安全公司
- [[karpathy]] — 同样倡导 Agentic Engineering 的实践者
- [[george-hotz]] — 对 AI Coding 持批判立场的工程师

## 关联概念

- [[ai-coding-agent]] — Claude Code 是 AI Coding Agent 的代表产品
- [[ai-native-organization]] — MTS 头衔、Generalist、token 预算等组织实践
- [[ai-commoditization-boundary]] — 品味被侵蚀，价值观成为最后防线
- [[ai-era-scarce-capabilities]] — 人的稀缺性继续上移到价值取舍
