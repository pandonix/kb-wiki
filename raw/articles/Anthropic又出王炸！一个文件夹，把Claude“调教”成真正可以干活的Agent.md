---
source: ima
kind: wechat
category: "技术"
title: "Anthropic又出王炸！一个文件夹，把Claude“调教”成真正可以干活的Agent"
url: "https://mp.weixin.qq.com/s?__biz=Mzg3MTkxMjYzOA==&mid=2247508677&idx=1&sn=c90297804afd4aa3b576748cce036d52&chksm=cfb18d7fc6cb32478f66eee42c580db278b46ab83b9097659b35dfb6427d71edd5f0acab2c42&scene=90&xtrack=1&sessionid=1760753860&subscene=93&clicktime=1760753894&enterid=1760753894&flutter_pos=1&biz_enter_id=4&ranksessionid=1760753662&jumppath=20020_1760753863645%2CWAWebViewController_1760753868181%2C20020_1760753889000%2C1104_1760753889585&jumppathdepth=4&ascene=56&devicetype=iOS18.6.2&version=18004029&nettype=3G+&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&countrycode=CN&fontScale=109&exportkey=n_ChQIAhIQd4Dqlz3Lcgy089aSPjPOHBLUAQIE97dBBAEAAAAAAJplBbWRUFwAAAAOpnltbLcz9gKNyK89dVj0%2Bm1zNPdz7lrA7tBMPqB4zYmZ0ZekEJfRh6a6oeteV3hpz%2BUVmtkxJbSHwwJwO0oR3MJ60VSbmJz8FfBQThZpLg%2BwqJxsX%2Fl4KdTgzH71EpeYg%2F2XqqogSqQnMPO%2F%2FSWh4ma4TIQffiHFVc2v8%2BLbKLNGft0OXX82wo9Eh%2BrnpMfBtiF0Cq3p6XjsyiP%2BuTfnkKTnGCbXxdRQkOARlNKIlgMyJWO5UYOXjb5tKAng&pass_ticket=JY9C49mpHc2BEyrnaCQZHg3EOSho1IgN%2F%2B0Hl%2B9lGT36NoMHOjndzot2n0vpqAOf&wx_header=3"
media_id: "wechatarticle_30987b07fe36143e35b82223ae18bcbe_d9aedafd3dbe2ed67f64c539dcfe5dc8"
media_type: 6
kb_name: "殷凇的知识库"
kb_id: "qzeC00QqxVZKyNdfTs2u_JmTwlIqypGehkvk2cjRaNw="
kb_folder_path: "/"
created_from_ima_at: "2026-05-11T10:27:18.695Z"
body_status: "full_text"
fetched_at: "2026-05-13T18:17:00Z"
---

# Anthropic又出王炸！一个文件夹，把Claude“调教”成真正可以干活的Agent

- 来源：ima 个人知识库
- 原文链接：https://mp.weixin.qq.com/s?__biz=Mzg3MTkxMjYzOA==&mid=2247508677&idx=1&sn=c90297804afd4aa3b576748cce036d52&chksm=cfb18d7fc6cb32478f66eee42c580db278b46ab83b9097659b35dfb6427d71edd5f0acab2c42&scene=90&xtrack=1&sessionid=1760753860&subscene=93&clicktime=1760753894&enterid=1760753894&flutter_pos=1&biz_enter_id=4&ranksessionid=1760753662&jumppath=20020_1760753863645%2CWAWebViewController_1760753868181%2C20020_1760753889000%2C1104_1760753889585&jumppathdepth=4&ascene=56&devicetype=iOS18.6.2&version=18004029&nettype=3G+&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&countrycode=CN&fontScale=109&exportkey=n_ChQIAhIQd4Dqlz3Lcgy089aSPjPOHBLUAQIE97dBBAEAAAAAAJplBbWRUFwAAAAOpnltbLcz9gKNyK89dVj0%2Bm1zNPdz7lrA7tBMPqB4zYmZ0ZekEJfRh6a6oeteV3hpz%2BUVmtkxJbSHwwJwO0oR3MJ60VSbmJz8FfBQThZpLg%2BwqJxsX%2Fl4KdTgzH71EpeYg%2F2XqqogSqQnMPO%2F%2FSWh4ma4TIQffiHFVc2v8%2BLbKLNGft0OXX82wo9Eh%2BrnpMfBtiF0Cq3p6XjsyiP%2BuTfnkKTnGCbXxdRQkOARlNKIlgMyJWO5UYOXjb5tKAng&pass_ticket=JY9C49mpHc2BEyrnaCQZHg3EOSho1IgN%2F%2B0Hl%2B9lGT36NoMHOjndzot2n0vpqAOf&wx_header=3
- ima media_id：`wechatarticle_30987b07fe36143e35b82223ae18bcbe_d9aedafd3dbe2ed67f64c539dcfe5dc8`
- ima 目录：/
- 内容分类：技术
- 正文状态：已抓取全文。

