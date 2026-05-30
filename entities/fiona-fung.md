---
title: Fiona Fung
created: 2026-05-22
updated: 2026-05-22
type: entity
tags: [person, management, coding, agent]
sources: [raw/articles/AI 时代到底该怎么管一个工程团队.md]
confidence: medium
---

# Fiona Fung

Fiona Fung 是 Anthropic 旗下 Claude Code 和 Cowork 两条产品线的工程与产品负责人。此前在微软工作十二年（从 Visual Studio 做起），后在 Meta 带过 Facebook Marketplace 和 Instagram 的工程团队，2025 年 9 月加入 Anthropic。

## 核心管理理念

在 Code with Claude 2026 大会上的演讲中，Fiona 分享了 Claude Code 团队的真实管理经验：

### 软件工程的瓶颈已转移

过去瓶颈是「写代码慢」，现在转移到了验证、评审、跨职能协作和安全性。过去的流程都基于「写代码很贵」的假设设计，既然现在代码几乎免费，流程必须全部重构。

### 流程极少会自然消亡

组织只会一层层叠加 SLA、规章制度和评审。用 AI 改造工程团队的第一步是明确允许砍掉陈旧流程。

### 「少做什么」清单

- **六个月路线图** → JIT planning（即时规划），原型成本趋于零
- **设计文档** → 默认讨论媒介从文档变为 PR
- **产品评审会** → 内部 dogfooding（ant-fooding）代替 mock 评审

### 「多做什么」：Shift Left

把质量保障从交付端（人工测试）往源头推（自动化），因为角色边界正在模糊——设计师在提交代码，PM 也在提交 PR。

### 技术辩论：从白板到三个 PR

「当写代码变得轻而易举，无休止的争论就显得极其昂贵。」让 Claude 同时搓出三个版本的 PR，直接对比完整代码实现。

### 代码评审分工

- **Claude 做**：风格检查、lint 去重、回应评审意见、抓常规 bug、补全单元测试
- **人保留**：法律合规审核、安全敏感代码、产品 sense 和品味

### 组织形态

- 尽量扁平，所有小组共享一个团队 mission
- **经理必须从 IC（一线工程师）做起** —— 不愿意的趁早分开
- 代码是唯一的 source of truth
- 衡量指标：新人上手时间、PR 生命周期、Claude 辅助提交比例（但警告别死盯「AI 生成代码比例」）

### 三个未解决的问题

1. 工程师跨平台流转后，传统平台分队（iOS/Android）是否还有意义
2. 自动化评审要推到多远
3. 角色模糊后，如何让所有人感觉同样有产出感

## 相关概念

- [[ai-native-engineering-management]] — AI 时代工程团队管理实践
- [[hierarchy-to-intelligence]] — 科层制到智慧型组织
- [[management-taboos]] — 管理禁忌
- [[claude-code]] — 她负责的产品线（待建实体页）
