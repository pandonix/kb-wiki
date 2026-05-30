     1|---
     2|title: AI Coding / Agent 工程
     3|created: 2026-04-24
updated: 2026-05-22
type: concept
tags: [ml, coding, infra]
sources: [raw/articles/AI编程的现状与未来.md, raw/articles/Codex的多Agent并行开发指南.md, raw/articles/OpenGame Open Agentic Coding for Games.md, raw/articles/How To Be A World-Class Agentic Engineer.md, raw/articles/消耗了上百亿 Token后， 对于 Agent 时代软件构建、软件形态及未来发展的思考.md, raw/articles/Karpathy 最新访谈：Vibe Coding 只是开始，真正重要的是 Agentic Engineering.md, raw/papers/SWE-chat Coding Agent Interactions From Real Users in the Wild.md, raw/articles/Agent Skills 终极指南：入门、精通、预测.md, raw/articles/OpenClaw和Claude Code只是第一阶段，Github 这两个项目正指向终局——AI 编程三阶段构想（万字长文慎入）.md, raw/articles/有效的 Context 工程（精读、万字梳理）.md]
     8|confidence: high
     9|---
    10|
    11|# AI Coding / Agent 工程
    12|
    13|## 核心定义
    14|
    15|AI Coding Agent 工程是指构建以 LLM 为核心执行者、能够自主完成复杂软硬件任务的系统所需的一套工程方法论。核心问题不是"模型够不够强"，而是**如何设计 harness（驾驭系统）让 agent 的能力得以兑现**。
    16|
    17|## 关键洞察
    18|
    19|### 2025年11月是临界点
    20|
    21|2025年11月，前沿头部大模型跨过了某个阈值——系统可以完全自主完成长程、复杂的软件任务，交付结果可用。之前所有 Coding Agent 都只能起到辅助作用；之后系统级自主成为可能。^[
    22|消耗了上百亿 Token后， 对于 Agent 时代软件构建、软件形态及未来发展的思考.md
    23|]
    24|
    25|### 代码已变成执行载体，不再是思考媒介
    26|
    27|程序员过去用代码思考；今天 AI 在生成代码，人不再需要看代码。代码变得和硬件一样——是执行载体，而不是思考对象。^[
    28|消耗了上百亿 Token后， 对于 Agent 时代软件构建、软件形态及未来发展的思考.md
    29|]
    30|
    31|### 提示词工程师已死，指令精确化才是壁垒
    32|
    33|模糊指令（"帮我做个认证系统"）让 agent 浪费上下文去调研，幻觉率高。精确指令（"JWT + bcrypt-12 + 7天刷新令牌旋转"）效果好得多。不知道细节时，应先做独立研究任务，再切到实现任务。^[
    34|How To Be A World-Class Agentic Engineer.md
    35|]
    36|
    37|### Agent 的"逢迎性"是真实陷阱
    38|
    39|Agent 天然想讨好：让你找 bug，它就会制造 bug；让你找问题，它就会硬找问题。解决方案是用中性提示，或构建三代理系统（Bug-finder → Adversarial → Referee）。^[
    40|How To Be A World-Class Agentic Engineer.md
    41|]
    42|
    43|### 上下文膨胀是最大杀手
    44|
    45|不能让 agent 同时看到过多历史上下文。最有效的模式是：先用一个 agent 做调研，再用全新上下文的另一个 agent 去编码，避免污染。^[
    46|How To Be A World-Class Agentic Engineer.md
    47|]
    48|
    49|### OpenGame 论文核心贡献
    50|
    51|游戏生成是从单次代码生成问题到 agentic software engineering 系统的范式转变。核心三点：多阶段 workflow 而非一次性生成；可复用模板技能（Template Skill）而非从零开始；动态执行评测而非只看静态代码。^[
    52|OpenGame Open Agentic Coding for Games.md
    53|]
    54|
    55|## OpenAI Codex 的实践
    56|
    57|Michael Bolin（OpenAI Codex 技术负责人）访谈核心观点：
    58|
    59|- 人类核心价值：提出正确问题的能力，比单纯写代码更重要
    60|- 长期趋势：Agent 执行更多迁移到云端，而非本地
    61|- 真正拉开差距的：不是写代码的速度，而是选择解决什么问题、如何定义"更好的系统"
    62|- 他本人工作中 80-90% 代码由 AI 生成，主要专注底层、安全性要求高或架构关键部分的手动编写
    63|
    64|## 多 Agent 并行开发模式
    65|
    66|### 角色三层分工
    67|
    68|| 角色 | 职责 |
    69||------|------|
    70|| 主控 Agent | 拆需求、判断依赖、分派任务、汇总结果、决定合并顺序 |
    71|| 实现 Agent | 各自负责边界清晰的子任务（API/Service/Frontend/Test/SQL/Docs） |
    72|| 审核 Agent | review 代码风格、检查接口契约、跑测试、回归检查、找冲突点 |
    73|
    74|关键原则：写的人和验的人必须分开。^[
    75|Codex的多Agent并行开发指南.md
    76|]
    77|
    78|### 任务拆分原则
    79|
    80|**适合并行：** 独立页面+接口、不同微服务、测试补齐、文档脚本配置调整、同一需求下前后端分工、独立子模块
    81|
    82|**不适合并行：** 多个 agent 同时改同一个核心文件
    83|
    84|## Karpathy：Vibe Coding vs Agentic Engineering
    85|
    86|Vibe Coding = 自然语言描述意图，AI 生成代码，人做高层方向控制。适合小项目，大项目仍需工程纪律。^[
    87|Karpathy 最新访谈：Vibe Coding 只是开始，真正重要的是 Agentic Engineering.md
    88|]
    89|
    90|真正重要的是 Agentic Engineering——从"人写代码"到"人设计系统、Agent 执行"的转变。关键技能从编码能力变为架构设计、意图精确表达、反馈闭环设计。
    91|
    92|### Software 3.0 的关键
    93|
    94|Software 3.0 不是"用自然语言写代码"，而是通过 prompt 和 context 操作 LLM 这个新的信息处理解释器。context window 成为人操纵 LLM 的"把手"。^[
    95|Karpathy 最新访谈：Vibe Coding 只是开始，真正重要的是 Agentic Engineering.md
    96|]
    97|
    98|### MenuGen 启示
    99|
   100|很多 AI 应用以为在做"更快的软件"，但 Software 3.0 里模型本身可能直接覆盖整个任务，中间 App 结构失去必要性。不是把已有东西做得更快，而是以前根本不可能存在的东西。
   101|
   102|### 可验证性决定自动化边界
   103|
   104|- 传统计算机：容易自动化你能写进代码的东西
   105|- LLM：容易自动化你能验证的东西
   106|- 数学/代码能力飙升 → 因为能构造 RL 奖励环境
   107|- "锯齿状智能"：模型受制于实验室喂了什么数据
   108|
   109|### 人类价值：品味、判断、规格设计
   110|
   111|- **细节可以外包，理解不能外包**：API 名称可以忘，但概念结构不能丢
   112|- Agent 可以写支付逻辑，但人要理解用户身份和资金归属
   113|- Agent 可以生成大量代码，但人要判断抽象是否臃肿
   114|- "你可以外包你的思考，但不能外包你的理解"
   115|
   116|### Agent Skill 是新编程范式
   117|
   118|Skill 将垂直领域知识、脚本调用方法挂载到 Agent 上下文窗口，零代码创建垂直 Agent 应用。非技术人员可将专业经验写成文档，Agent 即可照执行。^[
   119|Agent Skills 终极指南：入门、精通、预测.md
   120|]
   121|
   122|## AI 编程三阶段构想
   123|
   124|从 OpenClaw/Claude Code 到 GSD/Matt Pocock，AI 编程正在从个人增强走向流程组织，最终指向全智能软件工厂。^[
   125|OpenClaw和Claude Code只是第一阶段，Github 这两个项目正指向终局——AI 编程三阶段构想（万字长文慎入）.md
   126|]
   127|
   128|### 第一阶段：智能开发工作台
   129|
   130|一人 + 一强 Agent + 工具调用 + 项目上下文。人类是主体，Agent 是增强工具。上下文窗口是全部工作空间，没有显式流程和结构化任务分解。天花板：项目规模超过单上下文窗口容量时开始吃力。Claude Code 是典型代表。
   131|
   132|### 第二阶段：流程化 Agent 工坊
   133|
   134|从"人类手动驾驶 Agent"到"用流程和规格驾驶 Agent"。核心项目：
   135|- **GSD**：把聊天驱动推进到规格与流程驱动，维护 PROJECT.md/STATE.md/PLAN.md 等项目状态系统
   136|- **Matt Skills**：把资深工程师工作习惯（/grill-me → /to-prd → /to-issues → /tdd）沉淀为可调用 Agent 能力
   137|- **Sandcastle**：Agent 在隔离 Docker/分支/worktree 中运行，支持并行与 review
   138|
   139|关键转变：流程显性化，上下文管理从"聊天历史"升级为"项目状态"，Worker/Checker 角色分化，工程纪律编码为可执行约束。
   140|
   141|### 第三阶段：AI 软件工厂
   142|
   143|多个 Agent 组成能持续交付的软件公司。核心构件：
   144|- **认知时空图谱**：动态演化的生产图谱，时为阶段演进（需求→PRD→架构→开发→测试→交付），空为并行任务空间
   145|- **认知单元**：Worker + Checker + Contract + Runtime + Memory + Escalation Policy 的闭环生产细胞
   146|- **三个平面**：设计/契约平面（Contract Registry）→ 工作平面（认知单元调度）→ 运行环境平面（代码/容器/CI/测试），三者必须闭环
   147|- **Human-as-a-Skill**：人类成为系统可按需调用的专家资源——精确识别何时需要何种人类介入
   148|- **图谱可演化/可重构/可回滚**：从需求到代码到测试结果的完整因果追踪（Trace Graph）
   149|
   150|三个阶段不是互相替代，而是层层包含。^[
   151|OpenClaw和Claude Code只是第一阶段，Github 这两个项目正指向终局——AI 编程三阶段构想（万字长文慎入）.md
   152|]
   153|
   154|## SWE-chat：真实世界的 Coding Agent 数据
   155|
   156|6,000 coding sessions、63,000+ user prompts、355,000+ tool calls 的实证研究（2026）：^[
   157|SWE-chat Coding Agent Interactions From Real Users in the Wild.md
   158|]
   159|
   160|### Coding Mode 双峰分布
   161|
   162|| Mode | 占比 | 特征 |
   163||------|------|------|
   164|| Human-only | 22.7% | 纯人写 |
   165|| Collaborative | 36.5% | 人机协作 |
   166|| Vibe coding | 40.8% | 全自动（3 个月从 20% 升到 40%+） |
   167|
   168|### 关键发现
   169|
   170|- **代码存活率仅 44.3%**：Agent 产出代码中只有不到一半活进 commit
   171|- **Collaborative 更高效**：每 100 行 committed code，vibe coding 的 token 消耗约是 collaborative 的 3 倍
   172|- **安全风险显著**：vibe coding 引入漏洞速率为 human-only 的 9 倍（0.76 vs 0.08/1K lines）
   173|- **Agent 很少主动澄清**：只有 1.1%-2.6% 的 turn 主动 ask for clarification
   174|- **用户频繁纠偏**：约 39% 的 turn 出现 pushback
   175|- 核心结论："Autonomy is outpacing oversight"
   176|
   177|### 对工作流的启示
   178|
   179|- 不该只优化"最后写代码"，应优化理解/澄清/review/纠偏/安全验收
   180|- 一主一审的分工比单 agent 一把梭更符合现实
   181|- 未来真正有价值的是"监督成本最小化"
   182|
   183|## Hy3 与单位智能时代
   184|
   185|Agent 时代一次任务动辄几十万乃至上百万 token，**单位推理成本**成为决定产业形态的结构性变量。质量、速度、价格的"不可能三角"让"一个模型打天下"失效：^[从 Hy3 preview 看 AI 下半场.md]
   186|
   187|### 复杂推理 vs 日常 Agent 任务
   188|
   189|| 维度 | 复杂推理 | 日常 Agent 任务 |
   190||------|----------|----------------|
   191|| 典型场景 | 代码调试、数学证明、科研写作 | 识别、整理、抽取、改写、翻译、结构化 |
   192|| 质量要求 | 极高，少数关键调用决定产出 | "够用就好" |
   193|| 成本敏感度 | 愿为单次高质量付高价 | 价格×调用量 = 大窟窿 |
   194|| 模型倾向 | 旗舰大模型 | 中型高吞吐模型 |
   195|
   196|### 模型路由成为基本工作流
   197|
   198|通过自动路由或手工切换，在"复杂推理旗舰模型"和"日常任务中型模型"之间分工协作。主流 AI IDE 已在后台按任务复杂度自动分发模型。
   199|
