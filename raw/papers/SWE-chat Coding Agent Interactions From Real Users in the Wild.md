---
source_url: "https://arxiv.org/abs/2604.20779v1"
ingested: 2026-05-08
sha256: "b342952d92c2b0ab9fe2607b154830ee0aac9d72eef13d09e3df908b9e172b1a"
---

# SWE-chat: Coding Agent Interactions From Real Users in the Wild

> ArXiv: <https://arxiv.org/abs/2604.20779v1>
> Authors: Joachim Baumann, Vishakh Padmakumar, Xiang Li, John Yang, Diyi Yang, Sanmi Koyejo
> Date: 2026-04-23
> Tags: #论文 #ArXiv #CodingAgent #SoftwareEngineering #Benchmark

## 一句话总结

这篇论文最有价值的地方，不是证明 coding agent 又强了多少，而是第一次用真实世界的大规模交互数据告诉我们，今天的 coding agent 已经被大量采用，但离高效、可靠、低风险地自主完成开发还差得很远，当前最优形态更像是高频纠偏的人机协作，而不是彻底放手的全自动开发。

## 1. 这个 benchmark / dataset 属于哪个领域，解决什么问题？

这是一个面向 coding agent、软件工程智能体、人机协作开发的真实世界数据集与分析论文。

它要解决的核心问题是：

- 真实用户到底怎么用 coding agent
- agent 生成的代码到底有多少真的被接受
- 失败通常怎么发生，用户又是怎么补救的

现有评测大多还是人工挑题、任务边界清楚、成功标准明确，更像考试题。真实开发里则有多轮来回、需求澄清、中途打断、agent 跑偏后被纠正，以及大量并非纯“写代码”的任务。

## 2. 数据规模多大，评测环境是什么，有没有具体例子？

### 数据规模

SWE-chat 当前包含：

- 约 6,000 个 coding sessions
- 超过 63,000 条 user prompts
- 约 355,000 次 agent tool calls
- 约 2.7 million logged events

### 数据来源 / 环境

数据来自：

- 公开 GitHub 仓库
- 开发者主动 opt-in
- Entire.io CLI checkpoint logging

覆盖的 agent 包括：

- Claude Code
- OpenCode
- Gemini CLI
- Cursor
- Factory AI Droid

论文说明，约 85% 数据来自 Claude Code。

### 记录内容

SWE-chat 保留了整条真实轨迹：

- 用户 prompt
- agent 回复
- tool calls
- 文件读写
- shell 命令
- token usage
- 代码 diff
- 人类 vs agent 的代码归因

### 具体例子

论文里一个典型低成功案例是：用户要求修复历史列表卡片滚动时动画过慢的问题，agent 连续两次都改错参数，用户不断纠正，最后 session 没解决，也没有 commit。

这说明 agent 常见问题不是不会写，而是理解错问题对象后继续在错误方向上推进。

## 3. 同类 benchmark 有哪些，它和已有 benchmark 有什么区别？

已有相关数据集包括：

- SWE-smith-trajectories
- CoderForge-Preview
- SERA
- nex-agi-agent-sft
- SWE-rebench-openhands-trajectories
- Agent Trajectories
- Multi-SWE-bench_trajs
- Agent Data Protocol
- AIDev
- AgentPack

SWE-chat 的关键区别是，它是第一个同时具备以下四类信息的数据集：

- 真实 human prompts
- agent tool-use trajectories
- code diffs
- code attribution（人类 / agent 代码归因）

它最大的优势是：

1. 关注真实使用，而不是只看 benchmark 分数
2. 把交互过程本身变成可分析对象
3. 可以衡量 agent 写的代码最终到底活下来多少

## 4. 它怎么评估，主要结果是什么，有什么关键分析？

### 4.1 评估方法 / 指标

论文做了四类核心分析：

#### A. 行为统计

包括：

- 用户 intent 分布
- tool call 分布
- session turn 数量
- coding mode 分布
- user persona 分布

#### B. LLM judge 标注

包括：

- Session success
- User persona
- Prompt intent
- User pushback

#### C. 代码效率指标

包括：

- Agent-authored %
- Coding efficiency
- Code survival rate
- Token efficiency
- Cost efficiency
- Time efficiency
- Agent runtime efficiency

