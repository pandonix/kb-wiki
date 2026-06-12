# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete

## [2026-06-09] ingest | batch 2/2: AI tools & tech concepts (3 files)
- Ingested 3 raw source files from Obsidian notes
- Raw file 1: "LLMs are eroding my software engineering career" — frontmatter: url→source_url, +ingested, +sha256
- Raw file 2: "Token经济进入结果层" — frontmatter: url→source_url, +ingested, +sha256
- Raw file 3: "控制论与智能体编码中的人在环上" — frontmatter: url→source_url, +ingested, +sha256
- **New concepts (2)**:
  - [[senior-engineer-moat-migration]] — 高级工程师护城河迁移模型：三层侵蚀（领域知识/排障/代码品味）→新护城河（工作流设计/质量验收/组织记忆/结果owner）
  - [[human-on-the-loop]] — 人在环上（HOTL）：控制论视角下的Agent编码范式转移，衰减+放大+Gemba
- **Updated pages (5)**:
  - [[token-economics]] — added 三层计价结构、Intercom Fin case ($0.99/outcome)、结果型AI四个成立条件、场景适配性
  - [[harness-engineering]] — added HOTL connection section, linked to new page
  - [[ai-coding-agent]] — added links to both new pages, updated sources
  - [[ai-era-scarce-capabilities]] — added link to senior-engineer-moat-migration
  - [[ai-judgment-baseline]] — added link to senior-engineer-moat-migration
- Index updated: 164 → 166 total pages

## [2026-06-08] ingest | 2 raw articles: Multi-Agent coordination + Claude Code org
- Ingested 2 raw source files from Obsidian notes
- Raw file 1: "AI 不会合作？那是因为他们没见过市场经济｜Hao好聊趋势" — frontmatter: url→source_url, +ingested, +sha256
- Raw file 2: "Claude Code之父：品味不是人类护城河" — frontmatter: url→source_url, +ingested, +sha256
- **New entities (3)**:
  - [[anthropic]] — Anthropic: AI safety company behind Claude Code
  - [[boris-cherny]] — Boris Cherny: Claude Code core builder
  - [[friedrich-hayek]] — Friedrich Hayek: knowledge problem & multi-agent mapping
- **New concepts (2)**:
  - [[economy-of-minds]] — market-based multi-agent coordination (auction + bucket-brigade + natural selection)
  - [[solipsistic-superintelligence]] — why LLMs fail at cooperation (MDP vs Markov Game)
- **Updated pages (5)**:
  - [[multi-agent-collaboration]] — added orchestrator-worker critique, DPBench, More Capable Less Cooperative, Economy of Minds paradigm shift
  - [[ai-coding-agent]] — added Boris Cherny section: Claude Code as experiment platform, loops, knowledge compression
  - [[ai-native-organization]] — added Anthropic section: MTS, Generalist golden age, token budget advice, org knowledge compression
  - [[ai-commoditization-boundary]] — added Boris's challenge: taste also being eroded, only values remain
  - [[ai-era-scarce-capabilities]] — added Boris's taste erosion insight, re-evaluating L1.5 vs L2 boundary
- Index updated: 159 → 164 total pages

## [2026-05-27] ingest | Agent vault initial import
- Phase: full pipeline (copy → batch ingest → reconcile)
- Source: Obsidian agent vault → raw/agent/
- New raw files: 22 (60 previously hand-synced to raw/articles/)
- Batch 1 (5 large files): 5 new concepts, 6 existing page updates
- Batch 2 (7 files): 7 new concepts, 1 new comparison, 6 existing page updates
- Batch 3 (10 files, 1 empty): 9 new concepts, 4 existing page updates
- Total new wiki pages: 22 (21 concepts + 1 comparison)
- Reconciliation: index rebuilt (128 pages), all manifest marked built
- Broken wikilinks fixed: 6 ([[[...]]] → [[...]])
- Orphans noted: 15 (pre-existing + new, to address incrementally)
- Cron job + skill updated to include agent vault in daily sync
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-06-03] ingest | Daily sync: Agent vault → raw/agent/
- Phase: full pipeline (copy → ingest → reconcile)
- Source: Obsidian agent vault (top-level files)
- New raw files: 2 (raw/agent/AI到底是不是泡沫.md + 马斯克五步工作法.md)
- New entities: 2 (arvind-krishna, elon-musk)
- New concepts: 2 (ai-bubble-debate, musk-algorithm)
- Updated pages: 2 (hymin-minsky, index.md)
- Inbound links added: 7 (ai-infra-capex, minsky-financial-instability, harness-engineering, science-vs-engineering, pact-framework + media)
- Index rebuilt, all manifest marked built

## [2026-04-24] create | Wiki initialized
## [2026-04-24] ingest | Bulk ingest 23 raw sources (2026-04-24 batch)

### Sources ingested
- AI Alignment与写作.md
- AI 危机：经济与智能的悖论.md
- AI 时代的架构治理.md
- AI应用定价与成本.md
- AI时代的Code Review怎么做？.md
- AI编程的现状与未来.md
- Agentic Forecasting using Sequential Bayesian Updating of Linguistic Beliefs.md
- BlackTrader.md
- Codex的多Agent并行开发指南.md
- Fast and Forgettable A Controlled Study of Novices' Performance, Learning, Workload, and Emotion in AI-Assisted and Human Pair Programming Paradigms.md
- Harness工程与领导力.md
- How To Be A World-Class Agentic Engineer.md
- OpenGame Open Agentic Coding for Games.md
- Token经济学七问——一份关于AI新经济的入门地图.md
- Token计算：下一个十年的成本战争.md
- Vn.py.md
- 从 iproduct 重构到 harness 方法论：为什么 V1 应先做最小真实闭环.md
- 从科层制到智慧型组织：AI 时代，企业组织的终极革命.md
- 完整解读：斯坦福 AI 年度报告｜26版发布，423页.md
- 流量 2.0 时代.md
- 消耗了上百亿 Token后， 对于 Agent 时代软件构建、软件形态及未来发展的思考.md
- 起大早，赶晚集.md
- 适合投资者反复听的思维方式！霍华德·马克斯在沃顿的最新对话，关于成长还是价值、卖出还是持有，更多制胜还是减少犯错…….md

