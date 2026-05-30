---
source: 36氪
publish_time: "2026-05-22 17:30"
url: "https://mp.weixin.qq.com/s/HjvtKaw_jTaNdsCLyfMJ4w"
category: "管理"
kind: wechat
---

# 拆解Anthropic：最好的AI公司，可能也是一种组织发明

- 来源：36氪
- 发布时间：2026-05-22 17:30
- 原文链接：https://mp.weixin.qq.com/s/HjvtKaw_jTaNdsCLyfMJ4w
- 内容分类：管理
- 文章摘要：在AI时代，赢不一定靠更大的野心、更多的探索和更强的人才。

## 框架判断

- 阅读深度：Read Normally+。值得保存并正常阅读；如果后续研究 AI-native 组织能力，可二次深读。
- 框架定位：L2.5 人与组织适应为主，兼有 L1 技术路线、L2 商业扩散和决策层。
- 对应活问题：AI-native 组织到底长什么样？什么样的团队更适合做 agent / coding / 数据 / eval 这种脏活累活？
- 有用之处：把 Anthropic 当作组织样本，强调 focus = 判断力 + 压强；AI 竞争中的组织优势不只是明星人才，而是低 ego、高信任、使命一致、信息透明和愿意做细活的执行系统。
- 框架更新：评估本地 AI 能力建设时，不只看“用了多少 AI 工具”，还要看是否围绕关键变量形成资源压强、数据闭环、持续 eval 和跨团队 one team 协作。
- 噪音风险：文章有明显 Anthropic 叙事美化倾向；ARR、估值、人才流动和 OpenAI 内部对比多为二手信息，应作为组织分析材料而非事实底稿。
- 后续读法：重点看 focus、文化制度化、业务性质决定组织文化、smart people do dirty work 这几段；OpenAI/Anthropic 八卦和估值数字可低权重处理。

## 正文

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/o02wSnKAPeFLHGe5bldWZ6MstEMZH4xEafGMIorwtsIdcbY4tN2iarFt7bLYXwyVp8SOGfKa1baiaWQDOpcS716Y2iaKdcP13VGNjsSBsxSyh4/640?wx_fmt=png&from=appmsg

[图片] https://mmbiz.qpic.cn/mmbiz_png/QicyPhNHD5vagBvpJSWBnNYW2D0Lereibp3GVwr7pAWURUC5MH7xdLsTMSsaiayEzicByDcKTBHnpsGXGoTVQQ5Iyw/640?wx_fmt=png&from=appmsg

在AI时代，赢不一定靠

更大的野心、更多的探索和更强的人才。

[图片] https://mmbiz.qpic.cn/mmbiz_png/QDFNHs0vUhrvC75JRXlG0rM2iat53EoZMsodUxkMSYWXNSIFUEeuo2I89A9ibZcCic1oNlHEWLAxeWpFZgeic0wdtg/640?wx_fmt=png&from=appmsg

[图片] https://mmbiz.qpic.cn/mmbiz_png/QicyPhNHD5vagBvpJSWBnNYW2D0LereibplkrJOvk6R1Efiaq0NlWibAtLj0DDlMWGggbQ9KdrLibUvZbz91W4FNd7w/640?wx_fmt=png&from=appmsg

文｜Celia

编辑｜Siqi，penny

来源｜海外独角兽（ID：unicornobserver）

封面来源｜视觉中国

过去一年，Anthropic可能是整个AI行业里最值得研究的一家公司。

今年开年，它创造了人类商业史上最快的爆发性增长：ARR从9B增长到45B，如果算力供应跟得上，大概率年底ARR到100B，明年到200-300B，直接和Meta的体量拉齐。

在secondary market上，它现在的估值已经摸到1万亿美金，反超了OpenAI。

我们花了不少时间研究Anthropic是怎么后来居上的。

最后落下来，要理解这家公司，核心是理解两个点：

一个是战略判断，一个是组织文化。

大家对此应该已经有了很多片段式的了解，但并没有一个完整的picture，所以这篇文章试图做一个更详尽的梳理和还原。

希望能从战略和组织这两个角度解释一些外界好奇的问题，比如：

为什么Anthropic能在2021年就意识到coding可能是最重要的方向？

Dario和Sam的性格差异，如何塑造了两家公司完全不同的战略路径？

为什么Anthropic的人才流失率这么低？

为什么几乎每一个Anthropic的人，都在称赞它的文化？在公司快速扩张的过程中，这种文化是如何维持的？

[图片] https://mmbiz.qpic.cn/mmbiz_png/QicyPhNHD5vYs92nHCpdbueQF7gdhICh6n4bg74ZZBRll6JriaDqWuAUKCORW2pdPf2yVUIWtCJ5r1TYvaDtK5CA/640?wx_fmt=png&from=appmsg

Focus的重要性被低估了

首先，从战略上来说，OpenAI一直更像一家什么都想要的公司。

在模型能力上，math、science、coding、reasoning、多模态、架构创新等，OpenAI都在发力。

