---
title: 前沿部署工程师（Forward Deployed Engineer for AI）
created: 2026-05-29
updated: 2026-05-29
type: concept
tags: [agent, coding, management]
sources: [raw/articles/2026-05-28-AI越强人越忙一个住在未来的人说了什么.md]
confidence: medium
---

# 前沿部署工程师（Forward Deployed Engineer for AI）

## 核心定位

Dan Shipper（Every CEO）提出的概念：在 AI Agent 时代，组织内需要一种专门维护 Agent 的新角色——**前沿部署工程师**（Forward Deployed Engineer）。这个角色负责管理公司级的超级 Agent，确保 Agent 在复杂、长链路的真实业务中稳定运行并持续产生价值。^[2026-05-28-AI越强人越忙一个住在未来的人说了什么.md]

## 主要职责

- **Agent 维护**：Agent 会坏、会偏离、会需要 SSH 进服务器——需要有人照料
- **上下文管理**：保持 Agent 的知识库和上下文最新
- **权限治理**：分配和回收 Agent 的访问权限
- **质量监控**：检查 Agent 输出质量，处理错误和异常
- **工具编排**：设计 Agent 可用的工具链，持续优化工具 schema
- **错误归因**：分析 Agent 失败模式，将其沉淀为系统改进

## 与 Harness Engineering 的关系

前沿部署工程师实际上是在操作层面的 [[harness-engineering]] 实践。Harness 是 Agent 的运行时系统层，而 Forward Deployed Engineer 是这个系统的运维者。两者结合才能让 Agent 在真实任务中稳定工作。

## 岗位演化路径

Dan 预测的 Agent 部署路径：
1. **公司级通用 Agent** → 由 FDE 专责维护
2. → 模型更可靠 → 分裂出 **团队级 Agent**
3. → 进一步下沉 → **个人级 Agent**

这意味着 FDE 的职责会从「维护一个 Agent」演化为「维护一个 Agent 生态——设计框架、制定标准、治理权限」。^[2026-05-28-AI越强人越忙一个住在未来的人说了什么.md]

## 相关概念

- [[agent-owner-role]] — 每个 Agent 都需要一个人
- [[harness-engineering]] — Agent 的运行时层工程
- [[ai-native-organization]] — AI Native 组织的角色设计
- [[context-engineering]] — 上下文工程是 FDE 的核心技能
- [[fdx-forward-deployed-executive]] — FDX 前线部署高管：FDE 的进化，外置 CEO
- [[enterprise-ai-absorption-bottleneck]] — 企业 AI 吸收瓶颈：FDE/FDX 要解决的核心问题
