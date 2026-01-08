# MemOS


**仓库:** [MemOS](https://github.com/whipser030/dify-plugin-memos)

**作者:** MemTensor

**版本:** 0.0.3

**类型:** 工具

## 描述

MemOS 是一个面向 AI 应用的记忆管理操作系统，让 AI 应用像人一样拥有长期记忆，不仅能记住用户说过的话，还能主动调用、更新和调度这些记忆。
本插件支持 Dify 应用连接 MemOS 云服务，开发者通过核心操作「添加（Add）」和「搜索（Search）」接口，可以轻松实现记忆数据的读写与管理。

## 核心接口
在使用大模型构建应用时，一个常见问题是：如何让 AI 记住用户的长期偏好？
MemOS 提供了两个核心接口帮助你实现：
● **addMessage** —— 把原始对话交给我们，我们自动加工并存储记忆；
● **searchMemory** —— 在后续对话中召回记忆，让 AI 回答更贴近用户需求。

# 插件配置
要使用此插件，您需要在 Dify 中填写以下配置信息：
1. **MemOS URL**：MemOS云服务端点 URL https://memos.memtensor.cn/api/openmem/v1。
2. **MemOS API Key**：您可以从您的 [MemOS API 控制台](https://memos-dashboard.openmem.net/cn/apikeys/) 或配置中获取接口密钥。

## 用法
配置完以上信息，您可在 Dify 编排界面中使用 MemOS 。以下是接口参数：
（列举一下现在插件的输入输出参数，参考下面的表格）
![](https://cdn.memtensor.com.cn/img/1767863640064_sgfhsv_compressed.png)
您可以将这些工具添加到您的工作流中，实现以下功能：
1. **自动保存记忆**：在每次交互后自动创建并存储事实摘要和用户偏好，确保用户的长期上下文持续更新。
2. **上下文感知响应**：在每次聊天时检索记忆，为您的 AI 应用提供高度个性化和上下文相关的答案。
3. **构建复杂的记忆逻辑**: 将“添加”和“搜索”工具与 Dify 中的其他节点链接起来，以创建复杂的逻辑。
有关如何使用该工具的具体说明，您可以参考 [MemOS API 参考](https://memos-docs.openmem.net/cn)。

## 工作流示例
对于需要记录对话数据并提取相关记忆的情况，您可以构建以下工作流：
![](https://cdn.memtensor.com.cn/img/1767863857551_2dael7_compressed.png)
