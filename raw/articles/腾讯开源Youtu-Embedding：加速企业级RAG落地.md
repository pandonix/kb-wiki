---
source: ima
kind: wechat
category: "技术"
title: "腾讯开源Youtu-Embedding：加速企业级RAG落地"
url: "https://mp.weixin.qq.com/s?__biz=MjM5MDgwMzc4MA==&mid=2654905061&idx=1&sn=7fa03aa24dbf1f64c59d27b12e10e0aa&chksm=bc22086267f4f23b87068166d9745402359575fb1ae2836f3de09ed98de09ca7052687b4dd93&mpshare=1&scene=1&srcid=1014N4O1Zl51p2EqHZyVIlzC&sharer_shareinfo=8c993a4878cf24de2cc3fdd42c765c1e&sharer_shareinfo_first=8c993a4878cf24de2cc3fdd42c765c1e&from=groupmessage&isappinstalled=0&clicktime=1760450901&enterid=1760450901&ascene=1&devicetype=iOS18.6.2&version=18004029&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&countrycode=CN&fontScale=109&exportkey=n_ChQIAhIQtfrwKLsc6qXeSaAZRYaevhLoAQIE97dBBAEAAAAAAFaYN5B0W8sAAAAOpnltbLcz9gKNyK89dVj0axUT2JX14C2EasRM7XuUXI1zWs%2BJ5wSAhFVUgD3L0vH9tyxz8dIliA7PEWItSRuoNZJCx4C3F67eNpn7Ihrg5jbnbuHXrqkQwko4t4ZyzP8u%2B0YdZNHsM6Gwo4KgmxSQlQI4kmvY6B%2Bu86wFAqJQRreSaRw5eAYAm7oDoaHws34qACHvoGKNJFi7IX772hJgwGKniNVkQ7oUFttYZEDOnmY%2FOKvFDyb%2B1EghMtYeKE2LA%2FARZ%2BWiR85bpxjyuGTeAXY%3D&pass_ticket=IHBudd3uNsUTfXytXSciT7J6MipdbxsiuT15iv3lAVxg0L1vCihwRonL6o5FYs2i&wx_header=3"
media_id: "wechatarticle_30987b07fe36143e35b82223ae18bcbe_0d42d37cb89e093aae982f337b04932d"
media_type: 6
kb_name: "殷凇的知识库"
kb_id: "qzeC00QqxVZKyNdfTs2u_JmTwlIqypGehkvk2cjRaNw="
kb_folder_path: "/"
created_from_ima_at: "2026-05-11T10:27:18.695Z"
body_status: full_text
fetched_at: "2026-05-13T05:58:30+08:00"
---
# 腾讯开源Youtu-Embedding：加速企业级RAG落地

- 来源：ima 个人知识库
- 原文链接：https://mp.weixin.qq.com/s?__biz=MjM5MDgwMzc4MA==&mid=2654905061&idx=1&sn=7fa03aa24dbf1f64c59d27b12e10e0aa&chksm=bc22086267f4f23b87068166d9745402359575fb1ae2836f3de09ed98de09ca7052687b4dd93&mpshare=1&scene=1&srcid=1014N4O1Zl51p2EqHZyVIlzC&sharer_shareinfo=8c993a4878cf24de2cc3fdd42c765c1e&sharer_shareinfo_first=8c993a4878cf24de2cc3fdd42c765c1e&from=groupmessage&isappinstalled=0&clicktime=1760450901&enterid=1760450901&ascene=1&devicetype=iOS18.6.2&version=18004029&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&countrycode=CN&fontScale=109&exportkey=n_ChQIAhIQtfrwKLsc6qXeSaAZRYaevhLoAQIE97dBBAEAAAAAAFaYN5B0W8sAAAAOpnltbLcz9gKNyK89dVj0axUT2JX14C2EasRM7XuUXI1zWs%2BJ5wSAhFVUgD3L0vH9tyxz8dIliA7PEWItSRuoNZJCx4C3F67eNpn7Ihrg5jbnbuHXrqkQwko4t4ZyzP8u%2B0YdZNHsM6Gwo4KgmxSQlQI4kmvY6B%2Bu86wFAqJQRreSaRw5eAYAm7oDoaHws34qACHvoGKNJFi7IX772hJgwGKniNVkQ7oUFttYZEDOnmY%2FOKvFDyb%2B1EghMtYeKE2LA%2FARZ%2BWiR85bpxjyuGTeAXY%3D&pass_ticket=IHBudd3uNsUTfXytXSciT7J6MipdbxsiuT15iv3lAVxg0L1vCihwRonL6o5FYs2i&wx_header=3
- ima media_id：`wechatarticle_30987b07fe36143e35b82223ae18bcbe_0d42d37cb89e093aae982f337b04932d`
- ima 目录：/
- 内容分类：技术
- 正文状态：已抓取全文。

## 摘要

> 当前 ima 知识库列表接口未返回文章摘要字段；本条先保存标题、链接、media_id、目录与分类，便于后续按需补正文/摘要。

## 正文

众所周知，通用大模型并不总是「靠谱的专家」。

在企业级智能客服、知识库管理等场景中，它们常常一本正经地胡说八道——资料库明明有答案，却编出一段貌似合理的幻觉内容。为降低风险，越来越多企业引入文本Embedding，先精准提取信息，再交给大模型生成回复。

