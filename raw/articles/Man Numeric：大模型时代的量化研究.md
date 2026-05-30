---
source: ima
kind: wechat
category: "技术"
title: "Man Numeric：大模型时代的量化研究"
url: "https://mp.weixin.qq.com/s?__biz=MzAxNTc0Mjg0Mg==&mid=2653351421&idx=1&sn=24362d7b499c016ca5a9eba1d8fdbdd1&chksm=81b3df02c9921124a218d6cf9549c580c1e3c5abf24f7137b3139d782cb56155b61e66176bb2&scene=90&xtrack=1&req_id=1766639102664127&sessionid=1766639152&subscene=93&clicktime=1766639178&enterid=1766639178&flutter_pos=11&biz_enter_id=4&ranksessionid=1766639152&jumppath=50096_1766638943945%2C1101_1766638947668%2C1001_1766639102493%2C1104_1766639153115&jumppathdepth=4&ascene=56&devicetype=iOS18.7.2&version=18004237&nettype=3G+&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&countrycode=CN&fontScale=109&exportkey=n_ChQIAhIQcpeK5uKky3wMqiN1Sia8nhLUAQIE97dBBAEAAAAAAEZkN7b2ulMAAAAOpnltbLcz9gKNyK89dVj0P2ls7Jw%2BKEmMas%2F1OPNFfp9vQlBU%2BuF4L6fjFNs0TP3sIe9S6wvgNFQsOND55qsDVwJyUEc4tXPrqSi5vGto6E%2BycFF6rkzJW4FS9BWJCeHu32VrrVaWMUGQajdK6ujEOVmm%2Bdg2zyqyoQkmKr6KVB8FWOdHiSt7LCVwWbcaD0XzsinwlOhVKKEF3lwB8dwsaIcjmPUmKqRMbK2tHidAEZu25gHz%2Ff2KAnWtCbRI&pass_ticket=2GSkIV7rT77s9rPx8Ja03XfNsn8mJygYKO4kbgzU4We%2FJt7t9So0CT9%2F0%2FDajLpz&wx_header=3"
media_id: "wechatarticle_30987b07fe36143e35b82223ae18bcbe_50c03c8ce42fde57daf9b79baf990f75"
media_type: 6
kb_name: "殷凇的知识库"
kb_id: "qzeC00QqxVZKyNdfTs2u_JmTwlIqypGehkvk2cjRaNw="
kb_folder_path: "/"
created_from_ima_at: "2026-05-11T10:27:18.695Z"
body_status: full_text
fetched_at: "2026-05-14T12:59:49+08:00"
---

# Man Numeric：大模型时代的量化研究

