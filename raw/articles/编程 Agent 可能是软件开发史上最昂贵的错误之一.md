---
source: InfoQ
publish_time: "2026-05-26 14:05"
source_url: "https://mp.weixin.qq.com/s/jrx62vYAWfbJ42CO8mQveg"
category: "技术"
kind: wechat
ingested: 2026-05-31
sha256: c2074afe173cadbe49b3d1357eafc1e2fd75835bc523abd58ad0d8caa42ddf5a
---

# 编程 Agent 可能是软件开发史上最昂贵的错误之一

- 来源：InfoQ
- 发布时间：2026-05-26 14:05
- 原文链接：https://mp.weixin.qq.com/s/jrx62vYAWfbJ42CO8mQveg
- 内容分类：技术
- 文章摘要：一场清算正在到来。

## 框架判断

- **阅读深度**：Read Normally
- **保存建议**：保存
- **框架定位**：主层级 L2.5（人类/组织适应），副层级 L2（经济扩散）、L0（方法）
- **对应活问题**：AI编程工具的真实生产力和成本边界在哪？组织采用AI coding agent的正确方式和节奏
- **有用之处**：
  1. Hotz 六个月真实项目测试的一手经验——Agent "把所有进展提前堆在前面，然后递给你一个老虎机拉杆"
  2. Pi/OpenClaw 创建者 Zechner & Ronacher 的内部警告——"vibe slop" 现象和初级人才管道干涸
  3. Uber 真实成本数据——token消耗与功能产出之间的因果链尚未建立
  4. 英伟达 Catanzaro 确认：AI 计算成本目前远超员工成本
- **框架贡献**：
  - 事实校准：多方一手来源的负面信号，不是外行喊话
  - 因果机制：Agent 的前期提速 + 后期老虎机模式，解释了为什么"10x代码"在组织层面可能是"10x垃圾"
  - 决策含义：对凇哥当前的 AI coding 工作流有直接参考——大组织比小团队更脆弱，高绩效者的纠错能力是关键分水岭
- **框架更新**：无需更新层级页；可链接到活问题清单中的 AI编程工具边界问题
- **噪音风险**：
  1. 本文是 InfoQ 编译，非一手报道，存在选择性引用的可能
  2. Hotz 的立场在 LeCun/Marcus 阵营，可能有认知闭合偏误
  3. 缺少定量数据（代码质量指标、bug率对比等），主要依赖定性经验
- **后续读法**：建议读 Hotz 原文（geohot.github.io）和 Business Insider 对 Uber 的报道原文获取更多细节

## 正文

[图片] https://mmbiz.qpic.cn/mmbiz_jpg/hLLZnAbUwNgryNic0XShwObFicWBZibLNicI9QKcibHibiaDaCvflee1tuPUIEiaQct1icJxKlxiaofqAPOILJZc5vCVf7wktZRnyuiaUia8sLo0Y6bxDbA/640?wx_fmt=jpeg&from=appmsg

[图片] https://mmbiz.qpic.cn/mmbiz_gif/YriaiaJPb26VPQqHC66RJFpttVIMWG83T3lWHahUD4bvhxlKSayjeV2ibvC5ydqklP9QHDPD3qHJM07TV3IfHstjA/640?wx_fmt=gif

作者 | Tina

“我敢断言：把 AI Agent 引入软件开发，将会成为这个领域历史上代价最惨重的错误之一。”

说出这句话的人是 George Hotz。17 岁那年他第一个破解了 iPhone，后来又逆向工程了 PlayStation 3——Sony 因此把他告上了法庭。再后来他创办了 comma.ai，成了自动驾驶领域最不按常理出牌的人。

过去六个月，Hotz 把市面上叫得上名字的 AI 编程 Agent 全试了一遍。他用它们写过 tinygrad 的代码，用它们逆向过一个 USB 转 PCIe 芯片。他换过不同模型、不同 harness，也试过不同提示词。

上周日，他把自己的结论写成一篇博客，标题叫《永恒的 Sloptember》，认为大规模采用人工智能编码 Agent 将以灾难告终，或者至少接近灾难。

Hotz 的核心论点很明确：Agent 不是程序员。“Agent 不会编程，而且我们意识到它们不会编程这件事，正在变得越来越难。”他写道，“它们是一种高度复杂的统计模型，被设计出来模仿‘编程’这件事的分布。它们生成的东西就是坏的，只是坏得越来越隐蔽、越来越难查出来。而这，正是一个越来越精确的统计模型会带来的结果。”

