# Wiki Schema

## Domain

个人知识库 — 技术学习笔记为主，混合摄入，覆盖：

- **AI/软件工程**：AI Coding Agent、架构治理、声明式架构、多Agent协作、AI经济影响
- **量化与投资**：价值投资哲学（霍华德·马克斯、段永平、巴菲特）、量化回测、风险管理与遍历性、期权/固收
- **思维模型与认知**：二阶思维、资本现实主义、系统论/控制论、黑天鹅与贝叶斯
- **哲学/心理学**：斯多葛学派、辩证唯物主义、马克思异化理论、MBTI人格（ENTP/INTJ）
- **商业/组织**：科层制到智慧型组织、流量2.0、品牌与中介消亡
- **个人成长**：写作技巧、领导力、管理禁忌

## Conventions

- 文件名：小写、连字符、无空格（如 `ai-coding-agent.md`、`second-order-thinking.md`）
- 每页以 YAML frontmatter 开头（见下方）
- 使用 `[[wikilinks]]` 互链，每页至少 2 条 outbound links
- 更新页面时必更新 `updated` 日期
- 新页面必须加入 `index.md` 对应 section
- 所有操作必须 append 到 `log.md`
- 综合 3+ 来源的页面，在每个具体引用段落后加 `^[raw/articles/source-file.md]`
- raw/ 文件为 Layer 1（不可变），永远不修改

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary | thought
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
# Optional quality signals:
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

## Tag Taxonomy

**按性质：**
- `thought` — 自己的观点/感悟
- `summary` — 总结/摘要
- `question` — 未解决的问题

**按领域：**
- `ml` — 机器学习/深度学习/AI模型
- `infra` — 基础设施/系统设计/架构
- `coding` — 编程语言/工程实践
- `paper` — 论文
- `tool` — 工具使用
- `invest` — 投资/商业/量化
- `philosophy` — 哲学/思想史
- `psychology` — 心理学/人格类型
- `management` — 管理/组织/领导力
- `writing` — 写作/表达
- `agent` — AI Agent/智能体
- `alignment` — AI 对齐/安全
- `architecture` — 架构设计
- `company` — 公司/组织
- `person` — 人物
- `mbti` — MBTI 人格类型
- `insurance` — 保险/金融
- `research` — 研究报告/指数
- `safety` — 安全性/风险控制
- `decision-making` — 决策方法
- `economics` — 经济学/遍历经济学
- `ergodicity` — 遍历性
- `political-economy` — 政治经济学/制度经济学/暴力经济学
- `education` — 教育/学习/高等教育
- `energy` — 能源/电力/电网
- `game-theory` — 博弈论/博弈分析
- `marketing` — 营销/增长/GTM

**按状态：**
- `stale` — 已知过期/需要更新
- `growing` — 持续更新中

## Page Thresholds

- **建页：** 一个概念/实体被 2+ 来源提到，或在一个来源中处于核心位置
- **只补充：** 偶发提及不建页，合并到已有页面
- **拆分：** 超过 ~200 行时按子主题拆分并互链
- **归档：** 内容完全过时时移入 `_archive/`，从 index.md 移除

## Entity Pages

人物/公司/产品/模型，包含：
- 概述（是什么）
- 关键事实与时间线
- 关联实体（[[wikilinks]]）
- 来源

当前实体：Stanford HAI AI Index、VeighNa、Backtrader、霍华德·马克斯、ENTP、INTJ、伯克希尔·哈撒韦、Demis Hassabis、段永平、Andrej Karpathy

## Concept Pages

主题/技术/思想，包含：
- 定义/解释
- 当前认知状态
- 开放问题/争议
- 相关概念（[[wikilinks]]）

## Thought Pages

随手想法/感悟，包含：
- 原始触发点
- 思考过程
- 关联的概念或实体

`type: thought`，tag 打 `thought`

## Update Policy

新旧信息冲突时：
1. 看日期，新的通常覆盖旧的
2. 真的有矛盾 → 两条并列写明来源和日期
3. frontmatter 标记 `contradictions: [page-name]`
4. lint 时报告给用户 review

### Stale Review Cadence

| 领域 | 审查周期 | 说明 |
|------|---------|------|
| AI/Agent/ML | 每 30 天 | 行业变化快，模型/方法/评测频繁更新 |
| 投资/经济 | 每 60 天 | 宏观数据、市场事件更新 |
| 组织/管理 | 每 90 天 | 管理实践相对稳定 |
| 哲学/历史 | 按需 | 经典理论无需定期更新 |

超过审查周期未更新 → 自动加 `stale` tag → 下次健康检查时复核。
已标记 `stale` 的页面复核后，去掉 tag 并更新 `updated` 日期。

## Log Rotation

`log.md` 超过 500 条时，rename 为 `log-YYYY.md`，开新文件。
