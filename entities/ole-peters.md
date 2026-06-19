---
title: Ole Peters
created: 2026-06-19
updated: 2026-06-19
type: entity
tags: [person, invest, paper]
sources:
  - raw/papers/2026-06-18-Evaluating-gambles-using-dynamics.md
  - raw/papers/2026-06-18-The-ergodicity-problem-in-economics.md
confidence: medium
---

# Ole Peters

Ole Peters 是遍历经济学（Ergodicity Economics）的创始人，伦敦数学实验室（London Mathematical Laboratory）研究员。他的核心贡献是**将遍历性概念引入经济学决策理论**，指出经济学中长期将「群体平均」与「个人时间平均」混为一谈的底层问题。

## 核心贡献：遍历经济学

Peters 的核心主张：当财富过程是乘法（比例增长）而非加法时，**期望值不是正确的决策指标**。应该优化的不是「很多人同时玩一把的平均结果」，而是「一个人反复玩下去的长期增长率」。^[raw/papers/2026-06-18-The-ergodicity-problem-in-economics.md]

这个框架将传统的「风险厌恶」从心理偏好重新解释为**乘法财富动态下必须使用对数坐标**的物理必然。log(W) 不是人的心理效用曲线，而是乘法财富过程的正确测速仪。

## 关键论文

- **The ergodicity problem in economics** (Nature Physics, 2019) — 一篇 Perspective 文章，以硬币赌局为锚点，系统阐述遍历性缺失如何导致期望效用理论将「动态必须」误读为「心理偏好」
- **Evaluating gambles using dynamics** (Peters & Gell-Mann, Chaos, 2016) — 技术论文，提出赌局评估必须先指定财富动态（加法 vs 乘法），再选择对应的时间平均可观测量。将 Kelly criterion 置于遍历增长率框架内

## 思想谱系

Peters 的工作串联了一条被忽视的技术线索：

- **Huygens**（1657）：用在加法动态下的线性期望
- **Bernoulli**（1738）：引入 log utility，但将物理必要性与心理解释混在一起
- **Laplace**（1814）：实际上写出了乘法动态下的期望 log 财富变化（增长率）
- **Kelly**（1956）：利率视角下的最优下注——最大化 log 财富的期望，即最大化时间平均增长率

Peters 的贡献是把这条线讲清楚：**效用函数的凹性不是心理学，而是财富乘法动态在 log 空间里变成可加量后的自然投影**。^[raw/papers/2026-06-18-Evaluating-gambles-using-dynamics.md]

## 争议

旅程经济学并非没有争议。Nature Physics 曾刊出经济学家评论《Economists' views on the ergodicity problem》，主要争议点是：经济学家认为他们并非完全没处理动态、市场、保险和偏好问题；Peters 认为主流仍把时间平均放在辅助位置，而非基础对象。^[raw/papers/2026-06-18-The-ergodicity-problem-in-economics.md]

## 相关概念

- [[ergodicity-economics]] — 遍历经济学：遍历性、时间平均增长率、乘法动态
- [[risk-management-ergodicity]] — 风险管理与遍历性：非遍历系统中的生存优先
- [[kelly-criterion]] — Kelly 公式：最大化长期复合增长的最优下注比
- [[marcos-lopez-de-prado]] — 量化金融中回测过拟合与多重测试的批判
- [[quant-backtesting]] — 量化回测框架，遍历性对回测设计的启示
