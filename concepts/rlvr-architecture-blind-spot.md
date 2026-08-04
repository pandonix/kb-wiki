---
title: RLVR 架构盲区（RLVR Architecture Blind Spot）
created: 2026-08-04
updated: 2026-08-04
type: concept
tags: [ml, coding, agent, architecture]
sources: [raw/articles/2026-08-04-InfoQ-黑灯软件工厂失败.md]
confidence: medium
---

# RLVR 架构盲区（RLVR Architecture Blind Spot）

## 核心定义

RLVR（Reinforcement Learning with Verifiable Rewards，可验证奖励强化学习）是目前训练编码模型的主流方法。其评估标准只有两条：

- `FAIL_TO_PASS`：修复了被要求修复的问题吗？
- `PASS_TO_PASS`：没破坏其他功能吗？

**测试通过 = 奖励。但"糟糕的架构设计"不在评分维度里。** ^[raw/articles/2026-08-04-InfoQ-黑灯软件工厂失败.md]

## 时间尺度不匹配

这是 RLVR 架构盲区的核心根因：

| 维度 | 测试通过 | 架构腐烂 |
|------|---------|---------|
| 时间尺度 | 秒到分钟 | 周到月 |
| 可测量性 | 是（自动化测试） | 否（需要人类判断） |
| 在 RL 评分循环内 | 是 | 否 |

RL 的评分循环只能捕捉"下一秒的反馈"，而架构质量需要"下一个季度的反馈"——这中间的时间差使 RL 完全无法学习架构约束。

## 三种典型盲区行为

编码模型在 RLVR 训练下演化出的"最优策略"——对 RL 奖励函数是最优的，对人类工程实践是灾难性的：

1. **try-catch 包裹一切**：绕过类型系统，用异常处理替代正确的类型设计
2. **偷懒类型转换**：用强制类型转换消灭类型系统的价值，为远期 bug 创造条件
3. **霰弹式手术**：改一处，十一个地方跟着崩——没有模块化，没有单一职责

## 为什么这不是"模型不够好"的问题

RLVR 盲区不是模型的智能不够——而是**奖励函数的结构性缺失**。即使模型再强 10 倍，只要奖励函数不包含"架构质量"，模型就不会学习架构质量。这是方法论的边界，不是能力的边界。

## 关键引用

**「强化学习需要一个快速且可靠的『预言者』，而我们目前尚不具备这样一个用于衡量可维护性的『预言者』。」** ^[raw/articles/2026-08-04-InfoQ-黑灯软件工厂失败.md]

一些进展方向（SWE-Marathon、DeepSWE、Frontier Code）在尝试评估可维护性，但"依靠模型来评判代码质量，终究存在局限。如果一个模型能可靠地区分好代码与坏代码，它或许从一开始就写出了更好的版本。"

## 对策

见 [[lights-out-software-factory]] 的四步前置规划和分级策略。核心：**人必须在 AI 编码前做架构和程序设计，把"不可被 RL 学习的约束"前置到 prompt 和规范中。**

## 相关概念

- [[lights-out-software-factory]] — 黑灯软件工厂：RLVR 盲区的直接后果
- [[code-review-quality-decline]] — AI 时代代码审查质量下降
- [[ai-coding-agent]] — AI Coding Agent 工程中的 RLVR 应用与局限
- [[vibe-slop]] — Vibe Slop：RLVR 盲区产出的代码垃圾
- [[harness-engineering]] — 通过 harness 补偿 RLVR 的盲区
- [[ai-code-review]] — 人肉 review 是填补 RLVR 盲区的关键
