---
title: Vibe Slop：AI 编程垃圾与 Eternal Sloptember
created: 2026-05-31
updated: 2026-05-31
type: concept
tags: [coding, agent, ml, thought]
sources: [raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]
confidence: high
---

# Vibe Slop：AI 编程垃圾与 Eternal Sloptember

## 核心命题

Vibe Slop 是指由 AI 编程 Agent 大量生成的、看似可用但实际脆弱的代码。由 OpenClaw 核心组件 Pi 的创建者 Mario Zechner 和 Armin Ronacher 提出，指代「程序员不再认真设计和测试系统，而是让 AI 快速拼出一套东西，最后产出一堆经不起时间考验的软件」的现象。^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]

## Eternal Sloptember

George Hotz 在博客中提出「Eternal Sloptember（永恒的 slop 九月）」概念：大规模采用 AI Coding Agent 将导致垃圾代码成吨涌出的黄金时代，同时成为高质量精品的黑暗时代。他认为 Agent 最终会生产出比以往更多的代码、更多的应用、更多的功能，但质量的基线在系统性下降。^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]

## 关键警告者

### Mario Zechner & Armin Ronacher

Zechner 和 Ronacher 亲手打造了爆火 OpenClaw AI Agent 核心组件（Pi），数百万人使用。他们警告：

- 「基础设施正在崩溃，软件比以前漏洞百出」——我们还能再玩几个月甚至几年，但最终会付出代价^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]
- 许多公司正在用短期生产率换取长期麻烦：初级人才管道干涸、bug 增多、安全漏洞、技术债不断累积
- AI 编程工具擅长生成新代码，但不擅长评估和升级既有软件——尤其对成熟公司内部庞大复杂的遗留系统
- Zechner 对 Anthropic Claude Code 的评价：「Claude Code 是我这辈子用过的最破碎的软件之一」

### George Hotz

详见 [[george-hotz]]。Hotz 的核心论点：Agent 不会编程——它们生成的东西就是坏的，只是坏得越来越隐蔽。

## 因果机制

| 阶段 | 特征 |
|------|------|
| 前期 | Agent 把所有进展提前堆在前面，给人「进展飞快」的错觉 |
| 后期 | 进入「老虎机模式」——不断拉杆期望 Agent 完成最后的打磨，但总是差一点 |

这解释了为什么「10x 代码」在组织层面可能是「10x 垃圾」：前期提速掩盖了后期修复成本，局部效率提升不等于系统产出提升。

## 组织层面的不对称伤害

- **高绩效个人/小团队**：有纠错能力，能识别「什么时候垃圾就是垃圾」，不会转向「不再认真阅读并理解每一行代码」的模式^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]
- **大型组织**：反馈循环慢、对齐程度低，表现最差的人缺乏自我检查能力，却恰恰成为 Agent 的最大使用者

## 成本维度的佐证

{{george-hotz}} 的定性判断得到了定量数据佐证：

- **Uber**：CTO 称提前花光了 2026 年 Claude Code 预算；COO 指出 token 消耗与有用功能产出之间「没有因果关系」^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]
- **英伟达**：应用深度学习副总裁 Bryan Catanzaro 确认 AI 计算成本远超员工成本
- **Duolingo**：曾将 AI 使用纳入绩效考核，员工质疑后撤回

## 与已有数据的一致性

SWE-chat 研究（6,000+ coding sessions）发现：
- Vibe coding 的代码存活率仅 44.3%
- Vibe coding 引入漏洞速率为 human-only 的 9 倍（0.76 vs 0.08/1K lines）
- 「Autonomy is outpacing oversight」

Vibe Slop 批判与这些实证数据高度一致。详见 [[ai-coding-agent]]。^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]

## 恶性循环

坏代码从来不新鲜。新鲜的是：**坏想法现在可以以更快的速度变成 commit，而理解、审查和责任却没有同步变快。** 过去再差的代码，写的人至少有一个粗糙的心智模型，知道自己为什么这么写。现在大量 AI 生成的代码被快速提交、合并、发布，很多人没有真正理解它，只是看到它通过了测试——而测试本身可能也是残缺的。^[raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md]

## 相关概念

- [[george-hotz]] — Hotz 的立场与实证
- [[ai-coding-agent]] — AI Coding Agent 工程方法论
- [[openclaw-runtime]] — OpenClaw Agent Runtime（Zechner/Ronacher 的警告来源）
- [[karpathy]] — Karpathy 的乐观立场（争论的对立面）
- [[ai-code-adoption]] — AI 代码采纳率提升工程实践
- [[harness-engineering]] — 驾驭 Agent 的核心工程方法
- [[ai-cognitive-debt]] — AI 认知债务
