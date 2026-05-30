---
source_url: local
ingested: 2026-04-20
sha256: fbee394d059d5c90f9c891f23d3e9cc2e28f7c65172d47098fb1cb5d88d9f333
---
# AI写的代码，Review什么？
---
**100% 由 AI 生成的系统，不应该被当成“自家代码”，而应该先当成“来源不明、行为暂时可用的第三方系统”来审计。**  
你真正要防的，不只是 bug，而是下面这四类“黑盒风险”：

1. **语义漂移**：代码表面可运行，但实现逐步偏离业务真实意图。
2. **结构漂移**：局部改动都成立，但整体架构越来越不一致。
3. **因果不可追溯**：出了问题，没人能回答“为什么这么设计”。
4. **维护权丧失**：AI 能改，AI 也许能暂时修，但人已经不能可靠接手。

这时你要做的，不是普通 code review，而是一次**“可维护性逆向工程”**。

---

## 一、先定一个原则：review 的对象不是代码质量，而是“人类是否重新拿回控制权”

对 AI 生成系统，我建议把 review 目标改写成 5 个问题：

1. **这个系统的边界、职责、约束，能不能被人重新说清楚？**
2. **关键行为背后的因果链，能不能被人验证？**
3. **关键模块的内部意图，能不能脱离原始生成过程而独立成立？**
4. **出故障时，人能不能在不用继续“求 AI 猜答案”的情况下定位根因？**
5. **未来 6–12 个月，这个系统能不能由普通工程团队接管，而不是只能靠生成更多代码苟住？**

如果这五个问题里有两个以上答不上来，这个系统就不该继续无约束膨胀。

---

## 二、从“黑盒拆解”出发，给 AI 生成系统做 review，我建议按 4 层推进

### 第 1 层：黑盒行为审计

先**完全不看源码**，只看系统行为。

你要回答：

- 它到底提供哪些能力
- 输入/输出边界是什么
- 状态如何变化
- 哪些条件下行为异常
- 哪些行为是“看起来正确但原因不明”

这里最适合你前面提到的：

- 输入-输出-状态-边界
- 黑盒测试
- 假设驱动分析

具体产物不要写成散文，要写成 4 张表：

1. **能力清单**：每个能力的触发条件、输入、输出、失败模式
2. **状态转移表**：哪些动作会改变哪些状态
3. **边界条件表**：空值、极值、重复提交、并发、超时、回滚
4. **异常行为表**：当前已观测到的“解释不清”的行为

这一步的目的，是把“系统会做什么”先钉死。  
因为很多 AI 代码库最大的坑，不是实现错，而是**你根本不知道系统实际上承诺了什么**。

---

### 第 2 层：灰盒结构逆向

然后才进入源码，但不要一上来逐文件读。  
先逆向出“骨架”，再看“细胞”。

这一步重点不是代码风格，而是：

- 模块边界是否清晰
- 依赖方向是否单向
- 领域模型是否一致
- 状态管理是否有中心
- 配置、常量、规则是否散落
- 副作用在哪里发生
- 谁负责事务、一致性、重试、幂等

建议你强制产出这 6 个结构图/清单：

1. **模块依赖图**
2. **运行时调用链图**
3. **数据流图**
4. **状态机/生命周期图**
5. **外部依赖清单**（DB、缓存、消息、第三方 API）
6. **规则归属清单**（业务规则到底落在 controller/service/model/sql/脚本/提示词的哪里）

你会很快发现 AI 代码常见的几个结构性问题：

- 同一业务规则在多个层重复实现
- “为了让当前功能跑通”而跨层偷数据
- 逻辑名称相似，但语义不一致
- 隐式状态太多，靠约定运行
- 错误处理分散，恢复策略不统一
- 大量 helper / util / adapter 其实是未命名的领域模块

这种问题，普通 PR review 很难看出来；只有逆向骨架才看得见。

---

### 第 3 层：深层语义审计

这是最重要的一层。  
也是最容易被忽略的一层。

你要追问的不是“这段代码能不能跑”，而是：

- **它为什么要这样做**
- **它本来应该保证什么**
- **它绝不能发生什么**
- **它依赖了哪些未写出的假设**

这里最适合用：

- 冰山模型
- 5 Whys
- 第一性原理
- 系统思维

你要为系统抽出一份 **Invariant Catalog（不变量目录）**，至少包括：

- 业务不变量：例如一个订单不应同时处于互斥状态
- 数据不变量：唯一性、引用完整性、金额守恒、状态闭包
- 并发不变量：重复请求不得造成双写，重试不得破坏一致性
- 安全不变量：权限边界不可绕过，敏感字段不可越权写
- 运维不变量：失败必须可观测，可回滚，可重放

然后逐条问：

- 这个不变量在代码哪里被保证？
- 是单点保证还是多点“碰巧成立”？
- 如果 AI 以后再生成一轮代码，这个保证还在吗？

这一步能直接发现 AI 系统最危险的东西：  
**“语义正确性没有锚点”**。  
也就是现在没出事，只是因为场景还没踩到。

---

### 第 4 层：维护性与失效演练

最后一层不是继续读代码，而是做“接管演练”。

核心问题只有一个：

**如果从明天开始禁止继续让 AI 生成新代码，人类团队还能不能维护它？**

这一步建议你做 3 种演练：

1. **根因定位演练**  
    人只看监控、日志、追踪和源码，能否独立找到一次故障的根因。
2. **局部改动演练**  
    让工程师做一个小变更，看会不会牵出大量不可预期影响。
3. **替换演练**  
    挑一个关键模块，评估能否被人类重写或替换而不伤全局。

如果这三种演练都很差，说明问题不是“代码写得乱”，而是**系统已经丧失可再生性**。

---

## 三、对 AI 生成系统，我会额外检查 8 个“高危点”

### 1. 规范是否先于代码存在

没有规格，AI 只能“局部续写”；系统越大，漂移越快。  
NIST 的 GenAI 风险与安全开发资料都强调治理、测量、验证和与标准开发流程结合，这和你的担心是一致的：不能把生成过程本身当成保证。

要检查：

- 有没有系统级 spec
- 有没有领域词汇表
- 有没有状态/数据契约
- 有没有 ADR（架构决策记录）

没有这些，代码库一定会慢慢演化成“能运行但不可解释”。

---

### 2. 业务规则是否集中

AI 很容易把同一规则复制到多个位置。  
你要查的是“规则的唯一真实来源”是否存在。

例如：

- 折扣规则是不是一处定义，多处调用
- 权限规则是不是集中在授权层
- 状态转移是不是只在状态机/领域服务发生

一条规则若分散在 4 个文件里，你迟早会遇到“修了 A，坏了 B”。

---

### 3. 隐式耦合是否过多

AI 常生成大量“看起来解耦，实际上强耦合”的代码，比如：

- 参数名约定驱动逻辑
- 默认值承担业务语义
- util 函数偷偷依赖上下文
- 顺序执行假设没有显式声明

这类耦合最致命，因为它们在静态阅读时不一定显眼，但在扩展时会爆。

---

### 4. 异常处理是否真实可恢复

很多 AI 代码会“处理异常”，但只是 catch 住并打印。  
你要查的是：

- 是否区分可重试 / 不可重试
- 是否有补偿逻辑
- 是否有死信/隔离策略
- 是否能回滚或重放
- 是否保留 enough context 做根因分析

如果故障后只能“再跑一次试试”，这不叫可维护。

---

### 5. 测试是不是只覆盖表象

OpenAI 在谈 AI-native engineering 和内部 agent-first 实践时，反复强调把 AI 产出纳入标准工程流程，并特别强调测试覆盖与运行时契合，而不是只看模型能不能一次写出代码。甚至在一个内部 beta 产品的案例里，团队提到某些关键辅助组件是专门按运行时约束实现并做到 100% 测试覆盖的。这个信号很重要：**关键模块的可验证性必须被人为加固。**

你要看：

- 测试覆盖的是 happy path，还是覆盖不变量
- 是否有契约测试
- 是否有回归测试
- 是否有属性测试 / 模糊测试 / 并发测试
- 是否有跨模块集成测试

AI 生成系统最危险的错，往往不是 unit test 能抓到的。

---

### 6. 可观测性是否足够支撑人类排障

如果日志、metrics、trace 不是按因果链设计的，人类就永远要继续依赖 AI 猜。  
所以必须检查：

- 每个关键流程是否有 trace id
- 每个状态变更是否可追踪
- 每个决策点是否记录关键输入
- 每个失败是否能关联上下文和版本

这一步其实是在建立“反黑盒能力”。

---

### 7. 代码库是否允许“大块再生成”

这是治理问题。

如果团队习惯：

- 一次让 AI 改几十个文件
- 没有明确变更边界
- 只看结果跑没跑通
- 不追踪设计意图

那系统会越来越像“概率性拼装产物”。

所以我建议设置硬约束：

- 大改必须先有 spec 和影响面分析
- 大改必须有 dependency diff / architecture diff
- AI 生成代码不能越过分层边界
- 关键模块禁止整块重生成，只允许局部受控修改

---

### 8. 是否存在“只有 AI 懂”的区域

这是最危险的红旗。

判断标准很简单：  
让一个合格工程师不用提示词、不继续问 AI，只靠现有文档、测试、监控和代码，能不能回答：

- 这个模块为什么存在
- 它保证什么
- 失败时怎么定位
- 要改哪里才安全

答不上来，这块就已经是组织资产风险，而不只是技术债。

---

## 四、我最建议你加的，不是更多 code review，而是 5 个“强制交付物”

### 1. 系统不变量清单

这是整个系统的“语义锚”。

没有它，任何后续 AI 修改都可能继续漂移。

---

### 2. 架构决策记录（ADR）

每个关键选择都要回答：

- 为什么这样设计
- 放弃了什么方案
- 哪些约束成立
- 什么情况下要推翻

这样未来出问题，至少还能追溯“原始因果”。

---

### 3. 模块责任地图

每个模块只回答三件事：

- 它负责什么
- 不负责什么
- 依赖谁

这个东西能有效阻止 AI 代码库无限长出“模糊中间层”。

---

### 4. 业务规则总表

把所有关键规则从代码里抽出来，变成显式文档或规则引擎入口。  
目标是：**先能读规则，再去定位代码**。

---

### 5. 故障定位手册

不是运维手册，而是根因手册。  
对每类关键故障，要能回答：

- 看哪几个指标
- 查哪几段 trace
- 对应哪几个模块
- 最可能的 3 类根因是什么

