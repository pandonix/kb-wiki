---
source: ima
kind: wechat
category: "技术"
title: "解决特斯拉「监督稀疏」难题，DriveVLA-W0用世界模型放大自动驾驶Data Scaling Law"
url: "https://mp.weixin.qq.com/s?chksm=84e6d0e0b39159f6e06c51a14831612c700610930871d09bbd1233f80a30e10c3a0ad813effb&exptype=subscribed_close_feeds_exper_tlfeeds&ranksessionid=1763422929_2&req_id=1763422941019122&scene=169&mid=2651002014&sn=025f400e7456628a21519627321a47a7&idx=3&__biz=MzA3MzI4MjgzMw%3D%3D&sessionid=1763422929&subscene=200&clicktime=1763423031&enterid=1763423031&flutter_pos=18&biz_enter_id=5&jumppath=20020_1763422944879%2C1104_1763422956762%2C20020_1763422981264%2C1104_1763423024877&jumppathdepth=4&ascene=56&devicetype=iOS18.7.2&version=18004129&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&countrycode=CN&fontScale=109&exportkey=n_ChQIAhIQl9LEPTObJYIZyjHaSofNsBLUAQIE97dBBAEAAAAAAF8kLxdFbzIAAAAOpnltbLcz9gKNyK89dVj0ZdYQ258nwQwX2V8gjr9FUvK31xHIic6cQeBtvo9i49fk2tbDgZ9NLL2Lmt6J9ytsgySjAn8FzR7Ham41V9i2iBuG6DbiHU7um5%2FiSItrF8xZlllwG3ped1yC2vRyTAzVYSJ2jbTK4A7MiLmVRUjKEzleHXpCAcyRFUjlA3ltfUbjFUIkixhv%2BDcfTF2wNBMv8kAd08YJuGnGu4cKalRRVdoI%2FeOYhHdHbnruW%2BqA&pass_ticket=%2Bf18J%2BBaBPcHE6ZHLiaVkeFKDo5FlupP5n71DVq8WW0macshbaB%2Fr8C%2FeTgsC5sz&wx_header=3"
media_id: "wechatarticle_30987b07fe36143e35b82223ae18bcbe_fdf5851d0bc12ac2a54826e85f7f43c5"
media_type: 6
kb_name: "殷凇的知识库"
kb_id: "qzeC00QqxVZKyNdfTs2u_JmTwlIqypGehkvk2cjRaNw="
kb_folder_path: "/"
created_from_ima_at: "2026-05-11T10:27:18.695Z"
body_status: full_text
fetched_at: "2026-05-12T19:17:00+08:00"
---

# 解决特斯拉「监督稀疏」难题，DriveVLA-W0用世界模型放大自动驾驶Data Scaling Law

- 来源：ima 个人知识库
- 原文链接：https://mp.weixin.qq.com/s?chksm=84e6d0e0b39159f6e06c51a14831612c700610930871d09bbd1233f80a30e10c3a0ad813effb&exptype=subscribed_close_feeds_exper_tlfeeds&ranksessionid=1763422929_2&req_id=1763422941019122&scene=169&mid=2651002014&sn=025f400e7456628a21519627321a47a7&idx=3&__biz=MzA3MzI4MjgzMw%3D%3D&sessionid=1763422929&subscene=200&clicktime=1763423031&enterid=1763423031&flutter_pos=18&biz_enter_id=5&jumppath=20020_1763422944879%2C1104_1763422956762%2C20020_1763422981264%2C1104_1763423024877&jumppathdepth=4&ascene=56&devicetype=iOS18.7.2&version=18004129&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&countrycode=CN&fontScale=109&exportkey=n_ChQIAhIQl9LEPTObJYIZyjHaSofNsBLUAQIE97dBBAEAAAAAAF8kLxdFbzIAAAAOpnltbLcz9gKNyK89dVj0ZdYQ258nwQwX2V8gjr9FUvK31xHIic6cQeBtvo9i49fk2tbDgZ9NLL2Lmt6J9ytsgySjAn8FzR7Ham41V9i2iBuG6DbiHU7um5%2FiSItrF8xZlllwG3ped1yC2vRyTAzVYSJ2jbTK4A7MiLmVRUjKEzleHXpCAcyRFUjlA3ltfUbjFUIkixhv%2BDcfTF2wNBMv8kAd08YJuGnGu4cKalRRVdoI%2FeOYhHdHbnruW%2BqA&pass_ticket=%2Bf18J%2BBaBPcHE6ZHLiaVkeFKDo5FlupP5n71DVq8WW0macshbaB%2Fr8C%2FeTgsC5sz&wx_header=3
- ima media_id：`wechatarticle_30987b07fe36143e35b82223ae18bcbe_fdf5851d0bc12ac2a54826e85f7f43c5`
- ima 目录：/
- 内容分类：技术
- 正文状态：暂存元数据，尚未批量抓取正文。

