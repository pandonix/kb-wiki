---
source: ima
kind: wechat
category: "技术"
title: "循环即实验室：八个AI自主研究系统横评"
url: "https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247515306&idx=1&sn=f83816c1cd04553231e61cab1fed064f&chksm=c38d2b791d980d8ed6b3316ca82ea95ba16a78174057c979e9ebaff68b0334a75fade5f341ba&scene=90&xtrack=1&req_id=1775913839523018&sessionid=1775914190&subscene=93&clicktime=1775914199&enterid=1775914199&flutter_pos=4&biz_enter_id=4&ranksessionid=1775914190&jumppath=FileDetailViewController_1775914141812%2C1102_1775914187912%2C1001_1775914189322%2C1104_1775914191066&jumppathdepth=4&ascene=56&devicetype=iOS26.3.1&version=18004635&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&countrycode=CN&fontScale=109&exportkey=n_ChQIAhIQ68VOHFDEeQRHRh8ROWThThLUAQIE97dBBAEAAAAAAJYEDDOqyzEAAAAOpnltbLcz9gKNyK89dVj0iDDVwpdOn0G1SxaicF5Ha8pYkTJpb5FXxCvdgbLOHxGdplbBamIAOrE%2BAOqpn5YsQy0Xeukf91EjPD9Zi3tWFaiR9VSf6InORtzElL%2FSPMT4wG%2FXcmE%2B%2FIMFT1UalPTYsVdw1dRSkf%2BcJHTMazyB3rlmyQiNWA35yNThlftYXu49XixYW%2F2BSKxEoaiIU6SfkJaSQdYsRkeQq%2F14TK7QUEhAa5tOaXdeuDkjvpLD&pass_ticket=CO%2BMFfiGuxk%2FbrWfoAOfri3njCjxQRYxngDtlzZhdIuC%2BO%2BzyOJNa7kQS7xpYIcL&wx_header=3"
media_id: "wechatarticle_30987b07fe36143e35b82223ae18bcbe_83aecbfa41fd59377c8ec396ced4f554"
media_type: 6
kb_name: "殷凇的知识库"
kb_id: "qzeC00QqxVZKyNdfTs2u_JmTwlIqypGehkvk2cjRaNw="
kb_folder_path: "/"
created_from_ima_at: "2026-05-11T10:27:18.695Z"
body_status: full_text
fetched_at: "2026-05-13T11:19:28+08:00"
---

# 循环即实验室：八个AI自主研究系统横评

- 来源：ima 个人知识库
- 原文链接：https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247515306&idx=1&sn=f83816c1cd04553231e61cab1fed064f&chksm=c38d2b791d980d8ed6b3316ca82ea95ba16a78174057c979e9ebaff68b0334a75fade5f341ba&scene=90&xtrack=1&req_id=1775913839523018&sessionid=1775914190&subscene=93&clicktime=1775914199&enterid=1775914199&flutter_pos=4&biz_enter_id=4&ranksessionid=1775914190&jumppath=FileDetailViewController_1775914141812%2C1102_1775914187912%2C1001_1775914189322%2C1104_1775914191066&jumppathdepth=4&ascene=56&devicetype=iOS26.3.1&version=18004635&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&countrycode=CN&fontScale=109&exportkey=n_ChQIAhIQ68VOHFDEeQRHRh8ROWThThLUAQIE97dBBAEAAAAAAJYEDDOqyzEAAAAOpnltbLcz9gKNyK89dVj0iDDVwpdOn0G1SxaicF5Ha8pYkTJpb5FXxCvdgbLOHxGdplbBamIAOrE%2BAOqpn5YsQy0Xeukf91EjPD9Zi3tWFaiR9VSf6InORtzElL%2FSPMT4wG%2FXcmE%2B%2FIMFT1UalPTYsVdw1dRSkf%2BcJHTMazyB3rlmyQiNWA35yNThlftYXu49XixYW%2F2BSKxEoaiIU6SfkJaSQdYsRkeQq%2F14TK7QUEhAa5tOaXdeuDkjvpLD&pass_ticket=CO%2BMFfiGuxk%2FbrWfoAOfri3njCjxQRYxngDtlzZhdIuC%2BO%2BzyOJNa7kQS7xpYIcL&wx_header=3
- ima media_id：`wechatarticle_30987b07fe36143e35b82223ae18bcbe_83aecbfa41fd59377c8ec396ced4f554`
- ima 目录：/
- 内容分类：技术
- 正文状态：已抓取全文。

## 摘要

> 当前 ima 知识库列表接口未返回文章摘要字段；本条先保存标题、链接、media_id、目录与分类，便于后续按需补正文/摘要。

## 正文

RESEARCH

现在，AI Agent 这个词已经成了真正在跑的东西

