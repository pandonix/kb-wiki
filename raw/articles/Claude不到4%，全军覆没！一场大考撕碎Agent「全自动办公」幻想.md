---
source: AIGC新智界
publish_time: "2026-05-25 17:17"
url: "https://mp.weixin.qq.com/s/bQwDkUi6rqlTCc1vNdvu5w"
category: "技术"
kind: wechat
sha256: 33fc3f6c7f819b26cd31f42e46616823d3a5743b6a22cc31f1f51811d2c39e08
ingested: 2026-05-26
------

# Claude不到4%，全军覆没！一场大考撕碎Agent「全自动办公」幻想

- 来源：AIGC新智界
- 发布时间：2026-05-25 17:17
- 原文链接：https://mp.weixin.qq.com/s/bQwDkUi6rqlTCc1vNdvu5w
- 内容分类：技术
- 文章摘要：新智元报道  【新智元导读】许多实习生能轻松完成的任务，有时对于AI来说却是一场严酷大考。

## 框架判断

- 阅读深度：Read Normally，后续若要研究 agent 真实可用性，可追原始论文 / GitHub 做 Deep Read。
- 框架定位：主层是 L1 技术本体，副层是 L2.5 人与组织适应。L1 在于评估 computer-use agent 的长程执行、状态感知、闭环验证和错误恢复能力；L2.5 在于判断 agent 进入真实办公流的组织边界和改造成本。
- 对应活问题：当前 AI agent 离“全自动办公”还有多远；真实工作流中哪些任务适合交给 agent，哪些必须保留人类监督和验证；未来 SaaS 是继续让 agent 操作人类界面，还是需要重构为 agent-native 工作系统。
- 有用之处：SaaS-Bench 把 23 个真实开源 SaaS、106 个跨应用长程任务、resolved score / checkpoint score 放在一起，给出比玩具 benchmark 更接近工作场景的能力校准；文章总结的四类失败模式可直接用于判断 agent 项目风险：长程衰减、上游错误级联、缺少状态复核、路径依赖导致不稳定。
- 框架更新：评估 agent 不能只看单步能力、demo 或 benchmark 榜单，要看“端到端完成率”和“状态验证闭环”；在真实业务中，更现实的路径是人机协作、强约束工作流、检查点验证和可恢复设计，而不是直接追求全自动替人办公。
- 预测材料：未来 12-24 个月，企业 agent 落地更可能先发生在 API / workflow-native 场景，而不是让通用 GUI agent 自由操作多个 SaaS；如果软件厂商开始提供 agent-native 接口、状态验证器和任务恢复机制，落地速度会明显提高。
- 噪音风险：文章标题和措辞偏媒体化，有“全军覆没”“撕碎幻想”的情绪包装；具体模型版本、分数和 benchmark 设计需要以 UniPat 原始 blog、GitHub 和 arXiv 论文为准；SaaS-Bench 本身也可能存在任务构造、工具链、Browser-Use 框架和验证器偏差。
- 后续读法：先读本文结论和失败模式，再追 arXiv / GitHub；重点看任务定义、验证器设计、模型调用配置、失败案例和 resolved score 与 checkpoint score 的差距。

## 正文

[图片] https://mmbiz.qpic.cn/sz_mmbiz_jpg/Rvq8Ow69CYUXescerlw8GdfylNZEWVUm5mYTC45XsazibgibbOHibfficNJAPkt9FjHxibCXqpj2k30jf2cj7DE6AqxsIf5vLnr285qtHYsRMfZk/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=0

新智元报道

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYWGxcbmnyYvqrSqhntcbPdelKBG0JLug4pEX8icjBSe5eib6PekswOSvrq8ybatQJRDr9Vib5WOKaUuibKfLb5qH3J4kEIYmC4NQJU/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1

【新智元导读】许多实习生能轻松完成的任务，有时对于AI来说却是一场严酷大考。人类距离真正可用的Agent，还有多远？一份全新SaaS-Bench实战考卷，已经给出了答案。

Computer-Use Agent的「奇点」没有来，现实的冷水先泼下来了。

过去一年，各家GUI Agent争先恐后地宣称能替人类干活。Benchmark成绩一路飙升，投资人兴奋，媒体狂欢，「全自动办公」似乎就在眼前。