## 摘要

> 当前 ima 知识库列表接口未返回文章摘要字段；本条先保存标题、链接、media_id、目录与分类，便于后续按需补正文/摘要。

## 正文

[图片]

前几天OpenAI推出了拖拽式构建Agent方案，感觉大家普遍不是很看好，今天Anthropic也推出了一项名为Agent Skills（智能体技能）的重磅新功能，可以快速构建专属领域的Agent，这个方案概念非常清晰简单，可执行性又强，分享给大家看看

这段时间我写文章介绍了对构建Agent至关重要的的上下文工程，这篇文章Agent下半场！比Prompt更重要的是「上下文工程」，Anthropic首次系统阐述和这篇LangChain联合Manus季逸超最新分享！也许当前最好的「上下文工程」讲解目前都受到了大家的强烈关注，今天Anthropic这套方法可以说是契合了这两篇文章的最佳实践

简单来说，Agent Skills一个全新的、使用文件和文件夹来构建专业智能体的方法。

尽管Claude模型本身已经很强大，但要完成真实世界的工作，还需要程序化知识和组织背景。Agent Skills的出现，正是为了解决这一问题

现在，任何人都可以像为新员工准备“入职指南”一样，将自己的专业知识、操作流程和资源打包成可组合的“技能”，动态地加载给Claude，从而将一个通用的AI智能体，转变为满足特定需求的专属专家。

这项新功能的核心是什么？它具体如何运作？官方给出了详细解读

[图片]

什么是Agent Skills？

一个Agent Skill，本质上是一个包含SKILL.md文件的目录。这个目录里可以整理指令、脚本和各类资源，为智能体赋予额外的能力。

开发者不再需要为每个应用场景构建碎片化、一次性的定制智能体。通过Agent Skills，他们可以捕捉和共享程序化知识，用可组合的能力来让通用智能体变得专业化

激活技能非常简单：只需编写一个包含自定义指导的SKILL.md文件

技能的三个层次：渐进式披露是核心

官方通过一个为Claude增强PDF编辑能力的真实案例，展示了Agent Skills的内部构造

第一层：元数据（Metadata）

一个技能的核心是SKILL.md文件。该文件必须以YAML Frontmatter开头，包含两个必需的元数据：name（名称）和description（描述）

[图片]

在启动时，智能体会预加载所有已安装技能的名称和描述到其系统提示（system prompt）中

这便是“渐进式披露”的第一层：它只提供足够的信息，让Claude知道在什么情况下该使用哪个技能，而无需将所有技能的详细内容全部加载到上下文中

第二层：核心指令（SKILL.md主体内容）

当Claude根据当前任务，判断某个技能是相关的，它就会读取该技能的SKILL.md文件的完整内容，并将其加载到上下文中。这是披露的第二个层次

第三层：外部引用文件

当技能变得复杂，单一的SKILL.md文件可能不足以容纳所有内容，或者某些内容仅在特定场景下才需要。这时，开发者可以在技能目录中捆绑其他文件，并在SKILL.md中通过文件名引用它们。

这些被引用的文件构成了第三层（及更深层）的细节。Claude可以根据需要自主导航和发现这些信息。