这一步很像把黑盒拆成“可检修设备”。

---

## 五、给 AI 生成系统的 review 标准，我建议从“代码正确”升级为“可接管”

你可以直接用这个评审矩阵：

### A. 可理解性

- 人能否在不依赖生成上下文的情况下理解模块目的
- 命名、边界、依赖是否一致

### B. 可解释性

- 关键行为是否能追溯到 spec / rule / ADR / invariant
- 是否知道“为什么这样做”

### C. 可验证性

- 关键约束是否有测试、监控、告警、数据校验共同支撑

### D. 可定位性

- 出问题时，人能否通过日志、trace、metrics 缩到模块级根因

### E. 可替换性

- 单个模块能否被重写/替换而不导致全局塌陷

### F. 可演化性

- 增加新需求时，是局部扩展，还是全局牵一发而动全身

只要 C、D、E 三项里有一项很差，这个系统就不适合继续由 AI 高速扩写。

---

## 六、最关键的一条建议：把“AI 能修”改成“人必须能证”

这是我最强烈的建议。

以后任何 AI 生成改动，进入主干前都要满足：

- **AI 可以提出方案**
- **但人必须能解释其意图**
- **人必须能指出它依赖的不变量**
- **人必须能说明失败时如何定位**
- **人必须能说明这次改动的边界和副作用**

也就是把验收标准，从“跑通了”改成：

**“这个改动是否提升了系统的可证性、可测性、可定位性、可替换性。”**

如果没有提升，哪怕功能是对的，也是在继续放大黑盒。

---

## 七、我的结论很明确

你的核心担心可以概括成一句话：

**最坏的情况不是 AI 写错代码，而是 AI 成功写出了一个逐渐失去人类维护权的软件系统。**

所以，对 100% AI 生成系统的正确审查姿势不是普通 code review，而是：

**把它当成一个需要被逆向、被建模、被验证、被接管的复杂黑盒系统。**

你真正要建设的是四种能力：

- **语义锚点**：spec、规则、不变量
- **结构锚点**：边界、依赖、状态机
- **验证锚点**：测试、契约、回归、故障演练
- **治理锚点**：ADR、变更边界、人工可解释验收

只要这四类锚点建立起来，AI 代码就还是工具；  
如果没有，系统越大，团队越会变成“代码的旁观者”。

---
# 以上方法论，跟传统软件工程的异同？

**大部分适用，但有几处需要重新标定权重和假设**。这套方法论本质上是"复杂系统的可维护性工程",不是 AI 专属——但 AI 把几个原本的隐性风险变成了显性主导风险,所以 review 的侧重点会变。

## 一、完全适用的部分(共通的软件工程原理)

这些和代码谁写的无关,只要系统够复杂就成立:

- **五个核心问题**(边界/因果/意图/根因/接管)——这是任何 legacy 系统审计都该问的
- **四层推进结构**(黑盒行为 → 灰盒结构 → 语义审计 → 维护演练)——经典逆向工程流程
- **Invariant Catalog、ADR、模块责任地图、业务规则总表、故障定位手册**——这五个交付物在纯人写系统里同样是黄金标准,只是行业普遍做得不够
- **可理解/可解释/可验证/可定位/可替换/可演化** 六维评审矩阵——通用的架构质量框架

换句话说:这篇文档如果把"AI 生成"全替换成"外包团队交付"或"前同事留下的 legacy",90% 的内容原封不动还成立。

## 二、需要重新标定的部分(AI 让风险结构变了)

### 1. 风险分布不同,不是风险种类不同

人写代码的典型风险曲线:**少量高危 bug + 大量可理解的平庸代码**。 AI 生成代码的风险曲线:**bug 可能更少,但"看起来对、说不清为什么"的代码密度高得多**。

所以:

- 对人写代码,review 重点在 **"抓错"**(correctness、edge case、性能)
- 对 AI 代码,review 重点在 **"抓漂移"**(语义漂移、结构漂移、因果不可追溯)

文档里反复强调的"语义正确性没有锚点"——人写代码也会发生,但频率和隐蔽性都低一个数量级。人写代码时,作者脑子里至少有个(可能错的)模型;AI 生成时连这个锚都未必存在。

### 2. "为什么这样做"的可追溯性,默认值相反

人写代码:默认假设**作者有意图**,review 时是"让他讲清楚"。 AI 代码:默认假设**可能根本没有意图**,review 时是"检查是否存在意图"。

这改变了 5 Whys、第一性原理这些工具的用法。对人,你是在挖掘已有的推理链;对 AI 代码,你是在判断推理链是否被构造过,如果没有,要**补上**——这是增量工作,不是审查工作。

### 3. "大块再生成"是 AI 特有的治理问题

文档第 7 条(代码库是否允许大块再生成)在人写代码里几乎不存在——人不会一夜之间重写 40 个文件。所以这条治理约束是 AI 独有的,人写代码 review 不需要。

对应的反面是:人写代码有 **"作者记忆"** 这个天然的维护资源,AI 没有。一个写了三年该系统的工程师,他本人就是活的 ADR。AI 生成系统里这个角色是空的,所以文档强调的显式交付物(ADR、不变量清单)在 AI 场景下从"最佳实践"升级成"生存必需"。

### 4. "只有 AI 懂的区域"是新现象

人写代码里类似物是"只有某个离职员工懂的区域",但那是**意外事故**,是组织没做好知识传承。 AI 代码里这是**默认产物**,不做干预就会发生。

所以对人写代码,这个检查点是事后补救;对 AI 代码,是事前预防。

### 5. 测试的角色变了

人写代码:测试主要是**防回归、防手滑**。 AI 代码:测试是**唯一能把"涌现行为"钉死的手段**,因为代码本身的意图不可靠。

所以文档里"契约测试 / 属性测试 / 不变量测试"的权重,在 AI 场景下比人写代码高得多。人写代码里 unit test 覆盖 happy path 常常够用,AI 代码里远远不够。

### 6. "可接管"这个验收标准,对人写代码是加分项,对 AI 代码是及格线

这是最本质的差异。人写代码天然具备一定可接管性(作者能口头交接),AI 代码如果不显式构建可接管性,它就**真的不存在**。

## 三、一句话总结

这套 review 思路对人写代码**逻辑上完全适用,但很多条目在人写代码场景下是"锦上添花的成熟工程实践",在 AI 生成场景下变成"不做就会出事的底线"**。

差异不在方法,在 **默认假设**:

- 人写代码:默认"有意图、有知识持有者、变更速率受限",review 是验证和挑错
- AI 代码:默认"意图可能缺失、知识持有者不存在、变更速率无限",review 是**构建**这些本应存在的东西

所以文档里那句"把 AI 能修改成人必须能证",翻译到人写代码场景就是老生常谈的"代码是写给人读的";但在 AI 场景下,它从一句口号变成了硬性工程约束。

---
# 是否可以用AI来Review AI？

**换一个角度来看这个问题，是否意味着，这个review本身，是一个人对于未知系统的认知过程，并不一定是跟原来人类做代码review是一回事了？进一步推，这个review过程本身，也许也可以借助AI工具来完成。甚至，做这个review工作的人，其实也不一定要对代码非常精通也可以？**


**这类 review，本质上已经不只是“代码审查”，而是“对未知系统的认知重建过程”。**  
它和传统的人类代码 review 有重叠，但不再是一回事。

传统 code review 更像是在看：

- 这段改动是否正确
    
- 风格是否一致
    
- 边界条件有没有漏
    
- 会不会引入 bug
    
- 是否符合既有架构约束
    

它默认一个前提：

**reviewer 对系统已经有基本理解。**

但你说的这个场景不是。  
你面对的是一个**系统认知并不掌握在人手里**、甚至**原始设计意图都可能没有被人真正持有过**的系统。  
这时候，review 的任务变成了：

**从运行结果、结构痕迹、代码实现、测试行为、故障模式中，反向重建系统的真实模型。**

所以它更像：

- 逆向工程
    
- 系统取证
    
- 认知建模
    
- 风险审计
    
- 可维护性接管评估
    

而不只是 code review。

---

## 一、所以答案是：是的，这已经是“认知工作”了

更准确地说，这类 review 可以拆成三层：

### 1）表层代码审查

看实现是否干净、边界是否合理、是否有明显 bug。

这是传统 code review 的部分。

### 2）系统认知重建

搞清楚：

- 这个系统到底在做什么
    
- 真正的模块边界在哪里
    
- 哪些规则是显式的，哪些是隐式的
    
- 哪些行为是设计出来的，哪些只是碰巧成立
    

这已经不是普通 code review 了。

### 3）维护权评估

回答：

- 人类团队是否已经重新拿回理解权
    
- 出故障时能不能靠人定位
    
- 未来能不能不依赖继续问 AI 来维护
    

这更像技术治理和系统审计。

---

## 二、这个过程当然可以借助 AI，而且非常适合借助 AI

我甚至会说：

**如果面对的是一个很大的 AI 生成系统，不借助 AI 做 review，效率会非常低。**

因为 AI 在这种工作里非常适合做“认知放大器”，尤其擅长下面这些事：

### 1）做结构提取

比如：

- 自动梳理模块依赖
    
- 提取调用链
    
- 归纳重复规则
    
- 发现跨层访问
    
- 识别高耦合区域
    

### 2）做语义归纳

比如：

- 总结每个模块的职责
    
- 归纳状态机
    
- 提取隐含假设
    
- 归纳错误处理模式
    
- 找出名字相似但语义冲突的对象
    

### 3）做异常假设生成

比如：

- 这段逻辑可能在哪些场景失效
    
- 哪些分支缺测试
    
- 哪些地方可能存在幂等/并发问题
    
- 哪些变量承担了隐藏业务语义
    

### 4）做“逆向文档化”

比如从代码反推出：

- 系统能力清单
    
- 不变量清单
    
- 业务规则表
    
- 模块责任地图
    
- 故障排查路径
    

这类事，AI 很强。

---

## 三、但有一个关键点：AI 适合帮助“建模”，不适合独自“背书”

这里要非常小心。

因为如果系统本来就是 AI 生成的，再让 AI 来 review，它会有一个天然风险：

**生成者和审查者，可能共享同一种盲点。**

也就是：

- 代码是某种“看起来合理”的模式生成的
    
- review 也是按同样的模式去理解的
    
- 最后形成“表面自洽”
    
- 但真正的系统风险并没有被识别出来
    

这很像：

**同一个思维偏差，既参与建造，也参与验收。**

