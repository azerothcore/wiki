---
redirect_from: "/cn/Database-Manual-Setup"
---

# 数据库手动安装

## 如何手动安装 AzerothCore 数据库

### MySQL 客户端工具

为了安装你的数据库，你可以使用任何你喜欢的 MySQL 客户端，例如 [HeidiSQL](https://www.heidisql.com/) 或 [DBeaver](https://dbeaver.io/)。

我们假设你已经知道如何执行基本操作，比如创建新数据库、选择数据库以及导入 SQL 转储文件。如果你还不会，别担心：这非常简单，无论你使用哪种 MySQL 客户端工具，都能在 Google 上找到大量教程。

### 创建数据库

创建三个空的数据库：

- `acore_world`
- `acore_characters`
- `acore_auth`


### 导入 SQL 文件

SQL 文件位于 `/data/sql/` 目录下。

`data/sql/base` 中包含用于创建这 3 个数据库（world、auth 和 characters）基础结构与内容的文件。

同样，`data/sql/updates` 中存放着我们的开发人员随时间不断添加的更新。

手动逐个导入这些文件是一个漫长的过程，但可以自动化。脚本 `apps/db_assembler/db_assembler.sh` 允许你将这些文件组装起来（即合并到一起），从而使导入过程更快。
