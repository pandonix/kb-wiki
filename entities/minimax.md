---
title: MiniMax
created: 2026-05-30
updated: 2026-05-30
type: entity
tags: [company, lab, llm, ml]
sources:
  - raw/articles/2026-05-29-AI为什么会失语.md
  - raw/articles/Token生意在重新洗牌.md
  - raw/articles/智联网：移动互联网的下一站——当AI Agent重写数字世界的游戏规则.md
---

# MiniMax

MiniMax 是一家中国 AI 大模型创业公司（闫俊杰创立），是国产大模型第一梯队的代表厂商之一。

## 关键事实

- 模型产品线：M2.1、M2.5 等系列
- 2026 年 2 月 OpenRouter 数据显示，M2.5 曾位列平台调用量前五
- 输出价格普遍在每百万 token 2-3 美元区间，属于低价位高性能模型
- 在 AI Agent 领域，MiniMax 与腾讯、智谱、Kimi、字节等厂商同期推出了基于 OpenClaw/龙虾的定制版本

## 技术贡献

### AI 失语修复路径

MiniMax 的工程师在排查用户反馈时发现了一种新型模型故障——AI 失语（Aphasia），表现为模型知道答案但无法直接输出目标词。[[ai-aphasia]]

修复方案：在后训练阶段，给词表里的每一个 token 都安排上最低限度的训练机会，保护低频 token 的连接强度不被高频 token 持续挤压。^[raw/articles/2026-05-29-AI为什么会失语.md]

## 行业地位

- 中国大模型第一梯队成员，与 DeepSeek、月之暗面（Kimi）、智谱（GLM）并列
- 在性价比方面具有竞争力——以低价吸引了大量开源 AI 栈创业公司
- 2026 年，a16z 合伙人估计使用开源 AI 栈的初创公司中约 80% 跑在中国模型上，MiniMax 是主要选择之一 ^[raw/articles/Token生意在重新洗牌.md]

## 相关概念

- [[ai-aphasia]]
- [[token-economics]]
- [[agentic-ai]]
