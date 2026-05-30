---
source_url: ""
ingested: 2026-05-27
sha256: 8c9d43f3172783c087a9a0445dfe082854b110bb90bb5c460934b95dff583faa
---

# Palantir AIP 与 Ontology：从企业知识工程视角的系统解读

## 一、为什么这套东西值得单独研究

绝大多数"AI 中台"的方案，本质上是把 LLM 接到一个 RAG 系统上，让模型能"看到"企业的数据。Palantir 的不同之处在于，它把问题重新定义了：

> 企业 AI 的核心瓶颈不是"模型不够强"，而是**"模型没有被嵌入到企业决策的语境里"**——它不知道你公司里"客户"到底是什么、"订单"会怎么流转、"调拨"这个动作触发后会引起什么连锁反应、谁有权批准。

Palantir 的回答是 Ontology——一个**决策中心的语义层 (decision-centric semantic layer)**，把数据 (data)、逻辑 (logic)、行动 (action) 三件事缝合到一个统一的、可被人类和 AI 同时理解的表示里。AIP 则是建在 Ontology 之上的 AI 能力层。

这个抽象对你关心的"从数据挖掘 → 分析 → 决策 → 实施"闭环来说，恰好是核心。

---

## 二、Ontology：不是数据模型，是企业的"数字孪生"

### 2.1 它在表示什么

传统数据建模表示的是**"数据"** ——表、列、外键。Ontology 表示的是 **"业务现实"**：

| 维度 | 内容 | 例子 |
|---|---|---|
| **Object Types (名词)** | 业务实体 | `Customer`, `Aircraft`, `PurchaseOrder`, `FieldServiceTicket` |
| **Links (关系)** | 实体之间的语义关系 | "客户 *拥有* 订单"、"工单 *分配给* 工程师"、"飞机 *服务于* 航线" |
| **Properties** | 实体的属性，可来自多源融合 | 同一个"John Smith"在 HR 系统、邮件系统、财务系统里的不同 ID 都被 resolve 到同一个 Object |
| **Actions (动词)** | 业务上"可以做"的事 | `下单`、`调拨库存`、`派工`、`审批` |
| **Functions / Models** | 业务逻辑、ML 模型、优化算法 | 需求预测、库存优化、设备故障检测 |

关键的设计哲学：**Ontology 表示的是企业里"如何做决策"，不是"数据躺在哪里"。**

### 2.2 与传统知识图谱的区别

如果你熟悉 RDF/OWL 或学术性的 Knowledge Graph，会发现差异很明显：

| | 传统 KG | Palantir Ontology |
|---|---|---|
| 重心 | 知识表示与推理 | 操作 (operation) 与决策 |
| 实体粒度 | 概念级 | 业务对象级（每个具体客户、每个具体订单） |
| 是否包含动作 | 几乎不 | **核心组成部分** (Actions) |
| 与执行系统关系 | 解耦，主要用于查询 | **写回 (write-back) 是一等公民** |
| 安全模型 | 通常事后补 | 行/列/对象级权限内建 |

差别最大的就是 **Action**——传统 KG 里没有"动词"的位置，但企业决策的本质就是"在某个状态下，触发某个动作，改变状态"。把 Action 提到一等公民的位置，是 Palantir 在概念上做的最重要的一步。

---

## 三、AIP：让 LLM 在 Ontology 的"边界"内工作

### 3.1 OAG：Ontology Augmented Generation

你应该熟悉 RAG。Palantir 提出了一个延伸概念叫 **OAG (Ontology Augmented Generation)**。差别是：

- **RAG**：LLM 检索文本片段 → 拼到 prompt 里 → 生成回答。回答的质量取决于检索到的文本。
- **OAG**：LLM 拿到的不是文本片段，而是 **Ontology 对象**——它知道这是一个 `PurchaseOrder`，金额是多少、关联的客户是谁、当前状态是什么、可以执行哪些 Action、谁有权执行。

