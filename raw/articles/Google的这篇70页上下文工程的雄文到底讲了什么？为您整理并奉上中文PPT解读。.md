---
source: ima
kind: wechat
category: "技术"
title: "Google的这篇70页上下文工程的雄文到底讲了什么？为您整理并奉上中文PPT解读。"
url: "https://mp.weixin.qq.com/s?__biz=Mzk1NzQ1ODk5NQ==&mid=2247524703&idx=1&sn=c43f386c7e612ae0e763b36e71868db9&chksm=c2ebac5656f35b4ed83cea50ef3300addef5940a75293058066f45a10b23eeafaf4f563c6722&mpshare=1&scene=1&srcid=1204QGNwPSKgrmFLYPNBLob3&sharer_shareinfo=6e98b786e79d18591e5a7717051a4f27&sharer_shareinfo_first=5b77be8411147aa5b087325a2e9743e2&from=groupmessage&isappinstalled=0&clicktime=1765098406&enterid=1765098406&ascene=1&devicetype=iOS18.7.2&version=18004227&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&countrycode=CN&fontScale=109&exportkey=n_ChQIAhIQ763JJwJ9kclMX8dTegFFMRLoAQIE97dBBAEAAAAAAO2EK2dkjcIAAAAOpnltbLcz9gKNyK89dVj0O4q1am5kbn%2FO02Y9HOt7T3mxi%2FUdA%2BsmDskFO4T9mLvnu9D%2BgAT1BXFA22LWOUyWnjNy1xVZcwzHR4c3pd6K3pXvOJzKewPKZBvfF88vqPNsqFIdxMu0loVSdNJSBO7JWc3sMtwWJrPCDYGQrsGTzFqea7rsoBMd4gwgpEqjH2SYZ8zbwpiik0w%2B6O4v85UVuLSqgHdhQ2Pl2TPTEyDYoT5AnF%2FzySES5ASNn09jlb8OqtQXZvmr1i6cVDCdy3RavMY%3D&pass_ticket=c71bAfp1mgq1E3Y7QO1blpJhcpCHkPNPe96OVL0E0d%2FHfQnPQJXxAiKuFYxGiA1E&wx_header=3"
media_id: "wechatarticle_30987b07fe36143e35b82223ae18bcbe_70463860ee32aedb6264f65905c9a529"
media_type: 6
kb_name: "殷凇的知识库"
kb_id: "qzeC00QqxVZKyNdfTs2u_JmTwlIqypGehkvk2cjRaNw="
kb_folder_path: "/"
created_from_ima_at: "2026-05-11T10:27:18.695Z"
body_status: "full_text"
fetched_at: "2026-05-14T00:37:00Z"
---

# Google的这篇70页上下文工程的雄文到底讲了什么？为您整理并奉上中文PPT解读。

- 来源：ima 个人知识库
- 原文链接：https://mp.weixin.qq.com/s?__biz=Mzk1NzQ1ODk5NQ==&mid=2247524703&idx=1&sn=c43f386c7e612ae0e763b36e71868db9&chksm=c2ebac5656f35b4ed83cea50ef3300addef5940a75293058066f45a10b23eeafaf4f563c6722&mpshare=1&scene=1&srcid=1204QGNwPSKgrmFLYPNBLob3&sharer_shareinfo=6e98b786e79d18591e5a7717051a4f27&sharer_shareinfo_first=5b77be8411147aa5b087325a2e9743e2&from=groupmessage&isappinstalled=0&clicktime=1765098406&enterid=1765098406&ascene=1&devicetype=iOS18.7.2&version=18004227&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&countrycode=CN&fontScale=109&exportkey=n_ChQIAhIQ763JJwJ9kclMX8dTegFFMRLoAQIE97dBBAEAAAAAAO2EK2dkjcIAAAAOpnltbLcz9gKNyK89dVj0O4q1am5kbn%2FO02Y9HOt7T3mxi%2FUdA%2BsmDskFO4T9mLvnu9D%2BgAT1BXFA22LWOUyWnjNy1xVZcwzHR4c3pd6K3pXvOJzKewPKZBvfF88vqPNsqFIdxMu0loVSdNJSBO7JWc3sMtwWJrPCDYGQrsGTzFqea7rsoBMd4gwgpEqjH2SYZ8zbwpiik0w%2B6O4v85UVuLSqgHdhQ2Pl2TPTEyDYoT5AnF%2FzySES5ASNn09jlb8OqtQXZvmr1i6cVDCdy3RavMY%3D&pass_ticket=c71bAfp1mgq1E3Y7QO1blpJhcpCHkPNPe96OVL0E0d%2FHfQnPQJXxAiKuFYxGiA1E&wx_header=3
- ima media_id：`wechatarticle_30987b07fe36143e35b82223ae18bcbe_70463860ee32aedb6264f65905c9a529`
- ima 目录：/
- 内容分类：技术
- 正文状态：已抓取全文。

## 摘要

> 当前 ima 知识库列表接口未返回文章摘要字段；本条先保存标题、链接、media_id、目录与分类，便于后续按需补正文/摘要。

## 正文

Google的这篇70页上下文工程的雄文到底讲了什么？为您整理并奉上中文PPT解读。

原创

秋山墨客
秋山墨客

AI大模型应用实践

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

点击上方

蓝字

关注我们

Google 在上月发布了一篇重要的上下文工程白皮书  《Context Engineering: Sessions & Memory》 ，系统阐述了上下文工程的核心理念，以及构建智能 Agent 的两大基础： 会话（Sessions）  与  记忆（Memory） 。这篇文档不仅给出了理论框架，也为如何打造更聪明、更个性化、可持续学习的 AI Agent 提供了实践指南，是一篇很好的学习文章。
我们基于原文进行了 精读、翻译与结构化整理 ，形成了这套精简版解读 PPT（是的，借助了Nano Banana Pro），帮助读者更轻松地理解上下文工程的关键思想与应用方法。
【本文PPT文件获取方法在文末】

公众号发送消息“google”，下载本PPT文档
本PPT仅限交流学习，未经本公众号书面授权，
禁止任何形式的转载、改编或商业使用。
创作不易， 点赞转发 是对我们的最大支持。

END

加入公众号交流群（说明来意）

预览时标签不可点

微信扫一扫
关注该公众号

AI大模型应用实践

知道了

微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序

赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过