但新的问题也随之而来：Embedding 模型容易陷入「负迁移」困境。「负迁移」是指模型在原本训练的领域(比如通用语料)表现不错，但换到新领域，因为语境和表达方式有差异，其性能可能会急剧下降。

举个例子，把通用 Embedding 模型用在法律合同里，用户问「这份协议的甲方有哪些权利?」模型可能找不准答案。因为它依赖「甲方」「权利」这类通用语料里的常见搭配，反而忽略了合同中真正关键的表述，比如「许可方享有下述独家授权」。结果就是，检索出一些看似相关、实则无关的内容，错过了最该提取的信息。

为破解这一难题，腾讯优图实验室正式开源Youtu-Embedding——

这是一款面向企业级应用打造的通用文本表示模型，可同时胜任文本检索、意图理解、相似度判断、分类聚类等六大主流任务，既避免了「负迁移」的性能牵制，又具备即插即用的通用性。

开源后，开发者可直接使用Youtu-Embedding构建语义检索系统，也可以基于其训练框架，结合自身业务数据继续训练，打造更贴合自身场景的语义基础能力。

这款「全能」模型，是如何炼成的？我们用了三步——

//第一步：通读3万亿Token语料，打好语言底子

模型要具备强大的理解力，第一步就是把语言底子打牢。Youtu-Embedding 并不是在开源模型上做微调，而是从零开始训练，用3万亿Token的中英文语料，打下语言理解的基本盘。

同时，我们准备了充足的「数据燃料」，包括人工精标的语义任务数据、常见中文表达的真实语料，还有用大模型辅助生成并人工筛选的合成样本。这些数据不仅数量充足、结构清晰，更关键是贴近真实业务语境，为后续多任务协同训练打下语言理解基础。

//第二步：建好语义桥梁，让模型理解真实意图

语言模型天生擅长「生成」，但语义检索、相似度判断等任务，需要的是「理解」和「判断」能力。

我们引入大规模弱监督训练，让模型从「语言建模者」转变为真正的「语义理解者」。比如，用户问「这款产品保修多久？」和问「坏了可以免费修吗？」——一句是打听政策，一句是表达问题，用词和句式有差别，但语义相近，都是在问保修期。

通过这类训练，让模型学会识别「表达不同但意图一致」的句子，在向量空间中建立准确的语义映射。

//第三步：创新微调框架，多任务协同进化

要真正落地到业务场景中，还需要模型适配具体任务的复杂规则与多样需求。比如：检索任务，需要学会判断哪个文本更接近问题；分类任务，需要给内容打上合适标签……

每种任务的训练方式不同，如果一股脑塞给模型学，轻则混淆，重则能力互相干扰。为了解决「多任务训练」的问题，我们设计了一套创新的「协同－判别式微调框架」，核心做法包括：

● 统一格式：不同语义任务（如文本相似度、文本检索）的数据结构迥异，我们用统一建模方式实现格式统一，让模型不用切换理解不同的格式，就能适应不同任务；

● 差异化训练：我们为每类任务定制专属的损失函数——相当于针对不同的任务类型，设定不同的「评分标准」。比如，检索任务中，模型只需粗略判断文本与问题「相关」或「不相关」；语义相似度任务中，则要更细致地区分「非常相似」「有点相似」「基本无关」等不同程度。通过差异化设计，模型能明确每类任务该如何被评估、该往哪个方向优化，从而更精准地提升各项能力；

● 动态采样：不同任务难度不同、重要性也不同。我们引入了动态采样机制，让模型在训练过程中按阶段「合理分配精力」。就像安排课程表一样，模型不会所有任务一股脑儿混着学，而是「有计划地轮训」——今天重点练「检索」，明天专攻「语义相似度」。这种方式能让模型在各类任务上都学得扎实，既不会顾此失彼，也避免某些任务被「偏科」训练。

Youtu-Embedding本地实测效果图

Youtu-Embedding 的实力已经获得权威检验——

在中文语义评测基准CMTEB上，此前以77.46分的综合成绩登顶，成为表现最均衡的中文语义模型之一。

Youtu-Embedding可广泛应用于企业客服、智能问答、内容推荐、知识管理等场景，尤其适用于构建RAG检索增强生成系统。

同时，Youtu-Embedding支持集成至LangChain、LlamaIndex等主流框架，「开箱即用」，降低开发门槛，帮助开发者快速构建更智能的语义应用。

九月以来，腾讯优图实验室已陆续开源了Youtu-Agent和Youtu-GraphRAG、Youtu-Embedding。

我们相信，真正好用的 AI，不止于性能的提升，更在于底层能力的持续夯实与对开发者生态的长期开放。

欢迎开发者访问GitHub获取源码、查看技术报告。详情戳下方链接：

● GitHub源码（含微调框架）：

https://github.com/TencentCloudADP/youtu-embedding.git

● Hugging Face模型下载（效果全面领先的2B量级模型）：

https://huggingface.co/tencent/Youtu-Embedding

● 论文链接：

https://arxiv.org/abs/2508.11442

老规矩，不明白的地方，记得在评论区@元宝哦！

预览时标签不可点

微信扫一扫

关注该公众号

继续滑动看下一个

轻触阅读原文

腾讯云

向上滑动看下一个

知道了

