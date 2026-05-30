---
source: ima
kind: wechat
category: "技术"
title: "Claude Sonnet 4.5 vs. GPT-5 Codex: Best model for agentic coding - Composio"
url: "https://composio.dev/blog/claude-sonnet-4-5-vs-gpt-5-codex-best-model-for-agentic-coding"
media_id: "weburl_30987b07fe36143e35b82223ae18bcbe_5f4a8a92279427b7f11b5c511545ebf6"
media_type: 2
kb_name: "殷凇的知识库"
kb_id: "qzeC00QqxVZKyNdfTs2u_JmTwlIqypGehkvk2cjRaNw="
kb_folder_path: "/"
created_from_ima_at: "2026-05-11T10:27:18.695Z"
body_status: full_text
fetched_at: "2026-05-14T05:38:32+08:00"
---

# Claude Sonnet 4.5 vs. GPT-5 Codex: Best model for agentic coding - Composio

- 来源：ima 个人知识库
- 原文链接：https://composio.dev/blog/claude-sonnet-4-5-vs-gpt-5-codex-best-model-for-agentic-coding
- ima media_id：`weburl_30987b07fe36143e35b82223ae18bcbe_5f4a8a92279427b7f11b5c511545ebf6`
- ima 目录：/
- 内容分类：技术
- 正文状态：已抓取全文。

## 摘要

> 当前 ima 知识库列表接口未返回文章摘要字段；本条先保存标题、链接、media_id、目录与分类，便于后续按需补正文/摘要。

## 正文

Claude 4.5 Sonnet is out. After a month of the hue and cry from all the die-hard Claudians for lobotomizing Sonnet 4, Anthropic has released Claude 4.5 Sonnet, and, according to all Anthropic employees on Twitter, it's the best model for coding yet. It improves on the shortcomings of Claude 4 (personality) while retaining its best qualities (tool calling accuracy). Additionally, they also released Claude Code 2.0, powered by Sonnet 4.5, handling longer and more complex coding workflows. Which, in a way, means I am going to spend my salary on Claude now.