但UniPat AI刚刚用一组数据证明：这一切，都建立在沙子上！

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYULleIxUxaSYDCWlTdQ9H31BOqKtDV4M4HIhpZhBHR2c6noaqwiamrShyBznKtibzEJVMIpf0OJl9r98OyUD8EcrmCtMkQwKY52w/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2

Leaderboard

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3

23个真系统，106个任务

一场残酷的实战考试

现有的Agent评测，说白了就是：仿真环境、简单任务、最多几十步搞定。

跟真实工作完全是两回事。

真实办公长什么样？一个医疗管理员写完SOAP病历→填病例上报→生成正式文档。一个财务收到报销申请→审批→打款→记账。

跨好几个系统，步骤动辄几百步。

SaaS-Bench的思路很暴力：直接把真系统搬进Docker，让Agent在真实的前后端逻辑、数据库状态和业务约束中干活。

[图片] https://mmbiz.qpic.cn/mmbiz_png/Rvq8Ow69CYUzBtt9Y7ybmp73GFbLicxNicMc86yboZ3dwlRv12fA6g2Dibd3ibBfwnu8ugB4NPdk1AJOZ5M5d0oDuCGqjlOZdrDibZ7BHuo2icAMI/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4

SaaS-Bench任务——真实工作场景任务

SaaS-Bench精心挑选了23个开源SaaS（Software-as-a-Service）系统，全部通过Docker本地部署，保留了完整的前后端逻辑、数据库状态和业务约束。覆盖六个专业领域：

软件研发：OpenProject、Baserow、Code-Server、Metabase

业务财务：Twenty CRM、BigCapital、HRMS、Pretix

医疗管理：OpenEMR、OpnForm、OnlyOffice

团队协作：SiYuan、Roundcube、Mattermost、ownCloud

农业供应链：FarmOS、Grocy、Recipya、E-Label

独立媒体：PhotoPrism、MediaCMS、BookLore、Watcharr

更重要的是，这些系统不是「空壳网页」：每个软件里都填充了真实业务的数据，包括用户、项目、订单、文件等实体记录。

Agent进入的不是一个空白的测试页面，而是一个有历史数据、有干扰项、有跨系统关联的真实工作环境。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYV4LamtLibicoGh4kp8CmTC8bSWoNLDNHuyibzVwP1jXP5SNTN2iaMZ1c8noJVnUPStGibSdXFaTGkiciaR3PxWibLNmb0iceyJ38Hg9WjI/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5

任务模态、领域、app三层分布

106个任务中，93.4%跨越至少两个应用，三应用任务占了一半（53个）。

纯文本任务74个，涉及多模态理解的32个。以Claude Opus 4.6的执行轨迹估算，97.3%的文本任务操作步数超过100步，最长轨迹达300+步。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYX5fc4iasqicSqPotAoQvZfYzezvuYA9oEIaLoawENRsbNAew8UrqHuiaP2xFSPYzr0osGStf8mD4uf9SibvqyxaicD7EYSjEMCEhwY/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=6

任务难度分析 ——大多数任务是 Cross-App + Long-Horizon 的

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=7

这些任务是怎么来的？

如何评估Agent的操作能力？

SaaS-Bench 采用「LLM生成 + 专家把关」的方式完成任务构建：

先由LLM围绕六大专业领域和具体职业角色生成任务，明确任务目标、跨应用依赖和验证要求，并通过多轮修改减少歧义和漏洞。

随后，专家会对任务进行人工筛选和真实执行检查，重点判断任务是否专业、自然、可完成、可验证。对于堆砌步骤、逻辑混乱或验证不准的任务，会被修改或剔除，最终确保每个任务都能真实运行，并能被验证器准确评估。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYUZdZ73srCq8ib3IqRtU4Vvb36VwHnENhB49ibCLCpLiaHjoicMCLXPf8UDqaicNAY7zu2sKyNW3qIibBRUMTEZJwU6YV4sXYofKLDIY/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=8

任务构建流程图——四个阶段保证任务质量

SaaS-Bench允许Agent使用Browser-Use在SaaS环境中操作计算机，并给出了两个指标：

Resolved Score（完全通过分数，严苛）：全部检查点通过才算1，否则为0

Checkpoint Score（检查点分数，宽松）：按权重计算部分检查点完成比例

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYXmRuhia9hbWMztj9ZN3SPbPe9Sm1OOpibbHuvxT07BHkFlm69SX2tYqLwyoL1jSFzdQfxLOvYJkmRfsibUhdGJp9298f5w6lt15U/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=9

