---
title: Multica
created: 2026-06-12
updated: 2026-06-12
type: entity
tags: [agent, tool, company]
sources: [raw/articles/2026-06-11-人是最慢的节点还怎么管AI-Agent.md]
confidence: medium
---

# Multica

开源 Agent 协作与编排平台，由 [[zhang-jiayuan]] 创建。定位为模型和平台中立的「协作层」——处理多个 Agent 的分工、任务传递和上下文合并。^[raw/articles/2026-06-11-人是最慢的节点还怎么管AI-Agent.md]

## 核心概念

- **运行时（Runtime）**：Agent 运行的机器（MacBook、Mac Mini、服务器），统一注册到 workspace
- **智能体（Agent）**：相当于 AI 员工，可分配任务、设置角色
- **Agent Team（Squad）**：多个 Agent 组成的小队，有独立工作流程

## 产品数据（截至 2026 年 6 月）
- GitHub 2.75w Star，一周涨 1.2w Star
- 每 10 秒触发一个 Agent 任务
- 团队仅 4 人 + 几十个 Agent
- 支持 Claude Code、Codex、OpenCode 等主流 Agent 平台
- 每周平台 token 消耗约 3000 亿

## 组织实践

Multica 自身是最极端的用户——4 人团队 + 几十个 Agent：

### 工作流
- **周一 weekly planning**：Agent 提前准备会议文档和上周数据分析
- **每晚 6 点 demo 站会**：Agent 整理当天代码提交，demo 后直接部署上线，不 review 代码
- **日常**：每人建立任务 → 分配 Agent/Agent Team → 最终 review 即可

### 已上岗 Agent 岗位
- 每人一个本地 coding agent
- 一个 24 小时运行在 Mac Mini 的公共 coding agent
- 数据分析师 Agent（接入 PostHog，能写代码+分析）
- 部署/运维 Agent
- Go-to-market Agent（分析热点、联系 KOL）
- 淘汰制：一键淘汰无效 Agent

### Agent 协作设计
三类角色（Orchestrator / Worker / Validator）、最多两层结构。Agent 自己发现需要的信息，无显式 handoff。

## 开源策略
- 开源增强信任（协作工具 + 中立平台）
- 代码本身不构成防御——竞品几天就能抄完
- 开源带来社区反馈和快速迭代
- 长期壁垒来自网络效应（组织内使用的人越多价值越大）

## 关联概念
- [[zhang-jiayuan]] — 创始人
- [[multi-agent-collaboration]] — 多 Agent 协作模式
- [[ai-native-organization]] — AI Native 组织模式
- [[agent-idle-rate]] — Agent 空闲率
- [[agent-delegation-trap]] — Agent 委托陷阱
- [[economy-of-minds]] — Economy of Minds