在产品上，Codex、浏览器、机器人、企业平台、智能硬件、芯片和数据中心等等也都在同时推进，据说OpenAI内部的项目数一度高达约300个。

而Anthropic完全相反，他们是御三家里唯一很早就放弃多模态的，且从来没讲过架构创新，没强调过reasoning model、RL、continual learning等概念，只做好语言模型的scaling，只重点做coding一个方向，先把最关键的能力打穿。

关于为什么coding如此重要，现在市场也都清楚了，核心是三点：

1、Coding是通往一切的道路。数字世界的绝大多数任务都可以通过Code来表达。

2、Coding是最适合模型学习的能力。结果可验证性强、Feedback loop短，用户数据能更大程度上反哺模型训练。

3、Coding是AGI研发的核心加速器。现在头部AI labs已经进入了这种加速循环，今年模型一个季度的进步幅度，比过去一年更快。

最后的结果证实，Coding确实是最重要的方向，孤篇压全唐。

而OpenAI直到3月份才惊醒，砍掉了Sora等支线业务，把Coding提到公司第一优先级。

Anthropic是怎么选准coding的？

我们一直好奇的是：Anthropic为什么一开始就能选准coding？

追溯下来发现，一半是远见，一半是运气。

Anthropic早期融资一度很不顺利。没有那么多钱，就必须用更高效的方式往AGI迈进。

它需要先讲一个垂直场景的故事，证明自己可以形成商业闭环。于是他们当时认真研究过，如果只能选一个方向，coding可能是最好的选择：先训练更好的coding model→提供给客户使用→获得客户在真实工程环境里的使用数据→反哺模型训练。这有可能形成一个飞轮。

Anthropic增长负责人曾经提到，他看过一份公司联创写的内部文件，内容是，为什么我们应该focus在coding这个方向。重点是，这份文件的日期是2021年，这远远早于任何人知道这个方向实际的市场机会是什么。

但后来的情况是，融资变顺了，公司有了更多资源，coding这条线没有再被提起，他们还是先去做一个更通用的模型底座。

转折发生在ChatGPT爆火之后。Anthropic意识到，C端已经被OpenAI抢先，于是它颇为遗憾地（但事后看是异常幸运地）转移了战场，把重心转向toB。

这个战略转向整体还是谨慎和实证主义的，不是一次毅然决然的豪赌。

训练Claude 3时，Anthropic开始有意识地强化coding能力，并且在Sonnet3.5上拿到了很好的市场反馈。

之后就是一边加码，一边求证，内部逐渐坚定了对coding潜力的判断，一个是商业价值上，一个是加速研究上。于是团队开始专注地沿着这条路往前走，这中间不仅是彻底放弃了C端，甚至连多模态都没有分散精力来做。

另外除了市场方向上的聚焦，还值得一提的是技术路线上的定力。

过去两年，外界反复有明星researcher说scaling laws撞墙了，pretraining的边际收益已经见顶。就我们和各家researcher的交流感受，Anthropic一直是所有labs里最相信scaling laws的，也是把pretraining和数据做得最扎实的，没有在新范式上分散精力。

事后看这也是对的。Claude的能力跃迁，很大一部分就来自pretraining的扎实投入。

创始人的性格

但这又引发了我们的一个好奇：为什么Anthropic总能在几个关键方向上做出果决的取舍，并保持定力？

首先自然是资源的限制，Anthropic的历史融资额大概只有OpenAI的1/3，但再往深处看，这两家的战略差异也和创始人的性格和出身紧密相关。

Anthropic有4位联创都是当年scaling laws论文的核心作者，Dario本身就是GPT-3最核心的research lead，在这之前也已经在AI领域做了十年，对AI的技术进步有一手的体感，更敢于下判断。

此外，Dario是一个完全不fomo的人，甚至被人形容有点自恋和固执，很少被市场共识牵着走。

他在24年，Anthropic还远没有取得爆发性增长时就说过一段话，至今我觉得是理解这家公司很重要的一点，大意是：

过去十年，我学到的最深的一课，就是市场上总会存在一种所谓的共识，但当看过好几次共识在一夜之间翻盘，我就开始专注于自己的bet。

我也不知道我们一定是对的，但说实话，就算只有50%的时间是对的，也已经很有价值了，毕竟你提供了别人没有的东西。

这和Sam Altman很不一样，从我们和一些接近Sam的人交流来看：

1、Sam是硅谷公认最有野心的founder之一，一开始就什么都想要。再加上他过去在YC做投资，对“多点播种、并行下注”这套方法非常熟悉，所以OpenAI长出了无数支线。

2、Sam并非技术出身，对技术方向的判断不如Anthropic，所以更多依靠团队bottom up往前推。Sam发挥自己更擅长的搞资源能力，给一个个团队送去弹药。

3、VC背景让Sam格外偏好突破式的fancy ideas。所以OpenAI文化里非常value 0 到1的范式创新，但没有同样重视1到10的持续打磨。Sora、Atlas浏览器、Voice Mode等等很多产品线都没有延续性，发完就没人管了。

