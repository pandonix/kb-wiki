---
title: 每个 Agent 都需要一个人：Agent Owner 角色
created: 2026-05-29
updated: 2026-05-29
type: concept
tags: [agent, management, coding]
sources: [raw/articles/2026-05-28-AI越强人越忙一个住在未来的人说了什么.md]
confidence: high
---

# 每个 Agent 都需要一个人：Agent Owner 角色

## 核心洞察

Dan Shipper（Every CEO）提出的核心命题：**每个 Agent 背后都需要一个人（Every Agent needs a person）**。Agent 不是装上就能自动产生价值——它会坏、会偏离指令、需要权限和上下文维护、需要质量检查。Agent 会悄悄变得没用，除非有人在持续关心它在做什么。^[2026-05-28-AI越强人越忙一个住在未来的人说了什么.md]

## 为什么 Agent 需要 Owner

Dan Shipper 基于 Every 公司的实践发现了一个反直觉结论：AI 越强，人不一定越闲，反而会创造新的工作——管理自动化本身。Every 全员重度使用 Codex / Claude Code 等 AI 工具，按理公司应该更精简，但过去一年员工人数反而翻了一倍。原因正是每个 Agent 背后都需要一个人来照料。^[2026-05-28-AI越强人越忙一个住在未来的人说了什么.md]

Agent 需要 owner 的原因包括：

- **持续维护**：Agent 会坏，需要 SSH 进服务器，需要持续调整上下文和工具配置
- **权限治理**：Agent 需要权限才能工作，但权限需要有人分配和回收
- **质量门禁**：Agent 输出需要验证，错误需要归因和修复
- **上下文保鲜**：Agent 的上下文会过时，需要有人更新它的知识库
- **偏离纠正**：Agent 会逐渐偏离初始意图，需要人对齐

## Agent 部署的现实路径

现实路径并非「人各有 Agent」，而是分阶段推进：

1. **公司级通用 Agent**：整个公司共用一个挂载在 Slack 等协作工具里的 Agent，由专人维护（Forward Deployed Engineer）
2. **团队级 Agent**：随着模型更可靠，逐渐分裂出团队专属 Agent
3. **个人级 Agent**：最终下沉到个人层面

Shopify 和 Ramp 已有类似的公司级 Agent 实践。^[2026-05-28-AI越强人越忙一个住在未来的人说了什么.md]

## Forward Deployed Engineer（前沿部署工程师）

Every 内部已经设立了专门维护 Agent 的岗位，Dan 称之为「前沿部署工程师」（Forward Deployed Engineer）。这个角色的职责包括：维护公司级 Agent、处理 Agent 错误、优化上下文策略、治理 Agent 权限、确保 Agent 持续产生价值。

这与 [[harness-engineering]] 的框架高度一致——Harness 作为 Agent 的操作系统层，需要有人设计、维护和持续优化。

## 相关概念

- [[forward-deployed-engineer-ai]] — 前沿部署工程师的具体职责与定位
- [[harness-engineering]] — Harness 工程：Agent 的运行时层
- [[ai-native-organization]] — AI Native 组织的 Agent 主人角色设计
- [[agentic-ai]] — Agent 系统的设计与运维
- [[jevons-paradox-work]] — AI 创造新工作而非消灭工作的悖论
