---
title: 委托式交互范式
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [agent, ml, thought]
sources: [raw/agent/微信AI Agent.md]
confidence: medium
---

# 委托式交互范式（Delegation Interaction Paradigm）

## 定义

从**直接操作式交互（Direct Manipulation）**到**委托式交互（Delegation）**的范式跃迁。用户从"自己操作界面完成任务"变成"用自然语言表达意图，委托 Agent 代为完成端到端任务"。^[raw/agent/微信AI Agent.md]

## 交互范式对比

| 维度 | 直接操作（Direct Manipulation） | 委托式（Delegation） |
|------|-------------------------------|---------------------|
| 交互方式 | 用户发现应用 → 打开 → 手动导航 UI → 完成 | 用户表达意图 → Agent 自主完成 |
| 人的角色 | 操作者 | 指挥官 / 意图表达者 |
| 界面可见性 | 所有步骤和选项可见 | 执行过程不可见（"黑盒执行"） |
| 认知负荷 | 高（需知道所有步骤） | 低（只需表达意图） |
| 可靠性需求 | 低（人直接操作，错误容易感知） | 极高（看不见执行过程，错了难发现） |

## 范式层级

这被认为是和 GUI 取代命令行、触摸屏取代物理键盘同一层级的交互跃迁。人类从"操作机器"进化到"指挥智能体"。^[raw/agent/微信AI Agent.md]

## 微信 AI Agent 的具体体现

- **旧路径**：用户发现小程序 → 打开 → 手动导航 UI → 完成任务
- **新路径**：用户聊天表达意图（"帮我打车去机场"）→ Agent 自主完成全流程（可能完全不展示小程序界面）

^[raw/agent/微信AI Agent.md]

## 委托的代价

- **选项空间丧失**：Agent 替你选了，你再也看不到"还有什么没被端上来"
- **议价权削弱**：一站式便利 = 加深锁定，削弱比价/退出能力
- **偶遇消失**：选择被压缩成"最优解"，生活被压缩掉冗余
- **认知主权（Epistemic Agency）丧失**：你不知道 Agent 的排序逻辑

^[raw/agent/微信AI Agent.md]

## 频次悖论

委托式交互的真实价值区间被夹在两端之间：
- **高频任务**：摩擦极低（已有的肌肉记忆），Agent 边际价值小
- **低频但复杂任务**：最需要委托，但也最不放心委托——用户最想自己把关

^[raw/agent/微信AI Agent.md]

## 关联概念

- [[wechat-ai-agent]] — 微信 AI Agent
- [[platform-agent-centralization]] — 平台 Agent 的中心化张力
- [[agent-delegation-trap]] — Agent 委托-代理陷阱
- [[internet-dead-agent-alive]] — 互联网已死，Agent 永生
- [[agentic-ai]] — Agentic AI 设计模式
