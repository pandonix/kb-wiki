---
title: 金融ML研究卫生（Research Hygiene）
created: 2026-06-20
updated: 2026-06-20
type: concept
tags: [invest, ml, paper]
sources:
  - raw/papers/2026-06-19-Advances-in-Financial-Machine-Learning.md
  - raw/papers/2026-06-19-Pseudo-Mathematics-and-Financial-Charlatanism.md
  - raw/papers/2026-06-19-The-Probability-of-Backtest-Overfitting.md
confidence: medium
---

# 金融ML研究卫生（Research Hygiene）

## 核心问题

**金融机器学习的难点不在模型聪不聪明，而在你有没有先把研究流程改造成一个防泄漏、防污染、防自欺的实验系统。** ^[raw/papers/2026-06-19-Advances-in-Financial-Machine-Learning.md]

金融数据不是独立样本——价格互相影响、样本重叠、标签泄漏、多重试验选择偏差。普通 ML 流程在金融上运行时，绝大多数漂亮回测不是因为模型发现了市场规律，而是因为数据、标签、验证和多重试验一起泄漏。^[raw/papers/2026-06-19-Pseudo-Mathematics-and-Financial-Charlatanism.md]

## 五大防污染工具

### 1. Triple-Barrier Labeling（三重障碍标注）

不要问「下一天涨还是跌」，而是模拟一笔真实交易：
- **上边界**：赚够目标，止盈出场
- **下边界**：亏到阈值，止损出场
- **右边界**：时间到了，未触及上下边界，也出场

**哪条边界先被碰到，就决定这个样本的标签。** 金融 ML 的对象不该是抽象价格方向，而应该是一个有入场、有风控、有持有期的下注。^[raw/papers/2026-06-19-Advances-in-Financial-Machine-Learning.md]

### 2. Purged Cross-Validation（清除交叉验证）

金融标签有寿命——一个样本从 10:00 入场持有到 11:30，另一个从 11:00 入场，两者共享了 11:00–11:30 的行情。如果前者在训练集、后者在测试集，模型就间接见过测试集。

**Purging**：清除训练集中和测试标签时间重叠的样本
**Embargo**：在测试集后面留一小段空白期，防止紧挨着的样本继续串水

```text
普通切分: 训练训练训练 | 测试测试测试
金融切分: 训练训练 [清除重叠] | 测试测试 | [禁入一段]
```

### 3. Meta-Labeling（元标注）

第一层模型给交易方向（球探），第二层模型判断「这次要不要跟」（教练）。
- 第一层：这球往哪边踢？
- 第二层：这球值不值得踢？

很多金融团队真正需要的不是一个全知模型，而是一个更会说「这次别上」的第二层模型。金融里假阳性很贵，一个会过滤低质量信号的模型往往比一个到处预测方向的模型更有用。^[raw/papers/2026-06-19-Advances-in-Financial-Machine-Learning.md]

### 4. Fractional Differentiation（分数阶差分）

用一种更温和的差分方法，让价格序列更稳定，同时尽量保留长期记忆。普通差分像把老藤剪到只剩新芽——确实干净，但丢了生长纹路。分数阶差分像修枝，尽量让数据可分析，又不把历史结构剪光。^[raw/papers/2026-06-19-Advances-in-Financial-Machine-Learning.md]

### 5. Deflated Sharpe Ratio（DSR，调整后夏普比率）

你试了 1000 个策略，挑出最好看的那个。即使每个策略都没真本事，最后也会有一个看起来像神。DSR 考虑多重测试、样本长度和收益分布的前四个矩，回答的是：**在你试过这么多东西之后，这个 Sharpe 还剩多少可信度？** ^[raw/papers/2026-06-19-Advances-in-Financial-Machine-Learning.md]

## 三重防线体系

López de Prado 系列论文建立了三层递进防线：^[raw/papers/2026-06-19-Pseudo-Mathematics-and-Financial-Charlatanism.md] ^[raw/papers/2026-06-19-The-Probability-of-Backtest-Overfitting.md]

| 层级 | 工具 | 问题 |
|------|------|------|
| **第一层：问题识别** | MinBTL、Hidden Trials | 你试了多少次？回测样本够长吗？ |
| **第二层：流程审计** | CSCV、PBO | 挑选冠军的流程本身有多大可能在自欺？ |
| **第三层：指标修正** | Deflated Sharpe、Probabilistic Sharpe | 扣掉多重试验成本后，edge 还剩多少？ |

### MinBTL（最短回测长度）

如果试了 N 个策略配置，想避免从纯噪声中挑出看起来 Sharpe 很高的策略，回测样本至少要多长？N 不公开，MinBTL 就没法算——**如果不报告试了多少个模型配置，就没法判断这个回测有多可疑。** ^[raw/papers/2026-06-19-Pseudo-Mathematics-and-Financial-Charlatanism.md]

### PBO/CSCV（回测过拟合概率 / 组合对称交叉验证）

- **PBO**：样本内最优策略在样本外输给中位策略的概率
- **CSCV**：把历史切成 S 个连续片段，用所有对半组合轮流做样本内和样本外，观察样本内冠军在样本外的排名

如果样本内冠军到了样本外经常落到中位数以下，说明挑选流程大概率在挑噪声。**金融研究最该被验证的不是某个策略，而是「我们挑出这个策略的流程」。** ^[raw/papers/2026-06-19-The-Probability-of-Backtest-Overfitting.md]

## 迁移：超越金融

这套研究卫生框架可以迁移到所有「时间相关、反馈强、样本会串水」的场景：
- **AI 项目评测**：一个 demo 的成功可能和上一次 prompt、同一批测试样本、反复试错共享了大量信息。也需要 purging——把被反复调过的样本从真正验收集中拿掉
- **产品 A/B 测试**：只展示最好 case 本质上是在出售幸存者。记录完整的试验族，扣掉多重检验成本

## 相关概念

- [[backtesting-overfitting]] — 回测过拟合：DSR、FST、MinBTL、PBO 的原始讨论
- [[marcos-lopez-de-prado]] — Marcos López de Prado：这套方法论的提出者
- [[quant-backtesting]] — 量化回测框架：研究卫生在回测工程中的落地
- [[sharpe-ratio]] — 夏普比率：deflated Sharpe 修正的对象
- [[investment-regime]] — 投资 Regime：regime 切换是样本外验证的真正考验
- [[kelly-criterion]] — 凯利公式：参数估计误差≈研究卫生问题在仓位管理上的体现