### Wiki pages created (18 total)
**Entities (4):** stanford-ai-index-2026, veighna, backtrader, howard-marks
**Concepts (14):** ai-coding-agent, harness-engineering, ai-alignment, token-economics, ai-architecture-governance, ai-economy-impact, ai-software-form-evolution, multi-agent-collaboration, declarative-architecture, hierarchy-to-intelligence, flow-2dot0, copilot-learning, agentic-forecasting, ai-code-review, quant-backtesting, howard-marks-investing

### Actions
- All 23 raw sources: frontmatter added/updated (source_url, ingested, sha256)
- 18 wiki pages created with frontmatter, content, and cross-references
- Domain: 个人知识库 — 技术学习笔记
- Structure created with SCHEMA.md, index.md, log.md
- Tag taxonomy: thought, summary, question, ml, infra, coding, paper, tool, invest, book, podcast, stale, growing
- Page types: entity, concept, comparison, query, summary, thought

## [2026-04-24] ingest | Second batch: ~60 new raw sources + 7 changed files

### New raw sources (60 files added)
ENTP.md, INTJ.md, 二阶思维模型.md, 乱纪元里防住风险就是收益.md, Some Simple Economics of AGI.md,
公众号写作技巧.md, 世界的终结和资本主义的灭亡.md, 伯克希尔.md, 兼岗分析.md, 古董市场.md,
哲学__index.md, 四十不惑，五十知天命，六十耳顺.md, 固收与股权投资的差异.md, 塔勒布与道家思想.md,
大V和散文.md, 字节与抖音.md, 孙子兵法与道家.md, 家庭资产配置.md, 帕累托无效.md,
投资__index.md, 投资大师很少谈卖出.md, 斯多葛学派：理性与安宁之道.md, 期权.md,
李光耀2000年在哈佛肯尼迪政府学院的"领导力大师课"未命名.md, 段永平.md, 真诚才是必杀技.md,
私募产品能力评估.md, 突发事件后的正常心理反应.md, 管理禁忌.md, 经济学的前提假设.md,
能源转型与全球格局.md, 贪嗔痴.md, 辩证唯物主义.md, 阿里巴巴的投资分析.md, 隐形过度疲劳.md,
领导力的深度自我探索.md, 马克思讲的异化.md, 马克思：人的发展和物的繁荣.md, 高中数学.md,
黑天鹅与贝叶斯.md, Small Talk.md, 起大早，赶晚集.md

### Changed raw files (sha256 updated)
AI 时代的架构治理.md, Token经济学七问——..., Token计算：下一个十年的成本战争.md,
从科层制到智慧型组织：..., 完整解读：斯坦福 AI 年度报告｜..., 消耗了上百亿 Token后...,
适合投资者反复听的思维方式！霍华德·马克斯在沃顿的最新对话...

### Wiki pages created (7 new + updates)
**New Entities (3):** entp, intj, berkshire
**New Concepts (4):** second-order-thinking, risk-management-ergodicity, measurability-gap-agi, capitalist-realism, writing-techniques

### Pages updated (5)
ai-economy-impact.md (Stanford source path corrected)
howard-marks-investing.md (source filename corrected to full long filename)
ai-architecture-governance.md (sha256 updated)
hierarchy-to-intelligence.md (sha256 updated)
stanford-ai-index-2026.md (sha256 updated)

### Index updated
Total pages: 18 → 28

## [2026-05-08] ingest | Batch ingest: 25 new raw sources from Obsidian notes vault

### New raw sources (25 files added to raw/articles + raw/papers)
**From Obsidian 文章/网页剪藏/ (10):**
AI 时代的魔幻现实.md, 没有创业者气质的人.md, AI 的经济账根本算不通.md,
Demis Hassabis AGI访谈.md, Karpathy Vibe Coding访谈.md,
Vibe Reading.md, 金融知识体系终极指南.md, AI基础设施capex跟踪.md,
人生的觉醒之路.md, AI无法超过人类的维度.md

**From Obsidian 文章/微信公众号/ (13):**
是马还是煤.md, 新一代记忆智能体框架MIA.md, Agent Skills终极指南.md,
OpenClaw和Claude Code三阶段构想.md, Token并不等同于货币.md,
从Hy3 preview看AI下半场.md, 担心被Skill替代.md,
互联网已死Agent永生.md, 软件日抛化.md, 严肃聊聊Skill蒸馏.md,
段永平过时了吗.md, 高强度动脑如何休息.md, 只需10分钟养废大脑.md

**From Obsidian 论文/ (2):**
MATRAG Multi-Agent Transparent RAG.md, SWE-chat Coding Agent Interactions.md

### Wiki pages created (20 new)
**New Entities (3):** demis-hassabis, duan-yongping, karpathy
**New Concepts (17):** agent-memory, agent-skill-distillation, agent-skills, ai-coding-three-stages, ai-cognitive-debt, ai-economy-subsidy-crisis, ai-infra-capex, business-generalist, duan-yongping-investing, effective-rest, financial-knowledge-system, internet-dead-agent-alive, jevons-paradox-work, life-awakening, skill-distillation-depth, software-disposable, vibe-reading