4、Sam和Mark Chen（Chief Research Officer）的性格都是只say yes，不会say no。支线任务，团队只要努力推，上面就还是会给资源。

当OpenAI的兵力被各种支线项目不断摊薄，Anthropic就可以通过田忌赛马在最关键的战场上形成优势。

战略的精彩之处在于“略”

Anthropic在战略上的聚焦给了我们一个启发，focus的重要性被低估了。

我回想起去年听过的一期播客，嘉宾是Founders播客主播David Senra。过去8年，他几乎只做一件事：每周研究一位伟大的创业者。

当被问道，如果把他读过的超过400本创始人传记，提炼的所有创业经验，最后只压缩成一个东西，那会是什么？

他回答：Focus。

伟大的企业家往往不是全面的优等生，而是极端的偏执狂。他们会识别出对自己最重要的那一两个变量，比如Costco的价格、Apple的设计体验、字节的推荐算法&数据飞轮，然后不惜一切代价将其推向极致，甚至达到令竞争对手感到荒谬的程度。

这里要明确一下的是，很多人都以为自己很专注，但他们并不真正理解专注的含义和代价。

所谓focus，本质要拆分为两个层面：

一是判断力，知道什么是最关键的，并且敢于牺牲其它一切。

二是压强，能投入压倒性的资源把关键要素打穿。

前者是认知问题，后者是意志问题，缺一不可。

比如Google创立的时候，当时整个互联网行业的共识是——未来属于“门户”。Yahoo等搜索巨头都在把首页堆得越来越满，新闻、天气、购物、游戏、星座...每一个feature都被当成“提高广告价值”的杠杆。

但Google认为，信息会越来越多，用户需要的不是一个更大的门户，而是立刻找到最相关的答案。

所以，当别人想让用户停留更久时，Google想让用户更快离开。当时Google的首页异常干净，除了一个搜索框什么都没有。

商业模式上也是如此，Yahoo有几十种变现方式。而谷歌把所有精力都压在“搜索关键词竞价”这一个机制上，做了将近十年才开始认真做第二条业务线。

至今，Google的十大信条其中一个就是"It's best to do one thing really， really well"。

战略的核心不是想清楚你要选择什么，而是想清楚你要放弃什么。我想大部分人say no的次数都是不够的。

[图片] https://mmbiz.qpic.cn/mmbiz_png/QicyPhNHD5vYs92nHCpdbueQF7gdhICh6MebCYnvZdvTDPbOUA7ibvzc0o3YBuC9FURHiaKksE5qUFLohPK7nDqRQ/640?wx_fmt=png&from=appmsg

文化是最大的Secret Sauce

Anthropic最特别的地方，可能还不是战略，而是组织文化。

过去半年，在激烈的AI人才争夺战里，Anthropic的人才流失率远远少于其它AI labs。

下面两张图是对21年-23年的人才流动数据总结。

第一张图统计了各个AI labs之间跳槽的比例，我们可以看到：

每10.6个从DeepMind去Anthropic的人，才有1个反向去DeepMind。

每8.2个从OpenAI去Anthropic的人，才有1个反向去OpenAI。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/o02wSnKAPeFXtKmnPrsYCqav5ZSh2yQiczPEZ4bn766ewXxPlbPoFQrImaDn8KU9DJ9RWCo45pl1TaicsRictrTviaKMJxzf8ms0UfI2F35zy4Y/640?wx_fmt=png&from=appmsg

第二张图统计的是一个员工在入职2年后还留在公司的比例。

Anthropic的人才留存率是80%，这是当时头部AI labs里最高的，比DeepMind的78%还要高一点。

Anthropic作为一家更年轻、高速变化的公司，居然能做到比老牌DeepMind还高的retention，这是不容易的。

相比之下，OpenAI只有67%。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/o02wSnKAPeFH3v4H9qZBibrA1H1FYF39icJnOk4DHKsWME7mewhEdVC2lApwOFCHDjlIuuiaj3g6wXicEYaHCkscoKaxfTDCUhJH78QztZFib1NE/640?wx_fmt=png&from=appmsg

值得指出的是，这组数据还是在OpenAI如日中天，而Anthropic完全没有崭露头角之前所做的统计。

如果看近两年的新闻，Anthropic的人才吸引力和稳定性会更加明显。

比如最近Twitter很火的一个帖子，多家明星公司CTO甘愿跳去Anthropic成为一个普通技术员工（即MTS，member of technial staff）：

[图片] https://mmbiz.qpic.cn/mmbiz_png/o02wSnKAPeGic3Jn4ee5OD4CiaDOpGBcoOicRbo1VeFFwibDerMMujeTqc8hlwzic90FN39FiafMhuGRGmHbUic1Jzzuqg2ruJzjkkPa8StBudnRDM/640?wx_fmt=png&from=appmsg

这其中最大的原因，往往被归结于Anthropic的组织文化。

如果去看Anthropic成员出来录的播客，几乎每一个人都会提到Anthropic的文化，一些人甚至把这种教派般的文化视为Anthropic最大的secret sauce。

