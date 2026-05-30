---
source_url: local
ingested: 2026-04-20
sha256: d626a6104113a267e860d5d85da08a9d27cbef1c3509c55370c8b83ffab4147d
---
可以。下面这套更适合你这种目标：**用多 agent 做真正的并行开发**，而不是只把一个需求丢给一个大模型。Codex 公开能力已经支持多 agent 并行、独立 worktree / cloud 环境、以及通过 `AGENTS.md` 约束 agent 行为，所以这套方法是贴着它现在的能力设计的。

## 一套适合 Codex 的并行开发工作流

### 1. 角色分成 3 层

**A. 主控 agent**  
只负责这几件事：

- 拆需求
    
- 判断依赖关系
    
- 分派任务
    
- 汇总结果
    
- 决定合并顺序
    

它**不要直接写太多业务代码**，否则会变成又当经理又当程序员，最后容易乱。

**B. 实现 agents**  
每个 agent 只负责一个边界清晰的子任务，例如：

- API / Controller agent
    
- Service / Domain agent
    
- Frontend 页面 agent
    
- Test agent
    
- Migration / SQL agent
    
- Docs agent
    

**C. 审核 agent**  
独立于实现 agents，专门负责：

- review 代码风格
    
- 检查接口契约
    
- 跑测试
    
- 回归检查
    
- 找冲突点
    

这种结构最稳，因为“写的人”和“验的人”分开了。

---

### 2. 任务拆分原则

并行开发最怕的不是 agent 不够聪明，而是**拆分方式不对**。

最适合拆给多个 agent 的任务有：

**适合并行**

- 独立页面 + 独立接口
    
- 不同微服务的改动
    
- 测试补齐
    
- 文档、脚本、配置调整
    
- 同一需求下的前后端分工
    
- 一个 feature 中相对独立的子模块
    

**不适合并行**

- 多个 agent 同时改同一个核心文件
    
- 强依赖共享状态的大重构
    
- 边界还没定义清楚的需求
    
- 数据模型还没定就同时开工
    

所以正确顺序通常是：

**先由主控 agent 做“设计定稿”**  
再让实现 agents 并行开工。

---

### 3. 一个标准分派模板

比如你有一个“客户管理模块”的需求，可以这样拆：

#### 主控 agent 先输出

- 目标：新增客户查询、详情、编辑
    
- 约束：不改现有鉴权；沿用当前 DTO 规范；必须补齐集成测试
    
- 交付物拆分：
    
    - Agent 1：数据库 migration + repository
        
    - Agent 2：service + domain logic
        
    - Agent 3：controller + API contract
        
    - Agent 4：前端列表页 + 编辑页
        
    - Agent 5：单测 + 集成测试 + API case
        
    - Agent 6：文档和变更说明
        

这样每个 agent 的输入都尽量固定，避免它们自己脑补。

---

### 4. 每个 agent 的输入必须标准化

你不要只说“去实现这个功能”，要给它固定结构：

**给实现 agent 的任务卡**

- 任务目标
    
- 可改目录
    
- 禁止改动目录
    
- 依赖的接口 / 数据结构
    
- 输出要求
    
- 测试要求
    
- 提交格式
    

例如：

```text
任务：实现 CustomerService 的查询和更新逻辑
允许修改：
- src/main/java/.../service/**
- src/test/java/.../service/**

禁止修改：
- controller/**
- frontend/**
- pom.xml

约束：
- 不新增第三方依赖
- 沿用现有异常模型
- 必须补充单元测试
- 保持方法签名兼容

输出：
1. 修改说明
2. 代码 patch
3. 测试结果
4. 风险点
```

这样做的好处是，agent 更不容易越界。

---

### 5. 用 `AGENTS.md` 统一团队规则

Codex 官方支持 `AGENTS.md` 来定义代理在项目中的工作规则，这对多 agent 特别重要。你可以把它当成“给所有 agent 的团队开发手册”。

建议里面至少写这些：

