---
title: AI 编程三阶段构想
created: 2026-05-08
updated: 2026-05-08
type: concept
tags: [ml, coding, infra]
sources: [raw/articles/OpenClaw和Claude Code只是第一阶段，Github 这两个项目正指向终局——AI 编程三阶段构想（万字长文慎入）.md]
confidence: medium
---

# AI 编程三阶段构想

## 三阶段模型

### 第一阶段：AI 辅助补全（Copilot 时代）

- AI 作为代码补全工具，人仍是主要编写者
- 代表：GitHub Copilot、早期 Cursor
- 瓶颈：上下文窗口有限，只能做局部补全

### 第二阶段：Agent 自主执行（当前，2025-2026）

- AI Agent 可自主完成完整任务，但需要人设定边界和审查
- 代表：Claude Code、OpenAI Codex、Cursor Agent Mode
- 关键特征：
  - 能读写文件、执行命令、运行测试
  - 上下文管理成为核心挑战
  - Vibe Coding 现象：自然语言描述意图，Agent 生成代码
- 当前问题：代码存活率仅 44.3%，协作式比全自动更高效^[
SWE-chat Coding Agent Interactions From Real Users in the Wild.md
]

### 第三阶段：AI 全栈工程师（终局构想）

- AI 可端到端构建完整系统，人类只做商业意图定义
- OpenClaw 指向的方向：AI 可以理解整个代码库的组织逻辑
- 核心能力：系统级规划、跨文件重构、架构决策
- 挑战：长程可靠性、安全审计、需求理解的精确性

## OpenClaw 和 Claude Code 的启示

- OpenClaw：从开源项目提取 Skill，实现知识复用
- Claude Code：第二阶段的典型代表，Agent 式交互
- 两者共同指向：编程从"写代码"变为"设计系统 + 审查输出"

## 关键判断

- 第一阶段到第二阶段的过渡已完成（2025年11月为临界点）
- 第二阶段到第三阶段的过渡正在进行，核心瓶颈在可靠性
- 每个阶段不是替代关系，而是叠加——Copilot 仍在，但 Agent 成为更高抽象层

## 相关概念

- [[ai-coding-agent]] — AI Coding Agent 工程方法论
- [[harness-engineering]] — Agent 驾驭系统设计
- [[skill-distillation-depth]] — Skill 蒸馏与知识分层
