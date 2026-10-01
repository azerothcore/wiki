---
redirect_from: "/cn/FAQ"
tableofcontents: 1
---

# 常见问题

如果你在安装或编译 AzerothCore 时遇到问题，请阅读[常见错误](common-errors)。

| 本 FAQ 没有解决你的问题？请阅读[如何寻求帮助](how-to-ask-for-help)，了解如何以最佳方式提出你的问题。 |
| ------------------------------------------------------------------------------------------------------------------------ |

## 常规相关 FAQ

- 支持哪些操作系统/平台？
  - 目前支持 Windows、macOS、Linux 和 Docker。

- 我应该在什么时候更新我的源码？
  - 我们建议你频繁更新核心，至少每周一次，以便获得最新的核心修复和安全补丁。

- 什么是 "Blizzlike"？
  - AzerothCore 致力于复刻 World of Warcraft 的暴雪官方状态。"Blizzlike" 一词的意思是它已经足够接近暴雪服务器上的原始复刻效果。

- 为什么 AzerothCore 不模仿 "blizzlike" 的 bug 或漏洞？
  - 虽然我们努力提供 blizzlike 内容，但我们同样重视用户体验。这意味着我们有时会修复当时官方服务器上存在过的 bug 或漏洞，以便为玩家提供更好的整体体验。

