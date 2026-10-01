---
redirect_from: "/cn/Contribute"
---

# 参与贡献

你可以通过以下几种方式为 AzerothCore 做出贡献：

- [评论一个已存在的问题](#how-to-comment-an-issue)

- [提交一个问题](#how-to-open-an-issue)

- [测试一个 Pull Request](#how-to-test-a-pull-request)

- [测试仅包含数据库（DB）变更的内容](how-to-test-db-only-changes)

- [在线端到端（e2e）测试](live-e2e)

- [创建 Pull Request](#how-to-create-a-pull-request)

- [改进我们的 Wiki](#improve-the-wiki)

## 基本信息

要参与贡献，你显然需要一个 GitHub 账号。

## 如何评论一个 issue {#how-to-comment-an-issue}

你可以通过查看 [issues](https://github.com/azerothcore/azerothcore-wotlk/issues) 并加入相关讨论来提供很大帮助。

你可以做的一件事是：更新你的 core，检查该 issue 在你的版本上是否仍然有效，然后写一条评论，**附上 commit 哈希值**。

## 如何提交一个 issue {#how-to-open-an-issue}

在报告 bug 之前，有几件重要的事情需要做：

**1) 将你的 core 更新到最新的 AzerothCore 版本，并检查该 bug 是否仍然存在**

**2) 在 [issues](https://github.com/azerothcore/azerothcore-wotlk/issues) 中搜索，检查是否已经有人报告过这个 bug。如果是，你只需评论该 issue 以确认 bug（并附上你的 core 版本）**

如果（**并且仅在**）该 bug 尚未被报告过，你可以[提交一个 issue](https://github.com/azerothcore/azerothcore-wotlk/issues/new)，并包含以下内容：

- 该 **bug 的描述**，包括任何有用的**链接**以及相关实体（NPC、法术、游戏对象等）的 **ID/GUID/名称**
- 你所运行的 AzerothCore 的 **core 版本（commit 哈希值）**，**不要只写“最新版本”**，即使你刚刚更新过 core
- 如果是构建问题，最好还能提供你的**操作系统**和**编译器版本**

## 如何测试一个 Pull Request {#how-to-test-a-pull-request}

- 阅读 [如何测试 PR](how-to-test-a-pr)。
- 官方 PR 还会针对完整的 auth + world + MySQL 环境运行[在线端到端（e2e）测试](live-e2e)。但这不能替代游戏内的测试。

## 如何创建一个 Pull Request {#how-to-create-a-pull-request}

- 阅读 [如何创建 PR](how-to-create-a-pr)。
- 另外，你也可以查看[这个更简单的教程](how-to-create-a-db-pr)，了解如何通过 GitHub 提交包含 SQL 代码的 PR。
- 编写 commit 信息时，请遵循[commit message 规范](commit-message-guidelines)。

### 给代码原作者署名

如果你想提交由其他人编写的代码，可以在 commit 时给原作者署名：

`git commit --author="AuthorName <authoremail@address.com>" -am "Commit message here"`

更新：遗憾的是，当以 squash 方式合并 PR 时，GitHub 会自动将合并后 commit 的作者设置为提交该 PR 的人。因此，请在 PR 描述中提及原作者（如适用，也请附上原 commit）。

## 改进 Wiki {#improve-the-wiki}

你想改进我们的 Wiki 或添加新页面吗？很好！请使用[我们的聊天室](https://discord.gg/PaqQRkd)来讨论。