### Pages updated (12)
token-economics.md (Token非货币属性补充), ai-economy-impact.md (补贴危机+马型煤型工作),
ai-coding-agent.md (三阶段构想+Hy3), flow-2dot0.md (Agent新流量入口),
hierarchy-to-intelligence.md (马型煤型+通用创业者), ai-alignment.md (AI无法超越人类维度),
copilot-learning.md (SWE-chat实证+养废大脑实验), ai-software-form-evolution.md (日抛化+单位智能),
multi-agent-collaboration.md (MIA框架扩充), howard-marks.md (段永平互链),
harness-engineering.md (Karpathy Agentic Engineering)

### Index updated
Total pages: 28 → 48

## [2026-05-08] lint+fix | Post-ingest quality audit and fixes

### Issues found and fixed
1. **Broken wikilink**: [[vibe-writing]] → [[writing-techniques]] in vibe-reading.md
2. **Near-duplicate pages merged**: agent-skill-distillation.md merged into skill-distillation-depth.md
3. **Orphan pages fixed**: Added inbound links to 8 orphan pages (ai-code-review, backtrader, effective-rest, financial-knowledge-system, karpathy, skill-distillation-depth, stanford-ai-index-2026, veighna)
4. **Tag taxonomy expanded**: Added 10 new tags to SCHEMA.md (agent, alignment, architecture, company, person, mbti, insurance, research, safety, decision-making)
5. **Raw frontmatter completed**: Added frontmatter to all 68 root-level raw files (59 batch + 9 manual)
6. **Duplicate raw files removed**: Deleted 2 duplicate files from raw/articles/ that already existed at raw/ root
7. **Entity list updated**: Added Demis Hassabis, 段永平, Karpathy to SCHEMA.md entity list
8. **quant-backtesting.md**: Added missing outbound links (backtrader, veighna)

### Final wiki stats
- Total pages: 47 (10 entities + 37 concepts)
- Raw sources: 94 (23 articles + 2 papers + 69 root flat)
- Broken wikilinks: 0
- Orphan pages: 0
- Pages with < 2 outbound links: 0
- Invalid tags: 0
- Raw files without frontmatter: 0 (excluding index.md)

## [2026-05-18] query | AI 时代编码/软件工程中人的未来角色定位——「责任」
- 查询问题：人在 AI 时代编码和软件工程中的角色定位，尤其「责任」
- 涉及页面：[[harness-engineering]]、[[ai-coding-agent]]、[[ai-code-review]]、[[measurability-gap-agi]]
- 涉及 raw：Some Simple Economics of AGI.md、How To Be A World-Class Agentic Engineer.md、起大早，赶晚集.md
- 核心发现：四条独立线索汇聚——经济学（法律责任承担）、工程实践（设环境定意图）、认知分工（理解不外包）、组织治理（责任边界所有者）
- 是否存档：否（标准查询，不建 queries/ 页）

## [2026-05-18] ingest | 批量消化 46 篇未建 raw 文件（六批 delegate_task）
- 批次A（哲学/思维 10篇）：marx-alienation, dialectical-materialism, stoicism, taleb-taoism, art-of-war-taoism, human-meaning-agi, marx-human-development, desire-scarcity-migration, three-poisons, confucius-life-stages
- 批次B（投资 9篇）：duan-yongping(更新), options-basics, fixed-income-vs-equity, selling-in-value-investing, household-asset-allocation, alibaba-investment-analysis, black-swan-bayesian, private-fund-evaluation, antique-market-lemons
- 批次C（技术/AI 10篇）：claw-code-runtime, openclaw-runtime, copilot-learning(更新), 已合并至已有页面：token-economics, ai-infra-capex, ai-cognitive-debt, software-disposable, quant-backtesting, ai-second-half, ai-organization-adoption
- 批次D（管理/领导力 5篇）：management-taboos, leadership-self-exploration, dual-role-management, bytedance-douyin-analysis, sincerity-communication
- 批次E（杂类 4篇，Small Talk.md 不存在）：big-v-prose-writing, hidden-fatigue, energy-transition-geopolitics, economics-scarcity-assumption
- 批次F（补漏 5篇）：token-economics(更新), quant-backtesting(更新), pareto-inefficiency, emergency-psychological-response, lee-kuan-yew-leadership
- 收尾：rebuild index.md（81页：10 entities + 71 concepts），manifest 全部 mark-built，lint 通过（0 orphan, 0 broken, 0 invalid tags，1 INTJ→intj 大小写修复）

## [2026-05-19] query | 流量2.0
- 查询：wiki 中是否有「流量2.0」对应概念
- 命中：[[flow-2dot0]] (concepts/flow-2dot0.md)
- 关联页：[[ai-economy-impact]], [[token-economics]], [[bytedance-douyin-analysis]]（均有入链）

## [2026-05-22] ingest | Obsidian notes 试点导入 (10篇 + 超额完成)
- Phase: 0 (copy all 293 new) → 1 (delegate_task × 2 batches) → 5 (reconcile) → 6 (verify)
- New raw files copied: 293 (94→387 total)
- New entities: 4 (marcos-lopez-de-prado, dan-koe, fiona-fung, andrew-ng)
- New concepts: 8 (context-engineering, agent-memory, agentic-ai, backtesting-overfitting, ai-code-adoption, ai-native-organization, ai-native-engineering-management, psychological-survival)
- Updated pages: 4 (ai-coding-agent, harness-engineering, multi-agent-collaboration, quant-backtesting)
- Subagents exceeded scope: processed 290/293 new files in one pass
- 3 remaining unbuilt: papers/ (技术革命与金融资本, 技术陷阱, 血酬定律)
- 2 intentional broken links: fiona-fung→claude-code, context-engineering→context-rot (待建)
- 11 pre-existing orphans (not introduced by this import)