“我真的觉得文化是Anthropic的秘密武器，是我们最有防御力，其它家无法复刻的东西。这不是自然而然的，领导层在这上面投入了非常多。”

——Amol Avasare，Anthropic增长负责人

如果不是单独带着这个问题意识看的话，不太会注意到这一点，因为听人聊到文化或价值观，总觉得很虚，默认它是一句口号，但如果把所有一手信息和公开采访叠在一起看，就让我们很受震动。

Anthropic的三个特质

如果具体拆解一下，Anthropic和其它AI labs很不一样的三个特质是：

1.Mission-oriented

Anthropic的使命是“确保世界能够安全地度过transformative AI的转变”，也就是一切以安全为重。

很多公司都会说自己的是使命驱动，但Anthropic对此的认真程度，到了一种有点接近宗教性的程度。

这是一家带着强烈道德自我想象的frontier lab：它真心相信AGI可以拯救世界，也真心相信AGI可能摧毁世界，而它试图带领大家把这两件事之间那条很窄的钢丝走过去。

Claude Code负责人Boris Cherny曾说：“在Anthropic，随便在走廊里找个人问‘你为什么在这’，答案都会是safety”。

他和产品经理Cat Wu去年曾经双双离开Anthropic跳去了Cursor，没等两周后就跳了回来，因为他们发现自己深深怀念Anthropic内部的文化氛围。那种所有人纯粹地，为了一个更大的使命奋斗的感觉。

有人在加入Anthropic之前对这些半信半疑，进去之后发现，“Fuck，里面的氛围比外面讲的还要认真”。

这里甚至会有早期员工在全员会上说——如果Anthropic最终实现了自己的使命，但公司本身失败了，这依然是一个好的结果。

这句话解释了Anthropic的很多事情。

在大多数企业的逻辑里，商业成功永远是第一位的，使命只是用来装点门面。但Anthropic最特别的地方在于，内部确实存在一批人，把使命排在了公司存亡的前面。

如果检视Anthropic实际做的事情，也是知行合一的，比如他们非盈利信托掌权的治理结构设计、在可解释性上做的研究、在安全上的种种投入，包括前段时间因为价值观冲突而甘愿牺牲美国国防部2亿美金订单等等，这部分就不一一赘述。

2.High trust, low ego

当我们和其它前沿labs交流时，总能听到很多内部政治和山头问题。只有Anthropic没有。相反，大家非常团结，愿意为他人做嫁衣。

这里最神奇的地方在于，FrontierAI是一个太容易长出明星文化和资源斗争的地方。AI researcher几乎是这个世界上最聪明，最high ego的一群人，他们天然的追求就是要提出一个不一样的解法，另立山头，扬名立万，但资源又非常有限，所以部门冲突总会发生。

从谷歌跳来Anthropic的Daniel Freeman说，其它模型公司内部像一个个各管各的、暗暗较劲的诸侯国，但这种感觉他“在Anthropic从来没有过”。

Stripe前CTO Rahul Patil去年秋天加入Anthropic后，也提到自己最受震动的就是这里的文化。很难想象，一群这么聪明的人，居然还能同时这么谦逊。

他举了一个标准：如果公司明天告诉你，最适合你的位置不是继续做高管，而是去做IC（个人贡献者），因为那才是你对mission最大的贡献，你愿不愿意？他认为Anthropic 100%的人都会做，没有ego。

3.一种很强的人文底色

《纽约客》的作者曾在Anthropic内部做过几个月的深度跟访，然后对这里的人留下了两个很有意思的形容：

Bookish misfits

A disproportionate number of Anthropic employees seem to be the children of novelists or poets.

也就是说，这里的人不太像典型的硅谷精英，也不太像传统印象里的技术理工男，而是有点书卷气、有点nerd、有点理想主义。很多人给人的感觉，像是从作家和诗人的家庭里成长起来的。

这某种程度上从Claude模型命名里就能看出来：Haiku、Sonnet、Opus，分别对应着凝练的俳句、莎士比亚的十四行诗和古典语境下的大部头作品。

作为对比，OpenAI的GPT-4/4o/o1是工程编号命名，Google的Gemini Ultra/Pro/Flash是经典的产品线命名。多少能说明一些问题。

Claude Code负责人Boris也曾在播客里讲过一个有趣的细节：

他刚来Anthropic的第一顿午饭，随口提到一本非常冷门的书，作者是硬科幻作家Greg Egan。

那本书小众到什么程度呢？他之前没遇到过任何一个读过它的人。

他在饭桌上顺口讲了书里的一个梗，结果桌上的人竟然全接上了。

这件事让他大为震惊，也让他觉得自己真是来对了地方。

喜欢科幻的书呆子们往往有着某种宏大的人文关怀和历史责任感，也对蝴蝶效应有着更好的推理能力。

这种基于阅读趣味的共识，让他更加放心，这里可能是最好的推动AI边界的地方。

文化如何被制度化

