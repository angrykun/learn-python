# Python for AI/Agent 开发路线图

> **使用 FASTER 框架** — 主动学习 + 间隔复习
> **投入**：每天 2 小时（工作日）
> **周期**：约 5 个月（20-22 周）
> **前置**：有 .NET 开发经验，Python 语法略知一二
> **目标**：从"会用 Python"升级到"能用 Python 构建 AI/Agent 系统"

---

## FASTER 框架应用说明

| 字母 | 含义 | 在本路线图中的应用 |
|------|------|---------------------|
| **F** | Forget — 放下预设 | .NET 思维是资产，不是负担，但要理解 Python 的动态特性 |
| **A** | Act — 动手优先 | 每节必须有实战代码，只看不练等于没学 |
| **S** | State — 优化状态 | 每天 2 小时，30 分钟理论 + 90 分钟动手 + 30 分钟复习 |
| **T** | Teach — 教才是学 | 每学完一节，用自己的话解释给我（Teach-back） |
| **E** | Enter — 坚持日常 | 工作日每天学，不追求单次学很多，追求持续不断 |
| **R** | Review — 间隔复习 | 按 1d→3d→7d→14d→30d 的节奏复习关键概念 |

---

## 学习模式：每天 2 小时结构

```
┌─────────────────────────────────────────────┐
│  30 分钟：理论输入（看/读/理解新概念）        │
├─────────────────────────────────────────────┤
│  90 分钟：动手实战（写代码、调试、跑通）       │
├─────────────────────────────────────────────┤
│  30 分钟：复习 + teach-back（用自己的话讲一遍） │
└─────────────────────────────────────────────┘
```

---

## 三个大阶段

| 阶段 | 主题 | 周期 | 核心产出 |
|------|------|------|----------|
| **Phase 1** | Python 基础重构 | 3-4 周 | 能写独立 Python 脚本 |
| **Phase 2** | AI 编程核心 | 10-12 周 | 能调用 AI API + 搭建 RAG |
| **Phase 3** | Agent 实战 | 6-8 周 | 能构建完整 Agent 系统 |

---

## Phase 1：Python 基础重构（3-4 周）

### 目标
把 .NET 经验系统化地迁移到 Python，补足语法差异，建立 Pythonic 思维。

### 每日结构

| 天 | 理论（30min） | 实战（90min） | 复习（30min） |
|----|--------------|--------------|--------------|
| Day 1 | 1.1 语法迁移 C#→Python | FizzBuzz + 单词最长查找 | 讲给朋友听：Python vs C# 最大区别 |
| Day 2 | 1.2 OOP：类、继承、duck typing | 用 dataclass 重构数据模型 | 讲：dataclass vs C# record |
| Day 3 | 1.3 高级特性：装饰器、生成器 | 写装饰器计时器 + yield 斐波那契 | 讲：装饰器 vs C# 特性/中间件 |
| Day 4 | 1.4 异步：async/await vs C# | 用 aiohttp 异步并发请求 5 个 API | 讲：Python 异步 vs C# async |
| Day 5 | 1.5 包管理：pip/uv/env | 搭建干净虚拟环境，跑通 hello world | 讲：pip vs NuGet |

### 复习节点

| 概念 | 1d | 3d | 7d | 14d |
|------|----|----|----|-----|
| 动态类型 vs 静态类型 | ✅ | ✅ | | |
| dataclass | | ✅ | ✅ | |
| 装饰器 | | | ✅ | ✅ |
| async/await | | | ✅ | ✅ |

### Phase 1 实战项目

**项目 A：天气 CLI 查询工具**
- 功能：输入城市名，调用天气 API，返回结果
- 要求：异步请求、异常处理、命令行参数解析
- 涉及：requests/aiohttp、argparse、try/except、logging

---

## Phase 2：AI 编程核心（10-12 周）

### 目标
掌握 AI 开发所需的 Python 技能：API 调用、数据处理、向量化、RAG 流程。

### 每日结构

| 天 | 理论（30min） | 实战（90min） | 复习（30min） |
|----|--------------|--------------|--------------|
| Day 1 | 2.1 requests vs HttpClient | 调用百炼 API（兼容 OpenAI 格式） | 讲：REST API 调用流程 |
| Day 2 | 2.2 JSON 处理 + pydantic | 解析 AI API 响应，设计请求模型 | 讲：pydantic vs C# 数据类 |
| Day 3-4 | 2.3 提示词工程 | 设计 Few-shot + CoT 提示词 | 讲：为什么提示词设计很重要 |
| Day 5-6 | 2.4 Embedding 向量化 | 用 OpenAI Embeddings 生成向量 | 讲：什么是向量 Embedding |
| Day 7-8 | 2.5 向量数据库 FAISS/Chroma | 搭建本地向量数据库 | 讲：向量检索 vs 关键词搜索 |
| Day 9-10 | 2.6 RAG 流程 | 完整 RAG：文档→向量→检索→生成 | 讲：RAG 和微调的根本区别 |
| Day 11-12 | 2.7 异常处理 + 重试 | 给 AI API 调用加 tenacity 重试 | 讲：Python 异常 vs C# 异常 |
| Day 13-14 | 2.8 日志 + 调试 | 用 logging 追踪 Agent 行为 | 讲：logging vs Serilog |

### 复习节点