1 AI 编程的两极：Karpathy 看见革命，Hotz 看见灾难

五天前，AI 圈最知名的研究者之一 Andrej Karpathy 刚刚加入 Anthropic，并公开表示一个明确的观点：AI Agent 已经彻底改变了软件开发。

现在，这两个人代表了行业尚未解决的一场争论的两个极端，而且双方都有足够的可信度来支撑自己的立场。

[图片] https://mmbiz.qpic.cn/mmbiz_jpg/hLLZnAbUwNhiaGsON9O3utUPSia4M3exwHjMvV3rJxNVbT5pzlVNpPkQmE2ZiaMkcNJyuOWm1xCjCIocoAj2jicygP4AzfpGlPGLTdUyldpvZHo/640?from=appmsg

Hotz 并不是一开始就这么确信。他花了六个月时间，在真实项目中使用 Agent：包括为他的开源深度学习框架 Tinygrad 写部分代码，以及对一个 USB-PCIe 芯片做完整的固件逆向工程。但最后他的结论是，每一次他都本可以靠手工“做得更好、更快”。他观察到的模式是：“Agent 会把所有进展都提前堆在前面，然后递给你一个老虎机拉杆，让你不断去拉，指望它把最后的打磨做完。但它总是差那么一点。”

Hotz 预料到了最显而易见的反驳：

在有人跳出来说“是你用错了”之前，我先说：不同模型、不同 harness、不同提示词，我都试过。问题不在这里。那些说这种话的人，大概也会对老虎机说同样的话：你看，拿到一个樱桃之后就应该押五条线，难怪你一直赢不了！

我并不是说 AI 没用，它显然有用。对大多数搜索来说，它肯定是一个更好的 Google。只要你需要一个快速原型，又不在乎打磨程度，它的速度快得离谱。

但它是软件工程师吗？离我工作过的任何一家公司的标准都差得远。关键在于，你要知道什么时候该用它，什么时候不该用。

一个把手艺视为自我身份一部分的程序员，自然会抵触那些威胁要取代他的工具。他也认真对待了这个质疑，但也从事实层面驳回了它。

Hotz 写道：“我后来又想了想所谓维护自我价值这件事。（Google 的） AFL 找到的 bug 比 LLM 更多，也没人因此有这种感觉。国际象棋和围棋比以往任何时候都更流行。”从某种意义上说，他是对的，因为国际象棋 AI 统治人类已经有几十年了，但这项游戏反而变得更受欢迎。

所以，他担心的并不是自己被取代。他真正担心的是，当所有人同时使用这些工具时，代码质量会发生什么变化，尤其是在大型科技公司和华尔街不断推动这些工具大规模使用的情况下。

Hotz 认为：“我甚至觉得，这套说法有点像某种为了卖 Agent 而制造出来的心理战。对损失的恐惧，是少数能推动大公司行动的方式之一。只不过我认为，它们正在这种恐惧中犯下一个巨大的错误。”

他认为，到头来，Agent 对大型组织造成的伤害，会比对高绩效个人或小型组织更大。

过去六个月，我一直在观察身边的朋友和同事是怎么采用这些工具的。所有高绩效的人身上都有一个共同特征：他们有纠错能力，而且大多数时候，他们都能看出来什么时候垃圾就是垃圾。确实需要花一点时间去探索、试用，并调整外层循环，比如什么时候用它们、什么时候信任它们、该怎么用它们等等。但除了少数边界很清楚的领域之外，我没有见过他们中的任何一个人转向一种“不再认真阅读并理解每一行代码”的模式。

再看看大型组织。反馈循环慢得多，对齐程度也低得多。那些表现最差的人，不会有这种自我检查能力。而他们恰恰会成为借助 Agent 产出“10 倍代码”的人。你觉得这会让一个组织的平均产出变成什么样？又会让整个世界的平均产出变成什么样？

Agent 最终会生产出比以往更多的代码、更多的应用、更多的功能。这会是一个垃圾代码成吨涌出的黄金时代，也会是高质量精品的黑暗时代。

在更深层的技术问题上，Hotz 已经转向了另一个阵营。他说：“虽然我并不完全认同他们的所有观点，但在 LLM 这个问题上，我现在站到了 LeCun / Marcus 阵营。我不认为这类模型能够真正实现编程，我认为过程很重要。”

在他看来，真正的编程 Agent 需要世界模型，而不是现在这种基于 RLVR 的方法。对于后者，他说得很直白：那就是“把失败的测试注释掉，然后告诉你所有测试都通过了”的那套东西。

