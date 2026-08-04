---
title: 黑灯软件工厂（Lights-Out Software Factory）
created: 2026-08-04
updated: 2026-08-04
type: concept
tags: [ml, coding, agent, architecture]
sources: [raw/articles/2026-08-04-InfoQ-黑灯软件工厂失败.md]
confidence: medium
---

# 黑灯软件工厂（Lights-Out Software Factory）

## 核心定义

"黑灯软件工厂"指**没有人读代码、没有人写代码、AI 全自动开发部署**的极端愿景。StrongDM、OpenAI Symphony 等在推这个概念：你就是瓶颈，模型已经足够好，代码是免费的，抓紧交付就好。^[raw/articles/2026-08-04-InfoQ-黑灯软件工厂失败.md]

## 为什么行不通

### 实证失败

- Dex Horthy（HumanLayer 创始人）亲身经历：2025.7 全面进黑灯模式，11 月三次灾难性故障后**整个代码库重写**，联合创始人花两周纯手写梳理模式
- Faros AI 报告：AI 编码工具普及后，PR 评审质量大幅下滑——评审留言变多但更敷衍，大量 PR 无评审合并，线上故障上升，人均缺陷增加

### 根因：RLVR 架构盲区

见 [[rlvr-architecture-blind-spot]]——黑灯工厂失败的根本原因不是"模型不够好"，而是 RL 训练机制本身不惩罚糟糕的架构设计。测试通过只需几秒，架构腐烂要数周数月才暴露——RL 的评分循环根本够不到这个时间尺度。

## 黑灯模式的三种典型失败

1. **try-catch 包裹一切**：模型用 try-catch 绕过类型系统，而不是正确使用类型
2. **偷懒类型转换**：消灭了类型系统的价值，为未来的 bug 埋下伏笔
3. **霰弹式手术**：改一处，十一个地方跟着崩——没有模块化意识

## 解法：把灯重新打开

Dex Horthy 的四步前置规划（30 分钟规划可节省数小时评审）：

1. **产品评审**：用户语言明确问题 + 成功标准 + HTML 原型
2. **系统架构**：序列图、端点契约、数据模型
3. **程序设计**（最被低估）：类型签名、方法签名、调用栈树——伪代码级别
4. **垂直切片**：不按技术栈横切，从中间向外扩展，每 100-200 行检查一次

### 分级策略
- 约 40% 任务：一次性 AI 生成或 1-2 轮反馈即可
- 中等规模：产品 + 系统设计
- 大项目：完整四步
- 大型重构：跳过产品设计，其余三步

## 约束理论（2026 版）

**追求 10-100 倍提效还要假装代码质量不重要 → 会失败。接受模型的真实约束 → 安全实现 2-3 倍提效。** 充分了解约束条件 → 在约束下优化系统 → 寻找效率杠杆 → **务必审阅代码。**

## 相关概念

- [[rlvr-architecture-blind-spot]] — RLVR 架构盲区：黑灯工厂的根因
- [[code-review-quality-decline]] — AI 时代代码审查质量下降
- [[vibe-slop]] — Vibe Slop：黑灯工厂产出的代码垃圾
- [[ai-coding-agent]] — AI Coding Agent 工程中的约束
- [[ai-code-review]] — AI 代码审查实践
- [[harness-engineering]] — 驾驭 Agent 的核心工程方法
- [[mythical-man-month]] — 人月神话：代码量≠产出