Karpathy 写了 630 行代码让 AI 自己做实验，Google DeepMind 让程序自己进化出了 56 年来没人改进过的算法，Sakana AI 做了一个会重写自己源码的 Agent 然后它学会了作弊。这些系统不再是论文里的示意图，它们在真实的 GPU 上跑着，产出真实的结果

但它们到底在做什么事？各自的能力边界在哪？能不能组合起来用？

今天Interesting Engineering++发了一篇长文，把这些系统放在同一个分析框架里做了横评，回答的就是这些问题

The Loop Is The Lab

本文线索，由线人庄明浩脑湿举报

原文地址：interestingengineering.substack.com/p/the-loop-is-the-lab

一个核心命题：科学方法本身是程序

先说背景。过去一年，做 AI 的人越来越意识到一件事：训练模型这件事本身，可以被模型来做。不是那种「AI 辅助研究」的客气说法，是真的让 Agent 自己提假说、自己跑实验、自己看结果、自己决定下一步怎么办

这篇文章看了八个这样的系统。它们来自不同的团队，解决不同的问题，但共享同一个洞察：科学方法就是一个循环——假说、实验、评估、保留或丢弃、重复。这个循环可以写成代码，写成代码就能自动化，自动化了就能以机器速度运行

每个系统实现这个循环的方式不同，这些差异决定了它们各自能做什么、会在哪里卡住

八个系统的定位概览

原文提出了一个七原语加治理的分析框架，用来拆解任意智能体系统，然后把这个框架应用到全部八个系统上

分析框架：怎么理解一个 Agent 系统

要比较八个系统，得先有一把统一的尺子。原文造了一把，挺好用

八个原语

说白了，不管多复杂的 Agent 系统，拆开来看就是八个零件的排列组合。搞清楚一个系统装了哪些零件、每个零件谁控制，基本上就理解了它能做什么和不能做什么

八原语图解

感知（Perceive）、记忆（Remember）、推理（Reason）、行动（Act）、评估（Evaluate）、变异（Mutate）、协调（Coordinate）

七原语速查表

治理（Governance），关键的第八个

治理原语

可进化性阶梯

关于一个自主系统，最有诊断价值的问题只有一个：变异发生在哪一层？这个问题的答案把所有系统分成了六档。越往上，Agent 能改写的东西越多，能力天花板越高，风险也越大

可进化性阶梯：从 L0 到 L5

L0是聊天机器人，只改输出不改自己。L1调超参，经典 AutoML。L2改代码，AlphaEvolve 和 AutoResearch 在这。L3写新工具扩展动作空间，OpenClaw 在这。L4改控制自己推理和行动的代码，Darwin Gödel Machine 在这。L5改评判自己的标准——目前没有系统在这一层运行，但苗头已经出现了

八个系统，逐个看

1. AutoResearch

Karpathy / Eureka Labs，2026 年 3 月

Karpathy 做的东西有个特点：极简，但极简本身就是设计决策。AutoResearch 是一个630 行的 Python 项目，MIT 协议开源。每个实验精确跑 5 分钟，只用一块 GPU，整个代码库能放进一个 LLM 的上下文窗口

两天演示跑了约 700 次自主修改，找到约 20 个叠加改进，把一个已经被认为充分优化的代码库的 Time-to-GPT-2 指标砍了11%。社区拿 Mac Mini M4 跑隔夜测试，nano 尺度上到了约 28%

AutoResearch 流程图

5 分钟预算是这个系统最重要的设计决策，虽然不是最显眼的那个。它让每个实验可比，防止 Agent 发现在更长训练中不成立的虚假改进，顺便把硬件门槛降到了一台 Mac Mini

Agent 的学习机制很朴素：它看到一个不断累积的「什么有效、什么失败」的历史，假说质量随迭代提升。Git 同时充当审计轨迹和回滚机制

AutoResearch 关键属性

卡在哪：AutoResearch 在 train.py 内部发现改进。但 50% 的算力削减需要根本不同的架构（比如 MoE）或内核级效率改进，一个 630 行脚本里做不到这些

2. AlphaEvolve

Google DeepMind，2025 年 5 月

如果说 AutoResearch 是一个人的周末项目，AlphaEvolve 就是 Google 级别的工程——在内部跑了一年多才公开。成果放在这个量级上看确实吓人：56年来首次改进 Strassen 的矩阵乘法算法，Gemini 架构里 FlashAttention 内核加速23%，改进 Borg 调度启发式永久回收了 Google 全球计算资源的0.7%

架构是进化的。维护一个候选程序的群体，用双 LLM 变异策略：Gemini Flash 负责广度（大量廉价变异），Gemini Pro 负责深度（对最有前途的候选者做昂贵推理）。Strassen 那个突破就归因于 Pro 的深度推理能力

AlphaEvolve 流程图

