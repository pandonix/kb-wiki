---
title: Agentic AI（智能体 AI）
created: 2026-05-22
updated: 2026-05-26
type: concept
tags: [agent, ml, coding]
sources: [raw/articles/可能是目前最好的Agent课程！吴恩达官宣新课《Agentic AI》，手把手教你构建AI智能体.md, raw/articles/Claude不到4%，全军覆没！一场大考撕碎Agent「全自动办公」幻想.md]
confidence: high
---

# Agentic AI（智能体 AI）

## 核心定义

Agentic AI 是一种 AI 系统构建范式：让 LLM 作为核心执行者，通过四种设计模式自主完成复杂任务。与传统的「一问一答」式 LLM 使用不同，Agentic AI 赋予模型主动规划、执行、反思和协作的能力。

吴恩达将 Agentic AI 定位为「就业市场上最受欢迎的技能之一」。^[可能是目前最好的Agent课程！吴恩达官宣新课《Agentic AI》，手把手教你构建AI智能体.md]

## 四种核心设计模式

### 1. 反思（Reflection）

智能体检查自身的输出，并找出改进方法。这是自我纠错和自我提升的基础能力。

### 2. 工具使用（Tool use）

由 LLM 驱动的应用程序决定调用哪些函数来执行网页搜索、访问日历、发送邮件、编写代码等操作。工具使用是将 LLM 从「对话引擎」升级为「行动引擎」的关键。

### 3. 规划（Planning）

使用 LLM 来决定如何将一个任务分解为多个子任务来执行。规划能力让 Agent 能处理超出单次推理窗口的复杂目标。

### 4. 多智能体协作（Multi-agent collaboration）

构建多个专业化的智能体——就像公司雇佣多名员工一样——来完成一项复杂任务。每个 Agent 负责不同子域，通过协作产生超越单个 Agent 能力的成果。

详见 [[multi-agent-collaboration]]。

## 关键成功因素：Evals 与错误分析

吴恩达特别强调，**决定一个人能否成功执行 Agent 构建的关键预测因素，是他们推动评估（evals）和错误分析的规范化流程的能力。** 

让评估数据指导工作，而非猜测应该做什么——这显著领先于大多数构建智能体的团队。^[可能是目前最好的Agent课程！吴恩达官宣新课《Agentic AI》，手把手教你构建AI智能体.md]

## 课程特点

- 厂商中立，使用原生 Python
- 自定进度
- 不将细节隐藏在框架中
- 唯一先决条件：熟悉 Python

## Agent 真实能力 vs Benchmark 差距

SaaS-Bench 评测揭示了 Agentic AI 当前的残酷现实：最强模型（Claude Opus 4.7）在 106 个真实跨应用长程任务中端到端完全通过率仅 3.8%。四种结构性失败模式（长程衰减、上游错误级联、缺少状态复核、路径依赖不稳定）指向当前 Agent 范式的天花板——缺少对持久状态的有效推理、闭环验证和错误恢复能力。详见 [[saas-bench]]。

更现实的路径是人机协作、强约束工作流、检查点验证和可恢复设计，而非直接追求全自动替人办公。^[Claude不到4%，全军覆没！一场大考撕碎Agent「全自动办公」幻想.md]

## 相关概念

- [[ai-coding-agent]] — AI Coding Agent 工程全景
- [[multi-agent-collaboration]] — 多 Agent 协作的深度分析
- [[harness-engineering]] — Harness 设计如何支撑 Agentic AI
- [[agent-skills]] — Agent Skills 作为工具使用模式的具体实现
- [[ai-code-adoption]] — 提升 AI 编码采纳率的工程实践
- [[saas-bench]] — Agent 真实办公能力评测
- [[enterprise-agent-practice]] — 企业级智能体实践：从Copilot到数字员工

## 相关实体

- [[andrew-ng]] — 吴恩达，课程作者
