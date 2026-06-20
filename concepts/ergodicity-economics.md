---
title: 遍历经济学
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [invest, paper, decision-making]
sources:
  - raw/papers/2026-06-18-Evaluating-gambles-using-dynamics.md
  - raw/papers/2026-06-18-The-ergodicity-problem-in-economics.md
confidence: medium
---

# 遍历经济学（Ergodicity Economics）

## 核心问题

**一个人赌一次，和一千个人各赌一次，不是一回事。** 遍历经济学由 Ole Peters 提出，核心批判是：经济学长期将「群体平均」（ensemble average，很多人同时做一次的平均结果）当成「时间平均」（time average，一个人反复做很多次的长期结果）来用，而这在财富过程不满足遍历性时会系统出错。^[raw/papers/2026-06-18-The-ergodicity-problem-in-economics.md]

## 关键概念

### 遍历性

如果一个量沿时间走出来的平均值，等于很多个平行副本同一刻的平均值，这个量是**遍历的**（ergodic）。

类比：一个人每天吃一家餐厅，吃一百天后的平均体验；和一百个人同一天各吃一家餐厅后的平均体验。两者相等才可以用后者替代前者。

**财富增长通常不遍历。** 原因有三：^[raw/papers/2026-06-18-Evaluating-gambles-using-dynamics.md]

1. **乘法动态**：财富是按比例变化（×1.5, ×0.6），不是加减固定金额。群体平均会被少数暴富路径拉高，但典型个人的路径大概率衰减
2. **路径依赖**：今天亏损会减少明天可下注的本金，各轮结果不独立
3. **吸收边界**：破产（财富→0）是进去就出不来的状态，后面的高收益对已出局者没意义

### 乘法动态 vs 加法动态

**加法动态**：W → W + ΔW，每轮加减固定金额。正确指标是期望财富变化 ⟨ΔW⟩/Δt。适合小额、固定金额、不改变本金结构的场景（如工资、小额赌注）。

**乘法动态**：W → rW，每轮按比例涨跌。正确指标是期望 log 财富变化 ⟨ΔlogW⟩/Δt，即**时间平均增长率**。适合投资、下注、项目资本等场景。^[raw/papers/2026-06-18-Evaluating-gambles-using-dynamics.md]

### 核心示例：硬币赌局

正面：财富 +50%（×1.5），反面：财富 -40%（×0.6）。

- 期望值：0.5×50% + 0.5×(-40%) = +5% → 看起来该玩
- 典型路径：一正一反后 → 1.5×0.6 = 0.9 → 只剩 90%，多玩几轮大概率越玩越穷
- 时间平均增长率：⟨ΔlogW⟩ = 0.5×ln(1.5) + 0.5×ln(0.6) ≈ -5.3% → 不该玩

**群体平均 +5%，但时间增长率 -5.3%。** 这就是遍历性缺失的核心：对一群人做一次的统计，误导了一个人反复做的决策。^[raw/papers/2026-06-18-The-ergodicity-problem-in-economics.md]

## 与期望效用理论的差异

| 视角 | 期望效用理论 | 遍历经济学 |
|------|------------|-----------|
| log(W) 性质 | 人的心理效用函数（凹→风险厌恶） | 乘法财富过程的正确坐标变换 |
| 风险厌恶来源 | 个人性格/偏好 | 财富动态的物理要求 |
| 推理方向 | 从偏好到决策 | 从动态到应优化的可观察量 |

**汇合**：两边都可能写出 log(W)，但含义不同。Peters 的转身是：不是「人怕风险所以用 log 效用」，而是「在乘法世界里，看 log 财富变化才是对的测速仪」。^[raw/papers/2026-06-18-The-ergodicity-problem-in-economics.md]

## 与 Kelly Criterion 的关系

Kelly 公式 `g(f) = p⋅log(1+bf) + q⋅log(1-f)` 正是遍历经济学在乘法动态下的操作版——最大化时间平均指数增长率。Kelly 不是孤立的下注技巧，而是一个更大原则的特例：^[raw/papers/2026-06-18-Evaluating-gambles-using-dynamics.md]

1. 先指定财富动态（加法或乘法）
2. 再找这个动态下的遍历可观测量（加法：⟨ΔW⟩，乘法：⟨ΔlogW⟩）
3. 最后最大化这个可观测量

## 实践启示

### 决策前置问题

面对任何带风险的选择，先问五个问题：

1. 这是很多人平均，还是一个主体沿时间反复执行？
2. 成功和失败能不能共享？
3. 失败会不会降低下一轮本金/权限/信用？
4. 是否存在出局点或不可恢复损失？
5. 我们优化的是静态平均，还是长期增长率？

### 应用领域

- **投资**：不要只看年化期望收益，先判断是加性还是乘性动态，再评估时间增长率和破产边界
- **AI 项目**：不要只看单次 demo 的平均效果，问每次使用后组织能力是复利增长还是一次性消耗
- **职业选择**：每一步收益没有「这一步是否缩窄或扩大后续选择空间」重要

## 相关概念

- [[ole-peters]] — Ole Peters，遍历经济学创始人
- [[risk-management-ergodicity]] — 风险管理与遍历性：非遍历系统中的生存优先
- [[second-order-thinking]] — 二阶思维：追问「结果的结果」
- [[black-swan-bayesian]] — 黑天鹅与贝叶斯：模型之外的不确定性
- [[kelly-criterion]] — Kelly 公式：最大化长期复合增长
- [[quant-backtesting]] — 量化回测框架：遍历性缺失与回测过拟合共享底层逻辑
- [[backtesting-overfitting]] — 回测过拟合：时间序列中的多重测试问题
- [[marcos-lopez-de-prado]] — 量化金融方法论的批判与重建
- [[investment-regime]] — 投资 Regime：regime 切换中遍历性缺失的典型场景
- [[financial-ml-research-hygiene]] — 金融ML研究卫生：研究流程中的遍历性陷阱
- [[howard-marks-investing]] — 周期思维与风险优先
- [[berkshire]] — 巴菲特/芒格的「不输」哲学与长期复合增长
- [[household-asset-allocation]] — 家庭资产配置中的本金保全