接下来的问题是，这种纯粹的、近乎教派式的文化，是怎么维持下来的？

毕竟，Anthropic已经不是一家小的AI实验室了，这是一个有着3000人的大型公司，而且是在以史上最快的速度扩张的同时尽可能地维护了自己的文化浓度。

对此，Dario直接说，他大概会花1/3到40%的时间确保Anthropic的文化是好的。

即使在技术上、产品上、融资上、政商关系上都有无数事情要做。但他认为，自己杠杆更高的工作，是让Anthropic成为一个有高度凝聚力的，顶级人才喜欢在这里工作的地方。

落实到具体的实践上，有这样几点：

1.特殊的招聘标准

Anthropic招人，和很多AI labs不是一个思路。

一方面，在人才偏好上，和大多数公司争抢big names不同，Anthropic更愿意招underdog。比起外在标签，他们更看重有没有direct evidence of ability，例如，“你有没有做过独立研究，写过真正有洞见的blog，对开源社区有没有实质性贡献”等等。

另一方面，Anthropic对于非常严格的文化筛选。他们面试时专门有一轮Cultural interview，一个小时问15-20个scenario questions。

根据网上流传出的面试题，重点考察三点：

(1)你是不是真的会把safety mission放在前面。

最典型的一道筛选题就是：如果Anthropic因为无法保证安全，最终决定不发布模型，你愿意接受自己的股票归零吗？

(2)你是不是一个nice、ego小的人。

包括善良、同理心、people skills、能不能承认自己的无知和错误。

(3)你能不能处理复杂性。

Anthropic内部处理的很多问题都非常复杂多变，他们很看重一个人有没有系统思维，能不能深入推理事物的second-order effects，去想一个决定会怎样影响别的环节。

他们在招聘上花了大量时间做“反向筛选”，也为此确确实实放弃了很多最顶尖的10x developers。Stripe前CTO Rahul Patil就提到，他在加入Anthropic前，和当时的Anthropic CTO聊了很久。对方不但没有劝说他过来，反而专门花了两三周时间反复和他讨论你为什么不该加入Anthropic，善意地劝阻他，除非你在文化和mission上真正aligned，否则来了也不值得。

所以Anthropic的招聘逻辑，从来不是尽可能多地把最强的人招进来，而是尽可能早地把不适合的人筛出去。“我们非常擅长把为钱和名来的人剔走”。

与之对比，OpenAI在公司变大后，已经不做专门的文化面试了，据说还是造成了一些管理问题。

这一点在Meta去年挖人的那一轮里体现得很明显。面对Meta开出的天价package，OpenAI的反应更像是市场惯例：counter offer、发retention bonus、取消新员工的vesting cliff，让股票更快归属。Anthropic的反应则很Anthropic。他们对员工说，你来这里首先是为了mission，不是为了在外部竞价里不断抬高自己的价格。我们不会因为Mark Zuckerberg碰巧点中了你，就给你开出比身边同样优秀的同事高十倍的薪水，那不公平，要走就走。

这件事最后的结果也很说明问题。OpenAI据说走了几十个人，而Anthropic只走了2个，且这两个人本就是在Meta工作过6年和11年的老员工。

2.Context sharing的文化

Anthropic内部有着非常高的信息透明度。

首先是Dario自己会主动、高频、反复地做意义供给。他经常开全员会给公司所有人做分享，频率高达两周一次，名字就叫Dario Vision Quest（连Dario自己都吐槽，这名字的布道属性过于明显，听起来像是去山里吸了点什么回来顿悟）。

他会站到全公司面前讲一个小时，通常配一份三四页的文档，内容从公司方向、产品策略，到行业变化，什么都会讲，然后直接现场回答问题。

不少内部员工说他讲话特别直接、坦诚，“Dario是我见过最直来直去的人，他说话不是算计过的，而是真怎么想就怎么说。”

除了全员会，他平时还会在自己的Slack channel里频繁写很多东西，完全不加修饰地记录自己的碎碎念：公司最近发生了什么，他在担心什么，又怎么看大家关心的问题。

这样的文化会让公司里的每个人知道，决策是怎么被做出来的，哪些事该被放在最优先的位置。由此，在一个复杂多变的形势里，每个个体才能做出相对一致的分布式决策。

同时，这种透明不是单向灌输，而是可以被挑战的。有人在All Hands听完Dario的分享，觉得不认同，直接跑到Dario的notebook channel里公开说“我不同意你这个判断”，然后当场展开一场辩论。公开挑战领导层是被鼓励的。

更进一步的是，这套写作文化并不只属于Dario，而是一种全员参与的思考机制。

Anthropic里很多人都有自己的notebook channel，有点像个人版 Twitter feed，随时记录自己在想什么、做什么、有什么进展。别人可以订阅、围观，也可以加入讨论。

很多员工评价过很喜欢公司的写作文化，Slack就是一个巨大的宝库，很多事情都在上面展开。

