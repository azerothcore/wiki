# SQL 目录

$ 是相对于源码目录的。

## 创建与删除文件

所有创建和删除文件都位于 $\data\sql\create\ 目录中。

`create_mysql.sql` 包含创建 acore 用户和数据库的查询语句。

`drop_mysql.sql` 删除 acore 用户并删除所有数据库。

## 基础文件

所有基础文件都位于 $\data\sql\base\ 目录中，按数据库分别存放在 `db_auth\`、`db_characters\` 和 `db_world\` 子目录中。

每个文件包含单张表压缩后的内容，因此整个目录包含了截至最近一次压缩的所有数据。

该目录中的文件会由[自动数据库更新器](database-installation#automatic-database-updater)自动导入。

基础文件只由项目维护者重新生成，使用 $\apps\DatabaseSquash\ 目录中的 `DatabaseSquash.sh` 脚本。具体流程记录在该目录内的 `database-squash.md` 中。

## 更新文件

所有更新文件都位于 $\data\sql\updates\ 目录中，按数据库分别存放在 `db_auth\`、`db_characters\` 和 `db_world\` 子目录中。

这些文件包含自上次压缩以来提交的所有更新。

该目录中的文件会由[自动数据库更新器](database-installation#automatic-database-updater)自动导入。

## 待处理更新文件

所有待处理更新文件都位于 $\data\sql\updates\pending_db_*\ 目录中，每个数据库一个。

你在 AzerothCore 上为修复问题所做的所有 SQL 修改都应放在这里。

你可以通过运行同一目录下的 `create_sql.sh` 脚本来创建待处理更新文件。

## 自定义文件

所有自定义文件都位于 $\data\sql\custom\ 目录中，按数据库分别存放在 `db_auth\`、`db_characters\` 和 `db_world\` 子目录中。

你对数据库所做的所有自定义更新都应存储在该目录下的 SQL 文件中，以确保在更新服务器时不会丢失。

这些文件只要内容发生变化就会被重新应用，因此它们必须可以安全地重复运行，例如使用 `CREATE TABLE IF NOT EXISTS`、`REPLACE INTO`、`DELETE` + `INSERT` 或带有固定值的 `UPDATE` 语句。

该目录中的文件会由[自动数据库更新器](database-installation#automatic-database-updater)自动导入。

## 归档文件

所有归档文件都位于 $\data\sql\archive\ 目录中，按数据库分别存放在 `db_auth\`、`db_characters\` 和 `db_world\` 子目录中。

当 `updates` 目录变得过大时，更新文件会被移动到这里。它们不属于压缩流程的一部分，也不会被再次应用，因为基础文件中附带的 `updates` 表已经包含它们的条目。

## 旧文件

ACDB 10.0.0 之前的所有更新文件都存储在这里，先按数据库分组，再按主版本（`1.x` 到 `9.x`）分组。从 ACDB 10.0.0 开始，引入了更新基础文件的新方法。
