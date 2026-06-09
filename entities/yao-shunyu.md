---
title: 姚顺雨（Yao Shunyu）
created: 2026-06-09
updated: 2026-06-09
type: entity
tags: [person, ml, agent, company]
sources: [raw/articles/2026-06-05-汤道生 x 姚顺雨：腾讯AI下半场.md, raw/articles/2026-06-08-腾讯被错判了？.md, raw/agent/汤姚对话.md]
confidence: high
---

# 姚顺雨（Yao Shunyu）

腾讯首席 AI 科学家，ReAct 架构与 SWE-bench 的提出者。2025 年加入腾讯，直接向总裁刘炽平汇报，同时兼任 AI Infra 部、大语言模型部负责人。此前在 OpenAI 工作，发表《The Second Half》定义 AI 下半场议程。

## 核心贡献

### AI 下半场定义
> 去年之前 AI 发展了几十年，核心是寻找解决问题的方法；但预训练和后训练成熟后，我们有了「万能锤子」，反而更难的是寻找值得解决的好问题。

下半场 = 从「怎么解决」迁移到「解决什么」。这是一个 meta-shift：方法论成熟后，评估（Eval）从陪练位置推到驱动位置——「evaluation becomes more important than training」。^[raw/articles/2026-06-05-汤道生 x 姚顺雨：腾讯AI下半场.md]

### Co-Design 三要素（技术/模型视角）
1. **模型本身扎实**：预训练 solid，后训练摒弃刷榜，基于真实产品场景构建 Eval
2. **建立信任**（最难部分）：模型和产品团队深度绑定——混元派出后训练最强骨干支持元宝，即使预训练没准备好也优先保障
3. **充分利用 LLM 泛化性**：Coding Agent 需要的不只是 coding 数据，还需要聊天、推理、搜索、指令遵循等复合能力，这些能力可跨产品迁移形成网络效应 ^[raw/articles/2026-06-05-汤道生 x 姚顺雨：腾讯AI下半场.md]

### 三角形组织模型
AI 组织应由三足支撑：
- **foundation**：预训练 + 后训练，资源充足，做事方式正确
- **product**：把技术落地为价值，需要有产品 sense 的人
- **frontier**：探索新研究范式——姚承认「中国今天所做的前沿探索不够多」^[raw/articles/2026-06-05-汤道生 x 姚顺雨：腾讯AI下半场.md]

### Token 经济判断
性能 > 一切。用 Opus 比用更差模型更省钱——因为更快做对、省了人的精力。在中国，性价比首先是性能；如果性能不好，性价比无从谈起。^[raw/articles/2026-06-08-腾讯被错判了？.md]

## 认知特征与盲区

### 第一性原理：泛化
姚的 Co-Design 回答从泛化（ML 命题）出发：因为泛化是 LLM 本质，所以复合 data taxonomy 重要，所以跨产品数据汇聚成网络有价值。这与[[tang-daosheng]]从用户价值出发的产品第一性原理形成互补——姚把模型能力当作要优化的变量，把产品当环境；产品第一性原理把用户价值当不动点，把模型当变量。^[raw/agent/汤姚对话.md]

### 关键回避
在 Co-Design 讨论中，姚存在几个结构性盲区：
1. **Co-Design 的「Design」产品侧几乎只字未提**——不谈模型如何重塑产品交互、Agent 自主边界、人类在环位置、模型出错的兜底 UX
2. **「互信」被黑箱化**——承认这是最难部分但「有很多细节就不赘述」，跳过了利益冲突、数据治理、roadmap 话语权
3. **泛化被理想化**——没提负迁移、alignment tax、为一个产品优化会导致另一个回退、何时该退回到特化模型
4. **产品工程约束缺位**——不谈成本/调用经济性、延迟、可靠性、对幻觉的零容忍 ^[raw/agent/汤姚对话.md]

### 两种 Trust 的混淆
姚说「腾讯是基于 trust 而非 metric 运转的公司」，但这混淆了两种信任：
- **纵向/文化信任**（公司对人才的信任、low ego、长期主义）——真实存在
- **横向/组织间信任**（BG 之间愿不愿意交出数据/算力）——腾讯在这根轴上恰恰是高度 metric、高度竞争的赛马机制。姚作为被高规格请来、直接向总裁汇报的明星 hire，体验到的信任浓度是公司最高档，样本有偏。^[raw/agent/汤姚对话.md]

## 上下文（Context）护城河论

姚的核心战略判断：当模型越来越擅长把复杂输入变成标准输出，竞争壁垒转移到了最原始的输入端——「你知不知道这个人在干什么，知不知道企业的各种信息」。这是加入腾讯的首要原因。^[raw/articles/2026-06-05-汤道生 x 姚顺雨：腾讯AI下半场.md]

## 相关页面

- [[tencent]] — 腾讯公司
- [[tang-daosheng]] — 汤道生，认知互补的对话方
- [[co-design-ai]] — Co-Design 协同设计
- [[ai-second-half]] — AI 下半场与单位智能经济
- [[token-economics]] — Token 经济
- [[ai-native-organization]] — AI Native 组织模式
- [[enterprise-agent-practice]] — 企业级智能体实践