```md
# AGENTS.md

## Project Rules
- 所有 Java 代码遵循现有 package 结构
- 不允许引入新的基础设施依赖
- 所有 API 变更必须同步更新 OpenAPI 文档
- 所有数据库变更必须包含 migration script
- 所有功能改动必须附带测试

## Branch / Worktree Rules
- 每个 agent 在独立 worktree 工作
- 不允许直接覆盖其他 agent 的文件
- 合并前必须 rebase 到最新主线

## Coding Rules
- Spring Boot 3.x 风格
- DTO / Entity 不混用
- Service 层不直接返回 Entity 给 Controller
- 禁止硬编码配置

## Validation
- 后端必须通过单元测试
- Controller 改动必须有集成测试
- 前端改动必须通过 lint / build
```

---

### 6. 合并流程不要让实现 agent 自己决定

最稳的合并顺序是：

**先合“基础层”**

- migration
    
- model
    
- repository
    
- shared contract
    

**再合“业务层”**

- service
    
- domain logic
    

**再合“接入层”**

- controller
    
- frontend
    
- docs
    

**最后由审核 agent 做总体验证**

- 全量测试
    
- 回归检查
    
- 接口一致性检查
    
- 变更说明汇总
    

这能显著减少冲突。

---

### 7. 推荐的实际运行模式

如果你用 Codex 做并行开发，我建议你按下面方式组织：

#### 模式 A：轻量模式

适合 1 个开发者带多 agent

- 1 个主控 agent
    
- 2 到 4 个实现 agents
    
- 1 个审核 agent
    

适合中小 feature。

#### 模式 B：标准模式

适合小团队

- 1 个主控 agent
    
- 后端 agent
    
- 前端 agent
    
- 测试 agent
    
- 文档 agent
    
- 审核 agent
    

适合一个完整需求迭代。

#### 模式 C：重度模式

适合复杂项目

- 1 个主控 agent
    
- 架构 / 依赖分析 agent
    
- 数据层 agent
    
- 服务层 agent
    
- API agent
    
- 前端 agent
    
- 测试 agent
    
- 安全 / review agent
    
- 发布说明 agent
    

这个模式能力强，但管理成本也更高。

---

### 8. 你最该防的 4 个坑

#### 坑 1：多个 agent 改同一文件

这会直接让并行收益大幅下降。

解决办法：

- 任务分派时绑定目录
    
- 公共接口先冻结
    
- 主控 agent 先定义 contract
    

#### 坑 2：每个 agent 理解的需求不一样

解决办法：

- 先出统一 spec
    
- 明确输入输出
    
- 给出禁止修改范围
    

#### 坑 3：所有 agent 都会“顺手重构”

解决办法：

- 在任务卡里写清楚：只做目标任务，不扩大改动面
    
- 大重构单独开 agent，不混在 feature 里
    

#### 坑 4：最后没人做集成

解决办法：

- 单独设一个审核 agent
    
- 它只做整体验证，不负责功能实现
    

---

### 9. 最适合你的场景

结合你前面说的目标，“通过多 agent 完成并行开发”，Codex 最适合这类项目：

- Spring Boot 后台系统
    
- 有明确模块边界
    
- 有数据库、接口、前端、测试这类天然分层
    
- 团队愿意把规范写清楚
    
- 愿意接受“主控 + 执行 + 审核”的流程
    

如果是你那种**10 张表左右、微服务协作、TDD/Spec 驱动**的后台系统，这种方式其实很匹配。因为这种项目本身就适合按：

- 数据模型
    
- 服务逻辑
    
- 接口层
    
- 测试层
    
- 文档层
    

来拆分并行开发。

---

## 我给你的结论

**Codex 能做多 agent 并行开发，而且适合做工程化并行开发。**  
真正成败不在“有没有 agent teams 这个名字”，而在于：

- 任务有没有拆对
    
- 规则有没有写进 `AGENTS.md`
    
- agent 有没有隔离工作区
    
- 有没有独立审核 agent
    
- 合并顺序是不是受控
    

如果你愿意，我下一条可以直接给你一份：

**“Spring Boot 后台项目的多 agent 并行开发模板”**

我会按这些内容直接写成可用版本：

- 主控 agent 提示词
    
- 后端 agent 提示词
    
- 测试 agent 提示词
    
- 审核 agent 提示词
    
- `AGENTS.md` 样例