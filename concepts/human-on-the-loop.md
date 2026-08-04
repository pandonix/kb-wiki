---
title: 人在环上（Human-on-the-Loop）
created: 2026-06-09
updated: 2026-08-04
type: concept
tags: [agent, coding, infra, management, thought]
sources: [raw/articles/2026-06-08-控制论与智能体编码中的人在环上.md, raw/articles/2026-07-30-思林广不记-AI-First-or-Human-First.md]
confidence: medium
---

# 人在环上（Human-on-the-Loop）

## 核心命题

**随着 AI 智能体生成代码速度上升，人类逐行审查（Human-in-the-loop, HITL）会成为瓶颈。未来工程师的角色不是在执行环里审批每个改动，而是在环上设计控制系统、监测偏差、设置边界，并定期回到现场抽样校准。**

HOTL 是从「人审 AI 输出」到「人设计并校准控制系统」的范式转移。

## HITL vs HOTL

| 维度 | Human-in-the-Loop (HITL) | Human-on-the-Loop (HOTL) |
|------|-------------------------|--------------------------|
| 人的位置 | 在执行环内，逐项审批 | 在元维度，设计控制系统 |
| 瓶颈 | 人成为断裂点（fracture point）——要么拖慢系统，要么沦为无脑盖章 | 人定义约束和传感器，系统自主执行 |
| 控制方式 | 微观审查每一个改动 | 衰减机器侧多样性，放大人类侧意图 |
| 类比 | 流水线质检员 | 管理者领导组织：定义目标、结构、流程、指标、异常升级 |

### HITL 的实证失败

[[automation-bias]] 的数十年研究证明 HITL 在实际中不可靠：

- 放射科医生：AI 给错判断时，初级医生准确率从 ~80% 降到 <20%，资深从 >80% 降到 <50%
- 开发者：96% 不完全信任 AI 代码，但只有 48% 每次都检查
- 欧盟 AI 法案第 14 条（2026.8 生效）要求「人能推翻 AI 输出」——上述证据说明这个前提站不住

HITL 失败的根本原因是人类在处理 AI 输出时的认知局限，而非态度或动机。^[raw/articles/2026-07-30-思林广不记-AI-First-or-Human-First.md]

## 控制论基础

HOTL 的理论根基来自控制论（Cybernetics），由 Norbert Wiener 于 1940 年代提出——研究复杂系统中的通信与控制的科学。关键概念：

### 必要多样性定律（Law of Requisite Variety, Ross Ashby）

在 SDLC 语境下，智能体系统的「多样性」表现为在海量代码变更、架构决策和缺陷修复。人类无法在代码执行层吸收机器速度带来的全部复杂性——必须上移到**元维度**进行控制。^[raw/articles/2026-06-08-控制论与智能体编码中的人在环上.md]

### 可生存系统模型（Viable System Model, VSM, Stafford Beer）

将控制论与管理学科连接，为组织（包括人+Agent 系统）的生存能力提供系统架构。

## HOTL 的两个核心动作

### 1. 衰减（Attenuation）

衰减来自智能体系统侧的超高多样性，避免人类侧过载：

- 将高频输出物聚合为标准化报告或仪表盘
- 仅基于预设阈值升级异常情况
- 促进智能体系统内部的自我管理
- Agent 间互相验证（如 QA agent 独立检查 coding agent 产出）

### 2. 放大（Amplification）

放大来自人类侧的多样性，更高效地影响 AI 智能体：

- 将架构和准入决策规则编码进 agent 全局策略
- 为 agent 提供统一知识库
- 将控制权分散给多个人类角色或平台工程团队
- 通过培训和思维模型深化人类对系统的理解

这两个动作的工程实现，正是 [[harness-engineering]] 的核心工作。

## 康南特-阿什比定理（Conant-Ashby Theorem）

> 系统的优秀调节者必须是该系统的模型。

人类必须深刻理解系统本应如何运行。通过为 SDLC 设计和配置 agent，人类形成初始思维模型。但现实系统可能偏离——模型漂移或在未预料到的极端情况下失败，需要持续校准。

## Gemba：现地现物（Go See / Genchi Genbutsu）

Gemba 是精益管理概念，指「创造价值的实际场所」。在 agentic SDLC 中，Gemba 是智能体与代码、仓库打交道的微观世界。

### 为什么必须「降维」

工程师不能只依赖仪表盘和指南策略。必须定期、偶尔地回到代码和仓库现场进行**抽样深审**：

- 识别传感器过滤掉的问题（代码退化、隐性幻觉）
- 感知 agent 是否在「以正确的方式做正确的事」
- **保持工程师用于控制的思维模型处于最新、最准确的状态**

### 实践示例

每周五下午进行 Gemba session：随机挑选 3 个 agent 生成的复杂 PR，深度手动代码审查。可能发现：代码通过所有自动化测试，但使用了低效数据结构，未来高并发下会引发扩展性问题。此时修正系统模型并改进 harness。

### 双环学习（Double-loop Learning）

Gemba spot-check 是 HOTL 系统中的**次级反馈闭环**——不只是修正单个错误（单环学习），而是修正控制系统本身的设计假设（双环学习）。

## 对能力训练的启示

「现地现物」的有效性深度依赖人类的技术直觉。当大部分代码由 AI 代劳时，**如何保持和培养下一代开发者的技术直觉与工程硬实力**，是 HOTL 范式下未解决的关键问题。

## 与相关概念的关系

- [[harness-engineering]] 是 HOTL 的工程实现：传感器、指南、衰减/放大、异常升级、质量门禁的整套系统
- HOTL 的核心动作（衰减+放大）就是 Harness Engineering 的设计目标
- [[ai-coding-agent]] 中「人负责 spec，agent 负责执行」是 HOTL 的具体体现
- [[ai-architecture-governance]] 在 HOTL 语境下是「将治理规则编码进 agent 全局策略」

## 相关概念

- [[harness-engineering]] — Harness Engineering：HOTL 的工程实现层
- [[ai-coding-agent]] — AI Coding Agent 工程全景
- [[ai-architecture-governance]] — AI 时代架构治理
- [[multi-agent-collaboration]] — 多 Agent 协作：QA agent 独立验证是衰减的一种形式
- [[agent-owner-role]] — Agent Owner：HOTL 中人的角色锚定
- [[agent-skills]] — Agent Skills：放大人类意图的载体
- [[musk-algorithm]] — 马斯克五步工作法：为系统设边界、删流程
- [[hierarchy-to-intelligence]] — 科层制到智慧型组织：管理 Agent 团队的类比
- [[automation-bias]] — 自动化偏见：HITL 失效的认知机制
- [[skill-atrophy-ai]] — AI 导致的技能退化：HITL/HOTL 下的个人能力退化
- [[ai-human-first-framework]] — 两层决策框架：HOTL 的组织层实现
