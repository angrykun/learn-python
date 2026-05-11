# Python for AI/Agent 开发路线图

> 目标：系统掌握 Python，为 AI/Agent 开发打好基础
> 投入：每周 ~2 小时
> 预计周期：16-20 周（4-5 个月）
> 前置要求：有编程经验（.NET 开发背景）

---

## 阶段速览

| 阶段 | 主题 | 核心技能 | 预计周期 |
|------|------|----------|----------|
| **Phase 1** | Python 基础 | 语法、OOP、异步 | 3-4 周 |
| **Phase 2** | AI 编程核心 | API 调用、数据处理、向量化 | 8-10 周 |
| **Phase 3** | Agent 实战 | LangChain、LlamaIndex、实战项目 | 5-6 周 |

---

## Phase 1：Python 基础（3-4 周）

### 目标
快速把 .NET 经验迁移到 Python，补足语法差异。

### 章节安排

**1.1 语法快速迁移（C# → Python）** [week 1]
- 变量、类型、字符串（Python 无类型声明）
- 条件、循环（语法差异对比）
- 函数定义 vs C# 方法
- → 练习：常见算法迁移

**1.2 面向对象（OOP）** [week 1-2]
- 类 vs C# class
- 继承、接口 → Python 的 duck typing
- 特殊方法（`__init__`, `__str__`, `__call__`）vs C# 构造函数/运算符重载
- → 练习：实现一个简单的数据类

**1.3 Python 高级特性** [week 2]
- 列表/字典/集合推导式 vs LINQ
- 装饰器（Decorator）→ 类似 C# 特性（Attribute）+ 中间件的概念
- 上下文管理器（`with`）→ 类似 C# `using`
- 生成器（yield）→ 类似 C# `yield return`
- → 练习：写一个装饰器计时器

**1.4 异步编程** [week 3]
- `async/await` vs C# async/await（核心相同，语法差异）
- 事件循环、Task vs C# Task
- → 练习：异步 HTTP 请求（aiohttp）

**1.5 模块、包、环境管理** [week 3-4]
- `pip`、`venv` vs NuGet + .csproj
- `requirements.txt` / `pyproject.toml` → 类比 .csproj
- 虚拟环境隔离 → 类比 .NET 项目隔离
- → 练习：搭建一个干净的 Python 项目环境

### Phase 1 实战项目
- **项目 A**：天气查询 CLI 工具（调用公开 API，练习异步 + 异常处理）

---

## Phase 2：AI 编程核心（8-10 周）

### 目标
掌握 AI 开发所需的 Python 核心技能：API 调用、数据处理、向量化、提示词工程。

### 章节安排

**2.1 HTTP 与 API 调用** [week 4]
- `requests` 库 → 类比 HttpClient
- RESTful API 调用（GET/POST/JSON）
- 认证（API Key、Bearer Token）
- → 练习：调用 OpenAI API（兼容的百炼 API）

**2.2 JSON 与数据结构处理** [week 4-5]
- JSON 序列化/反序列化 → C# `JsonSerializer`
- Python dict/list vs C# object/dynamic
- `pydantic` → 类比 C# record/class + 数据验证
- → 练习：解析和构造复杂的 AI API 请求/响应

**2.3 提示词工程（Prompt Engineering）** [week 5-6]
- 结构化提示词设计
- Few-shot prompting
- Chain-of-Thought（思维链）
- 系统提示词 vs 用户提示词
- → 练习：为一个客服场景设计提示词模板

**2.4 数据处理与向量化** [week 6-7]
- `numpy` 基础 → 类比 C# Math.NET
- `pandas` 基础 → 类比 C# DataTable/LINQ to Objects
- 文本向量化（Embedding）→ 核心概念：把文字转成数字向量
- `sentence-transformers` / OpenAI Embeddings
- → 练习：对一组文档生成 Embedding，并做相似度搜索

**2.5 向量数据库** [week 7-8]
- FAISS（Facebook AI Similarity Search）→ 轻量级本地向量检索
- Chroma（本地向量数据库）
- 向量检索原理（余弦相似度、点积）
- → 练习：搭建一个简单的 RAG（检索增强生成）流程