![](https://framerusercontent.com/images/ossKyVaTYnH8EAQ5XhTTAxn7As4.jpg)

Like everyone else, I had also shifted to Codex after the Claude debacle some weeks back, when Anthropic lobotomized their models. I thoroughly enjoyed Codex with GPT-5-codex; it was an incredible combo that quickly filled the void left after Sonnet 4 was nerfed.

But now that we have a newer and better model, I, like everyone else, want to know how good it is compared to GPT-5-codex.

We’ll be comparing both side by side, and by the end, you’ll know exactly what to choose if you want to ship products that scale, stay secure, and move fast while keeping costs in mind. All the code for this comparison can be found here: [github.com/rohittcodes/fashion-hub](https://github.com/rohittcodes/fashion-hub). This is actually a fork of the Turbo repo template by create-t3-stack.

### Demo of the App We Built Using Both Models

Before diving into the comparisons, here’s a quick look at what we actually built. The UI and core features were generated collaboratively using **Claude Sonnet 4.5** and **GPT-5 Codex**, running through the same MCP-powered setup.

[Embedded media](https://www.youtube.com/embed/PVFyJtTGcKM?iv_load_policy=3&rel=0&modestbranding=1&playsinline=1&autoplay=0&mute=1)

## TL;DR

If you have somewhere else to be, here's a summary of my findings

-

**Claude Sonnet 4.5 + Claude Code**: Great at planning, system design, multi‑tool orchestration, and UI fidelity. Struggled more with lint fixes and schema edge cases in this project.

-

**GPT‑5 Codex + Codex**: Strongest at iterative execution, refactoring, and debugging; reliably shipped a working recommendation pipeline with minimal lint errors.

-

**Cost efficiency in my runs**: Claude used far more tokens for UI and lint-fixing; Codex stayed leaner and fixed issues faster in the code.

-

**Pick Claude** if you want design oversight, documentation, and multi‑tool orchestration. **Pick Codex** if you're going to grind through bugs, refactors, and ship features fast.

-

**My choices for this repository are**: Codex for implementation loops, and Claude for architecture notes and UI polishing.

## What We'll Be Comparing These Models and Agents With?

Before proceeding, here’s how I’ll test both models using the same MCP-powered setup employed across all my builds. This will help maintain consistency across Codex and Claude when evaluating speed, reasoning, accuracy, and context retention. The whole setup that I've planned includes:

-

Asking for ideation and Setup: The setup will include the app schema, laying out the whole project structure, and working on the repository structure.

-

Cloning a Fashion E-commerce App UI

-

Building the recommendation pipeline for the E-commerce App

Before we dive in, let's take a moment to understand what these models and agents truly bring to the table.

|

Metric

|

Claude Sonnet 4.5 + Claude Code

|

GPT-5 Codex + Codex

|
|

**Context & Memory**

|

Automatically pulls context and maintains tool state across sessions. See docs for contextual prompting.

|

Long-context reasoning tuned for coding workflows; supports extended sessions.

|
|

**Tool / MCP orchestration**

|

Sub‑agents isolate context and tools per task.

|

Tight tool protocol integration with dynamic tool usage.

|
|

**Error recovery / robustness**

|

Good recovery from tool/state resets, especially with specialized agents.

|

Strong at iterative correction loops and large refactors.

|
|

**Coding & execution**

|

Excellent planning/architecture; can stumble on subtle async/edge cases.

|

Very strong execution/debugging; often ships working code in complex domains.

|
|

**Steerability / prompting burden**

|

May need more guidance for multi‑step tool chains.

|

More steerable out‑of‑box; less micromanagement required.

|
|

**Session length / persistence**

|

Handles long sessions; benefits from task‑scoped agents.

|

Built for multi‑hour autonomous execution.

|
|

**Cost / efficiency**

|

Costlier for very long runs with large contexts.

|

Often more efficient on large coding tasks.

|
|

**Best for**

|

Orchestration, design oversight, documentation, multi‑tool workflows.

|

Generation, debugging, refactoring, shipping features reliably.

|

## Why MCPs Even Matter Here

MCP (Model Context Protocol) standardizes how agents call external tools and retain context across them. In this build, we relied on:

-

Rube MCP as the unified bridge to GitHub (repo init/commits), Neon (managed Postgres), Notion (planning docs), and Figma to pull frames/tokens for UI cloning reference

-

Context7 MCP to search documentation (e.g., Gemini API notes) directly inside the session

This made tool calls reproducible and auditable, allowing both agents to operate consistently across the same environment.

## Setting up MCP servers with Claude Code and Codex

I used Rube MCP because it's our product (yeah lol), but also it's very good ngl.

[**Rube MCP**](https://rube.app) is a universal MCP server, supporting over 500 apps through Composio’s integration stack. Instead of managing 10 separate MCP servers, you connect to Rube once and orchestrate multi‑tool workflows. Want to “take new GitHub issues and post them in Slack”? You can run it entirely through Rube without needing to determine which server handles what. Explore toolkits: [https://docs.composio.dev/toolkits/introduction](https://docs.composio.dev/toolkits/introduction).

Quick Setup:

-

Visit [https://rube.app](https://rube.app/) and click “Add to Claude Code”.

-

Copy the command, run it in your terminal, then use `/mcp` in Claude Code to authenticate Rube.

-

For Codex, you can update the `config.toml` file to include the Rube MCP server, by generating a new auth token from the Rube app, and then using it in the `config.toml` file. You can follow the steps mentioned [here](https://github.com/openai/codex/blob/main/docs/config.md#connecting-to-mcp-servers) to use the http streamable MCP servers with Codex.

## Ideation and Setup

The idea was to build something that actually showcases complex context handling, including how both models and agents handle it, and how the agents can autonomously handle multiple MCP tool calls through a single prompt.

So, I decided to build everything inside a monorepo, letting both agents work on the same large codebase for faster feature development and debugging. Initially, I wanted to include a scalable try-on feature that could handle outfit generation for many users. But as Anthropic’s costs spiked, I had to drop that part and instead focused on building a recommendation engine that suggests outfit combinations.

![](https://framerusercontent.com/images/86pVsySKYgj6gzOo2shNqgk8jg.gif)

The initial documentation and timeline for the project were generated using Cursor with Notion, utilising Rube MCP. Once the initial planning was complete, I began working on setting up the project using GitHub and Neon DB integrations with Rube MCP. (yeah, it can interact with all these apps)

The initial setup proceeded smoothly, with no major issues. I used `create-t3-turbo` to set up the monorepo, which includes a tRPC API, enhanced authentication, Drizzle, and Expo.

These were simple prompts to run the agents for performing these actions, and the agents did a good job at it. Here's a sample of the prompt I used to run the agents for performing these actions:

```
Using Rube MCP: create a Neon Postgres database, initialize a GitHub repo with the first commit, and generate a Notion planning page with milestones, and according to the tasks in `IDEATION.md` generate a plan for the project. Return the commands run, files changed, and any follow-ups.
```

## UI Cloning

I actually had a UI planned for the application, but I’m bad at design, and it didn't look very exciting. I decided to get the initial UI idea from Figma and let the agents handle their own UI building. Surprisingly, they did a good job at it.

The same prompt was used for UI cloning in both models, and they performed fairly well in this task. The task was not to capture the exact UI, but to get an initial idea of the UI, and the agents did a commendable job at it. To accurately clone the UI, it’s a simple fact that Anthropic’s LLMs perform better when replicating Figma Designs. You can read more about it here: [Claude code with MCP is all you need](https://composio.dev/blog/cluade-code-with-mcp-is-all-you-need)

```
Clone this [Link to the UI] from Figma, polished fashion e‑commerce UI for web (Next.js) and mobile (Expo): product grid/detail, cart, checkout, profile, wishlist, onboarding. Use brand style (soft pink accents, rounded‑XL, subtle gradients/shadows), add accessible focus states and good contrast, keep lint to a minimum, and build reusable primitives from packages/ui. Output how to run both apps.
```

Codex initially was unable to capture the design correctly, making abrupt errors with the flex properties of the design. As a result, the products weren’t visible in the catalogue for the expo app.

![](https://framerusercontent.com/images/bYPFiUumZtOmhsXnkkmtL2LI1M.png)

Our end user interface in the demo was designed by Sonnet 4.5 as you saw above in the intro, and honestly, it nailed the vibe: pixel-perfect layouts, smooth gradients, and a clean component hierarchy across both web and mobile. So I stuck with the same.

**What does it cost to clone the UI:**

-

**Claude Sonnet 4.5 + Claude Code**: ~5M tokens (UI cloning + iterations)

-

**GPT‑5 Codex + Codex**: ~250k tokens (UI cloning + iterations)

## Refactoring and Fixing the Lint Errors

I then wanted to build a try-on feature for the application, and I started with the setup. I tried setting up local LLMs to help orchestrate the AR try-on (I tested a list of models and noted what went wrong), but the models were not performing well, so the other part of the plan was to use some image generation models to generate the try-on outfits, **Gemini 2.5 Flash Image** (Nano Banana). For the initial setup, I used **Cursor** to set up the schema for the DB and started setting up the pipeline for the try-on outfits, though I knew it’d definitely produce lint errors and a bunch of bugs, which I planned to fix with one of the models.

![](https://framerusercontent.com/images/9SNrES1kOTLk0LRrZraC47o8.png)

Once everything was set up, as I expected, I found a lot of bugs and lint errors. I prompted Claude Code to fix them, but it failed here. The lint errors were due to the schema setup, where we needed to fix relations between the tables, which **Cursor (Auto mode)** missed on its side. I used the same prompt later for the Codex, and the first thing it did was grab the context from the monorepo regarding the current state of the project, and then it started fixing those relations in the schema.

Although the cost up to then was relatively high, I had another feature in mind that would enable us to conduct some real coding and test how both models would perform when building a feature. This feature would involve a recommendation pipeline utilising **content similarity** through specific algorithms within the API layer itself. Instead of going with a pipeline to check how they could perform under constraints of the environment and situation, I focused on shipping the recommendation work.

During this detour, **Context7 MCP** handled Gemini API/doc lookups directly in-session, and Rube MCP updated the Notion plan with decisions and blocked items to keep context aligned across tools.

Cost of refactoring and fixing the lint errors:

-

**Claude Sonnet 4.5 + Claude Code**: ~4M tokens (Lint fixing)

-

**GPT‑5 Codex + Codex**: ~100k tokens (Lint fixing)

## Building the Recommendation Pipeline

For the recommendation pipeline, both models were given the same prompt to build the required DB schema and the UI for both web and mobile apps.

![](https://framerusercontent.com/images/Fr9gh4aF0VdgjFgNProRuuoKGk.png)

```
Build an AI-powered Recommendation Engine in TypeScript that surfaces personalized
product suggestions (For You, Similar Items, Trending) using a hybrid model
(collaborative + content-based) with real-time learning from user interactions
(views/cart/purchase/wishlist). Ship polished, accessible UI components,
do not reference any design file. Match Fashion Hub’s brand style
(soft pink accents, rounded-XL, subtle gradients, soft shadows, clean typography).
The schema for the DB should be setup according to the current state of the project.
```

Claude Code took approximately 10 minutes to set up the schema, build the API layer, and the UI for both web and mobile apps. The total number of tokens used was around 1,189,670. However, it struggled with setting up the schema relations, which later caused issues with the API layer of the recommendation pipeline; that’s a significant oversight in terms of designing scalable and secure applications.

![](https://framerusercontent.com/images/5wYvLtatzyclWXBYfVGrupHxuB8.png)

Codex took almost 25 minutes, to set up the schema, build the API layer, and the UI for the web. I was exhausted by that time, so I had to drop the UI for the Expo app. Tokens: ~309k. But it set up the schema relations correctly and built the API layer with minimal lint errors.

The commit for the Claude code feature generation can be found here: [commit/5b193ef7d1ee8218649d6a266b475572ac0dc262](https://github.com/rohittcodes/fashion-hub/commit/5b193ef7d1ee8218649d6a266b475572ac0dc262)

![](https://framerusercontent.com/images/bH9T7RLPODABXtr2dbIfNGQc2UE.png)

![](https://framerusercontent.com/images/VZzeTlKkYToeX0nYTJO3nwEw7vU.png)

### Security Flaws and Issues in the Recommendation Pipeline (both models)

-

From the code we generated using Sonnet 4.5, there was an issue with **locking down the trending updates**, and the **anonymous tracking was not using a server-issued**, signed, HttpOnly token mapped to an opaque ID with **TTL/cleanup** to avoid spoofing/cross-user pollution. The **heavy queue work** wasn’t being processed in a **proper batching layer**, and the **long queries** were not being precomputed on a schedule, and the SQL-side aggregation and indexes were not being added.

-

According to the information we received from **Codex**, there was an issue with **long-running queries,** which is definitely undesirable in a **serverless environment**. The **UI** part was missing for the Expo app, while the web app had partial implementation of these features, but was still **not fully functional**.

## Comparing the Cost

![](https://framerusercontent.com/images/iiSUZ01Unzil1uReYoOKvRw4.png)

-

**Sonnet 4.5** cost me around $10.26 with 18M input and 117k output tokens, with a lot of lint errors but great UI design fidelity.

*LMAO.. You def need to improve this Sam..*

![](https://framerusercontent.com/images/GmOXVSfHVcBFzbH3tS7gJfews7U.png)

Till then, this is what I have:

![](https://framerusercontent.com/images/dDwz3TBb9TcjeHh28Wz4ETJREA.png)

-

**GPT-5 Codex** cost me around 600k input tokens and 103k output tokens which, approximately when valued with the pricing (i.e., $1.25 for input and $10 for output per 1 million tokens), would be around $2.50, with a clean-looking UI.

## Developer Experience Feedback

One significant issue with Codex is its developer experience (DX). There’s no clear way to track usage or cost. There’s an OAuth login, so why not generate an API key and show total usage or cost on the dashboard? Currently, it only displays the current session cost, and I couldn’t even verify if it has been deducted from my account.

They do show context usage via session IDs, which is excellent, but overall visibility is poor. The `?` Command for shortcuts doesn’t even work anymore. Even the docs feel outdated and not synced with the latest features. The DX used to be better a few weeks ago.

The first thing that came to my mind was the OpenAI team vibe-coding this thing??

## Final Thoughts

Today, Codex is the **more practical choice** for shipping features. It handles **larger contexts** well, iterates faster on code, fixes lint issues with fewer retries, and, in my runs, costs less than Sonnet 4.5. Claude Code has felt **inconsistent in longer sessions**, but Sonnet 4.5 remains strong at planning, architecture, and **UI fidelity**. It’s the best Sonnet so far and cheaper than Opus, just not as reliable as Codex for heavy refactors in this repo.

DX on Codex isn’t perfect, but performance and cost make up for it right now. If you depend on LLMs on a day-to-day basis, I’d pick **Codex** for the long run **if the DX improves**. If you care about perfect UI and architectural guidance, bring in Sonnet 4.5 for design and documentation, then let Codex implement and harden it.
