---
source: ima
kind: wechat
category: "技术"
title: "Claude_Code_Mastery_Agentic_Evolution.pdf"
url: ""
media_id: "pdf_30987b07fe36143e35b82223ae18bcbe_09b740ecb2110c43652fe5e2bcfe7fe20019f2a9d9404bc5"
media_type: 1
kb_name: "殷凇的知识库"
kb_id: "qzeC00QqxVZKyNdfTs2u_JmTwlIqypGehkvk2cjRaNw="
kb_folder_path: "/"
created_from_ima_at: "2026-05-11T10:27:18.695Z"
body_status: full_text
fetched_at: "2026-05-14T06:05:24+08:00"
---

# Claude_Code_Mastery_Agentic_Evolution.pdf

- 来源：ima 个人知识库
- 原文链接：（ima 未返回 URL）
- ima media_id：`pdf_30987b07fe36143e35b82223ae18bcbe_09b740ecb2110c43652fe5e2bcfe7fe20019f2a9d9404bc5`
- ima 目录：/
- 内容分类：技术
- 正文状态：已补全文（PDF OCR）。

## 摘要

> 当前 ima 知识库列表接口未返回文章摘要字段；本条先保存标题、链接、media_id、目录与分类，便于后续按需补正文/摘要。

## 正文

### Page 1

精通 Claude Code：从高效实践到范式革新

面向 Agentic 编程时代的战略手册

NotebookLM

### Page 2

超越“提示与祈祷”：构建全新的协作心智模型

Claude Code 不仅仅是一个工具，更是一种新型的合作者——一位“住在终端里的专家同事”。真正的精通需要从“提示与祈祷”式的交互，转变为一种结构化的、战略性的协作关系。本次分享将通过四个递进的阶段，引领您完成这一心智模型的转变。

工具使用者（Tool User）

单向命令-响应交互  
(Unidirectional Command-Response Interaction)

AI 协作者（AI Collaborator）

结构化协作与反馈循环  
(Structured Collaboration & Feedback Loops)

“Claude Code is like that co-worker that does everything on the terminal. It’s the sort of person that just never touches the GUI. They’re a whiz.” - Cal, Anthropic

NotebookLM

### Page 3

第一阶段：奠定根基

CLAUDE.md：为项目注入“记忆”与“规则”

`CLAUDE.md` 是最关键的文件，是项目的记忆库和规则手册。Claude 在会话开始时会自动读取它，从而理解项目特有的规范、架构和工作流。

层级结构（Hierarchy）  
Claude 会按顺序读取：`~/.claude/CLAUDE.md`（全局） -> 项目根目录/CLAUDE.md -> 子目录/CLAUDE.md。

核心要素（Key Elements）  
明确项目的风格指南、核心架构、常用命令和“禁止事项”。

健全性检查（Sanity Check）  
在 `CLAUDE.md` 顶部写下你的名字，然后向 Claude 提问 “What is my name?” 来快速验证配置是否生效。

```md
# My name is {NAME}
# This file provides guidance to Claude Code when
working with this repository.

## Code Style
- Use TypeScript everywhere.
- Functional components with hooks only.
- Follow ES module (import/export) syntax.

## Core Architecture
- State management: Zustand.
- API client lives in /src/utils/api.ts.
- All new components must have corresponding tests.

## Common Commands
- `npm run dev`: Start the development server.
- `npm run test`: Run the full test suite.

## Prohibitions
- IMPORTANT: Do not use class components.
- YOU MUST NOT bypass the primary error boundary.
```

NotebookLM

### Page 4

第一阶段：奠定根基

掌控交互：从安全默认到流畅自主

Claude 默认会为每个修改操作请求许可，这是为了安全。但我们可以通过精心配置，在保证安全的前提下实现更流畅的工作流。

- 自定义许可（Customizing Permissions）  
在 `.claude/settings.local.json` 文件中，为常用且安全的操作授权，例如 `Edit`（文件编辑）和 `Bash(git commit:**)`（git 提交）。永远不要允许 `rm` 或 `bash *`。

- 安装 CLI 工具（Install CLI Tools）  
安装 `gh`（GitHub CLI）等工具，Claude 知道如何使用它们来管理 Issues 和 PR，极大地扩展其能力。

- 安全“YOLO 模式”（Safe "YOLO Mode"）  
在开发容器（Dev Container）中，可以使用 `--dangerously-skip-permissions` 标志，让 Claude 在一个隔离的环境中完全自主运行，实现最高效率。

Before: 默认流程

请求许可?  
请求许可?  
请求许可?  
请求许可?  
请求许可?

任务开始  
任务完成

配置  
`settings.local.json`

After: 优化的工作流

任务开始

