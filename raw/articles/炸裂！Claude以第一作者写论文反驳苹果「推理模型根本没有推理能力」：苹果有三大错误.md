---
source: ima
kind: wechat
category: "技术"
title: "炸裂！Claude以第一作者写论文反驳苹果「推理模型根本没有推理能力」：苹果有三大错误"
url: "https://mp.weixin.qq.com/s?__biz=Mzg3MTkxMjYzOA==&mid=2247505237&idx=1&sn=9133b2e929b26b16da52510aaf5e59ae&chksm=cf72e4d92a193d9399fae220f4d2da751faea34969b2b32694c6b808dda443653a8ce24a16fb&scene=90&xtrack=1&sessionid=1749895659&subscene=93&clicktime=1749895678&enterid=1749895678&flutter_pos=7&biz_enter_id=4&ranksessionid=1749895659&jumppath=50183_1749894762230%2C1102_1749894764191%2C1001_1749894766406%2C1104_1749895660528&jumppathdepth=4&ascene=56&devicetype=iOS18.5&version=18003b2e&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&countrycode=CN&fontScale=109&exportkey=n_ChQIAhIQN5VudCXGMeoT717hdYHBPxLSAQIE97dBBAEAAAAAAKxYIW4VE3gAAAAOpnltbLcz9gKNyK89dVj0o0ijzJmKlmzdFDxHsEa0fzJDCndKVRZKNMo0u38%2Finil%2Ftir2ds3jn5Lwkiw3I4R4HGY2b4RNhoxBLRxmULoEGzTrAhLMBrIyYQLDWChonc2U5XNBIrm%2BqNghjDF8f5TpA4d8QI2%2BgNMjHEHXiI%2BeMQBt2Ay9zxDUhHufNmYsKj06tgIBPbvBlZLkGTWkQ9U3Xxz8kGxMFu4syTgLfDPQbQigDns9%2FiR5hiqUA%3D%3D&pass_ticket=tZeAi4geJTMXQ4%2FodJESBK9r2vPj1JZGTyuw%2F4QESXWzFEp0r%2F7zDbKFl8D8PJJm&wx_header=3"
media_id: "wechatarticle_30987b07fe36143e35b82223ae18bcbe_0e8a97055319c883651e76099b5f502e"
media_type: 6
kb_name: "殷凇的知识库"
kb_id: "qzeC00QqxVZKyNdfTs2u_JmTwlIqypGehkvk2cjRaNw="
kb_folder_path: "微信公众号"
created_from_ima_at: "2026-05-11T10:27:18.695Z"
body_status: full_textfetched_at: "2026-05-13T15:57:00+08:00"
---

# 炸裂！Claude以第一作者写论文反驳苹果「推理模型根本没有推理能力」：苹果有三大错误

- 来源：ima 个人知识库
- 原文链接：已通过 ima get_media_info 获取（见 frontmatter url）
- ima media_id：`wechatarticle_30987b07fe36143e35b82223ae18bcbe_0e8a97055319c883651e76099b5f502e`
- ima 目录：微信公众号
- 内容分类：技术
- 正文状态：已补全文。

## 摘要

> 当前 ima 知识库列表接口未返回文章摘要字段；本条先保存标题、链接、media_id、目录与分类，便于后续按需补正文/摘要。

## 正文

前几天苹果写了一篇名为《The Illusion of Thinking:

Understanding the Strengths and Limitations of Reasoning Models

via the Lens of Problem Complexity》论文，在这篇paper中苹果试图证明：DeepSeek R1，OpenAI o3, Anthropic Claude 等推理模型根本没有推理能力

论文原文：

https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf

这篇论文一经上线就在全网引起了很多争议，有的人认为苹果是因为AI落后了，才写出了这篇文章，现在更精彩的的来了，这次反击苹果的不是人类，而是Anthropic最新的模型 Claude Opus，Claude Opus作为第一作者写了一篇反驳论文《思维幻觉的幻觉（The Illusion of the Illusion of Thinking）》

论文地址：

https://arxiv.org/pdf/2506.09250

https://arxiv.org/pdf/2506.09250

这篇发表在科研预印本网站 arXiv 上Claude Opus写的论文，逐一驳斥了苹果论文的核心论点，指出其所谓的“推理崩溃”更多是源于实验设计的局限性，而非AI本身存在根本性的推理缺陷