在官方的PDF技能示例中，SKILL.md文件引用了reference.md和forms.md两个附加文件。将PDF表单填写的具体指令移入了forms.md，保持了核心技能文件的精简，并相信Claude只在需要填写表单时才会去读取它

[图片]

渐进式披露（Progressive disclosure）是Agent Skills设计的核心原则。它就像一本组织良好的手册，从目录（元数据），到具体章节（SKILL.md主体），再到详细附录（引用的文件），让Claude只在需要时加载必要信息

[图片]

官方强调，对于拥有文件系统和代码执行工具的智能体来说，它们无需在处理任务时将技能的全部内容读入上下文窗口。这意味着，一个技能可以捆绑的上下文数量实际上是无限的

技能如何被触发和执行？

用一张图清晰展示技能在上下文窗口中的触发流程：

[图片]

1.初始状态：上下文窗口包含核心系统提示、所有已安装技能的元数据，以及用户的初始消息

2.触发技能：Claude认为PDF技能相关，于是调用Bash工具读取pdf/SKILL.md文件的内容

3.读取附加文件：在处理任务过程中，Claude决定进一步读取该技能捆绑的forms.md文件

4.执行任务：在加载了PDF技能的相关指令后，Claude继续处理用户的任务

技能与代码执行

除了文本指令，Skills还可以包含代码，供Claude在适当时作为工具来执行

虽然大语言模型擅长许多任务，但某些操作（如对列表进行排序）使用传统代码执行会更高效、成本更低。此外，许多应用需要代码才能提供的确定性可靠性。

在PDF技能的例子中，技能包里包含一个预先编写好的Python脚本，用于读取PDF并提取所有表单字段。Claude可以直接运行这个脚本，而无需将脚本或PDF文件本身加载到上下文窗口中。由于代码是确定性的，这个工作流保证了一致性和可重复性

[图片]

如何开发和评估自己的技能？

Anthropic官方给出了四条实践指南：

1.从评估开始：在代表性任务上运行你的智能体，观察它在哪些地方遇到困难或需要额外上下文，以此确定其能力差距。然后，逐步构建技能来弥补这些不足

2.为规模化而设计：当SKILL.md文件变得臃肿时，将其内容拆分到不同文件中并进行引用。如果某些上下文是互斥或很少一起使用，保持路径分离可以减少Token消耗。代码既可以作为可执行工具，也可以作为文档。要明确Claude应该直接运行脚本，还是将其作为参考读入上下文

3.从Claude的视角思考：监控Claude在真实场景中如何使用你的技能，并根据观察进行迭代。注意技能的name和description，这是Claude决定是否触发该技能的关键

4.与Claude一起迭代：在与Claude合作完成任务时，可以要求它将成功的方法和常见的错误总结成可重用的上下文和代码，并固化到一个技能中。如果它在使用技能时偏离了轨道，让它自我反思，这能帮助你发现它真正需要的上下文。

安全注意事项

由于Skills通过指令和代码为Claude提供新能力，恶意的技能可能会在使用环境中引入漏洞，或引导Claude泄露数据、执行意外操作。

官方建议：

只从受信任的来源安装技能

在使用来自不太可信来源的技能前，进行彻底审计。检查文件内容、代码依赖项以及图像或脚本等捆绑资源

特别注意技能中指示Claude连接到潜在不受信任的外部网络源的指令或代码。

写在最后

目前，Agent Skills已在Claude.ai、Claude Code、Claude Agent SDK和Claude开发者平台全面支持。

Anthropic表示，未来几周将继续增加新功能，支持技能的创建、编辑、发现、共享和使用的完整生命周期

更长远地，Anthropic希望智能体能够自主创建、编辑和评估技能，将自己的行为模式固化为可重用的能力。

总而言之，Agent Skills是一个概念简单、格式也简单的功能，这种简单性使得组织、开发者和最终用户都能更容易地构建定制化的智能体，并赋予它们新的能力

Skill文档：

https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview

使用指南：

https://github.com/anthropics/claude-cookbooks/tree/main/skills
