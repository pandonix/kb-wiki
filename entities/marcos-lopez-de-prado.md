---
title: Marcos López de Prado
created: 2026-05-22
updated: 2026-06-20
type: entity
tags: [person, invest, ml]
sources:
  - raw/articles/回测不是研究工具！专访Marcos López de Prado.md
  - raw/papers/2026-06-19-Advances-in-Financial-Machine-Learning.md
  - raw/papers/2026-06-19-Pseudo-Mathematics-and-Financial-Charlatanism.md
  - raw/papers/2026-06-19-The-Probability-of-Backtest-Overfitting.md
confidence: medium
---

# Marcos López de Prado

Marcos López de Prado 是量化金融与机器学习交叉领域的权威研究者，曾任劳伦斯伯克利国家实验室研究员，著有多部金融机器学习著作。

## 关键贡献

### 微观阿尔法（Microscopic Alpha）

López de Prado 提出「微观阿尔法」概念，指只能通过先进量化方法和技术识别的细微市场异常。与之对应的是传统「宏观阿尔法」（如因子投资）。

类比黄金开采：宏观金矿（露天、易开采）已近枯竭，现代黄金开采进入微观层面——肉眼不可见的金，通过工业手段开采。历史上超过 50% 的黄金是过去 50 年通过工业手段开采的。微观阿尔法同样丰富且越来越丰富，但尚未被广泛开发。

### 阿尔法装配线（Alpha Assembly Lines）

灵感来自劳伦斯伯克利国家实验室的跨学科合作模式。将投资问题拆分为子问题，每个子问题归属明确的专业领域，由不同专业人员组成的团队协作解决。

对比传统量化研究「信息孤岛」模式：研究人员各自为战，成为什么都懂一点但鲜有精通的「通才」。

### 关键算法

- **HRP（分层风险平价）**：克服均值-方差优化的缺陷，尤其是噪声引起的不稳定性
- **NCO（嵌套聚类优化）** 与 **A2A（分配给分配者）**：投资组合构建算法
- **Deflated Sharpe Ratio（DSR，调整后夏普比率）**：解决回测过拟合问题，考虑多重测试、样本长度和收益分布的前四个矩
- **False Strategy Theorem（FST，虚假策略定理）**：证明只要试验次数足够，即使真实夏普比率为零，回测也能造出任意夏普比率
- **CPCV（组合清除交叉验证）**：估计夏普比率的分布而非仅其均值
- **Meta-Labeling（元标注）**：用第二个算法预测第一个算法的预测是否正确，牺牲部分召回率以提高精度

## 核心批判：回测不是研究工具

López de Prado 的核心观点：大多数量化研究人员发现的模式实际上是虚假的，因为金融领域的信噪比极低。由于大多数金融论文未考虑测试次数，大部分所谓的「发现」很可能是伪阳性。

金融机器学习不应被理解为「将机器学习应用于金融」，而应作为一个独立的研究领域，需要专门为金融过程和样本挑战设计的算法。

## 相关概念

- [[quant-backtesting]] — 量化回测框架与方法论
- [[backtesting-overfitting]] — 回测过拟合：DSR、FST、MinBTL、PBO 与稳健性验证
- [[financial-ml-research-hygiene]] — 金融ML研究卫生：Triple-Barrier、Purged CV、Meta-Labeling 的完整工具链
- [[risk-management-ergodicity]] — 风险管理与遍历性
- [[ergodicity-economics]] — 遍历经济学：群体平均与时间平均的区分
- [[ole-peters]] — Ole Peters：遍历经济学的理论来源
- [[sharpe-ratio]] — 夏普比率：deflated Sharpe 修正的对象
