---
title: Agentic Forecasting
created: 2026-04-24
updated: 2026-04-24
type: concept
tags: [ml, agent, research, stale]
sources: [raw/articles/Agentic Forecasting using Sequential Bayesian Updating of Linguistic Beliefs.md]
confidence: high
---

# Agentic Forecasting

## 核心问题

传统 LLM agent 在多轮检索中容易上下文膨胀——把所有检索到的内容不断追加到 context 里，信息越来越多，但真正关键的证据、反证、不确定点并没有被清楚维护。

论文的核心判断：**一个 agent 如果没有"结构化的当前信念表示"，即使有搜索能力，也很容易变成在一堆文本里漂。**^[
Agentic Forecasting.md
]

## 核心方法：BLF（Bayesian Linguistic Forecaster）

### Bayesian Linguistic Belief State

每一步 agent 都维护一个"语言化的信念状态"，包含：
- 当前对二元事件的概率估计 `p ∈ [0,1]`
- 置信度等级（low / medium / high）
- 支持 outcome 的关键证据
- 反对 outcome 的关键证据
- 还有哪些开放问题需要继续查

**信念状态不是只有一个概率数字，而是"概率 + 理由 + 反理由 + 下一步调查方向"的半结构化对象。**

### Agent Loop

1. 输入问题
2. LLM 在当前历史基础上，同时产出：下一步 action + 更新后的 belief state
3. 执行 action，拿到 observation
4. 把 action、observation、belief state 一起追加到历史
5. 循环，直到 submit

即：不仅选下一步做什么，还要同时明确说明"我现在为什么更相信/更不相信这个结论了"。

## 关键洞察

这其实让 agent 从"边搜边想"变成"边搜边更新自己的工作记忆"。Batch search then reason（先搜一批，再统一推理）缺少中间更新；BLF 的 Sequential Bayesian Updating 让 agent 能根据新证据及时改变搜索策略和判断。^[
Agentic Forecasting.md
]

## 相关概念

- [[ai-coding-agent]] — 更通用的 Agent 工程
- [[copilot-learning]] — 另一种 agent 研究
