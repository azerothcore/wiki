# 数据库安装

| 安装指南                                                                                                                             |                                     |
| :----------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 第 3 步：服务器设置](server-setup)                                                                                               | [第 5 步：网络设置 >>](networking) |

## 在 MySQL 中创建数据库

### 创建数据库和用户

首先，你需要创建 acore 用户。你需要在 MySQL 客户端中或通过 MySQL 命令行界面（CLI）运行下面的脚本。
你需要在 MySQL 客户端或 MySQL 命令行界面中，以 MySQL **root** 用户的身份运行该脚本。

https://github.com/azerothcore/azerothcore-wotlk/blob/master/data/sql/create/create_mysql.sql

{% include important.html content="仅使用 MySQL root 用户运行上述脚本，切勿以 root 或管理员身份运行核心！" %}

{% include tip.html content="你可以更改所创建用户的密码以增强安全性。" %}

## 填充数据库

如果你想知道 SQL 目录是如何工作的，或打算进行自定义修改，我们建议你阅读[这篇文档](sql-directory)。

#### 自动数据库更新器 {#automatic-database-updater}

认证服务器（Authserver）和世界服务器（Worldserver）会在启动时检查并应用所有必要的数据库文件。

若要编辑自动数据库更新器，你可以在 authserver.conf 和 worldserver.conf 的 **UPDATE SETTINGS**（更新设置）下找到相关配置。

1. 启动 Authserver.exe，它位于你创建的 Build 文件夹中的 \bin\RelWithDebInfo 或 \bin\Debug 文件夹下。
2. 启动 Worldserver.exe，位于同一位置。

如果你在控制台中看到以下信息，按回车键即可创建并填充数据库。

```
Database "acore_auth" does not exist
Do you want to create it? [yes (default) / no]:
```

<br>

## 帮助

{% include help.html %}

| 安装指南                                                                                                                             |                                     |
| :----------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 第 3 步：服务器设置](server-setup)                                                                                               | [第 5 步：网络设置 >>](networking) |