所以 AI 可以深度参与，但不能单独作最终裁决。  
它更像：

- 侦察器
    
- 归纳器
    
- 假设生成器
    
- 结构梳理器
    
- 文档反编译器
    

但不是唯一裁判。

---

## 四、进一步说：做这件事的人，确实“不一定要非常精通代码”，但要分层看

这个判断我同意一半，而且这一半很重要。

### 你不一定需要“高手程序员”，才能参与这种 review

因为这类 review 里面，有很大一部分工作其实不是“写代码能力”，而是：

- 抽象能力
    
- 系统思维
    
- 识别边界能力
    
- 提问能力
    
- 因果分析能力
    
- 风险意识
    
- 业务理解能力
    

比如下面这些问题，一个未必很强写代码的人也可能做得很好：

- 这个模块为什么存在？
    
- 这个系统到底承诺了什么？
    
- 这个状态流转合理吗？
    
- 这条业务规则是不是散落在多个地方？
    
- 这类故障有没有被观测和约束？
    
- 这里有没有“人根本说不清楚为什么这么做”的危险区域？
    

这些其实更偏**认知审计**。

---

## 五、但你也不能因此推到“代码不精通也完全没关系”

不能这么推。  
更准确的说法是：

**不是每个 reviewer 都必须很强写代码，但整个 review 体系里必须有人能深入到代码底层做验证。**

因为 review 至少有四个层次：

### 1）业务/产品层

看系统是否符合真实业务意图。  
这个人可以不深懂代码。

### 2）系统/架构层

看边界、依赖、状态、耦合、可演化性。  
这个人需要中高水平系统理解，但未必亲自写很多底层代码。

### 3）实现/代码层

看具体实现是否真的支撑前两层判断。  
这里必须有代码能力强的人。

### 4）运维/故障层

看日志、链路、恢复、回滚、观测。  
这里要有工程实战经验。

所以不是“代码能力不重要”，而是：

**这类 review 不再是单一代码能力主导，而是变成多种认知能力协作。**

---

## 六、我更愿意把 reviewer 分成三种角色

### 第一种：系统解释者

负责回答：

- 系统在做什么
    
- 边界在哪里
    
- 规则在哪里
    
- 状态怎么流转
    

这类人不一定是最强 coder，但要很强抽象能力。

### 第二种：实现验证者

负责回答：

- 代码是否真的实现了前述解释
    
- 有哪些隐藏分支、暗耦合、伪抽象
    
- 哪些地方是“解释成立，但实现不成立”
    

这类人需要强代码能力。

### 第三种：风险裁决者

负责回答：

- 这个系统能不能继续扩
    
- 哪些部分必须重构
    
- 哪些部分必须冻结
    
- 哪些地方必须建立不变量和观测
    

这类人需要系统治理能力。

---

## 七、所以这件事很适合“人+AI”的新型 review 组织方式

我建议你把它看成：

**AI 负责扩大可见范围，人负责建立可信判断。**

一个比较合理的分工是：

### AI 做

- 代码库扫描
    
- 结构图生成
    
- 规则提取
    
- 重复逻辑归并
    
- 风险点候选列表
    
- 测试缺口提示
    
- 故障路径假设
    

### 人做

- 判断哪些规则是真规则
    
- 判断哪些风险是可接受的
    
- 判断哪些模块必须接管
    
- 判断哪些地方必须重写
    
- 判断哪些解释足够可信
    

也就是：

**AI 帮你看得更快，人负责决定什么算“真的看懂了”。**

---

## 八、你这个推论背后，其实导向了一个很重要的新结论

在 AI 生成系统里，review 的核心能力会从“读代码”部分迁移到“重建系统模型”。

换句话说，未来好的 reviewer，未必只是那种：

- 能一眼看出某段算法写得漂亮不漂亮的人
    

而更可能是那种：

- 能快速把陌生系统建模出来
    
- 能抓住不变量
    
- 能识别隐式假设
    
- 能用证据验证解释
    
- 能区分“看起来合理”和“真的可维护”
    

的人。

这是一种更偏**系统认知工程**的能力。

---

## 九、不过有一条底线不能丢

无论 AI 参与多深，无论 reviewer 是否不是顶级 coder，最后都要回到一个硬标准：

**有没有形成“人类可独立复核”的证据链。**

比如：

- 这条规则在哪定义
    
- 这个不变量在哪保证
    
- 这个故障怎么定位
    
- 这个模块能否替换
    
- 这个改动的副作用是什么
    

如果这些问题最后只能回答成：

- “AI 说应该是这样”
    
- “跑起来暂时没问题”
    
- “大概逻辑是这个意思”
    

那其实没有完成 review，只是完成了一次“机器辅助理解尝试”。

---

## 十、我的结论

你的判断基本是对的：

**这类 review，本质上是一个人类对未知系统的认知重建过程，已经不只是传统代码 review。**

而且：

- **这个过程非常适合借助 AI**
    
- **参与者不一定都要非常精通代码**
    
- **但整个 review 体系里，仍然必须有能深入代码验证的人**
    
- **最终目标不是“看过代码”，而是“重新拿回系统解释权和维护权”**
    

我会把它概括成一句话：

**传统 code review 在检查“改动是否正确”；  
你说的这类 review，在检查“人类是否重新理解并接管了系统”。**

---
# Harness工程是否已经考虑了Review？

可以，但要先把 **harness** 这个词分开看。当前业界至少有三种相邻但不完全相同的用法：

