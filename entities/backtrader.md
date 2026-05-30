---
title: Backtrader
created: 2026-04-24
updated: 2026-04-24
type: entity
tags: [infra, coding]
sources: [raw/articles/Backtrader.md]
confidence: medium
---

# Backtrader

## 概述

Python 生态中最经典、功能最丰富的开源量化回测框架之一，由 Daniel Rodriguez 在 2015 年发起。核心哲学是"不要重复发明轮子"，采用事件驱动（Event-driven）机制，模拟真实市场中价格随时间变动的过程。

## Cerebro 系统

Cerebro（西班牙语"大脑"）是核心中央调度器：

| 组件 | 职能 |
|------|------|
| Data Feeds | CSV、Pandas、实时行情（IB、OANDA）等 |
| Strategies | 用户编写策略逻辑 |
| Brokers | 模拟真实交易环境，处理手续费、滑点、订单执行 |
| Analyzers | 计算夏普比率、回撤、胜率等关键指标 |

## 优缺点（2026 视角）

**优势：**
- 功能极其丰富：内置上百种技术指标（SMA、MACD、RSI 等）
- 回测即实盘：策略代码在回测和实盘几乎无需修改
- 强大的绘图能力：基于 Matplotlib

**局限：**
- 性能瓶颈：事件驱动模型在超大规模数据上速度慢于 VectorBT
- 学习曲线：API 设计非常"面向对象"，对初学者门槛较高

## 相关概念

- [[quant-backtesting]] — 量化回测框架对比
- [[ai-coding-agent]] — AI 与量化策略
