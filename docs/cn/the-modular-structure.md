---
redirect_from: "/cn/The-Modular-Structure"
---

# 模块化结构

基于我们的模块化、以领域驱动的[目录结构](directory-structure)，AzerothCore 项目允许你通过添加相互隔离的自定义模块来添加和扩展游戏功能，而无需直接修改核心。

这带来的结果是：始终拥有一个干净的核心，易于维护，并能与最新的 AzerothCore 更新保持同步。

## 钩子（Hooks）

### 脚本钩子

为了改变游戏功能，模块使用**脚本钩子（script hooks）**，这是一组[实现在核心中](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Scripting/ScriptMgr.h)的函数，能够从服务器启动之初（World 初始化一开始）就发挥作用。

脚本钩子的列表见[此处](hooks-script)。

有时你需要为自定义模块添加新的钩子，把它们添加到核心中是完全可行的。创建一个新钩子只需要几个步骤，请按照[此处](hooks-script)的指南学习如何操作。

当你添加新钩子时，别忘了[为它们创建一个 PR](http://www.azerothcore.org/wiki/How-to-create-a-PR)。这样，它们将由 AzerothCore 开发者评审，并收录进官方仓库。

### Cmake 钩子

CMake 钩子允许模块在 AzerothCore 编译阶段执行操作。例如，它可以用来在服务器启动时安装并加载自定义的 `*.conf` 文件。

这样模块就可以拥有自己的配置文件，你可以**避免修改** `worldserver.conf.dist` 文件。

CMake 钩子的列表见[此处](hooks-cmake)。

### Bash 钩子

Bash 钩子允许模块与 AzerothCore 的 bash 面板交互。借助它，你可以在使用 AzerothCore bash 控制台添加或移除模块时，添加自动化的操作。

例如，它可以用来在安装模块时自动执行 SQL 代码，向数据库添加额外的表；在卸载模块时移除它们。

要与我们的 bash 系统交互，请在根目录中创建并使用 `include.sh`。

Bash 钩子的列表见[此处](hooks-bash)。

## 如何创建模块

你可以通过阅读[如何创建模块](create-a-module)开始创建你的第一个模块。
