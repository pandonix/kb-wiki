---
title: Palantir Ontology 与 AIP
created: 2026-05-27
updated: 2026-05-27
type: concept
tags: [agent, architecture, company, ml, summary]
sources: [raw/agent/palantir-aip-ontology-analysis.md]
confidence: medium
---

# Palantir Ontology 与 AIP

## 核心洞察

企业 AI 落地的核心瓶颈不是"模型不够强"，而是**"模型没有被嵌入到企业决策的语境里"**——它不知道你公司里"客户"是什么、"订单"怎么流转、"调拨"触发什么连锁反应、谁有权批准。

Palantir 的回答是 **Ontology**——一个决策中心的语义层，把数据 (data)、逻辑 (logic)、行动 (action) 缝合到统一的表示里。AIP 是建在 Ontology 之上的 AI 能力层。

## Ontology：不是数据模型，是企业的"数字孪生"

Ontology 表示的是**"如何做决策"**，不是"数据躺在哪里"。

| 要素 | 内容 | 例子 |
|------|------|------|
| Object Types (名词) | 业务实体 | Customer, PurchaseOrder |
| Links (关系) | 实体间语义关系 | 客户*拥有*订单 |
| Properties | 多源融合的属性 | 同名实体被 resolve |
| Actions (动词) | 业务可做的事 | 下单、调拨、审批 |
| Functions/Models | ML/优化算法 | 需求预测、库存优化 |

**最关键的设计：Action 是一等公民。**传统知识图谱没有"动词"的位置。

## 与 RAG 的关键区别：OAG

- **RAG**：LLM 检索文本片段 → 拼到 prompt → 生成回答
- **OAG (Ontology Augmented Generation)**：LLM 拿到的是 Ontology 对象——知道这是 `PurchaseOrder`，金额多少、关联客户是谁、可执行哪些 Action、谁有权执行

OAG 同时解决三件事：幻觉（数据有结构化语义）、权限（继承 Ontology ACL）、可审计（每步都是 typed call）。

## AIP Logic：LLM 编排成可治理的函数

Block 类型：Use LLM / Apply Action / Execute Function / Transform / Loop/Branch

LLM 的工具分三类：Data tools / Logic tools / Action tools

**关键工程细节**：LLM 不能直接执行 Action，只能"请求"。Logic 函数要真正写回 Ontology，必须从 Action 里被调用。这是把"AI 的建议"和"对世界的修改"显式分离。

## 决策闭环：Write-back 与 Decision Lineage

完成后写回的内容：推荐内容 + 推理链 + 人工审核反馈 + 最终决策结果 + 实际效果。

决策血统 (decision lineage) 可用于：
- 微调模型（SFT 数据）
- 蒸馏成 prompt 原则
- few-shot 动态示例
- 评估系统性能（AIP Evals）

## "数据挖掘→分析→决策→实施"闭环映射

| 环节 | 对应能力 |
|------|---------|
| 数据挖掘 | Pipeline Builder + Object Type 映射 + LLM 非结构化抽取 |
| 分析 | Functions on Objects + Workshop + AIP Logic 多步推理 |
| 决策 | Scenario 模拟 + Agent 推荐 + Human-in-the-loop |
| 实施 | Actions + Automate + 写回源系统 |
| 学习闭环 | AIP Evals + Decision lineage + Feedback pattern |

## 批判性思考

- **重**：需要 FDE 驻场建 Ontology，持续投入
- **锁定效应**：迁移成本极高，"切换的主要驱动力不是软件迁移，而是重建 Ontology"
- **OAG 命名**：更多是营销包装，本质是 typed schema 检索替代 raw text 检索
- **适用场景**：大型企业（制造/能源/国防/金融/医疗）、受监管行业、有预算做长期本体建设
- **不适合**：中小型公司、决策靠经验创意难以建模、想快速试 AI

## 相关概念

- [[ai-coding-agent]] — AI Coding Agent
- [[agent-memory]] — Agent 记忆系统
- [[declarative-architecture]] — 声明式架构
- [[ai-architecture-governance]] — AI 时代架构治理
- [[harness-engineering]] — Harness Engineering
- [[context-engineering]] — 上下文工程