安全 “YOLO 模式”

NotebookLM

### Page 5

第二阶段：核心工作流

黄金法则：先规划，后执行（Plan, Then Execute）

这是从新手到专家的最关键转变。直接让 Claude 编码，结果往往不可预测。要求其先规划，能显著提升复杂任务的成功率。

1. PLAN  
（研究与规划）

2. EXECUTE  
（编码与实现）

规划模式（Plan Mode）

连按两次 `Shift` + `Tab` `Tab` 进入。在此模式下，Claude 只能进行研究和分析，无法执行任何修改性操作。这保证了输出的结构化和安全性。

✓ 强制深度思考  
迫使 Claude 在编码前进行更周全的考量。

✓ 结构化输出  
计划通常以清单形式呈现，清晰易懂。

✓ 安全可控  
在你批准计划前，代码库不会有任何改动。

自动规划模式（Auto Plan Mode）：一种更高级的防御性策略，通过系统提示强制 Claude 在执行任何破坏性操作前进入规划模式。

NotebookLM

### Page 6

第二阶段：核心工作流

引导思维过程：从指令到对话

仅仅要求规划是不够的，你还需要引导其思考的深度和方向。

思维深度阶梯（The `think` Hierarchy）

使用特定关键词来分配不同的“思考预算”，以应对不同复杂度的任务。

`ultrathink`  
用于遗留代码集成、复杂算法等最棘手的问题。

`think harder`  
用于性能优化或安全相关的代码。

`think hard`  
用于复杂的业务逻辑。

`think`  
用于直接的 bug 修复。

变被动为主动（Encourage Questions）

将单向指令变为双向沟通。在提示中明确要求 Claude 提问，以澄清需求和暴露你未曾考虑的假设。

“在你开始规划用户认证系统前，先就需求向我提问，确保我们构建的是正确的东西。”

AI

NotebookLM

### Page 7

第二阶段：核心工作流

修正的艺术与上下文卫生（Context Hygiene）

真正的协作离不开反馈和修正。管理好交互历史和上下文是保持高效的关键。

核心交互机制（Key Interaction Mechanics）

Escape

`Escape`：中断 Claude 当前的任何操作（思考、工具调用等）。

Escape  Escape

`Escape` x2（双击）：激活“回溯（Rewind）”功能，允许你跳回历史记录中的某一点，编辑当时的提示，并从那里重新开始，同时恢复当时的代码状态。

上下文卫生（Context Hygiene）

上下文污染（Context Poisoning）：在长会话中，不相关的历史信息会干扰 Claude 的判断，导致其做出错误联想或性能下降。

Poisoned Context

/clear

Clean Context

解决方案（Solution）：在切换到新任务时，频繁使用 `/clear` 命令。这会清空上下文窗口，确保 Claude 专注于当前任务，避免“污染”。

NotebookLM

### Page 8

第三阶段：构建工具箱

可复用工作流：自定义斜杠命令（Slash Commands）

将你最常用的、多步骤的提示流程，封装成可一键调用的自定义命令。

- 创建方法（How to Create）：在项目根目录下的 `.claude/commands` 文件夹中创建 Markdown 文件。文件名即为命令名。
- 参数化（Parameterization）：在 Markdown 文件中使用 `$ARGUMENTS` 关键字，即可在调用命令时传递参数。

命令源文件

fix-github-issue.md

```md
Please analyze and fix the GitHub issue: $ARGUMENTS.

Follow these steps:
1. Use `gh issue view` to get the issue details.
2. Understand the problem described in the issue.
3. Search the codebase for relevant files.
4. Implement the necessary changes to fix the issue.
5. Write and run tests to verify the fix.
6. Ensure code passes linting and type checking.
7. Create a descriptive commit message and create a PR.
```

终端执行

```text
> /fix-github-issue 1234

Running `gh issue view 1234`...
Analyzing issue details...
Understanding the problem described in the issue...
Searching codebase for relevant files...
Implementing the necessary changes to fix the issue...
Writing and running tests to verify the fix...
Ensuring code passes linting and type checking...
Creating a descriptive commit message and creating a PR...
```

NotebookLM

### Page 9

第三阶段：构建工具箱

组建专家团队：子代理（Sub-Agents）与钩子（Hooks）

超越单个通用代理，通过构建一个由专家组成的“团队”来解决复杂问题。所有代理都定义在 `.claude/agents` 文件夹中。

项目经理  
(Project Manager)

手动委派  
(Manual Delegation)

自动调用  
(Automatic Invocation)

手动子代理  
(Manual Sub-agents)

通过 `Task` 工具进行显式并行处理。适用于简单的并行操作。

自定义代理