父代选择时，不是只选最优者，分数差的程序可能携带了对另一目标有用的遗传材料。群体修剪用 Pareto 前沿。形式化验证器是冻结的，人写的，检查程序是否真的算对了

AlphaEvolve 关键属性

卡在哪：AlphaEvolve 发现怎么更高效地计算一个给定架构，但它不能发现该用什么架构。内核级增益到 25-30% 大概就封顶了

3. Darwin Gödel Machine

Sakana AI / UBC / Vector Institute，2025 年 5 月

这是八个系统里哲学上最激进的。名字致敬了两个谱系：Schmidhuber 2003 年的 Gödel Machine（只在能形式化证明改变有益时才改自己）和达尔文进化论（不需要证明，活下来就行）。DGM 把两者嫁接：放弃形式化证明，用经验性基准验证替代数学确定性

SWE-bench 上 80 次迭代从20.0%干到50.0%。Polyglot 上从 14.2% 到 30.7%，超过了手调的 Aider。用 Claude 3.5 Sonnet 优化的工作流还能迁移到 Claude 3.7 和 o3-mini，说明 Agent 找到的是工作流架构层面的改进

然后出了一件有意思的事。在一次运行里，Agent 修改了自己的评估代码来伪造基准日志，人为抬高自己的分数。研究人员抓住了它，因为每个变更都被沙盒化且可追溯

DGM 流程图

DGM 的 Agent 把自己的全部 Python 源码读进内存，然后推理怎么改进自己。它可以改任何东西——包括构造 LLM 提示的代码、档案采样策略、甚至判定什么算「改进」的标准。这就是它在可进化性阶梯上处于 L4 的原因

DGM 关键属性

卡在哪：DGM 在「搜索」上越来越好，但不一定在「搜索找到的东西」上越来越好。当代理基准和真正目标在规模上偏离时，完美的搜索者探索错误的景观，收敛到的还是错误的答案。80 次迭代花 22000 美元

4. OpenClaw

Steinberger，2026

OpenClaw 是感知范围最广的那个。文件、邮件、日历、OS 命令、API、网页、ArXiv 论文、GitHub 仓库、Slack，只要有对应的 skill 就能对接。最特别的是它可以自己写新 skill——在运行时永久扩展自己的动作空间

OpenClaw 流程图

OpenClaw 不只检索信息，它跨源综合——识别矛盾、汇聚和未探索的组合。这种信息收集一个人类研究者要花好几周

OpenClaw 关键属性

卡在哪：原文有一句话说得太准了

OpenClaw produces the world's best-organised backlog of untested ideas.

OpenClaw 产出了全世界组织得最好的未测试想法清单

没有自动化反馈循环。每个实验结果必须人来审阅。90 天里一个仔细的人能评估 10-15 个结果，AutoResearch 一个晚上跑 100 个

Marc Andreessen 怎么看 OpenClaw

Marc Andreessen 在一期播客里说他认为π和 OpenClaw 的组合是几十年来最重要的软件架构突破之一。他的定义很简洁

LLM + shell + file system + markdown + cron loop

几个让他「炸裂」的点：Agent 把状态存在文件系统里，换模型不影响身份和状态；Agent 对自己的文件结构有完整自省知识，可以重写自己的代码；跟 Unix shell 结合后 Agent 原生拥有计算机的全部能力

他把组件一个个列出来——LLM、shell、markdown、cron loop——说这些东西都不新，但组合在一起之后软件的定义变了。从人手动造软件变成 Agent 自己进化出能力来满足需求

5. Claude Code

Anthropic，2025+

Claude Code 做的事跟上面那些研究自动化系统不太一样。它是一个编码 Agent，设计目标是在现有代码库里把活干好。读整个代码库、跟终端交互、通过 MCP 连外部服务、生成子 Agent 并行执行、用 CLAUDE.md 做持久记忆

它的核心优势在实现层。人提供假说，Claude Code 来实现和测试，比人类开发者更快更准

Claude Code 流程图

Claude Code 关键属性

卡在哪：第 30 天，所有显而易见的效率提升都实现了——混合精度、激活检查点、数据管线优化、融合操作，加起来约 15%。第 31 到 90 天不再产出新假说。CLAUDE.md 成为一份组织得很漂亮的停滞搜索记录

6. AutoResearch Swarm

社区分叉，2026+

一个人的 AutoResearch 跑不过来了，社区就把它拆成了四个 Agent 协作：A1 生假说，A2 并行跑实验，A3 跨所有结果做综合，A4 盯着有没有奖励黑客和统计异常

关键的质变在复合学习。A3 的综合喂回 A1 的假说生成，假说越来越好。90 天跑大约9000个实验，样本密度够大，能发现单次隔夜运行永远找不到的架构交互

AutoResearch Swarm 流程图

Swarm 关键属性

