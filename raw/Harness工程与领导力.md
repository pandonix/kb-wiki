---
source_url: local
ingested: 2026-04-20
sha256: 67a9c6a7e9a369c205e810a407d3975cae28830b274976e3e2c9982399264be1
---
2026 年 AI/Agent 语境里的 **Harness Engineering**，那它不是“把模型调得更聪明”，而是把模型外面的整套系统设计好：包括状态、工具、提示、执行编排、反馈闭环和可执行约束。OpenAI 也把工程师的角色概括成：人负责“设环境、定意图、建反馈”，agent 负责执行。 ([LangChain Blog](https://blog.langchain.com/the-anatomy-of-an-agent-harness/ "The Anatomy of an Agent Harness"))

我会把它分成 **核心三件事**，再加 **三项放大器**。

1. **共享上下文 / 知识事实源**  
    这是第一关键。OpenAI 的做法不是塞一个超长说明书给 agent，而是把 `docs/`、架构说明、执行计划、质量文档、技术债都和代码一起版本化，`AGENTS.md` 只做“目录”。原因很简单：对 agent 来说，看不见的知识就等于不存在。 ([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))
    
2. **验证—反馈闭环**  
    这是第二关键。LangChain 的实验里，**模型不变，只改 harness**，成绩也能明显提升；最有效的抓手是 traces、自验证、verification/scoring，以及围绕失败模式的持续迭代。OpenAI 也是把 testing、validation、review、feedback handling、recovery 编进系统后，agent 才真正接近端到端完成任务。 ([LangChain Blog](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/ "Improving Deep Agents with harness engineering"))
    
3. **架构边界 / 强约束**  
    这是第三关键。OpenAI 明确强调的是 **enforce invariants, not micromanage implementations**：不要事无巨细规定怎么写，而是把边界、依赖方向、层次结构和必要校验做成机械可执行的规则，比如结构测试、lint、边界校验。这样 agent 才能快，但不至于把系统写散。 ([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))
    
4. **可观测性与系统可读性**  
    UI、日志、指标、trace，最好都直接暴露给 agent。OpenAI 为 Codex 接上了 UI 操作、DOM 快照、日志、指标和 trace 查询能力，这样 agent 才能自己复现 bug、验证修复、理解行为。没有这层“看见系统”的能力，很多自动化都只是盲飞。 ([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))
    
5. **自治执行 + 升级机制**  
    成熟 harness 不是全自动乱跑，而是“能自主就自主，需判断时再升级给人”。OpenAI 描述的阈值很清楚：agent 可以验证现状、复现问题、修复、开 PR、响应反馈、处理构建失败，只有遇到需要判断时才升级给人。 ([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))
    
6. **熵管理 / 持续清理**  
    agent 会复制仓库里已有模式，好的坏的都会复制，所以必须做持续“垃圾回收”。OpenAI 后来把 golden principles 写进仓库，并定期让后台任务扫描偏差、更新质量评分、发起定向重构 PR；否则系统会越来越漂。 ([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))
    

把它和组织管理中的领导力对照，最相通的是这几条：

1. **领导力的“定方向”**  
    对应 harness 的“给地图，而不是给一堆口号”。优秀领导不是把所有细节都讲一遍，而是把战略、原则、优先级沉淀成团队都能执行的共同语境。这个和“repository knowledge 是 system of record”本质一样。 ([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))
    
2. **领导力的“设边界，不微操”**  
    组织里好的领导会讲清楚什么不能碰、什么必须守、质量底线是什么，但不会连每一步动作都替下属决定。这和 harness 里“约束不变量，而不是微观实现”是同一思路。 ([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))
    
3. **领导力的“搭环境、长能力”**  
    OpenAI 说得很直白：工程团队的主业变成了“让 agent 能做好工作”。这和管理里最成熟的领导力也很像：不是自己下场包办，而是搭平台、给工具、补机制，让团队能持续产出。 ([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))
    
4. **领导力的“用反馈系统管理，而不是靠感觉管理”**  
    组织管理里看节奏、看复盘、看指标、看问题闭环；Harness Engineering 里看 trace、看 eval、看测试、看验证。两边共通点都是：不能只看“有没有做”，而要看“有没有证据证明做对了”。 ([LangChain Blog](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/ "Improving Deep Agents with harness engineering"))
    
5. **领导力的“授权，但保留升级通道”**  
    好的领导不会所有事都自己批，也不会完全撒手不管；而是让团队在边界内自主推进，碰到判断型问题再升级。这和 OpenAI 描述的 agent autonomy 很一致。 ([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))
    
6. **领导力的“反熵”能力**  
    组织天然会长出冗余流程、口头规则、隐性山头；代码库天然会长出坏模式和技术债。真正强的领导者，会持续做组织清理、原则固化、节奏校正。Harness 里的 garbage collection，本质上就是组织管理里的“持续反熵”。 ([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))
    

我自己的总结是：

**Harness Engineering 最像的不是“技术调参”，而是“组织操作系统设计”。**  
它和领导力最深的相通之处，不是“你有多会亲自干活”，而是：  
**你能不能把目标、边界、信息、反馈和纠偏机制设计到位，让系统在你不盯着的时候也持续做对事。**

如果你愿意，我下一条可以直接把它整理成一个 **“Harness工程 vs 领导力” 一页式对照框架**，适合拿去做团队分享。