真正的“专家”，拥有独立的上下文、专门的系统提示和受限的工具集，并能被主代理自动调用。

安全审查专家  
(Security Reviewer)

测试编写专家  
(Test Writer)

文档专家  
(Documentation Specialist)

钩子（Hooks）

在开发生命周期的关键节点添加确定性的自动化控制，例如在每次文件编辑后自动运行 linter。

NotebookLM

### Page 10

第四阶段：战略范式

实现规模化：并行执行的力量

真正的精通在于超越线性工作流，实现并行化。让多个 Claude 实例同时处理不同任务或探索同一任务的不同解决方案。

核心技术：`git worktrees`  
这是实现并行化的最佳实践。`git worktrees` 允许你从同一个仓库中检出多个分支到不同的目录。每个 worktree 都是一个隔离的环境，可以运行独立的 Claude 实例。

优势（Advantages）  
任务之间完全隔离，不会互相干扰，非常适合大型重构或同时开发多个不相关的功能。

1. 为不同特性创建独立的 worktree。
2. 在每个 worktree 目录中启动一个 Claude 实例。
3. 在多个终端中同时监督和指导它们。
4. 完成后，将工作成果合并回主分支。

主仓库  
(Main Repository)

`../project-feature-a (branch: feature-a)`

`../project-bugfix-123 (branch: bugfix-123)`

`../project-refactor-core (branch: refactor-core)`

NotebookLM

### Page 11

第四阶段：战略范式

拥抱心流：“氛围编程（Vibe Coding）”

“Vibe Coding” 是一种高级开发策略，你完全脱离底层代码的实现细节，专注于你期望达成的最终“结果”或“氛围”。你信任代理去处理具体的实现。

定义：由 Andrej Karpathy 提出，指一种“完全投入氛围，拥抱指数级增长，并相信代码会奇迹般出现”的开发方式。

适用场景：探索性工作和新功能发现；非破坏性、无副作用的任务。

关注实现

```js
function processData(data: any): void {
  const results = data.map(item => ...
  if (item.isValid) {
    // Implementation details here
    ...
  }
  else {
    return null;
  }
}
```

关注成果

Intuitive  
Elegant  
Fast  
Seamless  
Delightful UX

成功要素

“Plan Mode” + “ultrathink”：必须先进行彻底的规划。

频繁提交（Frequent Commits）：进行小而频繁的 git 提交，以便在代理“跑偏”时能快速回滚。

NotebookLM

### Page 12

第四阶段：战略范式

终局之战：拥抱“代理优先设计（Agent-First Design）”

这是一个根本性的范式转变。传统的“人类优先”设计为可读性和团队协作而优化。“代理优先”设计在此基础上，进一步为 AI 代理能够快速生成、扩展和个性化进行优化。

AI 生成的功能排列（AI-Generated Permutations）

核心模式  
(Core Pattern)

核心原则（Key Principles）

模块化架构（Modular Architecture）  
清晰的接口，让代理可以安全地扩展和重组组件。

可模板化体验（Templatable Experiences）  
定义核心用户体验模式，代理可以在此基础上生成无数变体。

自动化验证（Automated Validation）  
内置机制，让代理能够验证其修改是否正确，无需持续的人工监督。

转变（The Shift）：你的角色从实现者转变为架构师，从手动编码转变为审查和编排由 AI 生成的功能排列组合。

NotebookLM

### Page 13

你的精通之旅：四个关键阶段回顾

4. 战略范式 (Strategic Paradigms)  
编排并行代理，并为 AI 优先的未来进行设计。

3. 构建工具箱 (Power Toolkit)  
通过自定义命令和专业化代理，实现自动化和规模化。

2. 核心工作流 (Core Workflow)  
拥抱“先规划，后执行”的节奏，学会引导和修正。

1. 奠定根基 (Foundation)  
使用 `CLAUDE.md` 掌控你的上下文，并优化你的环境设置。

git worktrees

Agent-First Design

自定义命令

子代理组织

规划 (Plan) → 执行 (Execute)

CLAUDE.md

秘诀在于流程，而不仅仅是提示。

NotebookLM

### Page 14

从代码创作者到智能编排者

Claude Code 不仅仅是一个助手，它是一个新工程范式的催化剂。你的角色正在从创作者演变为架构师，从编码员演变为编排者。今天就开始你的旅程。

行动号召（Call to Action）

1. 立即行动（Immediate Action）  
为你当前的项目创建一个 `CLAUDE.md` 文件。

2. 养成习惯（Build the Habit）  
在你的下一个任务中，严格实践“规划模式”。

3. 开始实验（Start Experimenting）  
编写你的第一个自定义斜杠命令。

扫码获取官方文档与社区资源

claudecode.dev/resources

NotebookLM