## [2026-05-25] ingest | 技术革命与金融资本、技术陷阱、血酬定律 — 三篇书摘摄入

**Raw files processed:**
- raw/papers/技术革命与金融资本.md — prepended frontmatter (sha256: f9c78d2c...)
- raw/papers/技术陷阱-思维导图.md — prepended frontmatter (sha256: 2fddf8b6...)
- raw/papers/血酬定律-吴思.md — prepended frontmatter (sha256: caea2e0e...)

**Entity pages created:**
- entities/carlota-perez.md — Perez（技术革命与金融资本提出者）
- entities/hymin-minsky.md — Minsky（金融不稳定假说提出者）
- entities/wu-si.md — 吴思（血酬定律、潜规则提出者）

**Concept pages created:**
- concepts/tech-revolution-financial-capital.md — 技术革命与金融资本（Perez 框架 + Perez vs Minsky 对比）
- concepts/technology-trap.md — 技术陷阱（四段历史结构：大停滞→大分流→大平衡→大逆转）
- concepts/blood-money-law.md — 血酬定律（吴思暴力经济学框架 + 争议与硬伤）
- concepts/minsky-financial-instability.md — 金融不稳定假说（三阶段融资结构 + 当代综合）

**Schema updated:**
- Added `political-economy` tag（政治经济学/制度经济学/暴力经济学）

**Index updated:** 92 → 99 pages

## [2026-05-25] sync | 每日增量同步
- New files copied: 0 (all already in raw/)
- Unbuilt files processed: 3 (技术革命与金融资本, 技术陷阱-思维导图, 血酬定律-吴思)
- Pages created: 7 (3 entities + 4 concepts)
- Pages updated: ~5 (existing pages linked from new ones)
- Orphans fixed: 0
- Duplicates merged: 0
- Total: 99 pages / 394 raw

## [2026-05-26] ingest | 3 raw source files processed

### Sources ingested
- Claude不到4%，全军覆没！一场大考撕碎Agent「全自动办公」幻想.md
- "Token"必须死？.md
- 边界的消融：什么是更好的AI？.md

### Pages created
- concepts/saas-bench.md — SaaS-Bench：Agent 真实办公能力评测
- concepts/beyond-token-paradigm.md — 超越 Token 范式：连续表征与下一代架构
- concepts/ai-human-boundary.md — AI 与人的边界：效率解放还是系统加速

### Pages updated
- concepts/agentic-ai.md — Added SaaS-Bench findings section + source
- concepts/token-economics.md — Added "Token 范式面临的架构挑战" section + source
- concepts/human-meaning-agi.md — Added cross-link to ai-human-boundary
- concepts/jevons-paradox-work.md — Added cross-link to ai-human-boundary
- index.md — Added 3 new pages, updated total to 102

### Raw file frontmatter added
- All 3 files: added ingested date + sha256 hash

## [2026-05-26] ingest | 增量构建：5 篇 AI 产业文章（2新+3变更）

### New raw files with frontmatter
- raw/articles/Token生意在重新洗牌.md — Added full frontmatter (source_url, ingested, sha256)
- raw/articles/2026年，第一批"一人公司"老板已经退场.md — Added sha256 + ingested to existing frontmatter

### Changed raw files (wiki pages already current)
- raw/articles/Claude不到4%，全军覆没！一场大考撕碎Agent「全自动办公」幻想.md — saas-bench.md already current (created today)
- raw/articles/"Token"必须死？.md — beyond-token-paradigm.md already current (created today)
- raw/articles/边界的消融：什么是更好的AI？.md — ai-human-boundary.md already current (created today)

### Wiki pages created (1)
- concepts/one-person-company.md — 一人公司：AI 时代单人创业的幻觉与真相

### Wiki pages updated (1)
- concepts/token-economics.md — Added 8 new sections: 市场结构（分层式寡头垄断）、全球价格分化、巨头定价锚差异、三浪叠加定价模式、卖结果 vs 卖Token困境、Token交易所、碳排放定价、非OPEC走向. Added source ref to Token生意在重新洗牌.md

### Actions
- index.md: Added one-person-company page, updated total to 103
- 2 raw files: frontmatter added/updated

## [2026-05-26] create | ai-code-adoption-vs-review (comparison)
- type: comparison（首篇 wiki 比较页）
- 对比对象：[[ai-code-adoption]] vs [[ai-code-review]]
- 六维对比：核心问题、工作流位置、根因、方法论、人-AI 关系预设、知识网络位置
- 关键发现：adoption 的四大根因正是 review 四大风险的上游成因；两者构成质量控制环
- 综合判断：先建 review 防御基线，再用 adoption 提效——在无设防系统上提速只会让技术债累积更快
- index.md: 新增 Comparisons 区段，总数 105 → 106

## [2026-05-26] create | ai-era-scarce-capabilities
- type: concept（ai-commoditization-boundary 姊妹篇）
- 主题：AI 时代哪些能力变贵而不是贬值——六大稀缺能力（验证判断/定义问题/承担责任/审美品味/独特经验/造山能力）
- 三条底层机制：稀缺迁移、精度阶梯（L1/L2）、验证瓶颈
- 邓小闲三指标 + 马/煤框架 + 五层栈 + 导演-演员模型
- index.md: 新增 ai-era-scarce-capabilities，总数更新为 105

## [2026-05-26] create | ai-commoditization-boundary
- type: concept
- 主题：AI 替代边界——商品化梯度（可平均化/模板化/低成本复制）vs 人的价值迁移（意图/经验/审美/选择/责任/价值裁决）
- 交叉引用 16 个已有 wiki 页面和原始来源
- 综合框架：经济学（可复制认知劳动/稀缺迁移）、工作替代（马vs煤）、成本结构（五层栈）、写作理论（导演-演员）、哲学（人类意义）、验证瓶颈（可测量性鸿沟）
- index.md: 新增 ai-commoditization-boundary，总数更新为 104

