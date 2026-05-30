---
title: DeepSeek-V4 长上下文架构
created: 2026-05-30
updated: 2026-05-30
type: concept
tags: [ml, architecture, research, agent, paper]
sources: [raw/papers/20260529T100332--paper-deepseek-v4.md]
confidence: high
---

# DeepSeek-V4 长上下文架构

## 核心命题

DeepSeek-V4 解决的不是"模型还能不能更聪明"，而是一个更硬的约束：未来模型要做长时间 Agent、跨文档分析、长链路推理，必须能把百万 token 放进工作台，还不能每看一眼都烧掉巨大算力。^[raw/papers/20260529T100332--paper-deepseek-v4.md]

核心思路：**不再让模型逐字回看全部历史，而是把历史压成多种粒度的索引、摘要和局部窗口。** 模型看远处时看压缩地图，看近处时看原始细节。

## 模型规格

| 版本 | 总参数 | 激活参数/Token | 预训练数据 |
|------|--------|----------------|-----------|
| DeepSeek-V4-Pro | 1.6T | 49B | 33T tokens |
| DeepSeek-V4-Flash | 284B | 13B | 32T tokens |

两者均为 MoE 架构。训练长度从 4K 逐步拉到 16K、64K、1M。^[raw/papers/20260529T100332--paper-deepseek-v4.md]

## 三层注意力架构

### 1. 滑动窗口（近处）
- 128 token 原始窗口
- 近处不压缩，保留细节

### 2. CSA（中层压缩注意力）
- 每 4 个 token 的 KV 压成一个条目
- 轻量索引器选 top-k 条目（Pro: 1024, Flash: 512）
- 模型从"全看"变成"先找再看"

### 3. HCA（远层粗粒度压缩注意力）
- 每 128 个 token 压成一个条目
- 更便宜的 dense attention
- 不追求精细找针，只保留粗视野

```
near tokens  -> raw window        -> see exact words
mid history  -> CSA compressed    -> select useful blocks
far history  -> HCA compressed    -> keep broad memory
```^[raw/papers/20260529T100332--paper-deepseek-v4.md]

## 关键技术创新

### mHC（混合残差连接）
把残差连接从"简单相加"升级成"有约束的混合"，在多个通道间稳定分配信息流。增强深层网络建模能力，但实现复杂。^[raw/papers/20260529T100332--paper-deepseek-v4.md]

### Muon 优化器
Muon 不是 DeepSeek 原创，但首次工程化应用到 Trillion MoE 训练。多数参数用 Muon，embedding/head/RMSNorm 仍用 AdamW。收敛更快、训练更稳。^[raw/papers/20260529T100332--paper-deepseek-v4.md]

### 训练补丁
- **Anticipatory Routing**：MoE 路由用历史参数提前算好，而非模型即时算。降低 loss spike 风险
- **SwiGLU Clamping**：linear 分量限制 [-10, 10]，gate 分量上限 10。朴素但有效^[raw/papers/20260529T100332--paper-deepseek-v4.md]

## 效率提升

| 指标 | V4-Pro vs V3.2 (1M上下文) | V4-Flash vs V3.2 (1M上下文) |
|------|--------------------------|----------------------------|
| 推理 FLOPs | 27% | 10% |
| KV cache | 10% | 7% |

## 能力对比

| 基准 | V4-Pro-Max | 最佳竞品 |
|------|-----------|----------|
| SimpleQA-Verified | 57.9 | Gemini-3.1-Pro: 75.6 |
| HLE | 37.7 | Gemini-3.1-Pro: 44.4 |
| Codeforces | **3206** | GPT-5.4: 3168 |
| Terminal Bench 2.0 | 67.9 | GPT-5.4: 75.1 |
| SWE Verified | 80.6 | Opus-4.6: 80.8 |

开放模型在长上下文效率、代码竞赛、中文写作和部分 Agent 任务上追得很近；在知识密度和复杂指令上仍有短板。^[raw/papers/20260529T100332--paper-deepseek-v4.md]

## 分层工作台的设计哲学

DeepSeek-V4 的核心哲学超越了单纯的架构创新：**长上下文不是免整理的借口，上下文越长，越需要压缩、索引和分层**。

这个概念可以直接迁移到 Agent 记忆系统、项目知识库和个人工作流：
1. **当前窗口**：保留原文、最新状态、关键约束
2. **近期项目**：保留结构化摘要、决策、风险、下一步
3. **长期框架**：保留概念索引、链接、反复出现的问题

## 相关概念

- [[agent-memory]] — 压缩记忆地图与 CSA/HCA 类比
- [[ai-coding-agent]] — 三层上下文的 Agent 编码实践
- [[harness-engineering]] — Harness 作为 Agent 的分层工作台
- [[beyond-token-paradigm]] — 上下文压缩与 Token 范式演进
- [[ai-software-form-evolution]] — 单位智能与 Flash/Pro 双版本分工
