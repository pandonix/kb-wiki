---
title: AI Native 组织模式
created: 2026-05-22
updated: 2026-06-08
type: concept
tags: [management, agent, company]
sources: [raw/articles/组织能力才是 AI 公司真正的壁垒｜42章经.md, raw/articles/2026-05-28-AI越强人越忙一个住在未来的人说了什么.md, raw/articles/2026-06-01-AI-native下组织形式思考.md, raw/articles/2026-06-01-一个理想的组织是AI Agent在组织人.md, raw/articles/Claude Code之父：品味不是人类护城河；当工程师不再写代码，招聘看什么？.md]
confidence: medium
---

# AI Native 组织模式

42章经播客中任川分享的 AI Native 工程团队实践：从工作流、人才、组织三个维度重构研发。

## 工作流：默认由 AI 承担所有研发工作

核心思维转变：不是偶尔发现 AI 能帮忙时才让它介入，而是**默认所有事都由 AI 完成，只有当 AI 确实解决不了时，人类再补位**。

### 具体实践

- **Code Review**：只让 AI 来做 Review。传统 Google 级别效率也要 1-2 天，AI 只需 10 分钟。AI Review 还能减少人际摩擦——工程师不会觉得被「挑刺」。CodeRabbit 批准即合并。
- **Coding**：Linear 管理任务，Devin 生成代码。一次性创建 10 个任务，Linear 自动分配给 Devin 批量生成。约 90% 代码由此方式生成，甚至不需要打开 IDE。
- **生产监控**：incident.io 自动分析预警，覆盖近一半监控需求。不再需要专职运维。
- **GTM 自动化**：传统销售链条 4-5 人，AI 可能让一个人 end-to-end 完成。

### 三条经验

1. **默认由 AI 承担**，而非默认由人承担
2. **推荐 Claude Code**：能力本身强，且有 SDK 可做大量二次开发
3. **减少人与人之间的对齐**：让每个人从头到尾独立完成工作，在代码里对齐

## 人才：三类核心角色

### Context Provider（上下文提供者）

「人 + AI」的产出必须大于「AI 单独工作」的产出。AI 产出效果不够好，更多是因为 Context Engineering 不够好。人类的核心价值是提供 AI 不具备的领域知识。

### Fast Learner（快速学习者）

不在乎已有多少技能，更在乎能否快速掌握最少必要知识，把目标和问题定义清楚，激发 AI 的潜力。

### Hands-on Builder（动手建造者）

哪怕只负责产品的一小部分，也要对全流程和最终结果负责。只要出现 Context 传递，团队效率就显著下降。未来可能不再有「PM」和「工程师」的严格区分，大家都是 Builder。

## 组织：按结果分工

传统「按流程分工」（前端组、后端组、运维组）在 AI 时代不再合理——可能 98% 的工作由 AI 完成，人类只在 AI 做不了的地方补位。

改为**按结果分工**：对消费者体验负责的小组具备前后端、运维等全链路能力。工程师也参与产品设计、GTM，自己去跑客户获取一手反馈。

### 核心原则

- 以工程团队为核心：工程团队最容易为结果负责
- **「Talk is cheap, but code is cheaper」**：先上线 60 分版本，再一起做到 100 分
- 减少会议：集中在中间 3-4 小时，其他时间各自做事

### 未来的组织形态

「少量核心合伙人 + 大量灵活合同工」。每个人都按结果分工、为结果负责，一个人的价值和不可替代性很高。给核心员工合伙人级别的待遇，大量灵活合同工作为补充。

## 大厂为何难以效仿

大厂想调整组织架构要考虑的不只是效率，还有很多额外因素（如微软 CEO 因裁员过猛公开道歉）。但若未来几个人就能做出惊人的产品，可能也不需要十万人的公司。

## 相关概念

- [[ai-native-engineering-management]] — AI 时代工程团队管理（Fiona Fung 视角）
- [[hierarchy-to-intelligence]] — 科层制到智慧型组织
- [[ai-organization-adoption]] — AI 组织采纳困境
- [[context-engineering]] — 上下文工程
- [[business-generalist]] — 通用型创业者
- [[ai-native-bank]] — AI 原生银行：金融业的 AI Native 组织形态
- [[ai-strategy-positioning]] — AI 战略定位与组织形态选择
- [[ai-outcome-pod]] — AI Outcome Pod：人机混合结果单元
- [[soul-team]] — Soul Team：AI 原生组织的叙事一致性团队
- [[boris-cherny]] — Anthropic MTS：Generalist 黄金时代与 Token 预算
- [[anthropic]] — Anthropic 的组织实践：MTS、Builder、少招人多给 Token