## [2026-05-26] query | AI替代的不是整体，而是可模板化/平均化/低成本复制的部分
- 查询问题：AI替代的是创作/白领/程序员中可平均化、模板化、低成本复制的部分；人的长期价值在意图、经验、审美、选择、责任和价值裁决
- 查阅页面：ai-human-boundary, human-meaning-agi, desire-scarcity-migration, measurability-gap-agi, jevons-paradox-work, harness-engineering, internet-dead-agent-alive, software-disposable, token-economics, ai-cognitive-debt
- 查阅raw: 起大早赶晚集, AI Alignment与写作, 大V和散文, AI时代的乐观主义, 经济学的前提假设, Token计算, 人的欲望与稀缺迁移
- 结论：观点在wiki中有多维度交叉验证——从经济学（可复制认知劳动/稀缺迁移）、工程实践（harness五层栈）、写作（实质层vs表达层）、哲学（人类意义四层框架）、投资框架（马vs煤）均收敛到同一结论

## [2026-05-27] ingest | Batch 1/3：银行/管理类 5 篇大文件

### Raw files with frontmatter added
- raw/agent/银行ABCD科技战略：叙事还是实质.md (sha256: 286ad48d)
- raw/agent/个人的AI框架.md (sha256: 988697e4)
- raw/agent/AI原生银行.md (sha256: 50899cd1)
- raw/agent/人货场视角下的银行金融服务.md (sha256: 1d599ab2)
- raw/agent/文章的AI味.md (sha256: c79b60eb)

### Wiki pages created (5 concepts)
- concepts/bank-abcd-tech-strategy.md — ABCD 科技战略：叙事/实质分析、CIO 代理人问题、四种 AI First 驱动模式
- concepts/personal-ai-framework.md — 个人 AI 认知框架：六层结构（L-1→L3+L2.5）、三类反馈回路、学习方法论
- concepts/ai-native-bank.md — AI 原生银行 vs 互联网银行：认知带宽革命、深度增量、可信闭环
- concepts/people-goods-scene-banking.md — 人货场框架下的银行+Agent 时代重构：双面 Agent、四层架构
- concepts/ai-writing-flavor.md — AI 写作味：LLM 均值回归、三层结构、RLHF 副作用、去味路径

### Existing pages updated (6 cross-links added)
- writing-techniques.md ← [[ai-writing-flavor]]
- internet-dead-agent-alive.md ← [[ai-native-bank]]
- flow-2dot0.md ← [[people-goods-scene-banking]]
- ai-organization-adoption.md ← [[bank-abcd-tech-strategy]]
- ai-native-organization.md ← [[ai-native-bank]]
- hierarchy-to-intelligence.md ← [[personal-ai-framework]]

### Index updated
Total pages: 106 → 111

## [2026-05-27] ingest | Batch 2/3：7篇 raw/agent/ 源文件（经济学/哲学/科技）消化

### Sources ingested
- raw/agent/人类热衷寻找因果的哲学解释.md
- raw/agent/90年代国企改革与AI浪潮.md
- raw/agent/Skill与Utility.md
- raw/agent/企业级智能体实践.md
- raw/agent/Agent岗位要求.md
- raw/agent/康波周期.md
- raw/agent/科学与工程.md

### New concept pages (7)
- causality-philosophy.md — 因果：从休谟到珀尔的哲学追问
- utility-vs-skill.md — Utility与Skill：为什么判断力写不进规则
- enterprise-agent-practice.md — 企业级智能体实践：从Copilot到数字员工
- agentwashing.md — Agentwashing：智能体洗白与虚假智能体化
- agent-developer-capability.md — Agent开发者的三维能力立方体
- kondratiev-wave.md — 康波周期：技术革命与长期经济波动
- science-vs-engineering.md — 科学与工程：两种理性

### New comparison pages (1)
- ai-soe-reform-comparison.md — AI浪潮与90年代国企改革：两种劳动再配置

### Updated pages (6)
- entities/carlota-perez.md — Added cross-references to kondratiev-wave, ai-soe-reform-comparison
- concepts/tech-revolution-financial-capital.md — Added cross-reference to kondratiev-wave
- concepts/agent-skills.md — Added cross-reference to utility-vs-skill
- concepts/agentic-ai.md — Added cross-reference to enterprise-agent-practice
- concepts/ai-coding-agent.md — Added cross-reference to agent-developer-capability
- concepts/skill-distillation-depth.md — Added cross-reference to utility-vs-skill

### Raw file frontmatter
- All 7 raw/agent/ files: prepended ingested: 2026-05-27 + sha256

### Index updated
Total pages: 114 → 121

## [2026-05-27] ingest batch 3/3 | 10 misc topic files (9 processed, 1 empty)

### New pages (9)
- concepts/macroeconomic-investment-framework.md — 宏观经济投资框架 (type: concept, tags: invest, decision-making)
- comparisons/nev-vs-real-estate-macro.md — 新能源车与房地产的宏观角色对比 (type: comparison, tags: invest, political-economy)
- concepts/leadership-short-termism.md — 领导短期主义与任期错配 (type: concept, tags: management, psychology)
- concepts/palantir-ontology.md — Palantir Ontology 与 AIP (type: concept, tags: agent, architecture, company, ml)
- concepts/ai-strategy-positioning.md — AI 战略定位与政治博弈 (type: concept, tags: management, agent, decision-making)
- concepts/analogical-overshadowing.md — 类比遮蔽效应 (type: concept, tags: psychology, philosophy)
- concepts/mythical-man-month.md — 人月神话 (type: concept, tags: coding, management, agent)
- concepts/technology-containment-history.md — 大国技术遏制史 (type: concept, tags: political-economy, research)
- concepts/ba-vs-sa-boundary.md — BA 与 SA 的边界 (type: concept, tags: coding, management)