#### D. 安全性分析

用 Semgrep 分析 commit 前后快照，统计新增和修复的安全漏洞。

### 4.2 关键结果一：真实世界里常见任务并不只是写代码

论文发现，最常见的具体 intent 之一是：

- understand existing code / behavior，占 19.0%

此外还有：

- create new code
- git operations
- debugging
- refactor
- test
- connect

这说明很多 benchmark 过度聚焦“写 patch”，而忽略了理解代码、查上下文、跑命令这些真实开发中的高频任务。

### 4.3 关键结果二：tool use 很重，bash / git 占比很高

约三分之一 tool calls 是 bash commands，很多还是 git 相关操作。

真实 coding agent workflow 更像：

1. 搜索
2. 读文件
3. 跑命令
4. 局部改动
5. build / test / git

### 4.4 关键结果三：coding mode 呈现双峰分布

论文定义三类 coding mode：

- Human-only coding: 22.7%
- Collaborative coding: 36.5%
- Vibe coding: 40.8%

并指出 vibe coding 在 3 个月观察窗口里，从约 20% 上升到 40%+。

### 4.5 关键结果四：vibe coding 在现实里并不高效

关键数据：

- 所有 agent 产出的代码里，最终只有 44.3% 活进 commit
- vibe coding 的 survival rate 更高，但 token / cost / time 也显著更高
- 每 100 行 committed code，vibe coding 的 token 消耗约是 collaborative 的 3 倍

也就是说，全自动开发往往伴随大量废代码和更高的监督成本。

### 4.6 关键结果五：协作式人机共写反而更高效

论文隐含的重要结论是：

- collaborative sessions 是当前观察到的更高性价比模式

这说明现实中的最优解更像人机分工协作，而不是完全放手给 agent。

### 4.7 关键结果六：安全风险明显更高

Semgrep 分析结果：

- Human-only: 0.08 vulnerabilities / 1K lines
- Collaborative: 0.14
- Vibe coding: 0.76

也就是：

- vibe coding 引入漏洞速率约为 human-only 的 9 倍
- 约为 collaborative 的 5 倍

提到的漏洞类型包括：

- path traversal
- command injection
- unsafe format strings
- SQL injection

### 4.8 关键结果七：agent 很少主动澄清，但用户经常打断和纠偏

论文发现：

- agent 主动 ask for clarification 的比例只有 1.1% - 2.6%
- 用户会在 3.3% - 6.0% 的 turn 中直接打断
- 用户在约 39% 的 turn 里出现 pushback

作者一个很值得记住的判断是：

> Autonomy is outpacing oversight.

## 5. 作者有没有提出新的模型 / agent？

没有。

这篇论文的主要贡献是：

- dataset
- measurement
- empirical findings
- future evaluation direction

不是提出一个新的 coding agent 方法。

## 我觉得最值得吸收的 5 个判断

1. 真实 coding agent 任务，远不只是写 patch
2. agent 写了很多，不等于真正有价值
3. collaborative 才是当前更现实的最优点
4. vibe coding 越来越流行，但风险也更高
5. 下一代 benchmark 应该评测协作过程，而不是只评测结果 patch

## 对当前工作流的直接启发

### A. 不该只优化“最后写代码”

更应该优化：

- 理解阶段
- 澄清阶段
- 中间 review 节点
- 中断与纠偏机制
- 安全扫描与验收

### B. 一主一审的路子是对的

像 Codex 主开发、Claude 审查这种分工，比单 agent 一把梭更符合论文揭示的现实。

### C. 未来真正有价值的是“监督成本最小化”

重点不是让 agent 看起来更 autonomous，而是让它在关键节点：

- 主动问对问题
- 不乱冲
- 更少返工
- 更少引入隐患

## 论文局限

- 数据来自公开仓库 + opt-in 用户
- 偏早期 adopter
- 大量数据来自 Claude Code
- 企业私有代码库没覆盖
- 放弃 commit 的失败可能未被充分记录

所以它大概率高估了 agent 的成功率和效率。

## 结论

如果把这篇论文压成一句更狠的话：

> coding agent 已经进入真实生产使用，但当前主问题已经不是“能不能写代码”，而是“在真实协作中，它到底值不值、稳不稳、安不安全，以及人类要为它付出多少监督成本”。