## AI Outcome Pod：AI-native 的基本组织单元

Source 1 提出了 AI Outcome Pod 作为 AI-native 组织的核心建模概念。未来组织的基本单位不再是部门或岗位，而是由**人、AI Agent、数据、工具流和治理规则组成的结果单元**（Outcome Pod）。^[2026-06-01-AI-native下组织形式思考.md]

### 与传统组织的对比

以「上线一个新支付方式」为例，组织形态演化路径：
1. **层级制**：产品写需求→研发排期→测试验证→法务审核→运营培训→客服准备话术。每步很稳，周期长
2. **项目制/矩阵制**：从各部门借人组成临时项目组，效率提高但双重汇报
3. **敏捷 Pod**：固定小队长期负责，产品、研发、测试、数据同队快速迭代
4. **AI Outcome Pod**：小队不仅有人，还配置需求拆解 agent、代码生成 agent、测试用例 agent、风控规则检查 agent、客服知识库 agent。人的重点从「亲自做每个环节」转向**定义目标、审核关键判断、处理异常**

关键洞察：技术每降低一次协调成本，组织就有机会向更小、更快、更结果导向的单元迁移。^[2026-06-01-AI-native下组织形式思考.md]

### 行业样本

| 公司 | 实践 | 核心变化 |
|------|------|----------|
| Meta | AI-native Pods（Reality Labs 1000人团队试点） | 三个角色：AI Builder / AI Pod Lead / AI Org Lead；岗位边界弱化，结果导向强化 |
| Microsoft | Frontier Firm / Work Chart | 三阶段：Human with assistant → Human-agent teams → Human-led, agent-operated；传统 org chart 变为围绕目标临时组织的 dynamic Work Chart |
| McKinsey | Agentic Organization | 从职能孤岛转向跨职能 autonomous agentic teams；从单点 AI 工具转向端到端 agentic workflow；CEO 和业务负责人共同重构运营模式 |
| Shopify | AI-first 进入管理制度 | AI 使用是基础期待；申请新增人力前要证明 AI 不能完成；AI 使用进入绩效与同事评价 |
| Duolingo | AI-first 招聘与绩效 | 对 AI 可处理的工作减少承包商依赖；新增 headcount 要证明团队不能进一步自动化 |

Source 1 强调：AI 价值不是来自「买一个工具」，而是来自 **rewiring workflows**——重写组织运行方式。流程没变、决策权没变、数据权限没变、KPI 没变、人机责任边界没变时，AI 只能成为「更快写文档的工具」。^[2026-06-01-AI-native下组织形式思考.md]

### 四类未来组织原型

AI-native 组织不会只有一种形态，更可能出现四种并存：^[2026-06-01-AI-native下组织形式思考.md]

1. **超小型超级公司**：少数高判断力的人 + 大量 agent/自动化工具/外部服务，完成过去几十上百人的产出。出现在软件、内容、咨询、教育、投研、设计、营销等数字化领域
2. **平台化大组织**：大企业变成能力平台，财务、法务、数据、研发、营销变成可调用服务。业务团队像调用 API 一样调用内部能力
3. **流动项目网络**：围绕产品/市场机会/研究问题，临时聚合人类专家、AI agent、资金、渠道和供应链，完成后快速解散
4. **高信任专业组织**：高端咨询、医疗、教育、艺术、品牌等领域，AI 作后台放大器，人出可信判断

底层共同点：组织的价值不再来自拥有劳动力，而来自**如何配置智能、建立信任、沉淀上下文和承担责任**。^[2026-06-01-AI-native下组织形式思考.md]

## ColaOS：AI-native 组织的实战样本

Source 2 中 ColaOS/ListenHub 创始人橘子的实践提供了约 20 人团队的一线经验：^[2026-06-01-一个理想的组织是AI Agent在组织人.md]

### 组织架构：Builder + Explorer + Soul Team

- **管理层**：橘子（CEO）、CTO、COO 定方向
- **Builder**：Infra Team、Agent Loop Team、App Team
- **Explorer**：运营增长
- **Soul Team**：负责产品灵魂、叙事、方向一致性——不走传统品牌职能，而是像游戏制作人，把「一句话方向感」转化成每个产品细节的真实质感

### 关键实践

- **一天一版**：每人做完就放进当天包，自动打包、自动写 changelog。错了只持续不到一天
- **减少对齐**：每个人都应有把功能发布上线的权利，有问题再返工。中间每加一个讨论/评估/验收卡点都会慢很多
- **Soul Team 解决方向问题**：AI 开发速度极快，但方向不一致会乱。Soul Team 提供一致的宏大终点，让每个人在其中自由发挥
- **快的关键**：组织能把 AI 的速度变成成果速度，穿透到上线、反馈、撤回、修正和再次上线