### Skipped
- raw/agent/Claude Code.md — empty file, no content to ingest

### Updated existing pages (4)
- concepts/technology-trap.md — Added cross-reference to technology-containment-history
- concepts/management-taboos.md — Added cross-reference to leadership-short-termism
- concepts/financial-knowledge-system.md — Added cross-reference to macroeconomic-investment-framework
- concepts/energy-transition-geopolitics.md — Added cross-reference to nev-vs-real-estate-macro

### Raw file frontmatter
- All 9 non-empty raw/agent/ files: prepended ingested: 2026-05-27 + sha256

### Index updated
Total pages: 121 → 120 (adjusted for 9 net new pages)

## [2026-05-27] query | 三种职业限制脚本的Wiki交叉分析

### Query
用户提供了一段关于三种职业心理脚本的表述（续集剧本/讨好者剧本/史诗剧本），要求用wiki交叉分析。

### Pages consulted (10)
- concepts/psychological-survival.md — 心理生存与身份守护（底层框架）
- concepts/second-order-thinking.md — 二阶思维（路径依赖）
- concepts/ai-cognitive-debt.md — AI 认知债务（舒适区 = 债务）
- concepts/life-awakening.md — 人生觉醒三阶段（破解路径）
- concepts/marx-alienation.md — 马克思异化理论
- concepts/capitalist-realism.md — 资本主义现实主义（想象力被殖民）
- concepts/human-meaning-agi.md — 人类的意义与AGI
- concepts/confucius-life-stages.md — 孔子人生三境界
- concepts/three-poisons.md — 佛家三毒
- concepts/pareto-inefficiency.md — 帕累托无效与共谋均衡

### Filed
- queries/three-career-scripts-analysis.md — 查询结果存档

### Key synthesis
三种脚本共享底层：都是心理生存策略，且都把主体性交给了外部（过去/他人/社会）。
破解路径：life-awakening 三阶段 + confucius-life-stages 三境界。

### Index updated
Total pages: 128 → 129

## [2026-05-27] create + update | 心理脚本概念页 + 6页交叉链接补全

### New page
- concepts/psychological-scripts.md — 心理脚本：主体性外化的三种生存策略 (type: concept, tags: psychology, philosophy, decision-making)

### Cross-links added (12 additions across 6 pages)
- psychological-survival: +pareto-inefficiency, +life-awakening, +psychological-scripts
- pareto-inefficiency: +psychological-survival, +psychological-scripts
- marx-alienation: +psychological-survival, +psychological-scripts
- capitalist-realism: +marx-alienation, +psychological-survival, +psychological-scripts
- life-awakening: +confucius-life-stages, +psychological-survival, +psychological-scripts
- confucius-life-stages: +psychological-survival, +psychological-scripts

### Index updated
Total pages: 129 → 130

## [2026-05-29] ingest | 9 raw source files batch ingest
- Raw files processed: 9 (5 articles, 1 culture report, 1 AIGC detection, 1 Anne-Laure interview, 1 agent vault)
- Frontmatter added/updated for all 9 raw files (source_url, ingested, sha256)
- New wiki pages created: 12
  - Entities: anne-laure-le-cunff
  - Concepts: agent-owner-role, forward-deployed-engineer-ai, outsourcing-thinking-ai, aigc-detection-education, super-creator, think-make-framework, social-intelligence-baseline, human-ai-scale, pact-framework, cognitive-scripts, wechat-relationship-chain-value
- Existing pages updated: 8
  - harness-engineering: added self-evolving harness, tracing, execution snapshots
  - jevons-paradox-work: added Dan Shipper/Every observation
  - ai-economy-impact: added culture industry data, Every micro-sample
  - ai-era-scarce-capabilities: added human-ai-scale traits list, culture industry evidence
  - ai-native-organization: added Forward Deployed Engineer practice from Every
  - ai-human-boundary: added Anne-Laure Le Cunff's outsourcing thinking boundary
  - one-person-company: added super-creator framework and ternary market coordination
- Index rebuilt: 130 → 142 pages
- Reconciliation: orphan inbound links added (aigc-detection-education, wechat-relationship-chain-value)
- Broken wikilinks fixed in new pages: 5 (proxy-metric-gaming, ness-labs, kings-college-london, imposter-syndrome, generation-effect → plain text)
## [2026-05-30 08:47 CST] query | 微信护城河在AI时代是否会被打破 — Wiki交叉分析
- 查阅页面(12)：wechat-relationship-chain-value, internet-dead-agent-alive, ai-commoditization-boundary, flow-2dot0, desire-scarcity-migration, ai-era-scarce-capabilities, bytedance-douyin-analysis, ai-economy-impact, ai-software-form-evolution, ai-human-boundary, ai-organization-adoption, raw/agent/微信关系链的核心价值.md
- 结论：护城河不会碎但会被「精炼」——工具层萎缩，信任/情感层强化
- Filed: queries/wechat-moat-ai-era.md

## [2026-05-30 09:15 CST] query | AI写作是否是文学史上最大的错误 — Wiki交叉分析
- 查阅页面(13)：ai-writing-flavor, ai-alignment, big-v-prose-writing, social-intelligence-baseline, ai-commoditization-boundary, outsourcing-thinking-ai, super-creator, ai-cognitive-debt, ai-human-boundary, desire-scarcity-migration, ai-era-scarce-capabilities, writing-techniques, raw/agent/文章的AI味.md, raw/articles/AI Alignment与写作.md, raw/articles/从《纽约客》的担忧谈起.md
- 结论：AI不会杀死文学，但会让「写手」先失业。治理方式决定结局——导演-演员模型 vs 全面外包。
- Filed: queries/ai-writing-literary-mistake.md
- Index: 147 → 149 (2 new queries)
- Manifest: 433 built, 0 unbuilt
- Orphans checked and resolved (all 3 new pages have inbound links)

