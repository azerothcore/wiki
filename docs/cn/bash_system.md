# BASH 系统

AzerothCore 使用一个高级 bash 系统，使我们能够自动化诸如源代码**编译、模块安装、数据库设置**等流程。

目前我们使用 bash 而不是 Python，以减少外部依赖，因为 BASH 是一种跨平台的脚本语言，已经包含在 **OSX、Linux 和 Windows** 中（通过 GIT BASH，我们在环境要求中要求你安装它）。

你可以在此阅读官方 bash 文档：https://tldp.org/LDP/abs/html/index.html

## ACORE 仪表盘

我们与 azerothcore 相关的 bash 脚本位于 /app 文件夹内，但我们在根文件夹中还创建了一个名为 **acore.sh** 的脚本。
该脚本运行一个仪表盘，其中包含运行 /app 文件夹中所有相关脚本的命令。

运行 `./acore.sh --help` 可查看所有可用命令的完整列表。

### 配置

我们项目根目录中的 /conf 文件夹用于让你能够更改所有 bash 脚本的配置。

### 交互模式

运行 `./acore.sh`，你可以通过交互模式使用仪表盘：你可以在仪表盘菜单和子菜单中导航，并运行你需要的命令。

### 命令参数

你可以将仪表盘的命令用作 ./acore.sh 脚本的参数。例如：

`./acore.sh compiler configure` 将运行我们 C++ 编译器的配置过程。

所有命令都有更短的别名。例如 `./acore.sh c configure` 会运行编译器配置，同样 `./acore.sh 5 3` 也可以做到。


## DEPS

我们的 bash 系统使用外部 bash 库，这些库是通用的，与 azerothcore 本身无关。这些库由我们创建，
并放置在 /deps 文件夹下。


## HOOKS:

bash 内部的[钩子系统](hooks-bash)

## 其他资源

- 使用单条 bash 命令安装 azerothcore：[视频 + 描述中的脚本](https://www.youtube.com/watch?v=j1HI6pLZZvM)
