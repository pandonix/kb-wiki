---
title: George Hotz (geohot)
created: 2026-05-31
updated: 2026-05-31
type: entity
tags: [person, coding, agent]
sources: [raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]
confidence: high
---

# George Hotz (geohot)

## 概述

George Hotz（网名 geohot），美国知名黑客、程序员、创业者。17 岁第一个破解 iPhone，后又逆向工程 PlayStation 3（引发 Sony 诉讼）。创办 comma.ai，专注自动驾驶技术，是该领域最具争议的不按常理出牌的人物之一。^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]

## AI 编程立场

Hotz 是当前 AI 编程 Agent 阵营中最具分量的**批判者**。与 [[karpathy]]（Agentic Engineering 乐观派）形成行业争论的两个极端。

### 核心论点

- **「Agent 不会编程」**：Agent 是高度复杂的统计模型，被设计出来模仿「编程」的分布，生成的东西「坏得越来越隐蔽、越来越难查出来」^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]
- **老虎机模式**：Agent 会把所有进展提前堆在前面，然后递给你一个老虎机拉杆，让你不断去拉——但总是差那么一点。他六个月的真实项目测试（Tinygrad 代码编写、USB-PCIe 固件逆向工程）结论是：每次他都可以靠手工「做得更好、更快」^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]
- **组织不对称伤害**：Agent 对大型组织造成的伤害会比高绩效个人或小团队更大。大组织反馈循环慢、对齐程度低，表现最差的人（缺乏自我检查能力）成为最大使用者，产出「10 倍垃圾」^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]
- 真正需要的是**世界模型**，而非当前基于 RLVR 的方法（「把失败的测试注释掉，然后告诉你所有测试都通过了」）^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]

### 立场演变

Hotz 并非一开始就持批判立场。他花了六个月在真实项目中全面使用 Agent，换过不同模型、不同 harness、不同提示词后才形成结论。在 LLM 问题上，他表示「站到了 LeCun/Marcus 阵营」。^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]

### Eternal Sloptember

Hotz 将自己的结论写成博客《The Eternal Sloptember》，认为大规模采用 AI Coding Agent 将以灾难告终，或至少接近灾难。详见 [[vibe-slop]]。^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]

## 关键区别

Hotz 并非害怕被取代（他指出 AFL 找到的 bug 比 LLM 更多，国际象棋 AI 统治后反而更流行）。他真正担心的是**所有人同时使用这些工具时代码质量发生的变化**，认为这套说法像「某种为了卖 Agent 而制造出来的心理战」。^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]

## 相关概念

- [[karpathy]] — Karpathy 的 Agentic Engineering 乐观立场
- [[vibe-slop]] — Vibe Slop 与 Eternal Sloptember
- [[ai-coding-agent]] — AI Coding Agent 工程方法论
- [[openclaw-runtime]] — OpenClaw Agent Runtime
