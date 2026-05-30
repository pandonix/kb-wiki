---
title: Skill 蒸馏深度分析
created: 2026-05-08
updated: 2026-05-08
type: concept
tags: [ml, coding, philosophy]
sources: [raw/articles/严肃聊聊，Skill到底能蒸馏我们的几分之几？｜Hao好聊趋势.md, raw/articles/Agent Skills 终极指南：入门、精通、预测.md, raw/articles/担心被Skill替代的打工人发现：「根本不是那么回事」.md]
confidence: high
---

# Skill 蒸馏深度分析

## 核心定义

Skill 不是高级 prompt，而是一个可组合、可路由、可持久化的知识单元。浙大 SoK 论文定义 Skill = (C, π, T, R)：适用条件、执行策略、终止条件、可复用接口。^[
严肃聊聊，Skill到底能蒸馏我们的几分之几？｜Hao好聊趋势.md
]

万物皆可蒸馏？2026 年 GitHub Trending 上"同事 skill"把离职同事聊天记录喂给 Claude 生成 skill；exskill 蒸馏前任；老板 skills 复现老板风格；女娲 skill 用 6 个并行 Agent 蒸馏公众人物心智模型。但 anti-distill 轻松掏空 Skill 核心——说明蒸馏的只是一层特定东西。

## SkillsBench 实证数据（2026）

- 整体：加了 Skill 后平均通过率 +16.2pp
- 医疗健康：+51.9pp（从 34.2% → 86.1%）
- 软件工程：仅 +4.5pp（差 10 倍）
- Detailed 级 Skill：+18.8pp
- Comprehensive 级（面面俱到）：-2.9pp（越完整反而越差）
- SWE-Skills-Bench：80% 的 Skill 对通过率零改善

## 精度阶梯：L1 / L1.5 / L2

### L1 — 确定性注入（高精度）

- **陈述性知识**：新注入的专业事实和规则
- **程序性知识**：IF-THEN 产生式规则
- **扩散激活路由**：把模型已知但低激活的知识拉到前台
- 医疗飙升 51.9pp → 模型训练过诊断手册，Skill 做的是精准路由而非注入新知
- 软件仅 +4.5pp → 编程知识在代码语境下已是高激活状态

### L1.5 — 扩散激活（中精度）

- 风格化指令："说人话"、"多用短句"→ 给模型知识检索加权
- 范例锚定比抽象描述有效（Nosofsky 广义上下文模型）
- 但受 Goodman 欠定性约束：有限范例兼容无限模式
- 2-3 个 Skill 协同效果最好（+18.6pp），4 个以上反降（+5.9pp）

### L2 — Utility 不可编码（零精度）

- **冲突裁决**：知道什么时候优先级该翻转
- **维度爆炸**：架构决策同时权衡十几个因素，组合写不尽
- **Utility 本身不可表达**：CDSS 规则覆盖率 90%，但医生推翻系统多数时候是对的
- **写不得**：Polanyi 焦点/辅助意识——强行拉到焦点会破坏整合
- **认知负荷理论**：展开后元素交互性爆炸，带宽被淹没

## anti-distill 的启示

- 把 L1 规则抬升为"遵循团队规范"等空壳 → Skill 变废纸
- 本质：把高精度端推到低精度端
- 说明 Skill 的核心价值在 L1 层

## 回答"几分之几"

- **按时间量**：60%-80%（大部分工作时间做 L1 的事）
- **按价值量**：30%-40%（核心判断在 L2）
- 80% 时间节省 ≠ 80% 价值覆盖

## 蒸馏不会终止于 Skill

- RL + Preference Alignment 可直接蒸馏行为（跳过语言）
- Inference 期算力解锁 → 人类隐性偏好被 reward signal 拟合
- L1/L2 的护城河不像想象中坚固

## 相关概念

- [[agent-skills]] — Skill 的架构与使用
- [[ai-economy-impact]] — Skill 蒸馏对就业的影响
- [[copilot-learning]] — AI 辅助学习的认知效果
- [[ai-software-form-evolution]] — Skill 在软件形态演进中的角色
- [[utility-vs-skill]] — Utility与Skill：判断力与规则的深层张力
