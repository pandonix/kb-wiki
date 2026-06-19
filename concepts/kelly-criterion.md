---
title: Kelly 公式（Kelly Criterion）
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [invest, decision-making]
sources:
  - raw/papers/2026-06-18-Evaluating-gambles-using-dynamics.md
  - raw/papers/2026-06-18-The-ergodicity-problem-in-economics.md
confidence: medium
---

# Kelly 公式（Kelly Criterion）

## 定义

Kelly 公式是一个确定最优下注比例 f 的方法，目标是在重复投注中最大化财富的**长期指数增长率**（而非单次期望收益）。

标准形式：对于赢时回报 b:1、赢概率 p、输概率 q 的赌局，最优下注比：

```
f* = (bp - q) / b = p - q/b
```

或其等价的增长率形式：

```
g(f) = p·log(1 + bf) + q·log(1 - f)
```

最大化 g(f) 的 f 即为 Kelly 最优比例。

## 核心直觉

Kelly 不是让你「赌最大」，而是让你「长得最快」。

- 下注太少（f → 0）：增长率趋近于 0，浪费机会
- 下注适中（f = f*）：长期增长率最大
- 下注太多（f > f*）：波动放大，增长率反而下降，甚至变为负（财富长期缩水）^[raw/papers/2026-06-18-Evaluating-gambles-using-dynamics.md]

与直觉相反：超过 Kelly 比例后，下注更多不仅赚不到更多，反而会亏钱。

## 在遍历经济学中的位置

Kelly 公式不是孤立的下注技巧。Ole Peters 指出，它是**遍历经济学在乘法动态下的操作特例**：^[raw/papers/2026-06-18-Evaluating-gambles-using-dynamics.md]

1. 财富过程是乘法：W → rW（而非加法 W → W + ΔW）
2. 在乘法动态下，正确的遍历可观测量是 ⟨ΔlogW⟩（而非 ⟨ΔW⟩）
3. Kelly 最大化 ⟨ΔlogW⟩，即时间平均增长率

## 常见误区

- **误区**：「Kelly 太激进了」→ 半 Kelly 的确更安全，但这不是 Kelly 的问题，而是参数估计不确定性下的合理调整
- **误区**：「Kelly 只适用重复独立赌局」→ Kelly 假设重复独立，但框架可推广到相关、非稳态、多资产场景
- **误区**：「Kelly = 期望效用理论的特例」→ Peters 不这么看。Kelly 从动态出发（最大化增长率），效用理论从偏好出发（最大化期望效用）。形式相似但理论根基不同

## 相关概念

- [[ergodicity-economics]] — 遍历经济学：Kelly 在遍历增长率框架中的位置
- [[ole-peters]] — Ole Peters：将 Kelly 置于更大理论框架
- [[risk-management-ergodicity]] — 风险管理：非遍历系统中的破产边界
- [[howard-marks-investing]] — 周期思维与下注比例
- [[quant-backtesting]] — 量化回测：参数不确定性下如何估计 Kelly 比例