后者的好处不只是"更准"，而是 **LLM 的推理被限制在了一个语义闭包里**：它只能在你授予的对象、函数、动作的边界内活动。这同时解决了三件事：幻觉（数据有结构化语义）、权限（继承 Ontology 的 ACL）、可审计（每一步都是 typed call）。

### 3.2 AIP Logic：把 LLM 编排成可治理的"函数"

AIP Logic 是一个低代码环境，把 LLM 变成一个有清晰 I/O 契约的**函数**。它由 **blocks** 组成，blocks 有几种关键类型：

| Block 类型 | 作用 |
|---|---|
| **Use LLM** | 给 LLM 一段 prompt + 工具集，让它推理 |
| **Apply Action** | **确定性**地调用一个 Ontology Action（不经过 LLM） |
| **Execute Function** | 调用 TypeScript / Python 函数，或其他 Logic |
| **Transform** | 数据变换 |
| **Loop / Branch** | 控制流 |

LLM 能用的"工具"分三类，恰好对应 Ontology 的三要素：
- **Data tools**：查询对象、做语义搜索
- **Logic tools**：调用模型、调用函数
- **Action tools**：申请执行某个 Action（注意：LLM 不直接执行，它只能"请求"）

一个关键的工程性细节：**Logic 函数要真正写回 Ontology，必须从一个 Action 里被调用。**这是把"AI 的建议"和"对世界的修改"显式分离的设计——LLM 永远不能绕过 Action 的权限和验证去改数据。

### 3.3 决策的回写（write-back）：闭环的关键

这是整个架构最有价值的一环，也是大多数企业 AI 方案缺失的部分。当一个决策完成后：

1. LLM 的**推荐内容**被写回 Ontology
2. LLM 的**推理链 (chain of thought)** 被记录
3. **人工审核反馈**（接受/修改/拒绝）被写回
4. **最终决策结果**和**执行后的实际效果**被写回

这套数据 Palantir 称为 **decision lineage**，可以用来：
- 微调模型（用真实人工决策做 SFT 数据）
- 蒸馏成 prompt 时调用的"原则" (principles)
- 做 few-shot 动态示例
- 评估系统性能（AIP Evals）

这就是为什么 Ontology 被称为 agents 的"持久化记忆 (persistent memory system)"——不是 vector store 那种简单的语义记忆，而是包含了**事件性、语义性、程序性、决策性**记忆的统一表面。

---

## 四、对照你关心的"数据挖掘 → 分析 → 决策 → 实施"闭环

我把每一环和 AIP/Ontology 的对应能力列出来：

### 4.1 数据挖掘 / 集成
- **Foundry Pipeline Builder + 各类连接器**（JDBC、Kafka、OPC-UA、MQTT、SAP、Snowflake 等）做接入
- **Object Type 映射**：把表 + 列 → 业务对象，跨系统的同名实体被 resolve（实体解析）
- **AIP 在 pipeline 里**可以用 LLM 节点做非结构化数据抽取（例如从合同 PDF 里抽取条款 → 结构化 Object）

### 4.2 分析 / 洞察
- **Functions on Objects**：把分析逻辑（包括 ML 模型）挂在 Object 上，让查询能直接调用
- **Workshop**：业务用户拖拽式构建分析应用，但底下访问的是 Ontology
- **AIP Logic + LLM**：自然语言问答、多步推理（例如"找出过去 6 个月里所有维护成本异常的设备，并解释可能原因"）

### 4.3 决策
- **Scenario / Simulation**：在 Ontology 上做"假设性"修改，看下游影响（不实际写回）
- **AIP Agent 推荐**：LLM 给出建议 + 推理 + 引用的对象
- **Human-in-the-loop**：建议先 stage，人工审核

### 4.4 实施
- **Actions**：定义业务动作（带参数验证、权限、副作用）
- **Automate**：可以把 Logic 函数挂成自动化触发
- **Write-back to source systems**：通过 Ontology 的反向连接器写回 ERP、SCM、SaaS 等