## [2026-05-30 09:30 CST] create | expression-substance-framework
- type: concept
- 框架：AI 在 Expression 层有压倒性优势，但在 Intent 和 Substance 层存在结构性缺陷。跨软件工程、文学写作、社交平台等多领域成立。
- 综合来源：ai-alignment, ai-writing-flavor, ai-commoditization-boundary, harness-engineering, ai-code-review, big-v-prose-writing, outsourcing-thinking-ai, desire-scarcity-migration, wechat-relationship-chain-value + 两次查询交叉分析
- Cross-links: 9 个被引用页全部添加回链
- Index: 149 → 150

## [2026-05-29] query | 微信护城河在AI时代是否会被打破 — Wiki交叉分析
- 查询问题：未来的AI时代，微信的护城河是不是会被打破？
- 查阅页面(12)：wechat-relationship-chain-value, internet-dead-agent-alive, ai-commoditization-boundary, flow-2dot0, desire-scarcity-migration, ai-era-scarce-capabilities, bytedance-douyin-analysis, ai-economy-impact, ai-software-form-evolution, ai-human-boundary, ai-organization-adoption, raw/agent/微信关系链的核心价值.md
- 结论：护城河不会碎但会被「精炼」——工具层萎缩（信息分发、服务发现、弱关系中介），信任/情感层强化（信用承载、共同在场、社会性见证、弱连接option value）。唯一真威胁是AI原生社交身份层，但技术/信任/监管门槛极高。
- Filed: queries/wechat-moat-ai-era.md
- Index updated: 142 → 143

## [2026-05-31] ingest | 2 raw files ingested into llm-wiki
### Source 1: AI 时代分水岭 — 判断力基线
- Raw file: raw/articles/2026-05-30-9.5万大学生和37万高中生数据-AI时代分水岭.md
- Frontmatter updated: added ingested/sha256/source_url
- New concept: [[ai-judgment-baseline]] — 判断力基线的三层结构框架
- Updated: [[ai-era-scarce-capabilities]] — 加入Berkeley/Georgetown实证数据
- Cross-links to: outsourcing-thinking-ai, ai-human-boundary, aigc-detection-education, utility-vs-skill

### Source 2: 编程Agent可能是软件开发史上最昂贵的错误之一
- Raw file: raw/articles/编程 Agent 可能是软件开发史上最昂贵的错误之一.md
- Frontmatter updated: added ingested/sha256/source_url
- New entity: [[george-hotz]] — George Hotz (geohot)，AI编程批判者
- New concept: [[vibe-slop]] — Vibe Slop与Eternal Sloptember
- Updated: [[ai-coding-agent]] — 加入Hotz/Zechner/Ronacher批判视角 + Uber/英伟达成本数据
- Cross-links to: karpathy, openclaw-runtime, ai-code-adoption, harness-engineering

## [2026-06-02] ingest | 2 AI-native 组织形态 raw sources

### Sources ingested
- raw/articles/2026-06-01-AI-native下组织形式思考.md — AI Outcome Pod / Meta Pods / Microsoft Frontier Firm / McKinsey Agentic Organization
- raw/articles/2026-06-01-一个理想的组织是AI Agent在组织人.md — ColaOS创始人橘子深度访谈

### Raw file frontmatter updated
- Both files: added ingested (2026-06-02), sha256, source_url

### New wiki pages (3)
- concepts/ai-outcome-pod.md — AI Outcome Pod：人机混合结果单元
- concepts/soul-team.md — Soul Team：AI 原生组织的叙事一致性团队
- entities/juzi-orange.md — 橘子（冯雷）：ColaOS / ListenHub 创始人

### Existing pages updated (7)
- concepts/ai-native-organization.md — 新增AI Outcome Pod定义、四类组织原型、行业样本(Meta/Microsoft/McKinsey/Shopify/Duolingo)、ColaOS实战、判断与责任系统框架
- concepts/one-person-company.md — 新增ListenHub一人公司转型案例（一人+Agents维护20repo，产出提升10倍）
- concepts/ai-organization-adoption.md — 新增ColaOS采纳周期（不用→过猛→ROI约束）
- concepts/agent-owner-role.md — 新增「Agent组织人」反向命题（橘子视角 vs Dan Shipper视角互补）
- concepts/jevons-paradox-work.md — 新增「AI速度必须穿过组织变成成果速度」视角
- concepts/hierarchy-to-intelligence.md — 新增交叉链接到ai-outcome-pod和soul-team
- concepts/personal-ai-framework.md — 新增交叉链接到ai-outcome-pod和soul-team

### Index updated
- Added 3 new pages, updated total to 155

## [2026-06-03] ingest | AI bubble debate + Musk 5-step work method

### Raw files processed
- raw/agent/AI到底是不是泡沫.md — already has frontmatter (ingested: 2026-06-03)
- raw/agent/马斯克五步工作法.md — already has frontmatter (ingested: 2026-06-03)

### New wiki pages (4)
- entities/arvind-krishna.md — Arvind Krishna (IBM CEO), AI bubble perspective
- entities/elon-musk.md — Elon Musk, 5-step work method
- concepts/ai-bubble-debate.md — AI 泡沫辩论：Krishna 的经济账分析
- concepts/musk-algorithm.md — 马斯克五步工作法（The Algorithm）