所以，Anthropic看起来在公司内培育了一层很好的alignment土壤，每个人的项目、观点、思路，都足够透明，也足够流动，甚至曾有人感叹过财务数据都是透明的。

（但与之相反的是，技术上的保密做得很严，听说有些组之间甚至会刻意隔离，不太能一起吃饭。

结果就是，有其它家的researcher会遗憾感慨，这里所有关键know-how分散在不同人的脑中，不可能靠挖走几个人，就拼出一个全貌。)

3.7个创始人同股同权，founding structure本身就是文化机制

Anthropic的founding structure有一个很反商业常识的设计：它有7个创始人，而且Dario当时还毅然决然要给每个人同样的股权，而不是自己多拿一点。

当时，所有人都劝他这会是一场灾难，不然主导权模糊、激励错位，公司很容易因为内斗散掉。

但Dario认为，公司不是围着某一个founder转，而是围着mission转，而同股同权是这种理念最不可伪造的证据。

他们几个早已经多年共事，对彼此高度信任，同股同权本质上不是一种治理权的设计，而是一种对commitment的证明，一种文化扩散机制。

7个cofounder，就像7个文化复制节点，能分别在不同条线上，把价值观投射给更广的人群。这样一来，公司哪怕扩张，也不容易把最初的文化冲散。

[图片] https://mmbiz.qpic.cn/mmbiz_png/o02wSnKAPeETxSGaoYlyQZic4l53R6NaZB4fH4kMGWDzOlr4Exeek5JQC3YzTey46ZlAlUwn0acJ9sWm0THt7zRCblPL1jUibm8zWDtBNT868/640?wx_fmt=png&from=appmsg

对比来看，OpenAI的高管层其实一直非常动荡，11个founding team接连离开，现在只剩Sam Altman、Greg Brockman和Wojciech Zaremba还在。

而新换上的高管层就更不稳定：从26年开年到现在，产品一号位Fidji请假，市场一号位因健康原因离职，传播一号位出局，运营一号位被调岗，财务一号位也被边缘化...

4.极其强调one team，避免长出山头

Anthropic CTO曾经在播客里说，AI labs整体相比传统公司非常bottom-up，它是一种倒金字塔的组织方式，权力和创意自下往上流动。

这里最重要的工作都发生在一线。因为一线的人最接近AI的涌现行为。他们每天在跑实验，对模型能做什么有最直观的理解。绝大多数产品创意是由一线的人推出来的，而不是由高管roadmap驱动的。

但这也有一个问题，当判断权下放之后，每个团队都很容易守着自己的问题意识和价值函数，长成一个个彼此拉扯的山头。

Anthropic的特殊之处在于，它很早就意识到：既然判断必须分散，就更要主动制造团结。Dario不希望safety只会说安全最重要，product只会说产品最重要，然后把所有冲突一路推给高层拍板。他一个核心的管理理念，就是把trade-off分散给每个个人，让每个人都拥有一点创始人的视角，大家只是在各自岗位上参与同一场巨大的trade-offprocessing。

所以他们极其强调one team，也会通过各种制度设计去弱化职责之间的界限，比如高管以下没有title的区分，统一叫做member of technical staff，刻意弱化“研究员vs工程师”、“高级vs低级”、“架构师vs实现者”这种身份定义。

这个和OpenAI对比非常鲜明，OpenAI一直有着更强的研究员文化，内部存在着一个明显的“鄙视链”：Researcher>Research Engineer>software engineer。

所以产品经常被research压一头，拿不到太多话语权。当有冲突的时候，Research也不愿意配合产品。

在产品创新上，OpenAI有个很强的特征是researcher-driven：往往是研究团队出了一个新成果，产品团队才临时收到邮件，开始拿着锤子找钉子。

而在Anthropic，产品与模型团队咬合得更紧密，产品更能反向去影响和定义模型能力。

这其实也是OpenAI产品力不如Anthropic的一个原因。

文化的两个起源

接下来的一个问题是，为什么Anthropic会形成这种独特的组织文化？

或许可以从两个方面来看：

一、业务本身的要求

我记得两年前听一个头部大厂HR负责人的分享，印象很深，让我第一次深入思考组织文化到底意味着什么。

组织文化的本质是：员工的行为模式能够帮助公司走向成功的一种关键要素。

所以组织文化的第一性原理其实是，业务性质决定组织文化。

举个例子，字节和华为都是组织能力很强的两家公司，但如果把两家的组织体系交换一下，要不了多久，两家都要倒闭。因为它们处在同一个光谱的两个极端：字节讲的是“敢为人先”，华为讲的是“敢为人后”。一个更value创新，另一个更value效率。

这跟价值判断无关，而是业务性质决定的。同样是做一款新产品，华为做的是基站、芯片这类东西，一旦出了问题，召回成本可能吞掉一整年的利润。而字节不一样，它是典型的短周期、短链条业务，一个星期能跑出几十个版本，错了就改，改了再发。所以字节可以鼓励创新，可以选择"Context， not Control"，华为不行。对华为来说，过早创新反而可能是一种负担，华为真正擅长的是，当市场出现PMF之后，通过自己的组织能力和资源，一步步超越，直至碾压对手。