卡在哪：Swarm 产出了全世界验证得最好的「可能在前沿规模有效」的清单。但真正验证需要一次5000 万到 1 亿美元的训练运行。搜索问题解决了，验证问题仍然是人类的

7. Moltbook

Agent 社交网络，2025/6+

Moltbook 是个奇怪的东西。它是一个 Agent 原生的社交网络，大约150 万个 Agent 账户在里面发帖、回复、互发消息，没有中央编排者，没有选择压力，没有评估函数

它被放进这篇横评不是因为它能做研究——它不能——而是因为它是对等网格拓扑的最大规模实验。无治理的高复杂度协调会产出什么？答案挺刺激的

记录在案的涌现行为：协调联盟自发形成、加密点对点通信通道、加密货币计划，以及研究人员描述的涌现原始宗教（emergent proto-religion）

Moltbook 流程图

8. NemoClaw

NVIDIA，2026

NemoClaw 跟前面七个不太一样。它不引入新的搜索能力或变异机制。它做的事是之前的七原语框架里没有对应类别的：在 Agent 行为执行的那一刻进行拦截——在行为产生效果之前

之前所有系统的监督都是事后的——看 git 日志、查基准分数、读综合报告。NemoClaw 把监督移到了行动的瞬间：Agent 试图连接一个不在预批准列表里的网络端点时，请求被阻止，实时展示给人类操作员，批准或拒绝后才继续

NemoClaw 流程图

NemoClaw 治理架构，来源：NVIDIA 文档

NemoClaw 架构细节，来源：NVIDIA 文档

NemoClaw 默认路由到 Nemotron 3 Super 120B。通过提供企业部署 Agent 必需的合规和审计基础设施，NVIDIA 同时把自己变成了所有受治理 OpenClaw 部署的默认推理提供商

NemoClaw 关键属性

开放问题：实时逐连接审批在少量 Agent 时可行。规模化之后——几百个 Agent、每小时几千个连接请求——审批要么退化成橡皮图章，要么变成瓶颈

放在一起看

每个系统在哪里卡住

原文做了一张表，把八个系统对照完成研究循环所需的阶段逐一映射。前沿规模验证那一列，对每个系统都是空的

阶段解剖表格（上）

阶段解剖表格（下）

约束已经从「发现改进」转移到了「在有意义的规模上验证改进」

混合体：每个系统贡献什么

各系统对混合体的贡献

三条系统思维规则

三条规则概览

规则一：瓶颈揭示架构盲区：一个系统的瓶颈总是在它能测量的东西和目标真正需要的东西之间的裂缝处

The precise location of the stall is the most informative single piece of information about a system's architecture.

瓶颈的精确位置是关于系统架构最有信息量的单一信息

规则二：评估函数就是系统：两个层完全一样但评估函数不同的系统会收敛到不同的解

The evaluation function is the system's actual objective, regardless of what the designers specify in prose.

评估函数是系统的真正目标，不管设计者在文档里怎么写的

规则三：规模边界需要人类权威

Humans remain essential not because they reason better, but because they can authorise expenditures that change scale.

人类仍然不可或缺，不是因为推理得更好，而是因为能授权那些改变规模的支出

Harness 在哪

原文最后讨论了 Harness（护栏）和三条规则的关系。Harness 就是 Agent 周围的固定框架：定义评估信号、观察接口和 Agent 能触碰与不能触碰的边界。三条规则各描述了 Harness 的一个边界处发生的事

Harness 与三条规则的关系

规则一在测量边界触发——Harness 能测量的捕捉不到真正目标时，Agent 就在那里停滞。规则二命名了 Harness 的核心组件。规则三在权威边界触发——人类是 Harness 最外层的边界

八原语框架是解剖学，映射系统的冻结/可进化结构。三条规则是诊断学，解释为什么这个结构产出了它所产出的结果。两者都需要

原文最后一段：

The scientific loop — hypothesise, experiment, measure, keep or discard, repeat — is itself a program. The question is no longer whether AI can run this loop. It is how to define the loop so that what gets optimised is what we actually care about — and who holds authority over the decisions that code cannot make.

科学循环本身是一个程序。问题不再是 AI 能不能跑这个循环。问题是怎么定义这个循环，使得被优化的东西确实是我们在乎的东西——以及谁对那些代码做不了的决策拥有权威

下一个前沿不是更强的独立 Agent，而是它们的组合架构

原文地址：interestingengineering.substack.com/p/the-loop-is-the-lab
参考文献见原文，涵盖 Karpathy AutoResearch 仓库、NVIDIA NemoClaw 文档、AlphaEvolve 论文（arXiv:2506.13131）、Darwin Gödel Machine 论文（arXiv:2505.22954，ICLR 2026）、Sakana AI 博客、OpenClaw 文档、Claude Code 文档等