### Harness 的产业翻译

"竞争焦点从谁能把模型训练得更好，转向谁能为任务提供最丰富、最相关的 context。"——一个能力 80 分的模型配一套 90 分的 Harness，可以碾压一个 95 分但只有裸 API 的竞品。详见 [[harness-engineering]]、[[ai-second-half]]。

## 相关概念

- [[harness-engineering]] — 驾驭系统的核心方法论
- [[declarative-architecture]] — 架构治理的声明式路径
- [[ai-alignment]] — AI 目标与人类意图对齐
- [[ai-software-form-evolution]] — 软件形态的演进
- [[multi-agent-collaboration]] — 多 Agent 协作模式
- [[ai-code-adoption]] — AI 代码采纳率提升工程实践
- [[ai-code-review]] — AI 代码审查方法论
- [[context-engineering]] — 上下文工程与上下文污染管理
- [[agentic-ai]] — Agentic AI 四种设计模式
- [[ai-coding-three-stages]] — AI 编程三阶段构想
- [[ai-second-half]] — AI 下半场与单位智能经济
- [[saas-bench]] — Agent 真实办公能力评测
- [[copilot-learning]] — AI 辅助的学习效果
- [[agent-skills]] — Agent Skill 架构与编程范式
- [[agent-developer-capability]] — Agent开发者的三维能力立方体
- [[karpathy]] — Karpathy 的 Agentic Engineering 实践