### 4.5 学习闭环
- **AIP Evals**：单元测试、A/B 不同 LLM、跨执行的 variance 分析
- **Decision lineage**：上面提到的回写
- **Feedback design pattern**：在 Workshop 里建审核界面，把人类反馈作为 Ontology 对象（"Suggestion"对象），下次 LLM 推理时通过 Query objects tool 检索历史

---

## 五、几个值得批判性思考的点

我觉得有必要在你研究的时候保持一些清醒：

### 5.1 这套方法论的"重"

Palantir 这套架构能跑起来，前提是有人把企业的本体建好。这个工作非常重——Palantir 的盈利模式很大程度上依赖 **Forward Deployed Engineers (FDE)**，派工程师驻场和客户一起建 Ontology。文献里反复强调"Ontology 不是一开始就完美，而是在使用中不断丰富"——意思是这是一个**持续投入**的过程，不是装个软件就完了。

对比 RAG 类方案的"轻"，这是 trade-off 的另一极。

### 5.2 锁定效应

正因为 Ontology 是企业组织知识的具体化形态，一旦建成，迁移成本极高。文章里直接说："切换的主要驱动力不是软件迁移，而是重建 Ontology"。这是商业上的护城河，但对客户也是风险——你需要清楚自己接受的是什么。

### 5.3 概念上的真创新 vs. 营销包装

我个人的判断：
- **Ontology 把 Action 作为一等公民**——这是概念上真有分量的创新
- **OAG 这个名字**——更多是营销，本质是"用 typed schema 的检索代替 raw text 检索"，思路在工程界其实早就有（function calling、structured retrieval），但 Palantir 把它端到端做扎实了
- **Decision lineage / write-back 闭环**——执行层面非常扎实，多数竞品做不到这种程度的整合
- **k-LLM 哲学**（不绑死某一家模型）——务实

### 5.4 适用场景

我觉得这套东西最适合的场景：
- **已有大量异构系统**、数据集成是真痛点的大型企业（制造、能源、国防、金融、医疗）
- 决策有**明确的业务对象和动作**（不是开放式创意类工作）
- 需要**审计和可追溯**（受监管行业）
- 有预算和耐心做长期的本体建设

不太适合：
- 中小型公司，主要是 SaaS 拼装的轻量业务
- 决策主要靠人的经验和创意，难以建模
- 想"快速试一下 AI"而不愿做底层工作

---

## 六、给你的学习路径建议

如果是认真研究而不是泛读，建议这个顺序：

1. **先读 Palantir Blog 上的几篇核心文章**（不是产品文档，是讲哲学的）：
   - "Connecting AI to Decisions with the Palantir Ontology"
   - "Building with Palantir AIP" 系列（特别是讲 OAG 的那几篇）
   - "How Palantir AIP Enables UNS for Industry AI"

2. **官方文档里精读两块**：
   - Ontology 的核心概念（Object / Link / Action / Function）
   - AIP Logic 的 blocks 和 tools 模型

3. **看一个端到端的 demo**——Palantir AIP 有公开的演示视频，看完一个具体 use case（比如供应链中断响应、医院床位调度）会比读十篇文章都有用

4. **如果有机会**：参加 AIP Bootcamp（Palantir 主推的一种快速上手培训）。这是他们的销售漏斗，但内容是真的能学到东西

5. **批判性对照**：去看看 Databricks、Snowflake、微软（Fabric + Copilot Studio）的对应方案。Palantir 的概念比较前沿，但具体能力上各家都在追，你要看清楚自己的需求落在谱系的哪一端。

---

## 七、一句话总结

Palantir 的核心 insight 是：**企业 AI 落地的瓶颈不是模型，而是把"模型的输出"和"企业里真实的决策与动作"之间的鸿沟填上**。Ontology 是这条桥的语义骨架，AIP 是桥上跑的车，write-back 是回程的路——三者共同构成了一个**可学习、可审计、可治理**的决策闭环。

这套思路是否值得你借鉴，取决于你企业知识工程的目标，是"让 AI 能回答问题"，还是"让 AI 参与企业的运行本身"。如果是后者，这是目前最系统的参考样本之一。
