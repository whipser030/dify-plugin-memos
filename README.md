# MemOS

**Repository:** [MemOS](https://github.com/whipser030/dify-plugin-memos)

**Author:** MemTensor

**Version:** 0.0.3

**Type:** Tool

## Description

MemOS is a memory management operating system for AI applications. It gives AI apps human-like long-term memory: not only remembering what users said, but also proactively calling, updating, and orchestrating those memories.

This plugin enables Dify applications to connect to the MemOS cloud service. With the two core operations—Add and Search—developers can easily read, write, and manage memory data.

## Core APIs

When building applications with large language models, a common question is: how can an AI remember a user's long-term preferences?

MemOS provides two core APIs to help:

● **addMessage** —— Hand us the raw conversation, and we automatically process it and store memories;
● **searchMemory** —— Recall memories in later conversations so the AI responds closer to user needs.

# Plugin Configuration

To use this plugin, you need to fill in the following configuration in Dify:

1. **MemOS URL**：MemOS cloud service endpoint URL https://memos.memtensor.cn/api/openmem/v1。
2. **MemOS API Key**：You can obtain the API key from your [MemOS API Console](https://memos-dashboard.openmem.net/cn/apikeys/) or configuration.

## Usage

After completing the configuration above, you can use MemOS in the Dify orchestration interface. The interface parameters are:

(List the current tool input/output parameters here, referring to the table below.)
![](https://cdn.memtensor.com.cn/img/1767863640064_sgfhsv_compressed.png)

You can add these tools to your workflow to achieve:

1. **Automatically Save Memories**：Automatically create and store factual summaries and user preferences after each interaction, ensuring the user's long-term context is continuously updated.
2. **Context-Aware Responses**：Retrieve memories during each chat to provide highly personalized and contextually relevant answers for your AI application.
3. **Build Complex Memory Logic**: Link the "Add" and "Search" tools with other nodes in Dify to create complex logic.

For specific instructions on how to use the tool, you can refer to the [MemOS API Reference](https://memos-docs.openmem.net/cn)。

## Workflow Example

For scenarios where you need to record conversation data and extract relevant memories, you can build the following workflow:
![](https://cdn.memtensor.com.cn/img/1767863857551_2dael7_compressed.png)
