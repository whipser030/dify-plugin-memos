# memos


**仓库:** [dify-plugin-memos](https://github.com/whipser030/dify-plugin-memos)

**作者:** memtensor

**版本:** 0.0.2

**类型:** 工具

## 描述

MemOS 插件允许 Dify 应用程序连接并与用户的 **自托管或托管的 MemOS 实例** 进行交互。MemOS 是一个专为 AI 应用程序设计的开源长期记忆插件。它提供了强大的工具来管理用户对话数据、创建事实记录和捕获基于偏好的记忆。通过其直观的“添加”和“搜索”接口，用户可以轻松存储和检索所需信息。

## 特性
*   **存储用户对话数据:** 当输入原始对话内容时，MemOS 系统会自动生成相关的事实记忆和用户偏好记录，并将其存储在数据库中。
*   **检索用户数据:** 当输入用户查询时，MemOS 系统会根据输入内容搜索所有相关的事实记忆和偏好记录，并将结果返回给用户。

## 设置

[MemOS](https://github.com/MemTensor/MemOS) 是开源的，允许您部署自己的实例。

要使用此插件，您需要在 Dify 中添加它时提供与 **您的** MemOS 实例对应的以下凭据：

1.  **MemOS URL:** **您的** MemOS 实例的端点 URL（例如，`https://memos.memtensor.cn/api/openmem/v1`）。
2.  **MemOS API Key:** 用于验证 **您的** MemOS 实例的 **您的** API 密钥。（格式：必须是 Token mpg-************** 的格式。前缀 "Token" 是必需的。）

您可以从您的 [MemOS API 控制台](https://memos-dashboard.openmem.net/apikeys/) 或配置中获取这些信息。
![MemOS API console](/_assets/memos_console.svg)


## 用法

一旦配置了您的 MemOS 实例的详细信息，MemOS 工具将在 Dify 编排界面中可用。

您可以将这些工具添加到您的工作流中，以：

1. **自动保存记忆:** 将“添加记忆”工具集成到您的对话流程中，以便在每次交互后自动创建并存储事实摘要和用户偏好。这确保了用户的长期上下文持续更新。

2. **上下文感知响应:** 在工作流开始时使用“搜索记忆”工具。通过在生成响应之前检索相关的过去交互和用户偏好，您可以使您的 AI 应用程序提供高度个性化和上下文相关的答案。

3. **构建复杂的记忆逻辑:** 将“添加”和“搜索”工具与 Dify 中的其他节点链接起来，以创建复杂的逻辑。例如，您可以首先搜索现有的记忆以避免重复，或者仅在对话中检测到特定类型的信息时才有条件地添加新记忆。

有关如何使用该工具的具体说明，您可以参考 [MemOS API 参考](https://memos-docs.openmem.net/dashboard/api/overview/)。


## 工作流示例

对于需要记录对话数据并提取相关记忆的情况，您可以构建以下工作流：

![MemOS workflow](/_assets/memos_workflow.svg)(/_assets/memory_assistant.yml)