Agent → Browser-Use → 执行 → 验证 → 打分总览图

后面的结果会表明——这两个数字之间的巨大落差，恰好暴露了Agent最核心的问题。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=10

榜单出炉：全军覆没

来看这组数字 ——

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYWMKoAbTkgNHxpIzKRGNsuwD6BR9Ntnq4tsuZmfNTwR8dibVaRnWWWZHKmicPU67Y2OwgD6Xf7q6ibKj3ickA28ndwtuc937fibiaic9U/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=11

主要结果（DeepSeek V4 、M2.7和GLM5.1为单模态模型，仅测评Text-OnlyDomain）

最强的Claude Opus 4.7，检查点分数43.9%，端到端完全通过分数只有3.8%——106个任务，只完整通过了4个。Kimi K2.5和Gemini 3.1 Pro？完全通过分数为零。一个任务都没走完。

这组数字的含义极其残酷：Agent可以推进工作的部分中间环节，但几乎没有能力将一个完整的长程工作流走完。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=12

多跑几次能救吗？

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYWEPoVcAo37ggoqUhGPN2pVO5W0Gj8H2Zicdt0ZJpLn9kMxuxlHsibEEuIXL6z8HHEE9ESrD9ESoe7e6WkvwWl0X5XkwsfjZsatA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=13

四个模型的Pass@k结果

把每个模型在同一任务上独立跑3次，对一次就算通过。pass@3相比pass@1整体提升约8个百分点。

Sonnet 4.6在多模态任务上从33.9%跳到52.1%（+18.2pp）——它并非完全不行，而是执行极不稳定。

这不是环境随机性。每次运行的初始状态完全相同。这是路径依赖——模型在某个决策点的微小差异，导致后续轨迹完全分叉。

多跑几次有帮助，但远不是解决方案。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=14

越复杂，分越低

三个结构维度全部单调递减：

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYVDWJtPMVk5tlwsSQ3PhQRibcIdp1LoZib1PmzvZtrtQRp3iaA1E1ATeh6Zia6mNRehWshQVibBfEZnNFasayeUBFUmWnJGB0ibg2ySU/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=15

分数 vs 应用数 / 分数 vs 步长 / 分数 vs 检查点个数

跨应用数1→4：平均分从53%降至20%

操作步长增加：任务轨迹越长，得分显著越低

检查点个数≤6 vs ≥18：平均分从65%降至27%

「跨应用+轨迹长+细粒度验证」的任务得分最低——这恰恰是真实工作流最常见的形态。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=16

四种结构性失败：Agent到底在哪翻车

SaaS-Bench真正的价值不在于分数本身，而在于暴露了Agent在真实环境中的四种致命缺陷。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb351381bTy5MO2IN89mV41M88GEiaCCibDxJoaQjYV6HfRtafnmEmfM3R1p0tmkHgBOVuXBD6UJKpsQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=17

失败1：任务越长，越做不对

即使每个检查点通过率高达95%，12个检查点的全部通过概率也只有54%。而SaaS-Bench的平均检查点数远超12。

所有模型都呈现同一个模式：通过率随任务推进呈下降趋势，没有一个模型能在后半段维持住前期表现。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYW94z471L8SQ84eOPNXmOZ3ticbOP9CaNEtVics0PKLKVNmRmLkMVgQvll6UL260dxmbZFSpn1ZQVJ1Zpyw9EOQ0yXMxmVLXnrd4/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=18

模型随着任务执行，做对的越来越少

这是一条不可逆的下降曲线。越往后走，越不可能走完。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb351381bTy5MO2IN89mV41M88GEiaCCibDxJoaQjYV6HfRtafnmEmfM3R1p0tmkHgBOVuXBD6UJKpsQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=19

失败2：一步错，步步错

一个典型案例：任务要求创建一个公司客户「Arcturus Digital」。Agent同时填了联系人姓名和公司名，触发了个人客户逻辑，实际创建的是个人客户Elena Vasquez。

此后的10张发票、付款记录、账户对账，全部挂在错误实体下。核心检查点权重仅3%，但导致了下游30%的权重损失。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYXHLh9EUXtSTKEgJtkDNLnjeCkVPNiaYbhtVQjo9mE3ptMszADJVkUWdXYJHDJw5ukWJ5mLxWjuQbFEL8NA2YHeZPzLTuuUmq7s/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=20