那再说回Anthropic。

在AI竞争中，一个核心moat是能让“smart people do dirty work”。尤其是Coding和Agentic这个方向，表面上看是模型能力竞争，往深了看，其实是工程能力竞争。它不是那种靠几个天才灵光一闪就能解决的问题，而是大量脏、碎、细的系统工程。

其中最核心的壁垒是数据。

过往的Chat数据只是简单的文本数据，但Coding和Agentic数据更复杂，它不只是对话记录，还包括任务本身、环境搭建、执行轨迹，以及最后整套evaluation和verification体系。

这其中全是脏活累活，做好了很关键，但它不像发一篇paper、一个新产品那样，可以变成个人的高光时刻。

据我们跟一些researcher交流拿到的反馈，OpenAI今天最核心的一个问题是它很难组织几百个最强的人踏踏实实搞数据、干脏活。

OpenAI招的都是鄙视链最顶尖的人才，背景好、心气高，大家天然更想做自己的bet，想从0到1，至于收拾烂摊子、补数据，少有人愿意接。

OpenAI过往是这么成功的，它曾经确实靠一些核心的范式突破取得了巨大领先优势，但就像姚顺宇在最近的访谈中说的：“个人英雄主义的时代已经过去了”，“AI这个事不太需要脑子……最重要的特质就是靠谱，做事细”

这时候就会发现，Anthropic这种low ego、凝聚力强、使命驱动的氛围，优势会被放大得非常明显。

据说Anthropic的co-founder Jared Kaplan也是每天带领团队亲自过数据，数据清洗做得极其仔细，其余没有任何一家公司能做到这样。

（这也解释了一个现象：OpenAI的模型在竞赛级coding难题上是最强的，因为这类任务更多是一个research问题，但在日常工作中的agentic任务上往往不如Anthropic，因为后者更多是一个工程问题，考验数据、系统和执行细节。)

二、创始团队的出身

公司价值观可以说是创始人价值观的一部分，比如马云的武侠风、马化腾的柔和开放、乔布斯的审美导向、任正非的军人纪律。

如果更准确来说，创始人的价值观往往来自两部分东西：一部分是创始人原本相信什么，另一部分是他们曾经深深厌恶过什么。

前者决定你想成为什么样，后者决定你无论如何都不想再变成什么样。

Anthropic很明显两者都有，而后者的塑形力量，可能比前者还大。可以简单看一下Dario的经历：

Dario最早接触AI是在百度的AI实验室，他在那里第一次观察到了scaling laws，并逐渐成为了scaling laws的坚实信徒。但在百度做出突破之后，围绕控制权、资源的内部争斗很快爆发，团队最终解散。

Dario后来辗转加入了OpenAI，在这里深度参与了GPT系列的推进。OpenAI曾经把50%-60%的全公司算力交给他，让他主力领导GPT-3项目。

而因为Dario是一个有着鲜明价值观和个人主见的人，他跟OpenAI其它人在组织理念上的分歧开始渐渐显现。

比如，Greg Brockman曾提出过一个很惊人的想法：未来可以把AGI卖给联合国安理会里的核大国。Dario听完几乎当场辞职，在他看来，这已经不是一个商业分歧，而是底层价值观问题。

Greg和Dario两边几年来一直不太对路，Sam Altman就夹在中间调和。Sam此时发挥了自己最擅长的一个能力，就是让不同阵营都觉得，他其实站在自己这边。短期看，这是平衡术；长期看，这就是在透支信任。后来大家一对账才发现，Sam答应Dario的，和答应Greg的，根本不是一回事。

慢慢地，Dario自己在公司里形成了一个紧密的同盟圈子，有些人因为他喜欢熊猫，就把这个小团体叫作"the pandas"。他们和OpenAI领导层在路线选择、组织治理等问题上的分歧越来越大，最后发展成很严重的政治斗争。

高层之间甚至爆发过一次严重的当面对质。Sam指责Dario和Daniela（Dario的妹妹，Anthropic后来的联创之一）在背后组织对他的负面反馈；两人否认，并当场叫来Sam所说的消息来源对质。结果对方表示完全不知道这件事，结果Sam又转头否认自己刚刚说过这番指控。

这件事让Dario兄妹彻底失去信任，双方当场吵翻。

类似的内部drama还有很多，总之，Dario对两边的冲突上纲上线到了一个道德上的信任危机，他觉得一家掌握如此强大技术的公司，领导者必须是真诚、可信的。如果掌舵的人不诚实，就是在帮一个危险的方向添砖加瓦。

于是，Dario最终带着GPT-3的一些核心同事离开了OpenAI，创立了今天的Anthropic。

所以，Anthropic今天这种文化，不只是因为Dario这个人天生如此，更重要的是，它自己亲身经历了百度和OpenAI的两次政治斗争，它清楚一群ego强的聪明人有多容易因为资源争夺和价值分歧而导致分裂，所以他们后来本能地在朝相反的方向去建设Anthropic：

