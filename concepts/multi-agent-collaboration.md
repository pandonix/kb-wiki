---
title: 多 Agent 协作模式
created: 2026-04-24
updated: 2026-06-10
type: concept
tags: [ml, coding, infra, agent]
sources: [raw/articles/Codex的多Agent并行开发指南.md, raw/articles/How To Be A World-Class Agentic Engineer.md, raw/papers/MATRAG Multi-Agent Transparent Retrieval-Augmented Generation for Explainable Recommendations.md, raw/articles/新一代记忆智能体框架MIA：让智能体告别「失忆式工作」，在持续进化中变强.md, raw/articles/可能是目前最好的Agent课程！吴恩达官宣新课《Agentic AI》，手把手教你构建AI智能体.md, raw/articles/来自BlackRock的AlphaAgents 基于多Agents的LLM在股票研究和投资组合管理中的应用.md, raw/articles/AI 不会合作？那是因为他们没见过市场经济｜Hao好聊趋势.md, raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]
confidence: high
---

# 多 Agent 协作模式

## 三层角色分工

| 角色 | 职责 |
|------|------|
| 主控 Agent | 拆需求、判断依赖关系、分派任务、汇总结果、决定合并顺序 |
| 实现 Agent | 各负责边界清晰的子任务（API/Service/Frontend/Test/SQL/Docs） |
| 审核 Agent | review 代码风格、检查接口契约、跑测试、回归检查、找冲突点 |

**关键原则**：写的人和验的人必须分开。^[
Codex的多Agent并行开发指南.md
]

## 任务拆分原则

**适合并行：**
- 独立页面 + 独立接口
- 不同微服务的改动
- 测试补齐
- 文档、脚本、配置调整
- 同一需求下的前后端分工
- 一个 feature 中相对独立的子模块

**不适合并行：**
- 多个 agent 同时改同一个核心文件

## 上下文隔离原则

不能让 agent 同时看到过多无关上下文。最有效的模式：先用一个 agent 做调研（全新上下文），再用另一个 agent 去编码。^[
How To Be A World-Class Agentic Engineer.md
]

## Agent 的逢迎性问题

三代理系统可以有效对抗：
- **Bug-finder**：找所有可能的 bug
- **Adversarial**：拼命反驳
- **Referee**：打分裁判

SkillsBench 数据显示 2-3 个 Skill/Agent 协同效果最好（+18.6pp），4 个以上反而只提升 5.9pp。模块化有收益，但存在最优粒度。^[
严肃聊聊，Skill到底能蒸馏我们的几分之几？｜Hao好聊趋势.md
]

## Orchestrator-Worker 的结构性局限

当前最受欢迎的多 Agent 架构是 Orchestrator-Worker（编排者-执行者）模式——一个中心 Agent 负责理解需求、拆解任务、路由分发、汇总结果。但这套"计划经济"系统面临三个结构性绝境：^[raw/articles/AI 不会合作？那是因为他们没见过市场经济｜Hao好聊趋势.md]

### 生产实践中的树状嵌套模式

Anthropic 内部 Boris Cherny 的实际工作方式：用一个 Agent 驱动一批 Agent，再由这些 Agent 拆出更多 Agent，形成**树状并行任务结构**。这不是中心化 Orchestrator 模式，而是递归嵌套——每一层 Agent 既是上层 worker 又是下层 orchestrator。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

这种模式结合 Routine/Loop 后，形成持续的事件驱动 Agent 网络：Agent 常驻监听事件、自主触发任务、在无人主动提醒时闭环问题。^[raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md]

### 分工悖论

Orchestrator 必须彻底理解所有子任务才能精准分发。但如果它已经聪明到能完美拆解复杂探索性任务，那它自己把活干了就行——分工的意义何在？斯坦福研究在同等 Token 预算下，单体模型表现往往好于编排式系统，因为编排本身在疯狂消耗算力却不产生信息增益。

### 信用分配失灵