### Existing pages updated (2)
- entities/hymin-minsky.md — added cross-link to ai-bubble-debate
- index.md — added 4 new pages, updated total to 159
## [2026-06-08] ingest | Obsidian notes daily sync
- Phase: incremental (copy → single ingest → reconcile)
- New raw files: 2
  - Claude Code之父：品味不是人类护城河；当工程师不再写代码，招聘看什么？.md
  - AI 不会合作？那是因为他们没见过市场经济｜Hao好聊趋势.md
- New entities: 3 (anthropic, boris-cherny, friedrich-hayek)
- New concepts: 2 (economy-of-minds, solipsistic-superintelligence)
- Updated pages: 5 (multi-agent-collaboration, ai-coding-agent, ai-native-organization, ai-commoditization-boundary, ai-era-scarce-capabilities)
- Total wiki pages: 164

## [2026-06-09] ingest | Batch 1/2: 汤道生 x 姚顺雨对话（汤姚对话、腾讯AI下半场、腾讯被错判了？）
- Raw files updated (frontmatter): 2
  - raw/articles/2026-06-05-汤道生 x 姚顺雨：腾讯AI下半场.md (added source_url, ingested, sha256)
  - raw/articles/2026-06-08-腾讯被错判了？.md (added source_url, ingested, sha256)
- Raw file already had frontmatter: raw/agent/汤姚对话.md
- New entities: 3 (tencent, tang-daosheng, yao-shunyu)
- New concepts: 1 (co-design-ai)
- Updated pages: 1 (ai-second-half — added 万能锤子 framing, triangle model, context护城河论, Co-Design)
- Total wiki pages: 170

## [2026-06-09] ingest | Batch 2/2: AI tools & tech (LLMs eroding career, Token经济, 控制论/HOTL)
- Raw files updated (frontmatter): 3
  - raw/articles/2026-06-06-LLMs-are-eroding-my-software-engineering-career.md (url→source_url, +ingested, +sha256)
  - raw/articles/2026-06-08-Token经济进入结果层.md (url→source_url, +ingested, +sha256)
  - raw/articles/2026-06-08-控制论与智能体编码中的人在环上.md (url→source_url, +ingested, +sha256)
- New concepts: 2 (senior-engineer-moat-migration, human-on-the-loop)
- Updated pages: 5 (token-economics, harness-engineering, ai-coding-agent, ai-era-scarce-capabilities, ai-judgment-baseline)

## [2026-06-09] reconcile | Post-ingest reconciliation
- Index rebuilt from filesystem: 170 pages
- All 6 new pages have 2-4 inbound links each (no orphan fixes needed)
- 3 pre-existing broken wikilinks noted (claude-code, context-rot, first-principles-thinking)
- All raw frontmatter validated (6/6 have ingested + sha256)
- Manifest updated: 447 files, all marked built

## [2026-06-10] ingest | Obsidian notes daily sync
- Phase: full pipeline (copy → batch ingest → reconcile → audit)
- Source: 3 new files from Obsidian (2 articles + 1 agent vault)
- New raw files: raw/articles/2026-06-08-人人都聊未来产业无人关心未来社会.md, raw/articles/2026-06-09-Claude-Code一周年回顾-两次认知跃迁.md, raw/agent/微信AI Agent.md
- New entities: annalee-saxenian, claude-code, lyu-peng, zhang-xiaolong, ma-huateng (5)
- New concepts: agent-routine-loop, delegation-interaction-paradigm, future-society-social-infrastructure, platform-agent-centralization, wechat-ai-agent, agent-delegation-trap (6)
- Updated pages: anthropic, boris-cherny, tencent, context-engineering, multi-agent-collaboration, future-society-social-infrastructure, tech-revolution-financial-capital (7)
- Orphans fixed: annalee-saxenian, lyu-peng (added inbound links from related pages)
- Broken wikilinks fixed: ma-huateng, agent-delegation-trap (created stub pages)
- Wiki total: 170 → 181 pages
- Manifest: 447 → 450 raw files, all marked built

## [2026-06-12] ingest | Daily sync batch: 3 raw source files
- Source files: 2026-06-11-人是最慢的节点还怎么管AI-Agent.md (52KB, 腾讯研究院/Multica访谈), 2026-06-11-构建OpenAI做不了的双边网络这家AI原生营销平台增长凶猛.md (16KB, 36氪/AhaCreator), 2026-06-12-AI原生能源公司正在成为硅谷新物种.md (16KB, 腾讯科技/AI能源)
- Raw frontmatter: added ingested + sha256 + source_url to all 3 files
- SCHEMA.md: added `energy` and `marketing` tags to taxonomy
- New entities: zhang-jiayuan, multica, ahacreator (3)
- New concepts: agent-idle-rate, ai-bilateral-platform-moat, ai-native-energy-company (3)
- Updated pages: multi-agent-collaboration (O/W/V三类角色+两层结构+单vs多Agent漂移), ai-native-organization (Multica 4人+Agent样本+Agent idle率), outsourcing-thinking-ai (张佳圆思考退化), agent-delegation-trap (人类review瓶颈), ai-infra-capex (能源瓶颈细节) (5)
- Wiki total: 181 → 187 pages

## [2026-06-12] reconcile | Post-ingest reconciliation
- Index rebuilt from filesystem: 187 pages
- Broken wikilinks fixed: [[first-principles-thinking]] → plain text in elon-musk.md, [[context-rot]] → plain text in context-engineering.md (2/2)
- Orphans detected: 8 pre-existing (analogical-overshadowing, antique-market-lemons, ba-vs-sa-boundary, emergency-psychological-response, hidden-fatigue, lee-kuan-yew-leadership, sincerity-communication, three-career-scripts-analysis)
- Frontmatter validated: all 3 new raw files OK
- Manifest: 453/453 marked built