- 来源：ima 个人知识库
- 原文链接：[打开原文](https://mp.weixin.qq.com/s?__biz=MzAxNTc0Mjg0Mg==&mid=2653351421&idx=1&sn=24362d7b499c016ca5a9eba1d8fdbdd1&chksm=81b3df02c9921124a218d6cf9549c580c1e3c5abf24f7137b3139d782cb56155b61e66176bb2&scene=90&xtrack=1&req_id=1766639102664127&sessionid=1766639152&subscene=93&clicktime=1766639178&enterid=1766639178&flutter_pos=11&biz_enter_id=4&ranksessionid=1766639152&jumppath=50096_1766638943945%2C1101_1766638947668%2C1001_1766639102493%2C1104_1766639153115&jumppathdepth=4&ascene=56&devicetype=iOS18.7.2&version=18004237&nettype=3G+&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&countrycode=CN&fontScale=109&exportkey=n_ChQIAhIQcpeK5uKky3wMqiN1Sia8nhLUAQIE97dBBAEAAAAAAEZkN7b2ulMAAAAOpnltbLcz9gKNyK89dVj0P2ls7Jw%2BKEmMas%2F1OPNFfp9vQlBU%2BuF4L6fjFNs0TP3sIe9S6wvgNFQsOND55qsDVwJyUEc4tXPrqSi5vGto6E%2BycFF6rkzJW4FS9BWJCeHu32VrrVaWMUGQajdK6ujEOVmm%2Bdg2zyqyoQkmKr6KVB8FWOdHiSt7LCVwWbcaD0XzsinwlOhVKKEF3lwB8dwsaIcjmPUmKqRMbK2tHidAEZu25gHz%2Ff2KAnWtCbRI&pass_ticket=2GSkIV7rT77s9rPx8Ja03XfNsn8mJygYKO4kbgzU4We%2FJt7t9So0CT9%2F0%2FDajLpz&wx_header=3)
- ima media_id：`wechatarticle_30987b07fe36143e35b82223ae18bcbe_50c03c8ce42fde57daf9b79baf990f75`
- ima 目录：/
- 内容分类：技术
- 正文状态：已抓取全文。

## 摘要

> 当前 ima 知识库列表接口未返回文章摘要字段；本条先保存标题、链接、media_id、目录与分类，便于后续按需补正文/摘要。

## 正文

量化投资与机器学习微信公众号，是业内垂直于量化投资、对冲基金、金融科技、人工智能、大数据等领域的主流自媒体。公众号拥有来自公募、私募、券商、期货、银行、保险、高校等行业40W+关注者，曾荣获AMMA优秀品牌力、优秀洞察力大奖，连续4年被腾讯云+社区评选为“年度最佳作者”。

作者：Ziang Fang、Jason Moore
在当代量化研究中，一个尤为突出的挑战在于：可获取的数据规模和分析维度正以前所未有的速度扩张，而人类研究者的时间、精力和认知带宽却始终有限。即便能力再强，研究人员在任何时点也只能覆盖极其有限的一部分研究路径和假设空间。
正因如此，对冲基金、资产管理机构以及投资银行近年来持续探索将大语言模型（LLM）引入研究流程。在“开箱即用”的技术形态下，这类模型已经能够稳定承担相当于初级研究员或实习生层级的工作，包括代码编写、研究资料整理以及文献总结等任务。
然而，竞争的真正焦点早已不止于把 LLM 当作聊天工具或辅助问答系统，而在于如何系统性地释放其更深层的潜力：构建具备代理能力（agentic）的人工智能，使其能够在既定框架下自主推进研究流程——拥有大规模的知识储备，遵循严谨、可复现的研究方法，并持续产出既具创造性、又值得信赖的研究成果，在功能上逐步接近一名成熟的研究分析师。
正是在这一背景下，Man Numeric推出了其自研的代理式 AI 研究工作流——AlphaGPT。
什么是 AlphaGPT？
可以将 AlphaGPT 理解为一支永不休眠的“三人制数字化研究团队”：它能够在数秒内处理海量金融数据，并严格按照既定的系统化投资方法论推进研究流程。与人类研究团队类似，这个虚拟团队中的每一个“成员”，都各自负责研究流程中的一个关键阶段。
研究构想者（Idea Person）
这一模块负责提出投资概念与研究假设。正如人类研究员可能会提出诸如“买单多于卖单的股票是否更容易跑赢？”或“招聘效率更高的公司是否表现更好？”这样的问题，AlphaGPT 也会系统性地生成大量可检验的研究命题。
在实际应用中我们发现，该系统并不仅停留在直观或显而易见的关联上，而是能够持续探索看似无关的市场变量之间的细微关系，覆盖大量因认知带宽有限而往往未被人类研究者充分检视的研究空间。结果显示，AlphaGPT 往往可以在几分钟内产出数十个具备可行性的研究方向，而这一过程对人类研究员而言通常需要数天。
研究实现者（Implementer）
该模块负责将研究构想转化为可执行的研究代码。它能够编写生产级别的 Python 程序，直接调用 Man Numeric 内部的研究工具链，并与专有数据库进行交互。
原本需要研究员花费数小时甚至数天完成的编码与调试工作，AlphaGPT 往往能够在几分钟内完成。这使得多个研究假设可以被快速并行测试，大幅减少反复编码、修改与验证所消耗的时间。
研究评估者（Evaluator）
这一代理负责对研究成果进行严格评估。所有由 AI 生成的研究结果，都必须通过与人工研究完全一致的审查标准，包括统计显著性检验、风险分析以及经济逻辑的一致性检查。
换言之，任何 Alpha 信号不仅需要在数学意义上成立，更必须具备清晰、合理的经济解释，并通过与人工研究相同的评估门槛，才能进入下一阶段。
AlphaGPT 之上还配备了一套研究流程的编排与调度系统，用以协调上述三个角色的协同工作，并在系统层面嵌入多重防护机制，以降低幻觉（hallucination）等 AI 常见风险。截至目前，该系统已经产出多项符合内部研究标准、并通过与人工研究一致评估流程的研究信号。
它只是自动化既有工作，还是展现了真正的“创造力”？
尽管大语言模型本质上并不具备“思考能力”，AlphaGPT 在实际表现中仍展现出类似创造力的特征。
在与人类研究员的对比中我们发现，AlphaGPT 经常探索一些尚未被人类系统覆盖的研究方向——这并非因为研究员能力不足，而更多源于研究空间规模过大、筛选成本过高。该系统能够同时考察极其庞大的潜在关系组合，从而发现原本可能被忽略的研究路径，填补即便是经验丰富的研究人员也未必意识到的空白。
当然，AI 在创意生成上仍无法全面超越人类，但其所提供的补充视角，往往能够与人工研究形成良好的互补，使整体研究版图更加完整、立体。真正的差异并不在于“是否更聪明”，而在于假设生成的数量与速度——而这既带来了新的机会，也引入了新的风险。
风险在哪里？如何防止p-hacking与幻觉问题？
AlphaGPT 的高速探索本身会引入特定的统计风险。系统能够在极短时间内测试大量假设变体与组合，从而显著提高发现“看似显著、实则偶然”的统计假象的概率。这类结果在历史回测中可能表现良好，但在真实交易中往往难以复现，这正是多重检验问题（multiple testing），也常被称为 p-hacking。
对此，我们的应对方式并非降低探索强度，而是严格执行统一的研究流程约束。无论研究来源于人类还是 AI，都必须遵循同一套长期行之有效的统计纪律与研究方法。同时，我们也在持续扩展监控与治理基础设施，以确保在研究信号数量显著增加的情况下，依然能够保持高质量的监督能力。
另一类风险来自幻觉与“漂移”：AI 可能在概念上提出一个研究想法，但在代码实现时偏离原意；或在生成代码过程中误解研究假设，导致方法论表述与实际执行之间出现不一致。
针对这些问题，我们采用了精细化的提示工程（prompt engineering），以确保研究目标与约束被准确传达；同时，在代理式工作流中嵌入多层一致性校验机制，用于核查构想、实现与评估之间的对应关系。结合自动化与人工审核的系统性验证流程，确保研究意图与最终实现高度一致。
我们将这些问题视为工程挑战，而非不可逾越的根本障碍，并以管理传统量化研究风险的同样方式来管理 AI 风险。
人类在验证AI生成策略中扮演什么角色？
在 AlphaGPT 的当前发展阶段，人类监督仍然不可或缺。系统通过完整的日志机制记录从研究假设生成到最终实现的全过程，每一个决策节点、假设前提与逻辑步骤都可以被追溯与审查，从而确保透明性与可问责性。
所有 AI 生成的研究信号均需经过“双轨验证”：
1、投资委员会从研究假设、经济逻辑与结果合理性的角度进行评估；
2、技术团队则负责代码审查、单元测试、集成测试与情景分析，并评估潜在的实现风险。
随着系统逐步成熟，这一监督模式也将持续演进。我们正在构建更强健的自动化监督体系，以应对更高规模的研究产出。但可以明确的是，审查标准不会因此降低。无论策略来源于人类还是 AI，在进入实盘交易之前，都必须通过完全一致的门槛。
这种技术最终会不会被“商品化”？
我们完全预期，大语言模型与代理式工作流将在投资行业内被广泛采用，任何先发的技术优势本质上都是阶段性的。
真正可持续的竞争优势，来自于超越单一技术的系统化投资能力：长期积累的专有数据、技术基础设施、组织原则，以及经多个市场周期检验的研究哲学。此外，机构记忆与成熟的方法论，也并非短期内可以复制。
AlphaGPT 的架构具备高度模块化与技术中立性，能够随着底层模型能力的演进持续升级，而无需重构核心系统。我们也在积极探索针对系统化研究场景的后训练（post-training），甚至训练面向特定用途的小型语言模型。
AlphaGPT能否扩展至不同资产类别？
目前来看，AlphaGPT 在系统化股票研究中表现最为成熟，但核心研究原则在不同资产类别之间具有高度共通性。扩展的关键在于：在保留代理式研究流程内核的前提下，对数据源、研究方法与分析框架进行资产类别层面的定制。系统的模块化设计正是为此而生。
AlphaGPT的未来
当前，AlphaGPT 仍运行在“human-in-the-loop”的模式下。我们的长期目标，是在确保问责与透明的前提下，实现可规模化的自动化监督。
未来，随着技术基础设施的持续增强，监督能力将通过更先进的工具得到提升，而非通过降低标准来换取效率。AI 系统始终需要保持可解释性，并在必要时接受人工干预。
迄今为止，一个清晰的结论是：AlphaGPT 并非替代人类判断，而是放大人类能力。最有效的使用方式，是人类研究员与 AI 协同工作——人类负责战略方向、市场理解与最终决策，而 AlphaGPT 承担数据处理、假设生成与分析等高强度任务。