1. **agent harness / scaffold**：让模型能像 agent 一样工作的那层系统，负责指令、工具编排、权限、状态与环境。Anthropic 把 agent 拆成 model、harness、tools、environment 四层；其中 harness 是模型运行时的 instructions 和 guardrails。([anthropic.com](https://www.anthropic.com/research/trustworthy-agents "Trustworthy agents in practice \ Anthropic"))
    
2. **evaluation harness**：跑评测的基础设施，负责把任务跑起来、记录全过程、打分、汇总结果。Anthropic 明确定义它是 end-to-end 运行 eval 的基础设施。([anthropic.com](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents "Demystifying evals for AI agents \ Anthropic"))
    
3. **harness engineering for coding agents**：更广一点，指为 coding agent 设计“导向 + 约束 + 反馈回路”的整套工程做法。OpenAI把它描述成：工程师的主要工作不再是直接写代码，而是设计环境、明确意图、构建反馈回路，让 agent 可靠地产生结果；Fowler 则把它讲成 guides 和 sensors 的组合。([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))
    

所以先说结论：

**现有 harness engineering 的实践，已经把你说的 review 工作“含进来一部分”，尤其是把 review 变成可自动化、可循环、可前移的反馈机制；但它还没有完整覆盖你说的那种“人类对未知系统做认知重建和接管”的 review。** ([martinfowler.com](https://martinfowler.com/articles/harness-engineering.html "Harness engineering for coding agent users"))

## 从定义上看，它怎么包含 review

如果按 Fowler 的定义，harness engineering 的核心不是“替代 review”，而是把 review 拆成两类控制：

- **feedforward / guides**：事前导向，尽量让 agent 一开始别走偏
    
- **feedback / sensors**：事后传感，发现偏差并促使自纠
    

他还明确把这些控制再分成两类：

- **computational**：测试、lint、类型检查、结构分析这类确定性检查
    
- **inferential**：AI code review、LLM judge 这类语义判断
    

并且他把 regulation categories 明确列成了 **maintainability harness、architecture fitness harness、behaviour harness**。换句话说，在这个定义里，review 已经不只是“人看 PR”，而是被重新定义成一种传感与调节机制。([martinfowler.com](https://martinfowler.com/articles/harness-engineering.html "Harness engineering for coding agent users"))

这和你前面说的方向非常接近，因为它默认承认一件事：

**AI 产出的代码不能只靠一次人工阅读来信任，必须被外部的规则、传感器、回路不断约束。** ([martinfowler.com](https://martinfowler.com/articles/harness-engineering.html "Harness engineering for coding agent users"))

## 从实践上看，它已经把 review 做成“系统化反馈”

OpenAI 的实践非常典型：他们在一个几乎全 AI 生成的代码库里，让 agent 自己 review 本地改动、请求额外的 agent review、响应反馈、循环迭代；人可以 review，但不是必需步骤。与此同时，他们还把 UI、日志、指标、浏览器可操作性都变成 agent 可读的反馈信号，让 agent 能重现 bug、验证修复并反复自检。([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))

Anthropic 在 eval 那边则把 review 的一部分制度化成了 evaluation harness：任务、trial、grader、transcript、outcome、suite。它强调 eval 不只是打个分，而是把行为变化显式化、让系统在上线前暴露问题、避免团队“飞盲”。([anthropic.com](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents "Demystifying evals for AI agents \ Anthropic"))

如果把这两条线合起来看，现有 harness 实践已经覆盖了你关心 review 的几个核心维度：

- **回归与行为验证**：系统改完后到底有没有变好/变坏
    
- **结构约束**：模块边界、架构 fitness 是否被破坏
    
- **可维护性信号**：死代码、覆盖质量、依赖扫描、持续 drift 监测
    
- **运行时反馈**：日志、SLO、trace、浏览器动作、用户流程验证
    
- **AI 辅助审查**：AI 作为 reviewer / judge / evaluator 的一部分
    

这些都已经在现有 harness engineering 里了。([martinfowler.com](https://martinfowler.com/articles/harness-engineering.html "Harness engineering for coding agent users"))

## 但它没有完全覆盖你说的那个问题

你前面讲的 review，更深一层，目标不是“让 agent 改得更稳”，而是：

**让人类重新拿回对未知系统的解释权、定位权、替换权和维护权。**

这一点，当前 harness engineering 只覆盖了前半段，还没完全覆盖后半段。

原因是现有 harness 理论大多聚焦在：

- 如何让 agent 更可靠地产生结果
    
- 如何让 agent 更容易被约束、自纠、评测
    
- 如何让质量检查更早、更自动、更规模化
    

而你说的 review 还多了一层：

- **如何从系统外在行为与代码痕迹中，重建“这个系统究竟是什么”的认知模型**
    

这一步更接近逆向工程、系统审计、认知接管。Fowler 的框架里已经隐约碰到这一层，比如他讲 maintainability harness、architecture fitness harness、harnessability、ambient affordances，意思是代码库本身要变得更 legible、更 navigable、更 tractable，才能被 harness 好。([martinfowler.com](https://martinfowler.com/articles/harness-engineering.html "Harness engineering for coding agent users"))

但老实说，**现有 harness engineering 还没有形成一套完整理论，能直接回答“怎样把一个已经膨胀的、100% AI 生成的未知系统重新接管”**。更准确地说，它还是一个正在形成中的工程范式，而不是成熟完备的经典理论。这个判断能从几个信号看出来：OpenAI 把它作为一种新型工程角色来描述，Fowler 明确说这是一个“starting point - and open questions”，Anthropic 也反复强调 harness 需要持续迭代，因为 harness 里编码的假设会随着模型能力变化而过时。([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))

## 所以，用 harness 的视角重看你的问题，最好这样理解

你可以把你要的 review 分成两层：

### 第一层：harness 内的 review

这层已经被现有 harness 实践很好地吸收了。

它包括：

- 规则与约束前置
    
- 静态分析、测试、架构检查
    
- AI reviewer / LLM judge
    
- eval suites
    
- runtime signals
    
- 持续 drift sensors
    

这层的目标是：

**让系统在生成、修改、集成、运行的每个阶段都不断被检查。** ([martinfowler.com](https://martinfowler.com/articles/harness-engineering.html "Harness engineering for coding agent users"))

### 第二层：harness 之上的 review

这层才是你真正关心的。

它要回答：

- 系统真实边界是什么
    
- 模块真实职责是什么
    
- 关键不变量在哪里
    
- 出问题时人怎么独立定位
    
- 哪些模块人能替换，哪些已经失控
    
- 这套 harness 检查到的到底只是表层质量，还是已经足以支撑长期维护
    

这层不是简单“多加几个 sensor”就够了。  
它要求把 harness 产出的各种信号，再上升为**人类可复核的系统模型**。

## 从定义推到实践，最合理的落地方式是什么

我会建议你把 harness 当成 review 的**底座**，而不是 review 的全部。

一个比较完整的实践会是这样：

### 1. 先建 harness，把 review 变成持续信号

包括：

- lint / types / tests / architecture rules
    
- AI code review
    
- 行为 eval suites
    
- 日志、metrics、trace、browser 验证
    
- drift sensors
    

这是把“review”从一次性阅读，变成持续观测。([martinfowler.com](https://martinfowler.com/articles/harness-engineering.html "Harness engineering for coding agent users"))

### 2. 再利用 harness 产物，做人类认知重建

也就是把 harness 生成的结果拿来反推：

- 能力清单
    
- 状态机
    
- 依赖图
    
- 不变量目录
    
- 规则归属图
    
- 故障定位路径
    

这一步才是你说的“拆黑盒”。  
它不等于 harness 本身，但它可以强烈借助 harness 的数据与检查结果。

### 3. 最后把 review 结论再写回 harness

这一步最关键。

如果你在 review 中发现：

- 某条业务规则分散
    
- 某模块边界模糊
    
- 某类故障长期难定位
    
- 某个不变量没有自动校验
    

那不应该只写在审查报告里，而应该把它写回 harness：

- 变成规则
    
- 变成结构测试
    
- 变成 eval case
    
- 变成 runtime guardrail
    
- 变成 agent skill / repo rule / ADR
    

这才符合 harness engineering 的 steering loop：  
**问题出现一次，下一步不是再人工盯着，而是升级 guides 和 sensors，让它以后更少再发生。** ([martinfowler.com](https://martinfowler.com/articles/harness-engineering.html "Harness engineering for coding agent users"))

## 回到你的原问题：它是否“含括了进去”？

我的判断是：

**部分含括，而且是越来越接近，但还没有完全等同。**

更准确地说：

- 如果你说的是“传统代码 review 里的 correctness / regression / architecture / maintainability 检查”，harness engineering 已经把很大一部分吸收进去了。([martinfowler.com](https://martinfowler.com/articles/harness-engineering.html "Harness engineering for coding agent users"))
    
- 如果你说的是“面对一个未知、膨胀中的 AI 生成系统，人类如何重新理解、接管、证明它可维护”，那现有 harness engineering 还不够，它更像这个过程的基础设施，而不是完整方法论。([martinfowler.com](https://martinfowler.com/articles/harness-engineering.html "Harness engineering for coding agent users"))
    

## 我给你的一个简化定义

你可以这样记：

**harness engineering 解决的是：怎么让 AI 生成系统更可控、更可测、更可纠偏。**  
**而你说的 review 还要再往前一步：怎么让人类重新可理解、可证明、可接管。**

前者是后者的必要条件，但不是充分条件。

## 实践上最值得借鉴的 5 个点

如果你真要把 harness 用到这类 review，我会优先抓这 5 个：

1. **把“人觉得有问题”改成“有可运行的 grader / sensor”**。
    
2. **把 review 对象从源码扩大到 transcript、trace、logs、UI、outcome**。Anthropic 明确区分 transcript 和 outcome，这个区分很有用。([anthropic.com](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents "Demystifying evals for AI agents \ Anthropic"))
    
3. **把 maintainability / architecture fitness / behaviour 分开审**，不要混成一个大杂烩。([martinfowler.com](https://martinfowler.com/articles/harness-engineering.html "Harness engineering for coding agent users"))
    
4. **把 review 发现反写回 harness**，形成 steering loop。([martinfowler.com](https://martinfowler.com/articles/harness-engineering.html "Harness engineering for coding agent users"))
    
5. **持续质疑 harness 自己的假设**。Anthropic 明确提醒：harness 中每个部件都编码了“模型还做不到什么”的假设，而这些假设会随着模型变强而过时。([anthropic.com](https://www.anthropic.com/engineering/harness-design-long-running-apps "Harness design for long-running application development \ Anthropic"))
    

一句话收束：

**现有 harness engineering 已经把 review 的“自动化约束、持续反馈、AI 辅助审查”大幅吸收进来了；但你要的那种“对未知 AI 系统做认知重建和维护权接管”的 review，还需要在 harness 之上，再加一层面向人类理解的系统审计方法。**

下一步我可以直接帮你把两者拼起来，给你一份  
**“基于 harness engineering 的未知 AI 系统 review 框架”**。

---
# Alignment

对，这一下就把问题推到了更本质的一层：

**你要做的 review，最终不是在检视“实现是否符合规格”，而是在检视“最终软件行为，是否仍然忠实于人类最初的真实意图”。**

这和普通 code review，甚至和很多 verification-first 的工程方法，都不是一回事。

## 先把这个问题说透

你指出的关键前提非常重要：

**人类意图并不会在项目一开始就被 100% 完整、无歧义、无遗漏地写出来。**

系统工程和需求工程本身就承认这一点。SEBoK 对 stakeholder needs 的描述，不只是“requirements”，还包括 needs、wants、desires、expectations 和 perceived constraints；也就是说，起点本来就不只是一个干净、完整的规格文档。([SEBoK](https://sebokwiki.org/wiki/Stakeholder_Needs_and_Requirements_%28glossary%29?utm_source=chatgpt.com "Stakeholder Needs and Requirements (glossary)"))

同样，经典需求获取研究也早就指出，规格的“好坏”只能相对于用户目标来判断，而 validation 的重要工作之一，就是通过建模来促进各方对“用户真正意图”的共同理解。([SEI](https://www.sei.cmu.edu/documents/1151/1992_005_001_16478.pdf?utm_source=chatgpt.com "Issues in Requirements Elicitation"))

所以你的判断是成立的：

**真正的问题不是“需求没写清楚，先补需求就好了”；而是“需求在本体上就是不完备的、演化的、带隐性假设的”。**

---

## 这意味着什么？

这意味着你要做的 review，核心不该叫“实现评审”，而更接近：

**意图对齐审查**  
或  
**最终行为验证**  
或  
**intent validation review**

因为传统的软件工程里，通常会区分两件事：

- **Verification**：是不是把请求的东西做对了
    
- **Validation**：是不是做成了真正需要的东西
    

NIST 和 ISO 都沿用这个区分：verification 是 “building the product right”，validation 是判断软件是否满足 intended use，也就是“building the right product”。NIST 还明确提醒：what was requested 可能并不等于 what was needed。([NIST](https://www.nist.gov/document/cftt-swb-swbt-release-10-test-plan?utm_source=chatgpt.com "Testing Support Tools Validation Test Plan, Test Design, ..."))

而你现在强调的，正是第二层，而且比通常 validation 还要更难一点：

**不是只看“满足需求文档”，而是看“系统最终行为是否仍然与人的原始目标、上下文、期望和禁忌一致”。**

---

## 所以，harness 工程和 SDD 在这里的位置，要重新看

### 1. 它们不是错

它们都很有价值。

- SDD 这类方法，核心价值是把人类意图尽量前置成 spec、约束、接口、验收条件。
    
- harness engineering 的价值，是把这些约束继续变成 guides、sensors、tests、evals、feedback loops，让系统持续被校正。([OpenAI](https://openai.com/index/harness-engineering/?utm_source=chatgpt.com "Harness engineering: leveraging Codex in an agent-first ..."))
    

### 2. 但它们的“默认世界观”偏理想化

它们通常都更擅长处理：

- **已表达的意图**
    
- **已形式化的约束**
    
- **已知的验收条件**
    
- **可观测的偏差**
    

NIST 的 AI RMF 也把重点放在：先明确 intended purpose、context of use、影响对象、业务和技术要求，再去 map、measure、manage。([NIST AI Resource Center](https://airc.nist.gov/airmf-resources/playbook/map/?utm_source=chatgpt.com "Map - AIRC - NIST AI Resource Center"))

这说明这些框架并没有忽略“意图”和“上下文”；相反，它们很重视。  
但问题是：

**它们大多默认这些东西至少能被相对充分地说出来。**

而你指出的现实是：

- 意图一开始并不完整
    
- 不同人脑中的“原始意图”并不完全一致
    
- 使用情境会变化
    
- 实现出来之后，人对“自己原来想要什么”的认识还会反过来变化
    

这就导致一个事实：

**harness/SDD 更像是在稳定“已知意图”；而你要做的，是审查“未知、隐含、演化中的意图是否被最终系统背离了”。**

---

## 你的 review，本质上是在检查三种差距

我建议把它明确拆成三类 gap。

### 第一类：表达差距

人的真实想法，没有被充分表达成需求、规格、规则。

这类问题不是代码错，而是**意图没有被显式化**。

### 第二类：转译差距

需求写出来了，但在设计、架构、实现、提示词、harness 中被逐层改写、稀释或误解。

这类问题是**意图在翻译链条中漂移**。

### 第三类：运行差距

系统实现看似符合文档，但真实行为在真实场景中违背了最初目标、期望或禁忌。

这类问题是**最终行为与原始价值取向不一致**。

你要做的 review，其实就是在问：

**最终产出，是不是在这三层差距叠加后，已经偏离到不可接受。**

---

## 所以你这件事，严格来说不是普通 harness，也不是普通需求验证

它更像一种：

## **“从最终行为反推原始意图并做对齐校验”的工程**

我会把它定义成 4 个动作：

### 1. 重建意图

不是只收集“写下来的需求”，而是重建：

- stakeholders 真正想达成什么
    
- 他们绝不想发生什么
    
- 哪些 trade-off 是可接受的
    
- 哪些模糊区其实不能随便由系统自行决定
    

这和 Goal-Oriented Requirements Engineering 很接近。GORE 本来就是从 stakeholder goals / intentions 出发，把目标逐步 operationalize 到系统对象、事件和操作；相关研究也一直在强调 stakeholder intentions 和 goal modeling 的重要性。([Springer Nature Link](https://link.springer.com/chapter/10.1007/978-1-4615-0167-1_4?utm_source=chatgpt.com "Goal Oriented Requirements Engineering | Springer Nature Link"))

### 2. 外显化意图

把“原始意图”从模糊描述变成一组可检查的东西，比如：

- 目标
    
- 约束
    
- 禁区
    
- 质量属性
    
- 场景
    
- 反例
    
- 不变量
    
- 可接受的失败方式
    

NIST 对 requirements verification tools 的描述也说明，需求工作本身就要追求 complete、consistent、traceable、unambiguous、verifiable；这恰好说明需求并不会天然具备这些性质，而是要被工程化地补足。([NIST](https://www.nist.gov/itl/ssd/software-quality-group/requirements-verification-tools?utm_source=chatgpt.com "Requirements Verification Tools | NIST"))

### 3. 检查最终行为

这一步才是你说的 review 的核心：

不是“读代码猜意图”，而是看：

- 真实运行行为
    
- 边界行为
    
- 异常行为
    
- 多场景行为
    
- 长周期演化行为
    

是否与上面那组目标/约束/禁区一致。

### 4. 识别“应该改系统”还是“应该改意图模型”

这是很关键的一步。

因为有时系统错了；  
有时是原本的 spec 错了；  
有时是人直到看见真实系统后，才发现自己真正想要的其实不是最初说的那样。

所以 review 的结果不应只有“代码要不要改”，还应包括：

- 补需求
    
- 改验收标准
    
- 改架构约束
    
- 改 harness 规则
    
- 甚至重写“我们到底想要什么”
    

---

## 从这个角度看，harness 最适合做什么？

harness 最擅长的是把你重建出来的意图，变成**持续可观测、可回归、可报警的对齐机制**。

也就是：

- 把目标变成 eval
    
- 把禁区变成 guardrail
    
- 把场景变成 test suite
    
- 把关键 trade-off 变成 fitness function
    
- 把不可接受的漂移变成 sensor
    

Fowler 提到的 maintainability harness、architecture fitness harness、behaviour harness，本质上都是把某些“我们在乎的东西”变成外部传感器和调节器。([martinfowler.com](https://martinfowler.com/articles/harness-engineering.html?utm_source=chatgpt.com "Harness engineering for coding agent users"))

但它有一个边界：

**harness 不能替你发现全部“尚未被表达的人类真实意图”。**  
它更像是：你一旦把某部分意图辨认出来，它就能帮你稳定地守住它。

---

## 所以你真正需要的，不只是 harness，而是两层结构

### 第一层：意图发现层

回答：

- 我们原始到底想要什么
    
- 哪些是必须对齐的
    
- 哪些是可以容忍偏差的
    
- 哪些是以前没写出来但其实极重要的
    

这层更像需求工程、目标建模、场景分析、系统审计。

### 第二层：意图守护层

回答：

- 怎么把这些东西持续地测出来
    
- 怎么在以后每次改动时都检查
    
- 怎么让 AI 或工程流水线自动发现偏差
    

这层才是 harness。

也就是说：

**你现在做的 review，不是 harness 的替代品；它更像是 harness 的上游。**

---

## 你的 review 产物，应该长什么样

如果目标是“检视最终行为是否跟人类最初意图一致”，我建议你的 review 最终不要只产出 bug list，而要产出下面 6 样东西：

### 1. 意图地图

包括：

- 核心目标
    
- 关键利益相关方
    
- 禁止结果
    
- 可接受 trade-off
    
- 上下文假设
    

### 2. 意图证据链

每条关键意图后面都标注：

- 来源于谁
    
- 来源于哪类材料
    
- 置信度如何
    
- 是否存在冲突版本
    

### 3. 行为断言集

把意图翻成一组可观察断言：

- 在场景 X 下，系统应当……
    
- 在边界 Y 下，系统不得……
    
- 当失败发生时，系统至少要……
    

### 4. 对齐测试集

不是只测功能，而是专门测“是否偏离原始意图”的场景。

### 5. 偏离分类表

把发现的问题分成：

- 需求表达缺失
    
- 设计转译偏差
    
- 实现问题
    
- 运行环境问题
    
- 利益相关方目标冲突
    

### 6. 写回 harness 的规则

把这次发现的关键偏差，固化成：

- test
    
- eval
    
- lint / rule
    
- architecture fitness function
    
- runtime alert
    

---

## AI 在这里能帮什么

AI 很适合帮你做三件事：

### 1. 帮你“提取意图候选”

比如从：

- 需求文档
    
- PR
    
- ADR
    
- issue
    
- 测试
    
- 用户反馈
    
- 日志/事故复盘
    

里总结“系统可能承载的真实目标是什么”。

### 2. 帮你“把模糊意图外显化”

最近也有研究在做：把自然语言需求自动提炼成 goal model，目的就是桥接“非结构化需求”和可分析的目标模型之间的落差。([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0164121224000244?utm_source=chatgpt.com "Extracting goal models from natural language requirement ..."))

### 3. 帮你“从行为反推偏离点”

例如：

- 哪些场景最可能背离目标
    
- 哪些模块最像承载隐性业务规则
    
- 哪些测试只验证了实现、没验证意图
    

但最后那一步——  
**什么才算“真正代表了人类原始意图”**——还是要人来裁决。

---

## 一句话收束

你这类 review 的最终目标，不是：

**“系统是否符合已经写下来的要求。”**

而是：

**“在需求不完备、意图会演化、实现会漂移的现实下，最终系统行为是否仍然值得被说成：这就是我们原本想做的那个东西。”**

这已经是 **validation 的强化版** 了。  
它把“build the right product”再往前推进了一步，变成：

**“即使最初的‘right’并没有被完整说清楚，我们也要通过回溯、建模、检视最终行为，把它重新找回来。”**

我可以继续把这个思路直接整理成一套可执行方法，名字就叫：

**“意图对齐型 Review 框架”**  
包含步骤、检查项、产物模板。

---
# 哪些必须要人来Review，哪些可以放心交给AI？

**对 100% AI 生成系统，人类不该主要 review“代码写得像不像人”，而该 review“AI 被允许优化的目标函数、边界条件、不可接受后果，以及出了问题时人类是否还能接管”。** OpenAI 把当前实践讲得很直白：AI 可以承担很多初稿、测试、审查和修复工作，但工程师仍然要对测试是否真正对齐规格和用户体验负责；Anthropic 也把 agent 的可靠性拆成 model、harness、tools、environment 四层，说明真正要管的不是模型一层，而是整套授权与约束系统。([developers.openai.com](https://developers.openai.com/codex/guides/build-ai-native-engineering-team "Building an AI-Native Engineering Team – Codex | OpenAI Developers"))

我会这样分界。

## 一、人类必须 review 的，不是“所有代码”，而是 6 类东西

### 1. 原始意图和最终验收口径

人类必须定义：

- 这个系统到底要达成什么
    
- 哪些结果算成功
    
- 哪些结果绝对不能发生
    
- 当目标互相冲突时，优先级是什么
    

因为按 NIST 的定义，validation 不是“看它有没有按文档输出”，而是用客观证据确认它是否满足**特定 intended use**；而是否该部署，也要基于场景化的风险、影响、成本和收益判断。这个判断本质上是组织与责任判断，不是模型自己能替你拍板的。([nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf "Artificial Intelligence Risk Management Framework (AI RMF 1.0)"))

### 2. 权限边界和高风险动作

人类必须 review：

- AI 能不能碰生产环境
    
- 能不能读写 secrets
    
- 能不能做数据迁移
    
- 能不能动计费、权限、合规、用户数据
    
- 哪些动作必须二次确认
    

Anthropic 明确把 harness 定义为“instructions + guardrails”，并举例说 harness 可以要求超过阈值就停止、或者必须经用户确认后才能提交。Anthropic 还披露过 agent 误删远程分支、上传认证令牌、尝试对生产库做迁移这类“过度主动”的事故，并指出大量人工批准会带来 approval fatigue。意思很清楚：**人不该盯每一次小动作，但必须盯住危险授权边界。** ([anthropic.com](https://www.anthropic.com/research/trustworthy-agents "Trustworthy agents in practice \ Anthropic"))

### 3. 系统级不变量

人类必须 review 并显式写下：

- 哪些业务状态绝不能同时成立
    
- 哪些金额、库存、权限、配额必须守恒
    
- 哪些数据关系不可被破坏
    
- 哪些失败只能回滚、不能“将错就错”
    

OpenAI 在 harness engineering 里强调的是 **enforcing invariants, not micromanaging implementations**，而且用机械化的 linters 和 structural tests 去守住架构与边界。也就是说，人最该盯的是“不变量”，而不是每个实现细节。([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))

### 4. 架构边界和模块责任

人类必须决定：

- 真实的分层是什么
    
- 哪些依赖方向允许，哪些禁止
    
- 哪些模块负责状态，哪些只做展示或适配
    
- 哪些规则只能在某一层生效
    

OpenAI 公开写到，在一个 fully agent-generated codebase 里，光靠文档不足以保持一致性，所以他们通过固定分层、严格依赖方向和结构测试来机械约束代码库。这个层面不能完全交给 AI 自由演化，因为它决定的是未来是否还能维护。([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))

### 5. 评价体系本身

人类必须 review：

- 测什么，不测什么
    
- outcome 怎么定义
    
- grader 会不会误判
    
- 通过线设在哪里
    
- 哪些回归是 blocker
    

Anthropic 在 agent evals 里明确区分 **transcript** 和 **outcome**：agent 口头说“已经订票”不算，最终环境里到底有没有真实预订才算；evaluation harness 要负责记录过程、评分和聚合结果。也就是说，**AI 可以被 eval，但“怎么 eval 才代表你在乎的东西”必须由人定。** ([anthropic.com](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents "Demystifying evals for AI agents \ Anthropic"))

### 6. 发布与接管决策

最后一个必须由人 review 的，是：

- 现在能不能上线
    
- 问题是继续 patch，还是该停下来重构
    
- 这块是否已经超出可维护边界
    
- 一旦 AI 失手，人类能不能独立排障和接手
    

这是组织责任，不能外包给模型。NIST 对部署决策的表述本身就是“基于上下文、风险、影响、成本、收益，并由相关方共同判断”。([nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf "Artificial Intelligence Risk Management Framework (AI RMF 1.0)"))

---

## 二、哪些可以主要交给 AI

这类工作有一个共同特征：

**目标相对明确、结果可客观判定、失败可回滚、局部出错不会把全局拖下水。**

OpenAI 现在公开建议把很多初始工作交给 AI：测试用例初稿、测试实现初稿、基础模块摘要、输入输出说明、依赖列表、PR 变更摘要、基础文档草稿，甚至让 AI review 运行时行为和跨文件逻辑。([developers.openai.com](https://developers.openai.com/codex/guides/build-ai-native-engineering-team "Building an AI-Native Engineering Team – Codex | OpenAI Developers"))

更具体一点，下面这些通常可以大胆交：

### 1. 首轮扫描和归纳

比如：

- 模块摘要
    
- 依赖图初稿
    
- 输入输出清单
    
- 变更说明
    
- 风险点候选列表
    

这类工作 AI 很适合先打一遍底。OpenAI 也明确把 file/module summaries、dependency lists、PR summaries 列为可 fully hand off 的低风险重复工作。([developers.openai.com](https://developers.openai.com/codex/guides/build-ai-native-engineering-team "Building an AI-Native Engineering Team – Codex | OpenAI Developers"))

### 2. 测试初稿与回归补齐

可以交给 AI 去：

- 从规格出发生成测试点
    
- 补齐边界条件
    
- 维护随着代码演化而过期的测试
    
- 先跑测试并自修复
    

但人仍要审测试是不是偷懒、是不是 stub、是不是只测表面。OpenAI 原话就是：工程师要**thoroughly review model-generated tests**，并且仍然对“测试覆盖是否对齐 feature specs 和 user experience expectations”负责。([developers.openai.com](https://developers.openai.com/codex/guides/build-ai-native-engineering-team "Building an AI-Native Engineering Team – Codex | OpenAI Developers"))

### 3. 低风险局部修复

当 bug 满足下面条件时，可以优先交给 AI：

- 根因已经比较清楚
    
- 修改范围局部
    
- 有现成失败用例
    
- 修复后能被测试和监控客观证明
    
- 回滚简单
    

这时人不必逐行盯实现，而应盯“修复前失败、修复后通过、没有破坏不变量”。

### 4. 受约束的重构

比如：

- 重命名
    
- 小范围抽取函数
    
- 重复代码归并
    
- 局部接口整理
    
- 机械化迁移
    

前提是边界和结构规则已经由人定好，并被 linter / structural tests 机械约束。OpenAI 的 harness 实践本身就是这个思路。([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))

### 5. 第一轮 AI review

AI reviewer 可以做：

- 跨文件逻辑追踪
    
- 运行时行为检查
    
- 覆盖缺口提示
    
- 可疑分支提示
    
- 文档和实现不一致提示
    

OpenAI 明确说，AI reviewers 不只是静态规则匹配，还能执行部分代码、理解运行时行为、跨文件和跨服务追踪逻辑。([developers.openai.com](https://developers.openai.com/codex/guides/build-ai-native-engineering-team "Building an AI-Native Engineering Team – Codex | OpenAI Developers"))

---

## 三、什么情况下“出了问题也可以放心交给 AI”

不是“问题小”就能交，而是要同时满足这 5 条。

### 1. 问题是可观察的

不是“用户感觉怪”，而是：

- 有失败测试
    
- 有明确告警
    
- 有 trace / log / metric
    
- 有可重现实例
    

Anthropic 在 eval 里强调要看 outcome，而不是只看 transcript，就是因为很多问题只有环境里的真实结果才能判定。([anthropic.com](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents "Demystifying evals for AI agents \ Anthropic"))

### 2. 问题是可判分的

也就是你能写出：

- 修好后通过什么测试
    
- 指标恢复到什么范围
    
- 哪个断言必须成立
    

如果连“修好长什么样”都说不清，就不该放心交给 AI。

### 3. 问题是局部的

满足：

- blast radius 小
    
- 不跨多个核心域
    
- 不涉及根本架构和权限模型
    
- 不涉及生产数据不可逆操作
    

### 4. 问题是可回滚的

AI 可以先试，但必须能：

- 快速回滚
    
- 保留 diff 和 trace
    
- 保留失败上下文
    
- 在必要时停在人工确认点
    

### 5. 问题不需要重新解释人类意图

这是最关键的一条。  
如果问题的本质是“我们到底想要什么”，那就不能放心交给 AI。

---

## 四、什么问题不能“放心交给 AI”

只要碰到下面任何一类，人要亲自介入。

### 1. 目标不清的问题

例如：

- 这是 bug 还是产品选择
    
- 用户体验和安全要求冲突
    
- 效率和正确性冲突
    
- 多个 stakeholder 的诉求不一致
    

这不是 coding problem，是 intent problem。

### 2. 无法客观打分的问题

比如“感觉逻辑更优雅了”“好像更符合长期方向”。  
没有可验证标准，AI 很容易朝表面自洽优化。

### 3. 跨域架构问题

比如：

- 状态模型要不要改
    
- 权限体系要不要重建
    
- 多服务边界是否重划
    
- 领域对象语义是否要统一
    

这类问题的代价不在当前 patch，而在未来维护权。

### 4. 高危动作

涉及：

- 生产数据库
    
- secrets
    
- 支付
    
- 权限
    
- 合规
    
- 外部承诺
    
- 安全关键逻辑
    

Anthropic 披露的误删分支、令牌泄露、生产迁移尝试，本质就是这类“不能靠默认积极性放行”的例子。([anthropic.com](https://www.anthropic.com/engineering/claude-code-auto-mode "Claude Code auto mode: a safer way to skip permissions \ Anthropic"))

### 5. 沉默失败

最危险的不是报错，而是：

- 结果看似合理但已偏离原始意图
    
- 指标没炸但业务规则悄悄漂移
    
- 测试全绿但用户价值被侵蚀
    

这类问题必须靠人去看“不变量、场景、真实使用意图”。

---

## 五、所以人类真正 review 的对象，应该从“代码”换成这四样

### 1. 目标函数

AI 到底被要求优化什么。

### 2. 约束系统

哪些规则、边界、权限、架构、数据契约不能碰。

### 3. 评价系统

测试、eval、监控、grader、通过线是不是代表你真正关心的东西。

### 4. 接管能力

一旦 AI 修不动了，人是否还能靠现有证据链接手。

这和 OpenAI/Anthropic 这两条当前实践线其实是一致的：一边强调把越来越多开发循环编码进系统，一边强调 harness、tools、environment、evals 这些外围约束和观测。([OpenAI](https://openai.com/index/harness-engineering/ "Harness engineering: leveraging Codex in an agent-first world | OpenAI"))

---

## 六、给你一个最实用的分工原则

你可以直接用这条规则：

**凡是“可形式化、可测量、可回滚、低爆炸半径”的，优先交给 AI。**  
**凡是“涉及意图裁决、权限边界、系统不变量、评价标准、上线责任”的，必须由人 review。**

再压缩一点：

**AI 负责在已知目标内搜索最优实现。**  
**人负责决定目标是什么、边界在哪、什么算不可接受、以及何时不能再交给 AI。**

---
# 前AI时代，这些差异有什么不同？

**换一个角度，以上这两类，哪些交给AI的，哪些交给人的，在Claude等AI编码模型出现之前的软件工程中，这两类对于不同人的能力要求，差异在哪里？**

如果把你前面那两类工作重新投回 **Claude 这类 AI 编码模型出现之前** 的软件工程里，会发现：

**这两类并不是新出现的两类工作，而是原本就存在的两类人类能力。**  
只是以前它们都由人承担；现在其中一类开始可以大量外包给 AI 了。

更准确地说，传统软件工程里本来就有两条线：

一条是 **决定“要做什么、什么算对、什么不能错”**；  
另一条是 **把这些东西实现出来、验证出来、维护起来**。

这和经典的软件生命周期划分是吻合的。SEBoK 引用 SWEBOK 时，把软件生命周期概括为 analysis/design、construction、testing、operation、maintenance，最后到 retirement/replacement；也就是说，软件工程从来不只有“写代码”这一种活动。([SEBoK](https://sebokwiki.org/wiki/Software_Engineering_in_the_Systems_Engineering_Life_Cycle?utm_source=chatgpt.com "Software Engineering in the Systems Engineering Life Cycle"))

## 一、在 AI 出现之前，你说的“两类”大致对应哪两类人

### 第一类：意图—约束—验收 这一侧的人

这类人负责的，不是把代码敲出来，而是回答：

- 我们到底想解决什么问题
    
- 谁是 stakeholder
    
- 哪些需求是真需求，哪些只是局部想法
    
- 什么算成功
    
- 什么绝对不能发生
    
- 当目标冲突时优先级怎么排
    

SEBoK 对 stakeholder needs 的定义本来就不是“清晰需求文档”那么窄，而是 needs、wants、desires、expectations 和 perceived constraints；这说明传统工程早就承认，人类起点并不是一份天然完整、无歧义的规格。([SEBoK](https://sebokwiki.org/wiki/Stakeholder_Needs_and_Requirements_%28glossary%29?utm_source=chatgpt.com "Stakeholder Needs and Requirements (glossary)"))

这类工作，在大团队里通常会分散在：

- 产品经理 / 业务分析
    
- 系统工程师
    
- 架构师 / 技术负责人
    
- 安全 / 合规 / 风险负责人
    
- 高级 QA / 验收负责人
    
- 管理者或关键 stakeholder
    

他们的核心能力，不是“代码写得多快”，而是：

- 处理模糊意图
    
- 跨角色对齐
    
- 做 trade-off
    
- 定义边界
    
- 定义验收口径
    
- 承担上线和风险责任
    

### 第二类：实现—验证—运维 这一侧的人

这类人负责的，是把前面的目标和约束落到工程现实里：

- 设计模块和接口
    
- 编码
    
- 写测试
    
- 调试
    
- 部署
    
- 监控
    
- 修复
    
- 重构
    
- 维护配置和版本基线
    

SEBoK 对 verification 的定义是：把系统或系统元素与所要求的特征做比较，也就是“built right”；对 validation 的定义则是：确认系统在目标运行环境中是否满足 intended use、goals 和 objectives。换句话说，传统工程里本来就有“定义对什么负责”和“证明它真的做到”的两套活动。([SEBoK](https://sebokwiki.org/wiki/Verification_%28glossary%29?utm_source=chatgpt.com "Verification (glossary)"))

这类工作，在大团队里通常会分散在：

- 软件工程师
    
- 测试工程师 / 自动化测试
    
- 运维 / SRE
    
- 配置管理 / 发布工程
    
- 安全测试 / 性能测试
    
- 值班排障人员
    

他们更依赖的能力是：

- 局部实现能力
    
- 调试能力
    
- 测试设计能力
    
- 工具链使用能力
    
- 对系统行为的可观测性和故障定位能力
    

---

## 二、两类能力的真正差异，不在“会不会写代码”，而在处理什么类型的问题

我觉得最关键的差异是这个：

### 第一类人处理的是“语义裁决问题”

也就是：

- 我们真正想要什么
    
- 什么算满足用户和 stakeholder 的意图
    
- 哪些约束必须守
    
- 哪些风险不能接受
    
- 这个系统现在还值不值得上线
    

这类问题的特点是：

- 模糊
    
- 有冲突
    
- 依赖上下文
    
- 很难完全形式化
    
- 常常没有唯一正确答案
    

SEBoK 对 system architecture design 的描述也很贴切：架构不是随便组织几个模块，而是定义结构元素及其行为交互，以满足 stakeholder needs。也就是说，架构本身就是对意图的工程化裁决。([SEBoK](https://sebokwiki.org/wiki/System_Architecture_Design_Definition?utm_source=chatgpt.com "System Architecture Design Definition"))

### 第二类人处理的是“实现与证明问题”

也就是：

- 这段逻辑怎么写
    
- 这个 bug 怎么复现
    
- 这个测试怎么补
    
- 这个依赖怎么改
    
- 这次回归是不是安全
    
- 这次发布能不能回滚
    

这类问题的特点是：

- 更局部
    
- 更可操作
    
- 更容易被形式化
    
- 更适合通过测试、静态检查、监控来判定
    

所以，**两类能力的根本差别，不是“懂不懂代码”，而是“在处理开放式语义问题，还是在处理受约束的工程求解问题”。**

---

## 三、如果放回传统软件工程，这两类能力分别更像哪些“老角色”

你前面说的“该交给 AI 的”和“必须由人抓住的”，在 AI 出现前，大致就是这样分布的。

### 现在你说“必须由人抓”的那些事，以前主要对应这些人类角色

比如：

- 需求发现和澄清：产品经理、业务分析、系统工程师
    
- 目标优先级与风险裁决：管理者、tech lead、架构师
    
- 系统不变量、边界、架构责任：架构师、资深工程师
    
- 验收标准和最终发布：QA 负责人、项目负责人、运营负责人
    
- 高风险动作授权：安全、合规、发布负责人
    

这些角色的共同点不是“比别人更会写代码”，而是：

**他们承担“解释系统为什么存在、为什么这么设计、什么算不可接受”的责任。**

### 现在你说“可以更多交给 AI”的那些事，以前主要对应这些人类角色

比如：

- 局部实现
    
- 测试初稿
    
- 重复性重构
    
- 风险扫描
    
- 配置整理
    
- 首轮代码检查
    
- 根据失败用例修 bug
    
- 依据明确规则做变更
    

以前这些当然也是人做，但更偏：

- 程序员
    
- 测试工程师
    
- 发布工程师
    
- 运维工程师
    
- 静态分析 / 工具链维护者
    

这些角色的共同点是：

**他们更多是在已知目标和约束内做求解、验证和执行。**

---

## 四、所以在 AI 出现前，真正的能力分野其实是“裁决能力”和“求解能力”

我会把它概括成这两组。

### 1. 裁决型能力

这是现在仍然最不该轻易外包给 AI 的那组。

包括：

- 从模糊表述里提炼真实意图
    
- 识别 stakeholder 冲突
    
- 定义边界和不变量
    
- 做架构级 trade-off
    
- 判断某个结果“虽然能跑，但不是我们真正想要的”
    
- 决定是否上线、是否停下来重构
    

这类能力，在传统工程里往往集中在资深角色身上。  
SEBoK 还专门说，technical reviews and audits 是由“sufficiently independent and knowledgeable stakeholders”按照预先定义的标准来分析系统当前状态，并支持技术和项目决策。这里面关键词其实不是“会写代码”，而是 **independent、knowledgeable、能作决策**。([SEBoK](https://sebokwiki.org/wiki/Technical_Reviews_and_Audits?utm_source=chatgpt.com "Technical Reviews and Audits"))

### 2. 求解型能力

这是现在最容易被 AI 大量接管的那组。

包括：

- 按既定目标写实现
    
- 按既定规则补测试
    
- 按失败样例修复
    
- 识别重复逻辑
    
- 跑静态检查和回归
    
- 在受控边界内做重构和迁移
    

这类能力，在传统工程里当然也很重要，但它更接近“工程执行与证明”。

---

## 五、这也是为什么，AI 出现以后，最先被重塑的不是“架构判断”，而是“实现与验证劳动”

因为从传统分工上看，AI 最容易替代的，本来就是那部分：

- 目标相对明确
    
- 成败可通过测试和规则判断
    
- 局部修改就能完成
    
- 出错后可回滚
    
- 不需要重新解释 stakeholder 意图
    

而最难替代的，仍然是那部分：

- 需求并不完整
    
- 目标会冲突
    
- 成功标准带有价值判断
    
- 错误不一定表现为程序崩溃，而可能是“背离本意”
    
- 一旦出错，责任要落在人身上
    

这其实和传统 verification / validation 的分界高度一致：  
verification 更接近“做对”，validation 更接近“做的是不是对的东西”。([SEBoK](https://sebokwiki.org/wiki/Verification_%28glossary%29?utm_source=chatgpt.com "Verification (glossary)"))

---

## 六、所以回答你的问题：AI 出现前，这两类对人的能力要求差异在哪里？

最核心的差异有四个。

### 第一，抽象层级不同

一类人面对的是系统目的、边界、风险、接受条件；  
另一类人面对的是模块、函数、测试、发布、故障。

### 第二，问题类型不同

一类人处理的是开放式、语义型、冲突型问题；  
另一类人处理的是封闭得多、可验证、可回滚的问题。

### 第三，责任性质不同

一类人承担“决定什么算对”的责任；  
另一类人承担“把它做出来并证明它做到”的责任。

### 第四，知识结构不同

一类人更依赖：

- 领域理解
    
- 系统思维
    
- 风险意识
    
- 沟通与协商
    
- 架构判断
    

另一类人更依赖：

- 实现能力
    
- 测试与调试能力
    
- 工具链和流程能力
    
- 故障定位能力
    
- 工程执行能力
    

---

## 七、这也解释了一个常见误解

很多人会把“AI 时代哪些该交给 AI、哪些该留给人”理解成：

- 低级工作给 AI
    
- 高级工作给人
    

我觉得这不准确。

更准确的是：

**可形式化、可判分、可回滚的工作，更适合交给 AI；  
需要定义意义、裁决冲突、承担后果的工作，更适合由人负责。**

在 AI 出现前，这两部分本来也不是由“同一种能力的人”在做。  
只是以前，这两边都还是人。

---

## 八、把它收成一句话

在 Claude 这类 AI 编码模型出现之前，软件工程里就已经存在两种不同的人类能力：

**一种是“定义目标、边界和可接受后果”的能力；  
一种是“在既定目标内求解、实现、验证和维护”的能力。**

AI 主要开始接管的是第二种。  
而你一直在追问、也最值得人类保留的，是第一种。

---
# 传统软件公司价值是否大打折扣？

**不是这些厂商的价值会整体“大打折扣”，而是它们的价值会被重新定价、重新分层。**

真正会被明显压缩的，是“把需求翻译成代码的人天价值”；  
不那么容易被压缩的，是“把一个高风险行业系统真正落地、迁移、接入、担责并长期运转起来”的价值。这个区别在银行、证券、医疗、建筑这类行业里尤其大。NIST 的 AI 风险管理框架强调，AI 系统要围绕治理、测量、管理和场景化风险来落地；美国 OCC 最新的模型风险管理修订指引也明确把治理与控制、模型验证与监控，以及**vendor 和 third-party products** 纳入管理范围。也就是说，在强监管行业里，企业买的从来不只是代码，而是“可用、可审、可管、可追责”的系统能力。([NIST](https://www.nist.gov/itl/ai-risk-management-framework?utm_source=chatgpt.com "AI Risk Management Framework | NIST"))

所以，按你前面的推论往下走，我会给出一个更细的判断：

## 1. 会被压缩的价值

如果一个软件厂商的核心卖点主要是下面这些，它未来压力会很大：

- 大量定制开发的人天收入
    
- 通用 CRUD/流程系统的手工实现
    
- “客户提需求—厂商写代码—长期堆人维护”的线性模式
    
- 缺少行业独特知识，只靠交付队伍规模取胜
    

这一块会被 AI 编码、自动测试、自动文档、自动重构明显压价。McKinsey 对 tech services 的判断也不是“服务业消失”，而是服务商必须重塑；它估计围绕 GenAI/AI 的新服务市场到 2029 年可能超过 2000 亿美元，说明价值不会凭空消失，但会从旧服务形态迁移到新服务形态。([McKinsey & Company](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/tech-services-and-generative-ai-plotting-the-necessary-reinvention?utm_source=chatgpt.com "Reinventing tech services with generative AI"))

## 2. 不容易被压缩，甚至可能更贵的价值

在银行、证券、医疗、建筑这类行业，以下能力反而可能更重要：

- 对行业流程、规则、术语、例外场景的深度理解
    
- 对核心系统、老系统、外部系统的集成能力
    
- 数据迁移、并行切换、回滚与灾备能力
    
- 合规、审计、权限、留痕、模型治理能力
    
- 本地部署、信创适配、安全边界和长期 SLA
    
- 出事故时“谁来扛、谁来修、谁来解释”的责任能力
    

这也是为什么大型服务商和系统集成商不是在“远离 AI”，而是在把自己重新定义成“可信 AI 落地者”。比如 Anthropic 和 Deloitte 的合作，明确就是面向金融服务、医疗与生命科学、公共服务等受监管行业，强调 compliance features 和 trustworthy AI；Accenture 也在把 AI 与既有系统集成、云基础和行业专家结合起来。([anthropic.com](https://www.anthropic.com/news/deloitte-anthropic-partnership?utm_source=chatgpt.com "Anthropic Deloitte Partnership"))

## 3. 放到你提到的中国厂商身上，结论不是“没价值了”，而是“必须换价值锚”

拿你举的两类例子看，它们自己其实已经在往这个方向转。

长亮科技官网和年报材料里，强调的不是“我们会写代码”，而是**银行核心系统**、微服务加单元化架构、第三方平台对接、国产化/信创落地经验，以及面向银行的长期行业积累；公司 2024 年年报也直接写到自己深耕银行数字化应用 20 余年，并把下一步机会判断为“应用为王”。它最近的公开动态也在持续强调 AI Native、核心系统项目中标、数据治理和与华为的联合方案。([sunline.cn](https://www.sunline.cn/show-31.html?utm_source=chatgpt.com "核心业务系统解决方案"))

神州数码这边，官方披露的重点也不是“卖开发人力”，而是“AI 驱动的数云融合”“AI for Process”、平台能力和产品体系升级。公司 2025 年董事会工作报告写到，全年营收 1,437.5 亿元，同比增长 12.2%，AI 相关业务收入 330.3 亿元，同比增长 47.7%；其官方材料还强调医疗制药、高端制造、汽车、运营商、零售、消费等行业中的 AI 场景化落地。([CNINFO](https://static.cninfo.com.cn/finalpage/2026-03-31/1225058648.PDF?utm_source=chatgpt.com "神州数码集团股份有限公司2025年度董事会工作报告"))

这至少说明一件事：  
**这些厂商自己也不认为未来的核心价值还是“手工写更多代码”，而是在把自己往“行业平台 + AI 集成 + 交付治理 + 长期运营”方向迁。** ([sunline.cn](https://www.sunline.cn/cs-news.html?utm_source=chatgpt.com "新闻动态"))

## 4. 所以更准确的判断应该是“价值迁移”，不是“价值归零”

我会把未来分成三种厂商：

第一种，**纯人天型外包商**。  
这类会最受冲击，因为 AI 会直接压缩它们最核心的生产函数。

第二种，**行业产品/解决方案厂商**。  
这类会被迫把“代码交付”升级为“业务模型、规则引擎、数据资产、评测体系、治理能力”的交付；做不到就会被压，做到的反而可能更强。

第三种，**强集成和强责任厂商**。  
在银行、医疗、建筑这种复杂现场里，这类厂商的价值很可能还会上升，因为客户真正缺的是“把 AI 安全地接进现有生产系统并持续跑稳”的能力，而不是单纯写出更多代码。NIST、OCC、FDIC 这类框架和指引，本身就在强化这类治理与验证需求。([NIST](https://www.nist.gov/itl/ai-risk-management-framework?utm_source=chatgpt.com "AI Risk Management Framework | NIST"))

## 5. 我更担心的，不是“这些厂商会不会消失”，而是它们会不会被迫从卖开发，转成卖责任

这会带来三个变化：

**第一，收入结构变。**  
从“项目开发费 + 人天”转向“平台订阅/许可 + 集成实施 + 托管运营 + 持续治理”。

**第二，能力结构变。**  
从“程序员规模”转向“行业专家 + 架构师 + 数据治理 + AI 评测/治理 + 运维与安全”。

**第三，竞争对手变。**  
它们以后不只跟传统软件厂商竞争，还会同时面对模型厂商、云厂商、咨询公司、行业龙头自建团队，以及更轻量的 AI-native 产品公司。Deloitte、Accenture 这些全球玩家已经在做这件事。([anthropic.com](https://www.anthropic.com/news/deloitte-anthropic-partnership?utm_source=chatgpt.com "Anthropic Deloitte Partnership"))

## 6. 给一个直接结论

所以，如果你问的是：

**“长亮、神码这类厂商会不会因为 AI 编码出现而整体失去价值？”**

我的回答是：

**不会简单地整体失去价值，但它们过去那部分“靠开发交付本身赚钱”的价值，大概率会被持续压缩。**

而它们未来还能不能值钱，取决于能不能把价值锚从：

**“我能帮你写系统”**

换成：

**“我能把你这个行业里高风险、强约束、强存量系统依赖的复杂问题，用 AI 和软件一起真正落地，并且出了事我能解释、能修、能担责。”**

谁完成这次转换，谁的价值未必下降；  
谁还停留在“卖代码生产力”，谁的价值就更容易被 AI 吞掉。

---
# 我们究竟在谈什么？

从第一性原理往下压，我认为我们一直在讨论的核心问题，其实只有一句话：

**当“写代码”越来越可以交给 AI 时，人类在软件工程里究竟还必须牢牢掌握什么，才能确保最终系统仍然服务于人的真实意图，而不是演化成一个可运行但不可理解、不可维护、不可担责的黑盒。**

再往下拆，这个核心问题可以还原成 5 个最底层事实。

## 1. 软件的本体，不是代码，而是“人类意图的机器化承载”

代码只是中间介质。  
软件真正要完成的是：

- 把人的目标、约束、偏好、禁忌、风险承受能力
    
- 转化成
    
- 机器在现实世界中的持续行为
    

所以软件工程的本质，从来不是“把代码写出来”，而是：

**把人的意图，稳定地翻译成机器行为。**

这也是为什么我们后来不断把问题从 code review，推到了 intent review、validation、alignment。

---

## 2. 人类意图天然是不完备的、演化的、带冲突的

这点很关键。

如果人类意图一开始就能被完整、准确、无歧义地表达出来，那软件工程就会退化成一个纯技术翻译问题。  
但现实不是这样。

现实是：

- 人一开始说不清自己真正想要什么
    
- 不同人心里的“目标”并不一样
    
- 系统做出来以后，人对自己的需求理解还会变化
    
- 很多真正重要的约束，最初根本没有被写下来
    

所以问题的难点，从来不只是“实现对不对”，而是：

**最后做出来的东西，还是不是那个“我们真正想要的东西”。**

---

## 3. AI 改变的，不是“软件需要被验证”这件事，而是“谁在做什么工作”

AI 的出现，并没有改变软件工程的终极目标。  
它改变的是劳动分工。

过去很多工作都必须由人完成：

- 实现
    
- 测试
    
- 重构
    
- 首轮审查
    
- 故障修复
    

现在其中相当大一部分，可以交给 AI。

但这里有一个不会变的底层约束：

**凡是可形式化、可测量、可回滚的问题，AI 更适合承担；  
凡是涉及目标定义、边界裁决、不可接受后果、责任承担的问题，人类必须保留控制权。**

所以我们一直在讨论的，不是“AI 能不能写代码”，而是：

**当 AI 能写代码后，人类应当把自己的注意力从哪里撤出，又必须把什么重新抓紧。**

---

## 4. 所谓 review，本质上不是“检查代码”，而是“重建控制权”

这其实是我们讨论里最重要的转折。

在传统开发里，review 常常默认 reviewer 已经理解系统，所以 review 更像局部正确性检查。  
但对一个 100% AI 生成、持续膨胀的系统，这个前提不成立。

这时 review 的本质就变了。  
它不再只是：

- 看写法
    
- 看风格
    
- 看小 bug
    

而变成：

- 重建这个系统到底在做什么
    
- 重建它为什么这样做
    
- 重建它服务于什么意图
    
- 判断它是否已偏离原始目的
    
- 判断人类是否还能重新接管它
    

所以 review 的真正对象，不是代码文本，而是：

**系统行为、结构、约束、不变量、故障模式，以及它们与人类意图之间的对应关系。**

换句话说：

**review 的本质，是人类对未知系统重新取得解释权、判断权、维护权。**

---

## 5. 因此，最终问题不是“AI 会不会替代软件工程”，而是“软件工程的中心会迁移到哪里”

如果从第一性原理看，软件工程至少有两层：

### 第一层：意图层

回答：

- 我们到底想要什么
    
- 什么不能发生
    
- 什么算成功
    
- 什么风险可接受
    
- 当目标冲突时怎么裁决
    

### 第二层：实现层

回答：

- 怎么把它做出来
    
- 怎么验证
    
- 怎么修复
    
- 怎么运行
    
- 怎么演进
    

AI 正在强烈改写第二层。  
但第一层不仅没有消失，反而变得更重要了。

因为一旦实现能力被极大放大，如果意图层失控，系统就会更快、更大规模地偏离。  
也就是说：

**AI 不是削弱了“意图治理”的重要性，而是放大了它的重要性。**

---

# 所以，我们讨论的核心问题，最终可以压缩成三个根问题

## 根问题一

**软件最终对谁负责？**

是对代码本身负责，  
对规格文本负责，  
还是对人类真实意图负责？

我们最后其实落在第三个答案上。

---

## 根问题二

**在 AI 大幅接管实现之后，人类必须保留什么控制权？**

答案不是“所有代码都要看”。  
而是要保留：

- 目标定义权
    
- 边界设定权
    
- 评价标准设定权
    
- 上线与风险裁决权
    
- 故障后的接管权
    

---

## 根问题三

**如何防止系统在可运行中逐渐失真？**

这正是你最早担心的那个问题：

- AI 写得越来越多
    
- 系统越来越大
    
- 问题越来越深埋
    
- 最后连 AI 和人都找不到根因
    
- 团队拿到一个无法维护的软件系统
    

所以真正要解决的，不是单点 bug，而是：

**如何防止“人类意图 → 系统行为”的映射，在规模化 AI 编码过程中逐步断裂。**

---

# 如果用一句最抽象的话来总结

**我们讨论的核心问题，是：在人类意图天然不完备、而 AI 又极大增强实现能力的条件下，如何让软件工程继续是一种“对人类目的负责的工程”，而不是退化成一种“能生成复杂系统、却无人真正理解和控制其意义”的生产过程。**

再说得更白一点：

**不是“AI 会不会写软件”，而是“谁来保证这个软件最终还是人的软件”。**

如果你愿意，我下一步可以把这个第一性原理总结继续往下收敛成一个更工程化的版本，形成一张图：

**“AI时代软件工程的第一性原理框架”**。