[图片] https://mmbiz.qpic.cn/mmbiz_jpg/hLLZnAbUwNgu6Ik1YxyOLicXqtiargCtRFmw0cdWlDx0y1PF2iar9HP07CBwiawL3GwAaficvgfBpaJmeXnlXN3lyEjiac2lcZQRJHNAjeYVjV3tE/640?from=appmsg

他认为，更深的问题在于我们怎么看待一个产物。过去，人们看到一段代码或一个软件，会默认它背后有一个类似人类的创作过程。但这个默认前提现在不成立了。“东西可能以过去不可能出现的方式坏掉，而语法、文法这些过去用来判断底层质量的信号，已经没用了。”Agent 写出来的代码，不是按人类写代码的方式产生的。这种差别从统计上看也许很细，但当你试图像对待人写的代码一样去理解它、继续在上面开发时，它就会变得很明显。

Hotz 还警告那些正在用 AI Agent 做严肃软件的人：“这个时代真正的故事，将是谁能在自己的 AI 狂热中避免伤到自己。”

2 制造 AI 编程热潮的人，开始担心它失控

Hotz 不是唯一一个发出这种声音的人。

Mario Zechner 和 Armin Ronacher，亲手打造了爆火 OpenClaw AI Agent 核心组件的两位工程师，如今发出警告：那些号称能取代程序员的 AI，正在把大量糟糕的、甚至危险的代码推向世界。他们把这种现象叫做“vibe slop”——程序员不再认真设计和测试系统，而是让 AI 快速拼出一套东西，最后产出一堆经不起时间考验的软件。

“基础设施正在崩溃，软件比以前漏洞百出，”OpenClaw 内部框架 Pi 的创建者 Zechner 说。“我们还能再玩几个月甚至几年，但它最终会让我们付出代价。”

Zechner 和 Ronacher 不是 AI 黑。他们自己写代码时也用 AI 处理枯燥工作，亲手打造的工具 Pi 有几百万人使用。正因为他们身处其中，这个警告才不是外行人的空喊。他们担心的是：许多公司正在用短期生产率换取长期麻烦：初级人才管道干涸、bug 增多、安全漏洞、技术债不断累积。

Alphabet CEO Pichai 说 Google 75%的新代码由 AI 生成。Meta 的 Zuckerberg 预测 2026 年前 AI 将编写和审查其 AI 团队的大部分代码。但 Zechner 认为，这些说法恰恰说明很多人没搞清楚 AI Agent 能做什么、不能做什么。

AI 编程工具擅长生成新代码，但不擅长评估和升级既有软件——尤其是成熟公司内部那些庞大、复杂的遗留系统。用 vibe coding 冲起来的创业公司可以快速起步，但 Zechner 说，一旦系统长到一定规模，它们就会撞上和大公司同样的墙：AI Agent 的用处是有限的。

拿 Anthropic 的 Claude Code 来说。Zechner 的评价毫不留情：“Claude Code 是我这辈子用过的最破碎的软件之一。”这些问题源于开发者用 AI 来构建它。而 Anthropic 产品负责人 Catherine Wu 进行了辩解但也承认：“最终责任仍然在人类身上。”

计算机科学家 Timothy B. Lee 指出，Anthropic 拥有全球最优秀的一批 AI 工程师，所以这种高度依赖 AI 的方法对他们可能行得通，但不一定适用于这家公司的所有客户。很多公司在处理内部软件系统时，依赖的是员工程序员多年积累下来的隐性知识，而这些知识并不会出现在 AI Agent 的训练数据中。

“这些模型很容易走错方向，而必须有人注意到这一点。”

Zechner 认为，一场清算正在到来。

他认为，大公司很快就会意识到，它们对 AI 生成代码的过度强调正在推高成本，并导致软件质量下降。他认为，许多依赖 vibe coding 的小型创业公司会倒闭。他还认为，像 GitHub 这样托管有用软件工具的云端代码仓库，会继续被 AI 生成的编程垃圾填满。

3 AI 的回报，目前还没跟上它的消耗

如果说 Hotz 和 Zechner 担心的是代码质量，那 Uber 高管担心的就是另一件事了：钱。

Uber 首席运营官 Andrew Macdonald 在3天前的一期访谈里说，在公司内部，AI 成本正变得越来越难被说服为“合理投入”。