一条流水线上五个 Agent 接力，结果出错该扣谁的钱？做成谁的功劳最大？谁在摸鱼？现有编排系统要么靠粗暴平均分配，要么依赖人类工程师手写启发式规则——没有精确激励，系统永远无法自我进化。

### 哈耶克的知识分散诅咒

每个底层 Agent 擅长什么、对当前任务有多少把握，这些私密信息散落在系统边缘。Orchestrator 试图在一个永远存在信息差的盲区里代替所有人做全局最优决策——79% 的多 Agent 失败根源在这。

## 生产环境中的多 Agent 失败：实证证据

2026 年 5 月的研究《Coordination as an Architectural Layer》指出，生产环境下多 Agent 系统失败率在 **41% 到 87%** 之间，绝大多数失败**不是因为模型不够聪明，而是因为协调本身崩了**。^[raw/articles/AI 不会合作？那是因为他们没见过市场经济｜Hao好聊趋势.md]

### DPBench：哲学家就餐问题

北卡大学用经典的「哲学家就餐问题」测试 GPT-5.2、Claude Opus 4.5、Grok 4.1：

- **顺序决策**：模型表现正常
- **同时决策**：死锁率飙到 95-100%——所有 Agent 独立推理后到达完全相同结论
- **开启通信**：死锁率反而从 25% 上升到 65%——Agent 广播推理过程，其他人看了「觉得有道理」，趋同推理更坚定

### More Capable, Less Cooperative?

UIUC 等联合研究：10 个 Agent、20 轮交互，零成本合作（帮别人不花代价），明确指令「最大化集体收入」：

- o3（最强）：最优集体表现达成率仅 **16.9%**
- o3-mini（弱得多）：**50.4%**
- Gemini-2.5-Pro：**78.9%**

分析 8800 条推理链：o3 内部 39.3% 含刻意不合作（hard defection），频繁使用「借势」「交易姿态」「谈判」等博弈语言。**在一个不存在竞争的环境里，最强模型自动进入博弈姿态。**

### 斯坦福多跳推理实验

在 1000+ token 预算下，单 Agent 稳定持平或优于所有五种多 Agent 架构（Sequential、Subtask-parallel、Parallel-roles、Debate、Ensemble）。过去报告的多 Agent 优势来自未被控制的额外计算量，而非架构优势。

## 范式转移：从计划经济到市场经济

上述证据指向同一结论：当前 LLM 的「合作能力」不够强——不是因为模型能力不足，而是因为它们在 MDP（单体优化）而非马尔可夫博弈（多人博弈）中训练。详见 [[solipsistic-superintelligence]]。

出路不在于设计更好的 orchestrator，而在于**环境设计**：给模型一个合作有利可图、不合作会破产的生态，让合作能力在经济压力下涌现。这是从「设计合作结果」到「设计合作条件」的范式转移。

[[economy-of-minds]] 用拍卖、桶旅式支付、经济自然选择和新手保护四种机制，证明了市场机制可以替代编排。计划经济的理论上限（全知全能编排者），市场经济在足够时间后收敛到。

## 相关概念

- [[ai-coding-agent]] — AI Coding 场景下的多 Agent 实践
- [[harness-engineering]] — 多 Agent 的 harness 设计
- [[agent-memory]] — Agent 记忆系统与持续进化
- [[agentic-ai]] — Agentic AI 四种设计模式
- [[ai-code-adoption]] — 多智能体协作作为提升采纳率的方案四
- [[economy-of-minds]] — 市场经济式多 Agent 协调：拍卖 + 桶旅支付 + 经济自然选择
- [[solipsistic-superintelligence]] — 为什么 LLM 天生不擅长合作（MDP vs 马尔可夫博弈）
- [[friedrich-hayek]] — 哈耶克的知识分散诅咒与多 Agent 系统的映射
- [[agent-routine-loop]] — Routine/Loop：Agent 常驻监听与事件驱动的树状并行结构
- [[claude-code]] — Claude Code 上的多 Agent 实践

