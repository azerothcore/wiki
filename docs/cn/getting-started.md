# 开始使用 AzerothCore

## 简介

你想了解 AzerothCore（AC），第一次搭建你的 WoW 服务器，理解如何修改它并成为贡献者吗？你来对地方了！

刚开始接触 WoW 模拟器（emulation）可能会有些棘手，但别担心，如果你遇到任何问题或有任何疑问，我们都会在这里帮助你。在寻求帮助之前，请先阅读[此页面](how-to-ask-for-help)。

如果你在阅读本页链接的任何教程时发现有些内容不清楚：请告诉我们。我们会尽力改写，让初学者更容易理解。改进文档也是一种贡献方式！

![AzerothCore 学习代码](https://user-images.githubusercontent.com/75517/109369720-b6fa7d00-789d-11eb-86b4-5fe15d6ab834.png)


## 知识要求

**没有**任何技术要求。你只需要有耐心并愿意学习。

如果你已经有一些编程知识，那对你来说肯定是个优势。不过，相信我，你不需要任何先验知识就能学习 WoW 服务器。

*本教程作者的个人心得：当我第一次安装我的第一个 WoW 服务器时，我 15 岁，完全没有编程知识，用的是 Windows XP，而且几乎看不懂英语。我相信如果你正在读这篇文章，你已经比我当年尝试安装 MaNGOS+UDB+ScriptDev2 并在本地机器上运行一个像样的 WoW 服务器时拥有的技能多得多。
起初，我花了几个小时试图阅读和理解不同人在不同网站上写的教程，但最终我成功了。AzerothCore 是一个一体化项目，所以它会比那更容易，耐心一点，你会做到的！*

想改用 repack 吗？[别这么做](https://www.mangosrumors.org/why-you-should-not-use-repacks-to-run-your-wow-server/)。

## 在电脑上安装 AzerothCore

第一步始终是在你自己的机器上安装一个本地 WoW 服务器。有多种方法可以做到这一点，具体方法可能因操作系统而异。

### 你的操作系统

有一件事我要说清楚：**AzerothCore 支持所有操作系统**。
因此你可以毫无问题地在 GNU/Linux、macOS 或 Windows 上成功安装 AzerothCore。

不过，我可以告诉你，如果你使用 Linux 发行版（例如 **Ubuntu 26.04**），安装过程会更容易。如果你想安装 Ubuntu，可以[从这里](https://ubuntu.com/download/desktop)下载，而且网上有很多关于如何安装的教程。这里有一个关于在 Linux 上运行 WoW 的不错教程：[点击此处](https://www.mangosrumors.org/how-to-run-wow-on-linux/)。

你想坚持用 **Windows** 或 **macOS**？那也完全可以。

![AzerothCore 支持 GNU/Linux、macOS 和 Windows](https://user-images.githubusercontent.com/75517/109369213-e5775880-789b-11eb-8356-99a4ab842bfb.png)

### 安装 AzerothCore 的不同方式

基本上，有 3 种主要的安装 AC 的方式：

- "**经典安装（classic setup）**"：这是安装普通 WoW 模拟器时通常使用的传统安装方式。**支持所有操作系统。** 使用这种安装方式也可能让你对服务器的各个组件有更好的了解。
- "**Docker 安装（docker setup）**"：这是一种简化的安装方式，使用 Docker 为你自动完成很多事情。这种安装方式通常更容易。**只要你能够安装 [Docker](https://www.docker.com/products/docker-desktop) 的操作系统，都可以使用这种安装方式。**
- "**面板安装（dashboard setup）**"：这是一种**极其简单**的在你的机器上安装 AzerothCore 的方式，基于由 [Yehonal](https://github.com/Yehonal) 创建的一组 bash 脚本。不过，**你只能在 Ubuntu** 或类似平台上使用这种安装方式。不支持 Windows，而且 macOS 可能也还不行。

你可以选择一种安装方式，甚至可以尝试多种。你可以在这里找到所有说明：

- [azerothcore.org/wiki/installation](installation)

如果在尝试安装你的 AC 服务器时遇到任何问题或疑问，[请向我们寻求帮助](https://github.com/azerothcore/wiki/blob/master/docs/how-to-ask-for-help)。

你的 WoW 服务器安装好了吗？恭喜！现在让我们看看接下来你可以做什么。

![在 macOS 上运行的 AzerothCore 服务器](https://user-images.githubusercontent.com/75517/109369101-80236780-789b-11eb-900c-bcc17a3cf13c.png)

## 进入游戏，学习 GM 命令

首先，确保你的客户端已将 realmlist.wtf 设置为以下内容：`set realmlist localhost`。之后（假设你已经安装好了 AzerothCore），确保你创建了一个 `GM`（权限等级为 2 或更高）账号。如果你还没有创建账号或者不确定，请按照[创建账号](creating-accounts)操作。
之后，你的 `GM` 账号将能够使用以下链接中的命令，下面列出了所有命令的列表：

- [azerothcore.org/wiki/gm-commands](gm-commands)

熟悉这些命令，你在任何管理、测试或开发活动中都会用到它们。

![AzerothCore GM](https://user-images.githubusercontent.com/75517/109369940-ba423880-789e-11eb-88d6-e6d8f7b8a723.png)

## 考虑学习 git

你可以盲目地复制粘贴本页链接教程中出现的 `git` 命令，大多数情况下你都不会遇到问题。
不过，正确地学习 `git` 会让你真正了解自己在做什么，而且这些知识可以帮你处理你可能参与的任何其他软件开发项目。
是的，因为 `git` 是许多软件工程项目中使用的最重要的工具之一。学习它的基础知识不仅会对你使用 AzerothCore 大有帮助，而且也是写进简历的好东西。

网上有很多学习 `git` 的资源，例如 [try.github.io](https://try.github.io/)

![AzerothCore 学习 git](https://user-images.githubusercontent.com/75517/109370018-fb3a4d00-789e-11eb-8532-1ab1bf8fba60.png)

## 学习如何更新你的 WoW 服务器

我们每天都在发布 AzerothCore 的改进。你应该学习如何更新你的服务器并经常保持更新。我们建议避免使用旧版本的 AzerothCore，因为它们可能含有我们已经修复的 bug，而你不想落后。

所以**定期更新你的 AzerothCore 服务器非常重要**。我们建议你至少每周更新一次。请阅读本指南：

- [azerothcore.org/wiki/keeping-the-server-up-to-date](keeping-the-server-up-to-date)

在遵循更新流程之后，**验证**以下几点很重要：

- 你的服务器应用程序（核心 core）已正确更新，使用 `server info` 命令来确认。
- 你的数据库已正确更新并与你的核心版本对齐，[阅读这个 stackoverflow 上的回答](https://stackoverflow.com/a/55282168/3497671)。

![AzerothCore server info](https://user-images.githubusercontent.com/75517/109370296-00e46280-78a0-11eb-9ed0-b9df14f2008b.png)

## 学习如何查看 PR

开始贡献的一个好方法是测试其他贡献者提交的 PR。这不仅相当容易，而且对项目非常有益，还能帮助你进入我们的开发流程。

这个话题非常重要，因此有一个专门的教程：

- [azerothcore.org/wiki/how-to-test-a-pr](how-to-test-a-pr)

![image](https://user-images.githubusercontent.com/75517/109370244-d397b480-789f-11eb-9ac7-64d98ca0d33c.png)

## 学习如何使用数据库

数据库是开始开发 WoW 服务器的最佳起点。因为它比其他组件更容易，而且有些工具能够自动为你生成代码。例如 Keira3。

### 下载 Keira3

Keira3 是一个 AzerothCore 的数据库编辑器，让你能够非常轻松地编辑或向世界添加内容，我们建议你安装并试用它：

- [azerothcore.org/Keira3](https://www.azerothcore.org/Keira3)

Keira3 会自动生成在数据库中创建或修改内容所需的 SQL 代码。
听起来很复杂？试一试你就会明白它是如何工作的。

![AzerothCore Keira3](https://user-images.githubusercontent.com/75517/109370160-769bfe80-789f-11eb-9958-dc17ff48f39a.png)

### 下载一个 MySQL 客户端

你还需要一个通用的数据库管理工具来管理表及其内容。

- [数据库管理工具](database-management-tool)

![使用 sequel-ace 查看的 AzerothCore 世界数据库](https://user-images.githubusercontent.com/75517/109370368-42750d80-78a0-11eb-946c-c0831a02b52b.png)

### 数据库文档是你的朋友

始终阅读你所处理的每个表的相关文档：

- [azerothcore.org/wiki/database-world](database-world)

### SmartAI

使用 SmartAI 你可以做很多事情。你可以为游戏中的某个元素（例如生物 creature）添加特殊行为，而无需改动一行 C++ 代码。

简而言之，使用 SmartAI，你可以让一个实体（例如生物 Creature）在某个**事件**发生时执行某个**动作**，还可以选择指定**目标**。换句话说，你可以让实体对你定义的行为所对应的事件做出反应。

例如，你可以让一个生物在其生命值低于其总生命值的 50% 时（事件），对队伍中的随机成员（目标）施放一个法术（动作）。

从技术上讲，`smart_script` 只是世界数据库中的一个表（其文档可以[在这里](smart_scripts)找到）。像 Keira3 这样的工具可以帮助你通过实用的图形界面使用 SmartAI。

尝试打开 Keira3，找一个"AIName"为"SmartAI"的生物，打开它并点击右侧菜单中的"SmartAI"。
你会看到一个可视化编辑器，它会在你使用 SmartAI 时提供帮助。

![使用 Keira3 的 AzerothCore SmartAI](https://user-images.githubusercontent.com/75517/109367698-1bfea480-7897-11eb-9cf0-f047b3dcdb85.png)

尝试使用 SmartAI 并熟悉它。这是一个简单但非常强大的工具。
对它有所了解之后，你就能做很多事情。很多 bug 仅使用 SmartAI 就能修复。

你在世界中发现的大多数生物的 AI 都是用 SmartAI 实现的。而更复杂的生物（通常是团队副本首领）则用 C++ 编写脚本。

![SmartAI vs C++](https://user-images.githubusercontent.com/75517/109369529-e78de700-789c-11eb-97d5-02ecc6c85a0a.png)

### 学习 SQL 语言

通常，你只需要 SQL 语言的基础知识，而且在大多数情况下，你可能会自己摸索出来。不过，阅读一些关于 SQL 语言的资料并不是坏事。你可以在网上找到很多资源，例如：

- [https://www.w3schools.com/sql/sql_intro.asp](https://www.w3schools.com/sql/sql_intro.asp)

如果你理解了诸如 `SELECT`、`UPDATE`、`INSERT` 和 `DELETE` 之类的基本语句是如何工作的，那通常就足够了。你不需要深入研究 SQL 才能做出贡献。

## 分享你的代码！

你可以通过 PR 提交你的改进。请阅读本指南：

- [如何创建拉取请求（PR）](how-to-create-a-pr)

## 开始贡献！

如果你已经掌握了上述某些部分，那么你已经可以**做很多事情**来帮助我们的项目并成为一名贡献者。
例如：

- 通过测试 PR 并给出反馈来帮助开发者
- 通过确认 issue 并帮助我们识别和关闭无效报告来进行 bug 分诊（triaging），参见[分诊指南](guide-to-triaging)
- 你也可以通过[分诊来自 ChromieCraft 玩家报告的 bug](https://github.com/chromiecraft/chromiecraft)（我们的子项目）来提供帮助
- 报告你自己可能发现的任何 bug
- 尝试修复 bug，其中很多 bug 只需要一些 SQL 就能修复，你可以为此使用 Keira3（例如使用 SmartAI 或其他内置编辑器）。由于这是一个开源项目，你可以在我们的主要 GitHub 仓库中找到大量示例

想和我们聊聊吗？加入 [AzerothCore Discord 服务器](https://discordapp.com/invite/gkt4y2x)。

![为 AzerothCore 做贡献](https://user-images.githubusercontent.com/75517/109370461-b44d5700-78a0-11eb-916c-81c8500fa969.png)

## 结论与后续步骤

永远不要停止学习。去学习面向对象编程（OOP）的基础知识。
找一些 C++ 教程，开始尝试核心源代码。看看别人的 PR 作为示例。

研究游戏服务器的基本机制（阅读像[这篇](https://stackoverflow.com/questions/62249204/how-does-the-update-diff-work-in-azerothcore)之类的文章）。尝试[创建模块](https://stackoverflow.com/questions/66340549/is-it-possible-to-turn-a-core-patch-into-a-module-for-azerothcore)。

或者学习另一种编程语言，你可以用你最喜欢的编程语言为 AzerothCore 用户或开发者构建很多工具。

无论你打算做什么，永远记住：**StackOverflow 是你的朋友**。

-------------------------------------------------

在本教程中，我想帮助初学者，并展示即使不懂 C++，你也能学到很多并做出贡献。你所需要的只是一点时间和耐心。

祝你编码愉快！

-- Shin（即 Francesco）
