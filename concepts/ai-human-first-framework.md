---
title: AI First / Human First 两层决策框架
created: 2026-08-04
updated: 2026-08-04
type: concept
tags: [ml, management, agent, decision-making]
sources: [raw/articles/2026-07-30-思林广不记-AI-First-or-Human-First.md]
confidence: medium
---

# AI First / Human First 两层决策框架

## 核心命题

AI first 还是 human first，不是二选一——答案取决于在哪一个层面做决策。**社会/组织层必须是 Human First（人是目的，责任无法让渡给 AI），技术执行层可以是 AI First（AI 补能力短板，且是顺着人性的默认选项）。**

真正的风险不在选哪边，而在**执行层的小选择会顺着三条路径向上蔓延，侵蚀组织层本该守住的 human first。** ^[raw/articles/2026-07-30-思林广不记-AI-First-or-Human-First.md]

## 两层拆解

### 社会/组织层：Human First

两条理由：

1. **道义上**：人是目的不是手段。Lilian Weng 离开 Thinking Machines 时说的：「值得构建的未来，是属于人的。」加拿大航空聊天机器人案：仲裁庭判航司为机器人错误信息负责，不认「机器人是独立实体」的辩护。
2. **事实上**：最前沿 AI 公司都在拼命抢人。Meta 给顶尖 AI 人才四年最高 3 亿美元。越是把 AI 用到极致的公司，越把顶尖的人当成最稀缺的资源。

### 技术执行层：AI First

AI 补能力短板——Ethan Mollick 清单：打破僵局、大量摘要、批量生成再筛选、预判对手反应。Anthropic 2026.6 研究发现：把工作交给 AI 最彻底的人，对未来前景反而最乐观（六个维度无一例外）。加上行为经济学的默认效应——维持现状零成本，推翻要花力气——AI first 在执行层是顺着人性的默认选项。

## 三层侵蚀路径（执行层 → 组织层）

1. **个人能力退化**：见 [[skill-atrophy-ai]]
2. **工作流重构**：METR 实验——越来越多开发者「哪怕付钱也不愿意不用 AI 完成一半工作」，人上手的位置逐渐消失
3. **组织重新定价**：Klarna AI 替代 700 名客服；Amazon 裁 1.4 万岗

## 三问判主责

把工作拆成环节，每个环节用三个问题判断主责：

1. **产出需不需要本人签字对外负责？** → 需要 → 人主责
2. **AI 做错了，本人能不能发现？** → 不能 → 人主责（关联 [[automation-bias]]）
3. **这项能力荒废了，重建代价多高？** → 越高 → 越不该交出主责

三个都指向 AI，才放心交给 AI 主责。**门槛比想象中高。**

## 成长和效率是同一件事

能力越强 → 验得动的环节越多 → 能安全交给 AI 的范围越大 → 效率随之上升。不同能力水平的人，能安全交给 AI 的边界不同：新手能交出去的很少（这恰恰是该趁机练出来的部分），资深者可以放心交给 AI 更多（因为出错他能兜住）。

## 训练方法：AI 当教练

在人主责的环节，AI 当教练而不是替代：人先上手 → 卡住时让 AI 给思路 → 做完让 AI 挑错 → 不明白让 AI 讲清原因。Ethan Mollick 实验对比：直接用 ChatGPT 做作业的学生，考试反而不如没用的；用 AI 当导师带着一步步练的，考试成绩高出约 0.15 个标准差。

## 与相关概念的关系

- [[ai-human-boundary]] — AI 与人的边界问题的高阶框架
- [[ai-organization-adoption]] — 组织层面采纳困境（老板vs员工）
- [[human-on-the-loop]] — 人在环上：从 HITL 到 HOTL 的范式转移
- [[utility-vs-skill]] — 为什么判断力写不进规则
- [[ai-cognitive-debt]] — 个人层面过度依赖 AI 的认知代价

## 相关概念

- [[skill-atrophy-ai]] — AI 导致的个人技能退化（三层侵蚀的第一条）
- [[automation-bias]] — 自动化偏见：连数十年研究都无法纠正的认知偏差
- [[human-on-the-loop]] — 人在环上与 HITL 的局限性
- [[ai-human-boundary]] — AI 与人的边界
- [[ai-organization-adoption]] — AI 组织采纳困境
- [[human-ai-scale]] — 人应成为 AI 的尺度
