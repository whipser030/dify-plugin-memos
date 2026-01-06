# memos


**Repository:** [dify-plugin-memos](https://github.com/whipser030/dify-plugin-memos)

**Author:** memtensor

**Version:** 0.0.2

**Type:** tool

## Description

The MemOS plugin allows Dify applications to connect and interact with a user's **self-hosted or managed MemOS instance**. MemOS is an open-source long-term memory plugin designed for AI applications. It provides robust tools for managing user conversation data, creating factual records, and capturing preference-based memories. Through its intuitive "add" and "search" interfaces, users can effortlessly store and retrieve information as needed.

## Features
*   **Storage of User Dialogue Data:** When raw conversation content is input, the MemOS system automatically generates relevant factual memories and records of user preferences, which are then stored in the database.
*   **Retrieval of User Data:** When a user query is input, the MemOS system searches all related factual memories and preference records based on the input and returns the results to the user.

## Setup

[MemOS](https://github.com/MemTensor/MemOS) is open-source, allowing you to deploy your own instance.

To use this plugin, you need to provide the following credentials when adding it in Dify, corresponding to **your** MemOS instance:

1.  **MemOS URL:** The endpoint URL of **your** MemOS instance (e.g., `https://memos.memtensor.cn/api/openmem/v1`).
2.  **MemOS API Key:** **Your** API key for authenticating with **your** MemOS instance.(Format: Must be in the format Token mpg-**************. The prefix "Token" is required.)

You can obtain these from your [MemOS API Console](https://memos-dashboard.openmem.net/apikeys/) or configuration.
![MemOS API console](/_assets/memos_console.svg)


## Usage

Once configured with the details of your MemOS instance, the MemOS tools will be available within the Dify orchestration interface.

You can add these tools to your workflows to:

1. **Automatically Save Memories:** Integrate the "Add Memory" tool into your conversation flow to automatically create and store factual summaries and user preferences after each interaction.  This ensures the user's long-term context is continuously updated.

2. **Context-Aware Responses:** Use the "Search Memories" tool at the beginning of a workflow.  By retrieving relevant past interactions and user preferences before generating a response, you empower your AI application to deliver highly personalized and contextually relevant answers.

3. **Build Complex Memory Logic:** Chain the "Add" and "Search" tools with other nodes in Dify to create sophisticated logic.  For example, you can first search for existing memories to avoid duplicates, or conditionally add new memories only when specific types of information are detected in the dialogue.

For specific instructions on how to use the tool, you can refer to the [MemOS API Reference](https://memos-docs.openmem.net/dashboard/api/overview/).


## Workflow Example

For situations that require recording dialogue data and extracting relevant memories, you can construct the following workflow:

![MemOS workflow](/_assets/memos_workflow.svg)(/_assets/memory_assistant.yml)