因为见过平衡术如何透支信任，所以更强调真实、透明；

见过激化的政治斗争，所以鼓励大家把冲突前置，尽早说开。

见过理念分歧导致的组织瓦解，所以设置了严格的文化筛选；

见过超级明星的权力争夺，所以强调low ego，不爱招big name。

Anthropic今天的组织文化，很大程度上都像是当年百度和OpenAI经历留下的反作用力。

[图片] https://mmbiz.qpic.cn/mmbiz_png/QicyPhNHD5vYs92nHCpdbueQF7gdhICh69wicwdn3toUy1ib4ibVYZAHQXc4c9XqWjVkuIuz4WTgftXHEwpbIRia8KA/640?wx_fmt=png&from=appmsg

Conclusion

[图片] https://mmbiz.qpic.cn/mmbiz_png/o02wSnKAPeF48wWeKibqjVlDFfMsTa5lIvhHrBtllHHd17qmibTCEXX2rwKN4DTurc9UoxMRDIFzzCicjEUuC55RVeIkkg2lXnPibSAfN8plfWY/640?wx_fmt=png&from=appmsg

如果要做个总结，Anthropic和OpenAI其实是两家底色挺不一样的公司，前者是理想主义、使命清晰、有高度凝聚力的教派型组织，后者是野心驱动、多线扩张、不断寻找下一个爆点的超级平台。

为了看得更清楚一点，我们可以把两家的几个核心维度并列放在一起：

[图片] https://mmbiz.qpic.cn/sz_mmbiz_jpg/QUs3kaltEh3ozqrSTzCnibAUiavghGhFMSnZNMcCWYZ3icL0G40JYt8zlyMibicVibMDJAa0nLkxe6ibNEGukPQflrQPU1gTm8eFlqa58bgBknfTicw/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=6

不过，虽然前面讲了Anthropic的很多优点，但我们很难下结论说，某种文化一定压倒另一种，也很难预测三个月后的战局。AI的世界变化太快，而OpenAI现在反过来在被市场低估，比如：

Coding已经是明牌，OpenAI很可能追上来，现在一个明显趋势就是开发者在从 Claude Code向Codex迁移；

需求爆发远超所有人的预期，算力正在成为新的胜负手，而OpenAI很早锁定了远超Anthropic的算力资源；

OpenAI开放探索的文化有它自身的巨大优势，同时OpenAI也始终在更激进地探索和押注新范式，下一次跃迁就可能让局面翻盘。

只能说，站在2026回看过去三年，Anthropic确实给整个行业留下了一个值得记住的样本：

在AI时代，赢不一定靠更大的野心、更多的探索和更强的人才。

有时候，赢也可以来自相反的东西：更少的bet，更低的ego，以及一个天真的使命。

[图片] https://mmbiz.qpic.cn/mmbiz_png/QicyPhNHD5vagBvpJSWBnNYW2D0LereibpOTKhlQucdMlnua1EZPEftBTh3iaNT7QPQlFYa6jHJ58VcEIpc2SXg7A/640?wx_fmt=png&from=appmsg

[图片] https://mmbiz.qpic.cn/mmbiz_png/QicyPhNHD5vagBvpJSWBnNYW2D0LereibpaO1bAicFfUgxRicmVz0WLEJINuCCErEc1KS2r8fuFZCicO3END8ibSE2Ng/640?wx_fmt=png&from=appmsg

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/o02wSnKAPeHbJfBIAnhP1pdwMPDiblTUSkJ3Sic0Jy7810AI2lcjNVcvx5CYCXhrqPSCCuwzCfwv2uwMOL13OgnqvYRPl5wJh8rmBnemZl3k0/640?wx_fmt=png&from=appmsg

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/o02wSnKAPeGrqfWGeSvezmzHr8NMuJVBXSFSdJQrZveicQiaJ2gMRmbqXSXiadhgPoKGdxf73Zp0VAxtaMQpY541OezqDvia5vjEYRuibUWfVibTw/640?wx_fmt=png&from=appmsg

[图片] https://mmbiz.qpic.cn/mmbiz_gif/QicyPhNHD5vagBvpJSWBnNYW2D0LereibpbkBWeO9ZkPaT3HA1GmlmABENQmcfuVicLhA8MJnBVLEPpRmwlY5n0HA/640?wx_fmt=gif&from=appmsg

[图片] https://mmbiz.qpic.cn/mmbiz_gif/QicyPhNHD5vagBvpJSWBnNYW2D0Lereibph6S4cD1udwTvHO1f1TGc38MPePRKKvibuBqd6BCmY7buGgDxiaoUxgWA/640?wx_fmt=gif&from=appmsg

[图片] https://mmbiz.qpic.cn/mmbiz_png/QicyPhNHD5vagBvpJSWBnNYW2D0LereibpVtBKUEjKhlcnTamERSCcPu00rbtswUB7cpAibmAe1GzGWa8vDh5zvRw/640?wx_fmt=png&from=appmsg