详见 [[soul-team]] 和 [[ai-outcome-pod]]。

## Anthropic 的组织实践：MTS、Generalist 与 Token 预算

Boris Cherny（[[boris-cherny]]）在访谈中揭示了 Anthropic 作为 AI Native 组织的内部实践：^[raw/articles/Claude Code之父：品味不是人类护城河；当工程师不再写代码，招聘看什么？.md]

### Member of Technical Staff（MTS）：对未来的预演

Anthropic 很多人只有一个头衔：MTS——不区分设计师、工程师、经理。Boris 认为这是对「职能边界消失」的预演：

- **消除「礼貌性服从」**：如果给人「高级」头衔，别人会因为 deference 而不好意思反驳他的坏主意。把所有人放在平等场域里，迫使大家用想法而非资历竞争
- **经验在 AI 时代可能是负债**：有 20-30 年经验的资深工程师要花好几个月「unlearn」旧习惯；新人反而天然用模型思维思考
- **每次新模型出来，所有人都要 recalibrate**

### Generalist 的黄金时代

Claude Code 团队最喜欢的一类人是 **Generalist（通才）**。过去的软件组织有明确分工（用户研究员 → 设计师 → PM → 工程师），但在 Anthropic 内部这种分工正在迅速瓦解：

- 团队里每个工程师每天都在做各种「不属于工程师职责范围」的事
- 设计师也在写代码，财务同事也在写代码
- Satya Nadella 管这种角色叫 **Builder**——比「工程师」更准确，真正的边界不是「会不会写代码」，而是「能不能把一件事从想法变成现实」
- AI 正在降低能力之间的迁移成本，最有优势的人是能快速跨越不同领域、不断整合资源的人

### 「少招人，多给 Token」

Boris 给创始人的具体建议：

1. **尽量多给 tokens**，让大家疯狂实验
2. **每个项目故意少放人**——如果你觉得需要四个工程师，就只放两个人，然后给他们大量 token，让他们自己想办法

这不仅是降本，而是用**自动化资产替代持续人力摩擦**的组织设计。前期成本（upfront cost）抬高，但持续成本（ongoing cost）大幅降低——像 pre-compiling。

### Claude Code 压缩组织隐性知识

Claude Code 的组织价值不只是写代码更快：新工程师从数周熟悉系统压缩到约两天。过去「数据库怎么查」需要在 Slack 上找人问；现在标准答案是「打开 Claude，让 Claude 去查数据库」。**组织内部隐性知识被转移到 Agent 身上。**

## 从劳动分工到判断与责任系统

综合 Source 1 和 Source 2，AI-native 组织的本质变化是：组织的中心从**劳动分工**推向**判断分工**，从**管理人力**推向**治理智能**，从**拥有员工**推向**编排责任网络**。^[2026-06-01-AI-native下组织形式思考.md]

> 真正的 AI-native 组织，最终不是「AI 很多」的组织，而是「智能被制度化、责任被清晰化、学习被自动化、判断被珍视」的组织。

## Every 实践：Forward Deployed Engineer

Dan Shipper（Every CEO）的实践更新了 AI Native 组织的认识：

Every 是一家约 30 人、全员重度使用 Codex / Claude Code 的公司。反直觉的是，过去一年员工人数翻了一倍。原因正是 **AI 创造了新的工作——管理自动化本身**。^[2026-05-28-AI越强人越忙一个住在未来的人说了什么.md]

### Every 的组织发现

1. **每个 Agent 都需要一个人**：Agent 会坏、会偏离、需要持续维护。没人关心它时就会变得没用
2. **公司级通用 Agent 先于个人 Agent**：现实路径是公司共用一个 Agent → 团队级 → 个人级，而非反过来
3. **Client-to-Agent 架构**：过去把 AI 嵌进 SaaS，未来把 SaaS 放进 Agent 里运行
4. **SaaS 支出反而更高**：Agent 在高频使用 SaaS，成为 SaaS 新用户而非替代者
5. **CLI 被快速穿过**：真正优势不在 CLI 本身，而在本地权限完整和训练数据充分。长期战场回到 GUI

### Forward Deployed Engineer 岗位
Every 内部设立了专门维护 Agent 的角色——Forward Deployed Engineer（前沿部署工程师），负责维护公司级 Agent、处理错误、优化上下文、治理权限。

详见 [[forward-deployed-engineer-ai]] 和 [[agent-owner-role]]。
