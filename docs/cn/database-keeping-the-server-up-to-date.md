# 数据库：保持服务器更新

| 安装指南                                                                                                                   |                                         |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读，也可以点击前面的链接在各步骤之间轻松切换。 |
| [<< 第 6 步：服务器最终步骤](final-server-steps)                                                                                  | [第 8 步：客户端设置 >>](client-setup) |

1. 首先确保你的核心是[最新的](keeping-the-server-up-to-date)。

如果你想了解 SQL 目录的工作方式，或者打算进行自定义修改，我们建议你阅读[这篇](sql-directory)文章。

## 自动数据库更新器

默认情况下，Worldserver 和 Authserver 会检查并执行所有新文件到你在配置中指定的数据库。

1. 启动 worldserver.exe

要编辑自动数据库更新器，你可以在 authserver.conf 和 worldserver.conf 的 **UPDATE SETTINGS** 下找到所需设置。

## 数据库更新工具 (dbimport)

AzerothCore 还附带了一个名为 **dbimport** 的独立工具。它运行与 Authserver 和 Worldserver 完全相同的更新器，但不会启动服务器：它连接到三个数据库，如果它们为空则创建并填充它们，应用所有待处理的 SQL 更新，然后退出。

当你想要以下操作时，这会很有用：

- 在服务器离线时或从脚本（部署、定时任务、CI）更新数据库
- 维护一台只管理数据库、不编译服务器的机器
- 在没有挂载到运行中服务器的数据库上运行更新器

### 只编译数据库更新器

该工具属于 **tools** 构建列表的一部分，因此可以单独编译：

- `-DTOOLS_BUILD=db-only` 只构建 `dbimport`，不构建其他工具（map/vmap/mmap 提取器）
- `-DAPPS_BUILD=none` 跳过 Authserver 和 Worldserver

{% include tip.html content="TOOLS_BUILD 默认为 `none`，所以如果你想要更新器，必须显式指定。TOOLS_BUILD 可接受值的完整列表为 `none`、`all`、`db-only` 和 `maps-only`，APPS_BUILD 为 `none`、`all`、`auth-only` 和 `world-only`。" %}

{% include important.html content="模块 SQL 文件仅在运行 cmake 时模块存在于 `modules/` 文件夹中且未被禁用时才会被应用。请使用与你构建服务器时相同的 MODULES 值，否则更新器将不知道你的模块。" %}

### 使用数据库更新器

该工具安装在其他二进制文件旁边（例如 Linux 上的 `env/dist/bin/dbimport`，或 Windows 上构建输出文件夹中的 `dbimport.exe`），并读取它自己的配置文件 **dbimport.conf**，该文件与其它配置文件一样由 `dbimport.conf.dist` 创建。

`dbimport.conf` 包含与 authserver.conf 和 worldserver.conf 相同的 **UPDATE SETTINGS**（`Updates.EnableDatabases`、`Updates.AutoSetup`、`Updates.Redundancy`、`Updates.AllowedModules`、...），此外还有 MySQL 连接设置，因此请确保这些设置与你的服务器配置一致。

<br>

## 帮助

{% include help.html %}

| 安装指南                                                                                                                   |                                         |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读，也可以点击前面的链接在各步骤之间轻松切换。 |
| [<< 第 6 步：服务器最终步骤](final-server-steps)                                                                                  | [第 8 步：客户端设置 >>](client-setup) |