## 摘要

> 当前 ima 知识库列表接口未返回文章摘要字段；本条先保存标题、链接、media_id、目录与分类，便于后续按需补正文/摘要。

## 正文

在自动驾驶领域，VLA 大模型正从学术前沿走向产业落地的 “深水区”。近日，特斯拉（Tesla）在 ICCV 的分享中，就将其面临的核心挑战之一公之于众 ——“监督稀疏”。

这一问题直指当前 VLA 模型的 “七寸”：其输入是高维、稠密的视觉信息流，但其监督信号却往往是低维、稀疏的驾驶动作（如路径点）。那么即便使用 PB 级的海量数据，VLA 模型的巨大潜力也无法被有效释放。

正当业界热议这一瓶颈时，一支来自国内顶尖学术机构与华为合作的团队，已经悄然给出了破解这一难题的 “锦囊”。一篇名为 《DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving》 的新工作，为解决这一 “监督稀疏” 提供了极具洞见的解决方案。该研究提出，世界模型（World Model）是解锁 VLA 数据规模定律（Data Scaling Law）的关键钥匙。

论文标题：DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving

论文链接：https://arxiv.org/abs/2510.12796

VLA 的 “监督赤字”：Data Scaling Law 为何在自动驾驶失效？

自动驾驶领域的研究者普遍希望复现 Data Scaling Law 在 LLM 上的成功：通过扩大模型参数和数据规模，实现自动驾驶性能的飞跃。

但 DriveVLA-W0 指出，VLA 模型面临着与 LLM 截然不同的困境：“监督赤字”（Supervision Deficit）。

一个数十亿参数的 VLA 模型，其输入是高维、稠密的视觉信息流，但其监督信号却往往是低维、稀疏的驾驶动作（如路径点）。模型的大部分表征能力被浪费，导致其无法充分学习驾驶环境的复杂动态。

研究团队的实验证实了这一点：在稀疏的动作监督下，VLA 模型的性能会随着数据量的增加迅速饱和，Data Scaling Law 的效应在此大打折扣。

破解之道：用世界模型提供 “稠密” 的自监督信号

如何填补这一 “赤字”？DriveVLA-W0 的答案是：与其依赖稀疏的 “动作”，不如让模型学习稠密的 “世界”。

研究团队创造性地引入了世界模型，将 “预测未来图像” 作为一项稠密的自监督训练任务。

传统 VLA（左）仅依赖稀疏的动作监督。DriveVLA-W0（右）则额外引入了稠密的视觉预测任务，迫使模型理解环境。

当模型被要求去预测下一帧的完整视觉画面时，它必须去学习和理解这个世界的真实运行规律 —— 例如，其他车辆的运动趋势、行人与车辆的交互关系等。

这一设计为 VLA 模型提供了远比 “动作” 更丰富和稠密的学习信号，从根本上缓解了 “监督赤字” 问题。

核心贡献：世界模型 “放大” 了 Data Scaling Law

如果说解决 “监督赤字” 是这项工作的起点，那么其更核心的贡献在于发现了：世界模型能够显著 “放大”（Amplifies）数据规模定律。

在 700K 到 70M 的数据规模上，DriveVLA-W0（红线）的性能提升斜率显著优于基线（蓝线），展现了更强的扩展潜力。

研究团队在高达 7000 万帧的内部大规模数据集上进行了严格的 Scaling 实验。结果清晰地显示：

基线模型（仅动作监督）： 随着数据量增大，性能提升迅速放缓。

DriveVLA-W0（世界模型）： 性能随着数据量增加，实现了持续且显著的提升，与基线模型的性能差距越拉越大。

在 70M 帧的规模下，世界模型的加入，使模型的碰撞率降低了 20.4%。这证明了世界模型带来的 “质变”，是单纯堆砌动作数据所无法企及的。

兼顾性能与效率：轻量级 MoE 专家

DriveVLA-W0 并非一个不考虑落地的 “学术模型”。针对 VLA 大模型在自动驾驶中面临的 “高延迟” 痛点，团队还提出了一种轻量级的 MoE “动作专家”（Action Expert）架构 。

该设计在不牺牲性能的前提下，显著降低了模型的推理延迟，仅为基线 VLA 的 63.1% ，为 VLA 模型的实时部署提供了可能。

结语

这项研究工作不仅为特斯拉等行业先行者提出的 “真问题” 提供了清晰的解题思路，也为自动驾驶乃至整个具身智能领域，展示了世界模型在 “生成” 之外的另一条核心价值路径 —— 作为强大的自监督引擎，撬动 VLA 模型的 Data Scaling Law。

© THE END

转载请联系本公众号获得授权

投稿或寻求报道：liyazhou@jiqizhixin.com
