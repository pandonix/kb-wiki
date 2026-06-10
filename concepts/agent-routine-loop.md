---
title: Agent Routine / Loop 模式
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [agent, coding, ml]
sources: [raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]
confidence: medium
---

# Agent Routine / Loop 模式

## 定义

Routine / Loop 是 AI Agent 的一种运行模式：Agent 常驻监听外部事件（GitHub issue、bug 反馈、CI 结果、review 请求、rebase 等），满足预设规则后自动触发处理流程——修复代码、提交 PR、通知 owner，甚至处理 owner 尚未感知到的问题。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

## 与传统 Agent 的区别

| 维度 | 传统 Agent（对话驱动） | Routine/Loop Agent |
|------|----------------------|-------------------|
| 触发方式 | 人发起对话 | 事件自动触发 |
| 运行模式 | 单次对话→完成 | 常驻监听→持续闭环 |
| 人的位置 | 发送指令 + 审批结果 | 设计规则 + 异常介入 |
| 闭环程度 | 人必须主动提出问题 | Agent 发现并处理人尚未感知的问题 |

## 关键意义

Routine/Loop 是判断 Agent 是否真正接管工作流的观察点：**是否能常驻监听事件、触发任务、生成修复、提交结果，并在无人主动提醒时闭环问题**。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

这是从"人驱动 Agent"到"Agent 主动运作"的质变——人的角色从操作者转移到控制系统的设计者和异常处理者。

## Anthropic 的实践

在 Anthropic 内部，Routine 被认为是最值得关注的应用方向之一。工程师可以让 Claude Code Agent 常驻监听：

- GitHub issue 创建 → 自动分析、修复、提交 PR
- CI 失败 → 自动诊断、修复、重新触发
- Review 请求 → 自动 review、提供建议
- Rebase 冲突 → 自动解决

## 潜在风险

- Routine 是否能在普通公司稳定运行，而不只是 Anthropic 内部自举样本？^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]
- 多 Agent 协调税（coordination tax）在某些场景下可能抵消 routine 的效率收益
- 安全性：Agent 自主触发代码修改和 PR 需要严格的权限控制和审计

## 关联概念

- [[ai-coding-agent]] — AI Coding Agent 工程
- [[human-on-the-loop]] — 人在环上：从微观审批到控制系统设计
- [[multi-agent-collaboration]] — 多 Agent 协作模式
- [[claude-code]] — Claude Code 产品
- [[agent-skills]] — Agent Skills 沉淀与复用