上游任务导致下游失败链示意图

一个3%的错误节点，造成30%的分数损失。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb351381bTy5MO2IN89mV41M88GEiaCCibDxJoaQjYV6HfRtafnmEmfM3R1p0tmkHgBOVuXBD6UJKpsQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=21

失败3：做完不检查，自以为对了

Claude Opus 4.6在Step 124识别出日期错误（2026-03-19 vs. 2026-03-20），执行了修改，但没有回到页面复查，直接推进后续子任务。

Step 210提交时，汇报写的是「账单日期2026-03-20，已修复」——页面上实际日期仍是03-19。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYXurmJ1j4O2eGpsB6H72hX8pfPicxNclwMJP4UfZKQNs9QteD6HfzJQnZoFXXWRI1YyWX5ElSLX3ibcOmRVjHtBt8VE6hgSa0ouM/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=22

Agent 在意图层面认为成功，Verifier 在状态层面发现失败

Agent在意图层面认为成功，验证器在状态层面发现失败。两者之间的断层是系统性的。

当前CUA框架缺少「严谨的反思闭环」 —— Agent是个不会检查自己作业的学生。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb351381bTy5MO2IN89mV41M88GEiaCCibDxJoaQjYV6HfRtafnmEmfM3R1p0tmkHgBOVuXBD6UJKpsQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=23

失败4：同一张考卷，成绩忽高忽低

Claude Sonnet 4.6在同一任务的三次独立运行中，分数范围从 0.00 到 0.68。

这不是环境随机性造成的 —— 每次运行的初始状态完全相同 —— 而是路径依赖：模型在某个决策点的微小差异，会导致后续执行轨迹完全分叉，这让Agent在长程任务中的执行变成了赌博。

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYVb5WUa95UcM0nCtr65mwYxV2HYCFulb66NGKJcQuS2gUick04BWpI3SuX7jqTJPHLNkcwl5qSu55iaXjXzFMuts9ichiajhThtNibI/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=24

Claude Sonnet 4.6在同一任务的三次运行

[图片] https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3uEdSPKrwGNmZEOaaGyzVvZ8dTtE9jU1rFsda3llYbCZpmWfiazUYjWBLTGvlPpXucH8Q0lEUJN3Q/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=25

这意味着什么

SaaS-Bench撕碎了一个幻觉：Agent的Benchmark成绩和真实工作能力之间，存在巨大的鸿沟。

四种结构性失败模式——越往后越做不对、一步错步步错、做完不检查、次次分数不一样——指向同一个底层事实：当前Agent缺少对持久状态的有效推理能力，缺少操作后的闭环验证机制，缺少从错误中恢复的能力。

这些不是靠模型变大、或者加几个工程模块就能解决的问题。它们指向的是当前Agent范式更深层的局限：在长程任务中，模型缺少对全局状态的持续感知，无法像人一样「心里有数」。这不只是技术债，而是当前范式的天花板。

Computer-Use Agent想要真正替人干活？路还很远。SaaS-Bench把地图摊开了——接下来就看各家怎么走了。

但这也引向了一个正在逐渐形成的共识：今天的SaaS是给人设计的——菜单、按钮、表单，都在服务人类的眼睛和手指。但当Agent成为主要用户，这些界面就变成了累赘。

未来不是让Agent学会操作人类的软件，而是软件本身要为Agent重新设计。

SaaS-Bench揭示的不只是Agent的短板，也是当前软件形态的保质期——面向人类的SaaS，可能都要为Agent重做一遍。

· Blog：https://unipat.ai/blog/SaaS-Bench

· GitHub：https://github.com/UniPat-AI/SaaS-Bench

· 论文：https://arxiv.org/abs/2605.15777

UniPat AI

UniPat AI致力于构建面向真实场景的AI训练、评测与应用新范式，推动Agent能力在千行百业中规模化落地，创造切实的经济与社会价值。

官网链接：https://unipat.ai

文章转载自【新智元】公众号

AI新智界园区开放合作啦！

[图片] https://mmbiz.qpic.cn/mmbiz_jpg/kEYD8Ms4k95QNJY8UblnF2iatkSCRz9C2AAvt6Ra4Lbg9OYybGbjC8L25HA9y3YA03BSHag1qUW1JxxapibTBPVA/640?wx_fmt=jpeg