| 概念 | 1d | 3d | 7d | 14d | 30d |
|------|----|----|----|-----|-----|
| REST API + JSON | ✅ | ✅ | | | |
| pydantic 数据验证 | | ✅ | ✅ | | |
| Embedding 向量化 | | | ✅ | ✅ | |
| FAISS 向量检索 | | | ✅ | ✅ | |
| RAG 流程 | | | | ✅ | ✅ |
| tenacity 重试 | | | | | ✅ |

### Phase 2 实战项目

**项目 B：文档问答机器人（RAG 系统）**
- 功能：上传文档 → 向量化存储 → 用户提问 → 检索相关段落 → AI 生成答案
- 要求：支持 PDF/TXT、FAISS 向量检索、可配置提示词
- 这是你在《动手做 AI-Agent》中学到的 RAG 概念的 Python 实战版

---

## Phase 3：Agent 实战（6-8 周）

### 目标
从"调用 AI"升级到"构建 Agent"，用 LangChain/LlamaIndex 搭生产级 Agent。

### 每日结构

| 天 | 理论（30min） | 实战（90min） | 复习（30min） |
|----|--------------|--------------|--------------|
| Day 1-2 | 3.1 LangChain 快速上手 | 用 LangChain 调用百炼 API | 讲：LCEL vs .NET 管道 |
| Day 3-4 | 3.2 LlamaIndex vs LangChain | 用 LlamaIndex 搭文档问答 | 讲：两者适用场景 |
| Day 5-6 | 3.3 ReAct Agent | 复现 ReAct 循环（Python 版） | 讲：ReAct 框架核心原理 |
| Day 7-8 | 3.4 Plan-and-Execute | 实现规划+执行解耦 | 讲：和 ReAct 的区别 |
| Day 9-10 | 3.5 多 Agent 协作 | AutoGen/LangGraph 多 Agent | 讲：多 Agent vs 单 Agent |
| Day 11-12 | 3.6 记忆管理 | 给 Agent 加短期+长期记忆 | 讲：记忆 vs 上下文 |
| Day 13-14 | 3.7 生产级 Agent | 成本追踪、错误恢复、评估 | 讲：Demo vs 生产的差距 |

### 复习节点

| 概念 | 1d | 3d | 7d | 14d | 30d | 60d |
|------|----|----|----|-----|-----|-----|
| LangChain LCEL | ✅ | ✅ | | | | |
| LlamaIndex 索引 | | ✅ | ✅ | | | |
| ReAct 框架 | | | ✅ | ✅ | | |
| 多 Agent 协作 | | | | ✅ | ✅ | |
| 记忆管理 | | | | | ✅ | ✅ |

### Phase 3 实战项目

**项目 C：花语秘境 Agent 系统**
- 功能：自主规划任务、调用多个工具、记忆对话历史
- 这是你在《动手做 AI-Agent》中学到的 Agent 概念的完整 Python 实现

**项目 D：多 Agent 代码审查团队**
- 规划 Agent → 审查 Agent → 修复 Agent 三者协作

---

## 复习日历（概览）

```
Week  1-4:   Phase 1（基础）
Week  5-16:  Phase 2（AI 核心）+ 穿插复习 Phase 1
Week 17-24:  Phase 3（Agent 实战）+ 穿插复习 Phase 1-2
Week 25+:    综合项目 + 复习冲刺
```

---

## .NET → Python 快速对照（持续查阅）

| .NET 概念 | Python 对应 | 关键差异 |
|-----------|------------|---------|
| `var x = 5;` | `x = 5` | 无类型声明，靠推断 |
| `List<T>` | `list` | 动态大小，无泛型约束 |
| `class Foo : IBar` | `class Foo(Bar):` | 无接口，用 duck typing |
| `async Task<T>` | `async def` + `await` | 协程语法不同，概念相同 |
| `yield return` | `yield` | 几乎一样 |
| `using` 块 | `with` 语句 | 功能相同 |
| `[Attribute]` | `@decorator` | 装饰器语法更灵活 |
| `HttpClient` | `requests` / `aiohttp` | API 不同 |
| `JsonSerializer` | `pydantic` / `json` | pydantic 带验证 |
| `LINQ` | 列表推导式 / `pandas` | 语法差异大 |
| `Polly` 重试 | `tenacity` | 功能相同 |
| `NuGet` | `pip` / `uv` | 包管理器 |
| `.csproj` | `requirements.txt` / `pyproject.toml` | 项目配置 |

---

## 进度追踪

| 章节 | 状态 | 完成日期 | 复习记录 |
|------|------|----------|---------|
| 1.1 语法迁移 | ⬜ | - | - |
| 1.2 OOP | ⬜ | - | - |
| 1.3 高级特性 | ⬜ | - | - |
| 1.4 异步编程 | ⬜ | - | - |
| 1.5 包管理 | ⬜ | - | - |
| 2.1 API 调用 | ⬜ | - | - |
| 2.2 JSON/pydantic | ⬜ | - | - |
| ... | ... | ... | ... |

---

## 学习原则

1. **不追求一次学很多，追求每天都学** — 每天 2 小时 >> 周末 10 小时
2. **看不懂就跳过，后续会补** — 有些概念需要后续章节的前置知识
3. **代码一定要跑通** — 理论看懂了不够，必须实际运行成功
4. **用 teach-back 检验理解** — 能讲清楚才算真的懂
5. **复习比学新更重要** — 间隔复习才是记忆的秘诀
