# 安装模块

| 安装指南                                                                                                                                |
| :--------------------------------------------------------------------------------------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读，也可以点击上面的链接在步骤之间轻松切换。                                                        |
| [<< 步骤 9：可选附加项](optional-additions)                                                                                             |

添加模块是一个可选步骤，用于修改 AzerothCore 默认提供的仿暴雪（blizzlike）游戏玩法。

## 安装模块

1. 在 [AzerothCore 目录](https://www.azerothcore.org/catalogue#/) 中找到你需要的模块。
2. 克隆仓库
    - 使用 Git 克隆仓库，方式与最初在[核心安装](core-installation)中克隆 AzerothCore 相同。仓库应克隆到 \modules\ 目录中。例如 E:\AzerothCore\modules\
    - 从目录中下载 ZIP 文件并将其解压到 \modules\ 目录中。例如 E:\AzerothCore\modules\mod-anticheat

{% include note.html content="如果你的模块带有后缀（例如 -master），则必须将其移除，模块才能正常工作！" %}

## 重新编译

为了让你的模块正常工作，你需要重新编译源码。关于如何重新编译的详细指南，请再次阅读[核心安装](core-installation)。

1. 重新配置并重新生成 CMake。
    - 为确保模块已正确安装，你可以检查它是否出现在 CMake 日志的 **\* Modules configuration (static)** 下

2. 重新构建核心。

你的 Worldserver 会自动运行模块提供的任何 SQL 查询。

你应该始终检查模块的 README 文件，看看是否有模块正常运行所需的手动步骤。

## 常见错误

- 编译期间我收到错误 "error LINK2019: unresolved external symbol "void __cdcel Addmod_module_masterScripts(void)"
    - 从模块目录名称中移除 **-master**。

- 该模块出于某种原因在游戏内不生效。
    - 你始终可以使用 **.server debug** 命令查看所有已加载的模块。
    - 对于该模块的确切安装步骤，请始终以模块的 README 文件为准。

<br>

## 帮助

{% include help.html %}

| 安装指南                                                                                                                                |
| :--------------------------------------------------------------------------------------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读，也可以点击上面的链接在步骤之间轻松切换。                                                        |
| [<< 步骤 9：可选附加项](optional-additions)                                                                                             |
