---
title: Claude Code
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [tool, agent, coding, ml]
sources: [raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md, raw/articles/Claude Code之父：品味不是人类护城河；当工程师不再写代码，招聘看什么？.md]
confidence: high
---

# Claude Code

## 概述

Claude Code 是 Anthropic 开发的 AI 编程 Agent，上线一周年，经历了从"不好用的原型"到工程组织中心工作方式的转变。

## 两次认知跃迁

### 第一次跃迁：用自然语言编程
工程师意识到不必亲手写代码，可以用自然语言让 Agent 写代码。这改变了编程的交互方式——从写代码到描述意图。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

### 第二次跃迁：多 Agent 协调
工程师不再直接对话单个 Agent，而是通过 **loop、routine、agent view、remote control** 等机制调度一批 Agent。Boris Cherny 的工作方式已变成用一个 Agent 驱动一批 Agent，再由这些 Agent 拆出更多 Agent，形成树状并行任务结构。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

### 第三次跃迁（进行中）
方向是 Agent 运行时间更长、自主性更强、并发数量更大，产品形态会继续变化。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

## 关键机制

### Routine / Loop
工程师可以让 Agent 常驻监听 GitHub issue、bug 反馈、CI、review、rebase 等事件，满足规则后自动修复、提交 PR、通知 owner，甚至处理 owner 尚未感知到的问题。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

### Auto Mode 安全逻辑
不要让人审批每一个工具调用，而是用另一个模型筛选风险，把人的注意力集中到真正重要的请求上。这比大量弹窗式人工确认更安全。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

### SKILL 沉淀
Claude 犯错后，不应只在对话里纠正，而应把正确做法写进 `CLAUDE.md` 或沉淀为可复用 skill，让系统下次自动继承经验。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

## 组织影响

- Claude Code 使用已跨出工程团队：设计师改代码、产品经理改功能、财务团队做预测、数据科学家把它当标配工具。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]
- Boris 认为未来工程师和产品经理的边界会合并，真正受益的是有好奇心、有产品品味、愿端到端负责的人。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

## 关联实体

- [[anthropic]] — Claude Code 的开发公司
- [[boris-cherny]] — Claude Code 核心建设者

## 关联概念

- [[agent-routine-loop]] — Routine/Loop 模式
- [[ai-coding-agent]] — AI Coding Agent 工程
- [[ai-native-organization]] — AI Native 组织模式
- [[context-engineering]] — 上下文工程的转向
- [[agent-skills]] — Agent Skills 沉淀机制