**2.6 异常处理与日志** [week 8]
- `try/except` vs C# try/catch
- 自定义异常
- `logging` 模块 → 类比 Serilog
- 重试机制（`tenacity`）
- → 练习：给 AI API 调用加完整的异常处理和重试

### Phase 2 实战项目
- **项目 B**：文档问答机器人（RAG 流程：加载文档 → 向量化 → 检索 → 生成答案）

---

## Phase 3：Agent 实战（5-6 周）

### 目标
从"调用 AI API"升级到"构建 AI Agent"，配合 LangChain/LlamaIndex。

### 章节安排

**3.1 LangChain 快速上手** [week 9-10]
- LangChain 的核心概念（Model、Prompt、Chain、Agent）
- LCEL（LangChain Expression Language）→ 链式调用
- → 练习：用 LangChain 调用百炼 API

**3.2 LlamaIndex 快速上手** [week 10-11]
- LlamaIndex vs LangChain（专注 vs 全能）
- 索引类型：VectorStoreIndex、SummaryIndex...
- 查询引擎（Query Engine）
- → 练习：用 LlamaIndex 搭建文档问答

**3.3 ReAct Agent 实现** [week 11-12]
- 复现第 6 章的 ReAct 框架（Python 版）
- Tool Calling 与 Action 映射
- 循环终止条件
- → 练习：给文档问答 Agent 增加"搜索 + 计算"能力

**3.4 多 Agent 协作** [week 12-13]
- AutoGen / LangGraph 多 Agent 编排
- Agent 间的通信协议
- 任务分配与结果聚合
- → 练习：设计一个"规划 + 执行"双 Agent 系统

**3.5 生产级 Agent** [week 13-14]
- 记忆管理（短期 + 长期）
- 错误恢复与重试
- 成本控制（Token 计数）
- 评估与调试
- → 练习：给 Agent 加记忆和成本追踪

### Phase 3 实战项目
- **项目 C**：花语秘境 Agent 系统（自主规划任务、调用工具、记忆对话）
- **项目 D**：多 Agent 代码审查团队（规划 Agent + 审查 Agent + 修复 Agent）

---

## 学习资源

### 官方文档（优先）
- Python: https://docs.python.org/3/
- LangChain: https://python.langchain.com/
- LlamaIndex: https://docs.llamaindex.ai/
- aiohttp: https://docs.aiohttp.org/

### 书籍
- 《Python 编程：从入门到实践》（基础）
- 《Hands-On RESTful API Design Patterns》（API 设计）

### 工具链
- `uv` — 极速包管理器（比 pip 快 10 倍）
- `ruff` — 超快 Python Linter
- `pytest` — 测试框架
- `Poetry` / `uv` — 依赖管理

---

## 进度追踪

| 章节 | 状态 | 完成日期 | 备注 |
|------|------|----------|------|
| 1.1 语法迁移 | ⬜ | - | - |
| 1.2 OOP | ⬜ | - | - |
| 1.3 高级特性 | ⬜ | - | - |
| 1.4 异步编程 | ⬜ | - | - |
| 1.5 模块管理 | ⬜ | - | - |
| 2.1 API 调用 | ⬜ | - | - |
| ... | ... | ... | ... |

---

## 与 .NET 经验的对照速查

| .NET 概念 | Python 对应 |
|-----------|------------|
| `class` | `class` |
| `interface` | duck typing / Protocol |
| `async/await Task<T>` | `async/await` + coroutine |
| `NuGet` | `pip` / `uv` |
| `.csproj` | `requirements.txt` / `pyproject.toml` |
| `var` | Python 动态类型（无声明） |
| `record` | `dataclass` / `pydantic` |
| `yield return` | `yield` |
| `using` 块 | `with` 语句 |
| `Attribute` | 装饰器 `@decorator` |
| `Middleware` | 装饰器 / Chain |
| `HttpClient` | `requests` / `aiohttp` |
| `JsonSerializer` | `json` / `pydantic` |
| `LINQ` | 列表推导式 / `pandas` |
| `Serilog` | `logging` |
| ` Polly`（重试） | `tenacity` |
