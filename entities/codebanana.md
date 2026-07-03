---
title: CodeBanana
created: 2026-07-03
updated: 2026-07-03
type: entity
tags: [tool, agent, management, company]
sources: [raw/articles/超级个体时代｜腾讯研究院3万字报告_腾讯新闻.md, raw/articles/如何把超级个体的产能，转化成组织能力？ AI跃迁者调研_腾讯新闻.md]
confidence: medium
---

# CodeBanana

## 概述

[[li-zhifei]] 为出门问问（[[mobvoi]]）自研的 AI 原生组织操作系统。核心理念：**「沟通在哪里，执行就在哪里」**——将管理沟通（IM）和任务执行（Coding Agent）合二为一。李志飞称之为「组织容器」而非个人 Copilot。^[raw/articles/如何把超级个体的产能，转化成组织能力？ AI跃迁者调研_腾讯新闻.md]

## 设计理念

企业工作分两大类：管理沟通（开会、项目管理）和任务执行（写代码、做交付）。飞书/企业微信解决前者，Cursor/Claude 等解决后者。CodeBanana 将两者合并——**任务、讨论、Agent、文件、权限和运行环境在同一项目空间**。

核心原则：**「未来绝大部分人包括 CEO，某种程度上都在配合 AI 干活。」**

## 产品架构

### 三区域布局
每个项目有三个区域：
1. **Discussion**：人类聊天区
2. **Team Agent**：共享 Coding Agent 工作空间
3. **Private Ask**：先私聊再公开

### 关键功能
- **Agent 作为正式员工**：有 A2A 通讯（Agent-to-Agent）、Skill 商店、Teams.md 通讯录、Dashboard 量化指标
- **每个项目有独立文件系统和虚拟机**
- **项目 = 群聊 = Agent 工作空间 = 共享文件系统**
- **三端**：桌面端、手机端、云端版/本地版
- **心跳机制**：Agent 主动行为如自动总结日报、跟踪 bug 全流程
- **Dashboard**：量化 AI First、组织扁平、全栈、原型工作流、多 Agent 协作等维度

## 与超级团队的对应

CodeBanana 是实现 [[super-team]] 中 **AI 中枢型**形态的组织基础设施。AI 承担协调中介角色——任务分配、信息同步、决策路由通过 AI 完成。人围绕 Agent 工作，Agent 不围绕人工作。

## 组织效应

- 非产研用得比产研更好：控制权还给需求方
- 全栈转型的铁腕工具：不允许不用
- 「员工互发消息都经 AI 加工，人类的消息不会直接到达另一个人类」
- 系统筛选人：谁用得好自然浮现，不用纠结先裁员还是先转型

## 商业状态

- 研发投入六七成甚至 80% 投在 CodeBanana 上
- 营收非常少，商业验证仍在早期
- 内部效率已验证：组织效率约 4-5 倍

## 相关实体

- [[li-zhifei]] — 创建者
- [[mobvoi]] — 所属公司

## 相关概念

- [[super-team]] — CodeBanana 是 AI 中枢型超级团队的实现基座
- [[system-designer]] — CodeBanana 上的新角色
- [[prototype-driven-workflow]] — CodeBanana 支持的工作流
- [[ai-native-organization]] — AI Native 组织的工具层
- [[organization-competitiveness-formula]] — CodeBanana 降低组织摩擦
- [[super-individual]] — CodeBanana 将超级个体能力转化为组织能力