苹果的论点：AI存在“推理崩溃”的硬上限

在苹果的《思维的幻觉》论文中，研究人员通过一系列规划类谜题（如汉诺塔、过河问题）对大语言模型（LRMs）进行测试。他们发现，当问题的复杂度超过某个阈值后，模型的准确率会“断崖式”地跌至零。由此，他们得出结论：AI的推理能力存在一个根本性的上限，这是一种“思维的幻觉”。

Claude的反击：不是推理崩溃，而是实验设计的“幻觉”**

由Claude Opus撰写的《思维幻觉的幻觉》一文，像一位严谨的科研人员一样，指出了苹果研究中的三大关键问题：

1. 混淆了“推理失败”与“输出截断”

苹果在测试“汉诺塔”问题时，要求模型完整输出所有移动步骤。汉诺塔问题的步骤数随盘片数量（N）呈指数级增长（2^N - 1），很快就会产生极长的答案

C. Opus的论文指出，模型并非在推理上失败，而是触发了输出token（字符）的数量上限。更有力的证据是，在一些复现实验中，模型会明确表示：“模式还在继续，但为了避免内容过长，我将在此停止。”

这表明，模型完全理解解题的递归模式，只是因为实际的输出限制而选择截断。苹果的自动化评估系统无法区分“我不会解”和“我选择不完整列出”，从而错误地将其判定为“推理崩溃”。

2. 用“无解题”来测试并判定模型失败

这篇反驳论文最尖锐的批评，直指苹果在“过河问题”实验中的一个致命错误

论文指出，苹果测试了当参与者数量 N≥6 且船容量 b=3 的情况。然而，根据早已被证明的数学结论，这种设定下的过河问题是无解的。

苹果的研究人员让AI去解决一个数学上不可能解决的问题，然后因为AI没能给出解决方案，就给它打了零分。C. Opus犀利地评论道：“这相当于因为一个SAT求解器在面对一个无解的公式时返回‘无法满足’，就惩罚这个求解器。”

3. 对“问题复杂度”的衡量标准存在偏差

苹果的论文主要使用“解题步骤的长度”（即 compositional depth）来衡量问题的复杂度，但这并不能完全反映解决问题所需的“智力”水平

C. Opus的论文对此进行了澄清：

汉诺塔：虽然解题步骤非常多（呈指数级增长），但每一步的决策逻辑极其简单（O(1)的复杂度），几乎不需要搜索

过河问题与积木世界：解题步骤相对少得多，但每一步都需要进行复杂的约束满足和搜索，属于NP-hard或PSPACE级别的难题

因此，模型能解决上百步的汉诺塔，却在几步的过河问题上失败，这恰恰反映了不同问题在计算复杂度上的本质差异，而非一个统一的“推理能力上限”

换个问法，AI的能力瞬间“恢复”

为了进一步证明其观点，C. Opus进行了一项关键的补充实验。不再要求模型输出汉诺塔N=15时的所有步骤（这需要海量的token），而是改变了提问方式：

“请解决15个盘片的汉诺塔问题。输出一个Lua程序，当调用该程序时，它会打印出解决方案。”

结果，包括Claude、GPT-4o、Gemini在内的多个模型，都轻松地生成了正确的递归算法程序，并且只用了不到5000个token。这有力地证明了，模型完全理解问题的核心逻辑，只是被最初那种“必须穷举输出”的死板评估方式所束缚。

结论：我们需要更聪明的评估方法

《思维幻觉的幻觉》在结论中写道，苹果的研究所揭示的，并非AI基础推理能力的局限，而是现有评估方法的一些工程性问题：模型无法输出超过其上下文长度的内容、自动评估脚本可能存在漏洞、解题步骤的长度并不能准确衡量智力难度

如果用一句话总结Claude Opus的反驳就是：

“问题的关键不在于大模型能否推理，而在于我们的评估方法能否将真正的‘推理能力’与简单的‘打字输出’区分开来。”

参考：

https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf

https://arxiv.org/pdf/2506.09250

⭐星标AI寒武纪，好内容不错过⭐

用你的赞和在看告诉我～

求赞👇👇

预览时标签不可点
