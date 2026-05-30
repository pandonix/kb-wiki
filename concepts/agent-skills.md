---
title: Agent Skills
created: 2026-05-08
updated: 2026-05-08
type: concept
tags: [ml, coding, tool]
sources: [raw/articles/Agent Skills 终极指南：入门、精通、预测.md]
confidence: high
---

# Agent Skills

## 核心定义

Skills 是通用 Agent 的扩展包：模块化能力单元，打包了 LLM 指令、元数据、可选资源（脚本、模板等），Agent 会在需要时自动使用。2025 年 10 月 Anthropic 发布 Claude Skills，两个月后作为开放标准推出。^[
Agent Skills 终极指南：入门、精通、预测.md
]

## 与 MCP 的区别

- **MCP**：开放协议，关注 AI 如何统一调用外部工具/数据/服务，不定义任务逻辑
- **Skill**：教 Agent 完整处理特定工作，封装执行方法、工具调用方式和知识材料

## Skill 的架构

```
Skill 文件夹
├── SKILL.md          # 必需：元数据 + 技能指令（Level 1-2）
├── scripts/          # 可选：预写脚本，Agent 直接调用
├── ref/              # 可选：参考文档
└── assets/           # 可选：模板、素材资源
```

### 三级渐进披露

| 层级 | 内容 | 加载时机 | 大小建议 |
|------|------|----------|----------|
| Level 1 | 元数据（名称+描述） | 始终加载 | ~100 tokens |
| Level 2 | SKILL.md 正文指令 | 触发时加载 | <5000 tokens |
| Level 3 | 子技能/脚本/资源 | 按需动态加载 | 无限制 |

关键：Level 1 始终加载意味着可同时安装大量 Skill 而不占上下文。

## Skill 的三种加载模式

1. **显式调用**：用户 query 直接指定
2. **隐式匹配**：LLM 根据元数据描述自动匹配
3. **多 Skill 联用**：如 brand-guidelines + pptx 联合使用

## Skill 的三大核心优势

### 1. 零代码创建

- 最简形式：仅一个 SKILL.md，纯自然语言
- 复杂形式：包含脚本、向量数据库、Persona 模板
- 非技术人员可将专业经验写成文档，Agent 即可照执行

### 2. 突破预设限制

- Workflow/传统程序假设所有情况可预设 → 遇到意外就报错
- Skill + Agent 利用 LLM 推理智能，灵活应对边缘情况
- 示例：Agent 自适应切片（日期标题切分 vs 语义切分）

### 3. 多 Skill 自由联用

- N 个 Skill 可应对远超 N 的应用场景
- 示例：Web Scraping → PDF 提取 → Data Analysis → Brand PPTX

## Skill 设计的最佳实践

- SKILL.md 建议少于 5000 tokens
- 子技能拆分为子文档，避免一次性加载过长
- 代码脚本节省 tokens、避免出错、提升速度
- 复杂子流程用独立 Sub-SKILL.md

## 对 AI 产品设计的影响

Skill 是一种新范式：借用通用 Agent 内核，0 难度创造具备通用 AI 智能的垂直 Agent 应用。人给指引，Agent 根据自己的智力看着执行。

## 相关概念

- [[skill-distillation-depth]] — Skill 蒸馏精度与知识分层
- [[ai-coding-agent]] — Coding Agent 中 Skill 的应用
- [[ai-software-form-evolution]] — Skill 在软件形态演进中的角色
- [[harness-engineering]] — Harness 设计与 Skill 的关系
- [[utility-vs-skill]] — Utility与Skill：为什么判断力写不进规则
