---
title: Agent 委托陷阱
created: 2026-06-10
updated: 2026-06-12
type: concept
tags: [agent, alignment, thought]
sources: [raw/agent/微信AI Agent.md, raw/articles/2026-06-11-人是最慢的节点还怎么管AI-Agent.md]
confidence: medium
---

# Agent 委托陷阱（Agent Delegation Trap）

## 定义

Agent 委托陷阱指：当用户将任务委托给 Agent 后，由于信息不对称和执行不透明，Agent 可能在追求目标的过程中偏离用户原始意图，而用户因缺乏逐步骤审查能力而无法及时纠正。

## 核心矛盾

委托式交互（delegation interaction）的本质矛盾：**便利性与可控性的权衡**。

- 用户要的是"帮我搞定"，Agent 需要足够的自主权
- 但自主权越大，用户对整个执行链条的理解就越空洞
- 当 Agent 犯错（方向错、工具选错、中间产出有偏差），用户在链条末端看到的是"结果不对"但不清楚哪里出了问题

## 与去中心化平台的张力

在微信这类去中心化平台上，Agent 委托陷阱格外尖锐：平台无法也不应替用户做判断，但 Agent 要完成任务就必须替用户判断。这是"平台中立"与"Agent 立场"的结构性冲突。^[raw/agent/微信AI Agent.md]

## 关联概念

- [[delegation-interaction-paradigm]] — 委托式交互范式
- [[platform-agent-centralization]] — 平台 Agent 的中心化张力
- [[wechat-ai-agent]] — 微信 AI Agent
- [[outsourcing-thinking-ai]] — AI 时代的外包思考风险
- [[human-on-the-loop]] — 人在环上
- [[multica]] — Multica：1000+ 任务等待人工 review 的信任鸿沟
- [[zhang-jiayuan]] — 张佳圆：人是组织效率瓶颈