他提到，Uber CTO Praveen Neppalli Naga 今年 4 月接受 The Information 采访时曾说，Uber 已经提前花光了 2026 年的 Claude Code 预算。这句话后来在网上传开。

Macdonald 说，这句话在 Uber 内部炸开了锅，大家开始认真讨论 AI token 消耗的问题，以及这种消耗带来的取舍，比如是否会影响人员编制。他说，在和 Uber 多位高级工程负责人沟通之后，他意识到，token 用得更多，并不意味着公司就能同比例地交付更多真正有用的消费者功能。

“这个关联现在还不存在，” Macdonald 说。“很难把其中某一个指标和‘好，现在我们实际产出了 25% 更多有用的消费者功能’直接对应起来。”

当这条因果线画不出来的时候，AI 的成本就很难被合理化。Uber 的 CEO 本月早些时候已经表示，为了对冲 AI 投资，公司正在放缓招聘。

Macdonald 还补了一句：如果你只是一个坐在那里想各种有趣用例的用户，又不用自己掏钱，AI 看起来确实是免费的。但账单最终是由公司来买单的。

有些公司已经开始往回调。比如 Duolingo，此前曾计划把 AI 使用情况纳入绩效考核，但员工很快提出疑问：到底是为了把事情做得更好而使用 AI，还是为了证明自己“用了 AI”而使用 AI？随后，公司撤回了这一决定。Duolingo CEO 后来也承认：“当时给人的感觉是，我们不是在要求大家对实际结果负责，而是在推动某种工具的使用；但在一些情况下，它其实并不适用。”

今年 4 月，英伟达应用深度学习副总裁 Bryan Catanzaro 提到，AI 并没有降低用人成本——实际上，目前人工智能的成本比公司现有的人力成本更高。至少在他的团队里，“计算成本远远超过员工成本。”

4 结语

所以，真正的问题不是“人写烂代码，AI 也写烂代码，那有什么区别”。

区别在于，过去再差的代码，至少写它的人心里有一个粗糙的心智模型：他知道自己为什么这么写。但现在，大量 AI 生成的代码被快速提交、合并、发布，很多人并没有真正理解它，只是看到它通过了测试——而测试本身可能就是残缺的。

坏代码从来不新鲜。新鲜的是，坏想法现在可以以更快的速度变成 commit，而理解、审查和责任却没有同步变快。

有人在 Twitter 上说：“再等六个月，持续学习和记忆系统会解决这些问题。”也许吧。但过去六个月的进展，并没有让 Hotz 和 Zechner 变得更乐观。

参考链接：

https://geohot.github.io//blog/jekyll/update/2026/05/24/the-eternal-sloptember.html

https://archive.ph/iyszw

https://www.businessinsider.com/uber-coo-andrew-macdonald-ai-token-spending-harder-justify-2026-5

https://www.youtube.com/watch?v=y_mQ6xLcKyc&t=1776s

声明：本文为 InfoQ 整理，不代表平台观点，未经许可禁止转载。

[图片] https://mmbiz.qpic.cn/mmbiz_png/hLLZnAbUwNhLSIh1ZduDjRDsU8OGQRmwBscMG7ZHucztXRKWAnNP0CUNKw8iaicn4SeFxlwNS07wa4gf3OQKrj0ic3XMmkaZN9GdIOALYlPC70/640?wx_fmt=png&from=appmsg

今日好文推荐

中国首次提出半导体演进新原则：华为“韬定律”5 年内冲刺等效1.4nm制程，麒麟、昇腾将先后落地量产

微软将弃用Claude：太贵了还是薅明白了？

C++之父开撕AI Coding：资深开发者宁愿退休也不愿伺候AI生成的代码

别再骂 Claude 限速了，Boris 亲口承认：最挑剔的用户，反而最离不开我们

会议推荐

但企业级 Agent 落地，绕不开 4 个真实的工程问题。如何在 Agent 安全性和可用性之间找到平衡点？Agent 需要什么样的记忆系统才能真正理解上下文？如何通过算法压榨实现智力增量与成本控制的极致平衡？多 Agent 协作，如何做到可观测、可治理、可控制？6 月 26-27 日，AICon 全球人工智能开发与应用大会·上海站国内头部公司的 Agent 实践，一次说透。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/hLLZnAbUwNhqIeQXv7PbV71q0nxmPEKfOaDiaicxaFsjDYINZGQwq3paOGhibe0DqKy7g8avhl3dBiaQ0VbjKmhicdxibgTonrxm1I3UFtlibufGmw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10
