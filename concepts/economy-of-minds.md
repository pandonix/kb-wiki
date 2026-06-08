---
title: Economy of Minds — 市场经济式多 Agent 协调
created: 2026-06-08
updated: 2026-06-08
type: concept
tags: [ml, agent, coding, infra, research]
sources: [raw/articles/AI 不会合作？那是因为他们没见过市场经济｜Hao好聊趋势.md]
confidence: medium
---

# Economy of Minds — 市场经济式多 Agent 协调

## 核心定义

Economy of Minds（EOM）是哈佛和 MIT 的 Sham Kakade & Yilun Du 在 2026 年 6 月提出的多 Agent 协调框架。其核心主张：**不依赖中央 orchestrator，而是通过市场经济机制让 Agent 自主分工、定价和演化**。^[raw/articles/AI 不会合作？那是因为他们没见过市场经济｜Hao好聊趋势.md]

与 Orchestrator-Worker 模式的根本区别：后者是「设计合作结果」（人写编排规则），前者是「设计合作条件」（让合作在经济压力下涌现）。

## 四大机制

### 1. 拍卖（Auction）

任务到来时，所有满足条件的 Agent 各自出价，出价最高者赢得执行权。出价本身就是信息披露——Agent 愿意出高价意味着对自己的能力有信心，系统不需要理解推理过程。

### 2. 桶旅式信用分配（Bucket-Brigade Credit Assignment）

下游 Agent 花钱购买上游 Agent 的输出。A 拆解问题 → B 购买 A 的结果推导公式 → C 购买 B 的结果验证 → 用户支付终端奖励给 C。下游愿意掏多少钱接盘，就是对上游工作价值最精确的市场定价。不需要任何评委打分。

### 3. 经济自然选择（Economic Natural Selection）

每个 Agent 有银行账户记录累积收支。赚钱的 Agent 被克隆（system prompt 微调变异），亏损到零的 Agent 被删除替换为随机新 Agent。进化选择压力发生在 **prompt 空间**而非参数空间——LLM 权重全程冻结。

### 4. 新手保护（Novice Rule）

新生成 Agent 首次出价强制设为当前最高竞标者 + ε，保证至少一次执行机会。表现好就赚回来，表现差一次亏损后快速破产退出。防止市场被已有富 Agent 垄断。

## 实验结果

在 MATH benchmark、HumanEval 代码生成、创意写作、ALFWorld 多步骤规划、科研文献综述五个领域，用 50 个 Agent（GPT-4 Turbo）运行 200 轮任务：

- **所有领域超过单 Agent 基线、Best-of-N 采样和编排式多 Agent（AutoGen 风格）** ^[raw/articles/AI 不会合作？那是因为他们没见过市场经济｜Hao好聊趋势.md]
- MATH: +8.3% vs Best-of-16
- HumanEval: +11.7%
- ALFWorld: +23.4%（越需要多轮迭代和自动纠错，优势越大）

消融实验：关掉拍卖 -12%，关掉桶旅支付 -9%，关掉经济选择 -15%，关掉新手规则 -7%。四个零件都不可或缺。

## 四大理论定理

1. **出价收敛**：市场选择驱动 Agent 出价趋近其真实价值
2. **终端奖励充分**：仅凭最终结果就够了，桶旅式支付自动分解到每一步
3. **渐近最优**：对标全知全能编排者的性能差距随时间趋于零——计划经济的理论上限，市场经济在足够时间后收敛到
4. **信用分配近似 Shapley 值**：桶旅式支付在理论上和最精密的公平分配方案等价

## 反直觉发现：通才无法垄断

通才 Agent（可访问全部工具）在一群专才中短暂扩张后收缩，专业化的族群持续繁殖。每个 Agent 输出预算有限（平均 128 tokens），通才把能力摊薄在所有领域，专才在每个单一领域做到极致——在任何单一领域，专才的精细度碾压通才。

## 当前局限

论文为理论清晰做了激进简化，每个简化都是研究方向：

- **冻结权重**：适应只在 prompt 空间，天花板有限
- **强制匿名**：Agent 互不知身份，丢掉整个信任/声誉维度
- **无 Agent 记忆**：每次被选中执行时对历史一无所知，无法渐进学习
- **未引入训练端**：如果在训练阶段就引入多 Agent 环境（multi-agent RL），模型可能从权重层面学会合作

## 产业意义

EOM 证明的不是「多 Agent 合作的终极方案」，而是「市场机制 + 无编排这条路在原理上可行」。当 Agent 进入交易、投资、供应链、合规等多行为者环境时，单边优化可能破坏系统均衡。未来需要把协调层、激励层、声誉机制和失败恢复做成 agent runtime 的一等能力。

## 相关概念

- [[multi-agent-collaboration]] — 多 Agent 协作模式（Orchestrator-Worker vs 市场机制）
- [[solipsistic-superintelligence]] — 为什么 LLM 天生不擅长合作
- [[agent-skills]] — 专才 vs 通才的竞争动态
- [[harness-engineering]] — 市场机制作为 harness 设计的新范式