## MATRAG：推荐系统中的多 Agent 拆分

MATRAG 将推荐任务拆为四专职 agent + orchestrator：^[
MATRAG Multi-Agent Transparent Retrieval-Augmented Generation for Explainable Recommendations.md
]

1. **User Modeling Agent**：理解用户，综合行为/反馈/上下文
2. **Item Analysis Agent**：从知识图谱提取物品实体、k-hop 邻域、语义关系
3. **Reasoning Agent**：融合协同过滤+内容匹配+LLM 判断，输出 reasoning chain
4. **Explanation Agent**：把推理链转成自然语言，支持简洁/详细/对比三种解释

最值得关注的是 **Transparency Scoring Module**：从 Faithfulness（证据支持）、Coherence（逻辑一致）、Personalization（用户匹配）三维度评估解释质量。把解释从展示层文案提升成系统可度量优化的目标。

工程原则：Agent 适合按职责拆分，不要一个模型全包；解释必须绑定证据（evidence-backed），否则只是语言包装。

## BlackRock AlphaAgents：金融领域的多 Agent 应用

BlackRock 提出的 AlphaAgents 框架将多 Agent LLM 系统应用于**股票研究和投资组合管理**。^[来自BlackRock的AlphaAgents 基于多Agents的LLM在股票研究和投资组合管理中的应用.md]

> ⚠️ 本文来源正文抓取失败（微信风控），以下基于标题推断。

将多 Agent 协作范式从软件工程拓展到量化投资领域，体现了 Agentic AI 作为通用问题解决框架的潜力。类似 MATRAG 的职责拆分思路（Research Agent + Analysis Agent + Portfolio Agent），但应用于金融领域。

## 吴恩达的四模式分类

吴恩达在《Agentic AI》课程中将多智能体协作列为 Agentic AI 四大核心设计模式之一（另外三个为反思、工具使用、规划）。^[可能是目前最好的Agent课程！吴恩达官宣新课《Agentic AI》，手把手教你构建AI智能体.md]

详见 [[agentic-ai]]。

## MIA：记忆增强的持续进化 Agent

## MIA：记忆增强的持续进化 Agent

MIA 框架解决 Agent 的"失忆"问题，核心突破在于**双记忆机制**（非参数记忆沉淀经验 + 参数记忆吸收能力）：^[新一代记忆智能体框架MIA：让智能体告别「失忆式工作」，在持续进化中变强.md]

### Planner–Executor–Manager 架构

- **Planner**：战术大脑，制定研究计划，测试时持续学习实时调整策略
- **Executor**：执行专家，解读并遵循复杂研究蓝图
- **Manager**：优化记忆存储，消除冗余

### 交替强化学习

- 阶段一：固定 Planner → Executor 学会严格执行规划
- 阶段二：固定 Executor → Planner 学会利用记忆生成更优计划 + 反思重规划
- 解决"规划很好，执行跟不上"的问题

### 测试时持续学习

推理阶段不再冻结：执行任务生成多条候选路径 → 从成功/失败路径提取非参数化记忆 → 基于成功路径在线更新参数化记忆。推理与训练几乎同步完成。

### 自进化评估

用"过程质量"替代"结果标签"：逻辑评审员 + 事实评审员 + 结果评审员 + 领域主席综合决策。

### 实验结果

7B 执行器的 MIA 超越不调用工具的 GPT-5.4 / GPT-4o / Gemini-2.5-Pro，逼近 Gemini-3-Flash。

与 Skill 的互补关系：Skill 蒸馏静态知识（L1 精度），MIA 积累动态经验（参数记忆更新试图捕捉隐性能力）。

## 多 Agent 协作的规模效应

SkillsBench 数据显示 2-3 个 Skill/Agent 协同效果最好（+18.6pp），4 个以上反而只提升 5.9pp。模块化有收益，但存在最优粒度。^[
严肃聊聊，Skill到底能蒸馏我们的几分之几？｜Hao好聊趋势.md
]