- 我该如何贡献？
  - 你可以通过提交 Pull Request 来帮助修复问题，点击[此处](contribute)了解更多。
  - 你可以通过测试我们的 [Pull Request](contribute#how-to-test-a-pull-request) 并参与 [github issue 的讨论](https://github.com/azerothcore/azerothcore-wotlk/issues) 来帮助我们。
  - 你可以通过提交 [Pull Request](https://github.com/azerothcore/wiki) 来帮助改进 wiki。

- 为什么你不合并我的修复？
  - 所有修复都必须由开发人员审核。并非所有开发人员都无所不知，所以你需要等待有人来审核。
  - 有些修复需要测试，并非所有开发人员都能测试，所以你需要等待其他人来测试。
  - 它们会在获得 To Be Merged 标签后最终被合并。
  - 也许你没有遵循 [SQL/C++ 规范](standard-operating-procedure)。
  - 更多信息请阅读[合并流程](merge-process)。

- 我该如何报告崩溃？
  - 将你的崩溃日志粘贴到 PasteBin 或 Gist 中。
  - 崩溃日志**必须来自 RelWithDebInfo 或 Debug 编译**。如果来自 Release，则是无用的。
  - [如何重启与调试](how-to-restart-and-debug)。

- 你们支持基于 AzerothCore 的 Repack 吗？
  - 不支持。Repack **不被支持**，我们强烈建议不要使用它们，原因有[很多](https://www.mangosrumors.org/why-you-should-not-use-repacks-to-run-your-wow-server/)。你可以按照我们的[安装指南](installation)轻松安装 AC，无需使用任何 repack。

## 数据库相关 FAQ

- 你们多久更新一次数据库？
  - 数据库几乎每天都会更新。

- 我该如何更新数据库？
  - 你可以在[保持服务器数据库更新](database-keeping-the-server-up-to-date)这篇指南中找到保持数据库最新所需的一切。

## 核心相关 FAQ

- 源码什么时候才能稳定？
  - 快了……™
  - 我们尽最大努力保持 master 分支稳定且可玩。我们从不直接把代码推送到 master 分支，而是首先要求所有人（包括 AC 管理员和工作人员）先打开一个 PR，这样每个人都能在合并到 master 之前检查它们。
  - 请通过[测试 PR](how-to-test-a-pr) 并报告你发现的任何 bug 来帮助我们。

- 我无法在 Windows 平台上运行提取器，点击后它就消失了？
  - 请理解它是一个**命令行**工具，而不是 GUI 工具。这意味着你需要使用 Windows 的命令行（例如 "命令提示符"）来运行它，而不是直接双击它。

- 为什么我无法运行旧版的 MAP/DBC 提取器？
  - 它们更新是有原因的。如果你不使用最新版本进行提取，启动 Worldserver 时会报错。
  - 只要使用 "TOOLS" 编译，你总能获得最新版本。

- 什么是 Maps、VMaps、MMaps 和 DBCs？
  {% include note.html content="AzerothCore 不支持也不认可对客户端文件或私人/公共服务器的任何形式的修改！AzerothCore 本身仅用于理论研究和学习。" %}
  - 除了作为可执行文件、提供基本功能以及让各个客户端解释功能、定义和命令的核心之外，核心可以被描述为一个 '身体'，由以下数据构成它的 '解剖结构'：
    - **Maps**：Maps 是**运行 AzerothCore 所必需的**。Maps 为核心提供要解释的物理数值和数据。基于这些数据，核心拥有可以与每个客户端进行比对的布局。这包括区域定义。
    - **VMaps**：VMaps 是**可选的，但强烈推荐**。例如，VMaps（"Virtual Maps"）计算视线（line-of-sight）的可能性。基于它们的内容，服务器可以（例如）计算施法是否可行（例如目标与施法者之间是否隔着一堵墙）。
    - **MMaps**：MMaps 是**可选的，但强烈推荐**。为了进一步限制物理边界，MMaps（"Movement Maps"）对非玩家角色（例如 NPC）强制执行物理边界，因为它们的碰撞不受客户端处理。它们还能改进路径生成。
    - **DBC**：DBC 是**运行 AzerothCore 所必需的**。DBC（"Data Base Client [Files]"）提供 World of Warcraft 客户端解释所需的基本数值。它们定义了种族、纹理、本地模型等。AzerothCore 会解释并加载这些内容。
  - 使用 "TOOLS" 编译 AzerothCore 将始终创建提取和生成这些文件所需的工具。

- 我在提取 Maps、VMaps、MMaps、DBCs 时遇到问题（而且我试过旧版本的提取器）——是哪里出了问题？
  - 旧版工具已被弃用，将无法使用。
  - 你必须使用命令行才能运行这些工具。

- 我缺少 MySQL 的库文件，而且在仓库中找不到它们？
  - 该库文件名为 "mysql.lib"，不由 AzerothCore 提供。
  - 请确保你安装了带有开发头文件（DEVELOPMENT HEADERS）的 MySQL-Server。
  - 你可以按照[核心安装](core-installation)指南找到这些库文件。

- 我缺少 OpenSSL 的库文件，而且在仓库中找不到它们？
  - 你需要以下 dll 文件：
    - legacy.dll
    - libcrypto-3-x64.dll
    - libssl-3-x64.dll
  - 你可以按照[核心安装](core-installation)指南找到这些库文件。

## 调试相关 FAQ

- 在 Windows 上如何获得一份有效的崩溃日志？
  - 使用 RelWithDebInfo 或 Debug 编译你的核心。来自 Release 的崩溃日志是无用的。
  - 如果你[在 Visual Studio 中运行 worldserver 和 authserver](run-worldserver-and-authserver-in-visual-studio)，你可以自己调试它。

## 模块相关 FAQ

- 我的自定义模块需要一个新 hook，我该怎么办？
  - 你可以将 hook 添加到自己的 fork 中（参见：[创建新 hook](hooks-script)），并向官方仓库创建一个新的 Pull Request，这样我们就可以验证并合并它。

- 是否可以把核心补丁转换成模块？
  - 可以。[是否可以把核心补丁转换成 AzerothCore 的模块？ - StackOverflow](https://stackoverflow.com/questions/66340549/is-it-possible-to-turn-a-core-patch-into-a-module-for-azerothcore/66340683#66340683)。

## 功能相关 FAQ

- 哪些副本/竞技场/战场是可用的？
  - 其中大部分都能完美运行，有些运行得较差。
  - 核心一直在不断完善，最准确的数据来自你亲自尝试。

- Warden 能用吗？
  - 能用，但成功率并非 100%。Warden 无法检测所有外挂，即使在官方服务器上也是如此。

- 我该如何关闭一个副本或战场？我该如何禁用某个法术？
  - 所有禁用操作都在 [disables 表](disables) 中处理。

| 本 FAQ 没有解决你的问题？请阅读[如何寻求帮助](how-to-ask-for-help)，了解如何以最佳方式提出你的问题。 |
| ------------------------------------------------------------------------------------------------------------------------ |
