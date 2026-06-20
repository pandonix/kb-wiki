---
title: 回测过拟合
created: 2026-05-22
updated: 2026-06-20
type: concept
tags: [invest, ml]
sources:
  - raw/articles/回测不是研究工具！专访Marcos López de Prado.md
  - raw/papers/2026-06-19-Pseudo-Mathematics-and-Financial-Charlatanism.md
  - raw/papers/2026-06-19-The-Probability-of-Backtest-Overfitting.md
confidence: medium
---

# 回测过拟合

Marcos López de Prado 对量化研究最核心的批判：**回测不是研究工具。** 大多数量化研究人员发现的模式是虚假的，因为金融领域的信噪比极低。

## False Strategy Theorem（虚假策略定理）

金融数学中的关键结论：**只要试验次数足够，即使真实夏普比率为零，回测也可以造出任意夏普比率。** 由于大多数金融论文未考虑测试次数，大部分所谓的「发现」很可能是伪阳性。

## 多重试验的数学本质

**试验次数越多，样本内最优 Sharpe 的期望值越高。即使所有策略的真实样本外 Sharpe 都是 0，你也能从一堆随机策略里挑出一个样本内 Sharpe 很漂亮的。** ^[raw/papers/2026-06-19-Pseudo-Mathematics-and-Financial-Charlatanism.md]

这接近金融欺诈的结构——骗子给很多人发预测，一半说涨一半说跌，每轮后只保留收到正确预测的人。你看到的是连续命中，不知道的是自己只是被筛到最后的观众。**只展示成功策略、不展示失败尝试，效果一样。** ^[raw/papers/2026-06-19-Pseudo-Mathematics-and-Financial-Charlatanism.md]

## Minimum Backtest Length（MinBTL，最短回测长度）

如果你试了 N 个策略配置，想避免从纯噪声里挑出一个看起来 Sharpe 很高的策略，回测样本至少要有多长？

这不是评价单个 Sharpe 显著不显著，而是评价**一组试验里「挑冠军」的偏差**。N 不公开，MinBTL 就没法算——**如果不报告试了多少个模型配置，就没法判断这个回测有多可疑。** ^[raw/papers/2026-06-19-Pseudo-Mathematics-and-Financial-Charlatanism.md]

## PBO（回测过拟合概率）与 CSCV（组合对称交叉验证）

PBO 是样本内最优策略在样本外输给中位策略的概率。CSCV 通过把历史切成多个连续片段、用所有对半组合轮流做样本内和样本外来计算它。^[raw/papers/2026-06-19-The-Probability-of-Backtest-Overfitting.md]

```text
样本内: 选冠军
样本外: 看冠军是不是变路人
PBO: 冠军变路人的频率
```

- **PBO 低**：样本内挑出来的策略，样本外通常也不错
- **PBO 高**：样本内冠军，样本外经常输给普通策略

衍生诊断：^[raw/papers/2026-06-19-The-Probability-of-Backtest-Overfitting.md]
- **Performance Degradation**：样本内越好，样本外是否越差（面试越会背题的人，入职后越不会干活）
- **Stochastic Dominance**：按样本内最优来选，是否真的优于随机抽签——如果不如，问题不在候选人，在选人机制

## Deflated Sharpe Ratio（DSR，调整后夏普比率）

通过考虑多重测试、样本长度和收益分布的前四个矩来估计策略绩效的显著性。不是问「Sharpe 高不高」，而是问「试了这么多次以后，这个 Sharpe 还剩多少可信度」。

## CPCV（组合清除交叉验证）

传统交叉验证在金融时间序列中存在泄漏问题。CPCV 通过组合方式清除（purge）训练集与测试集之间的信息泄漏，并估计夏普比率的分布而非仅其均值。

## 三层防线体系

| 层级 | 工具 | 问题 |
|------|------|------|
| 第一层：问题识别 | MinBTL、Hidden Trials | 试了多少次？样本够长吗？ |
| 第二层：流程审计 | CSCV、PBO | 挑选流程多大可能在自欺？ |
| 第三层：指标修正 | Deflated Sharpe、Probabilistic Sharpe | 扣掉多重试验成本后 edge 剩多少？ |

## 训练集过拟合 vs 测试集过拟合

- **训练集过拟合**：模型过于复杂，不仅捕捉信号还「学习」了噪声
- **测试集过拟合**：研究者通过反复调整策略参数和特征，隐式地「记住」了测试集

应对方法：正则化、早停（early stopping）、降维。

## 金融机器学习的特殊性

金融市场不同于物理系统——一个新风险因子的发现往往会影响其本身的盈利能力。因此金融机器学习应作为**独立研究领域**，需要专门为金融过程和样本挑战设计的算法（HRP、CPCV、DSR、PBO/CSCV）。

## 相关概念

- [[quant-backtesting]] — 量化回测框架
- [[marcos-lopez-de-prado]] — Marcos López de Prado 人物页
- [[risk-management-ergodicity]] — 风险管理与遍历性
- [[ergodicity-economics]] — 遍历经济学：多重测试与遍历性缺失共享底层逻辑
- [[financial-ml-research-hygiene]] — 金融ML研究卫生：从问题识别到流程审计的完整工具链
- [[sharpe-ratio]] — 夏普比率：deflated Sharpe 修正的对象
