---
redirect_from: "/cn/SQL-Versioning"
---

# SQL 版本管理

我们有两种版本类型：

- 按时间顺序的版本管理，用于已接受的 sql 文件
- 按 id 的版本管理，主要用于待处理的 sql

## 按时间顺序的版本管理

我们使用经典的 MaNGOS 方式，以确保 **/data/sql/updates/** 中的所有文件按正确的顺序导入，防止重复导入或跳过文件。

为了实现这一点，我们使用特定的**文件命名约定**，并在文件内容顶部添加一个特殊的 **SQL 头部（SQL Header）**。

### 文件名

文件名不应被重命名，应保持 `create_sql.sh` 为文件创建的名称。

文件名看起来像这样：`rev_XXXXXXXXXXXXXXXXXXX`

### SQL 头部

SQL 头部是一个特殊查询，**必须**添加在**每个** sql 更新文件内容的顶部。

格式如下：

```sql
ALTER TABLE version_db_[database] CHANGE COLUMN [previous_file_name] [this_file_name] bit;
```

替换：

- **[database]** 为 **world**、**character** 或 **auth**
- **[previous_file_name]** 为最新文件的名称（不含扩展名）
- **[this_file_name]** 为新文件本身的名称（不含扩展名）

以下是 SQL 头部查询的示例（针对 auth 数据库）：

```sql
ALTER TABLE `version_db_auth` CHANGE COLUMN 2016_07_09_01 2016_07_10_00 bit;
```

## 按 id 的版本管理

待处理的 sql 文件无法使用上述保护系统，因为我们无法预先知道它们何时会被接受。

因此我们使用一种可选的版本管理方式（但推荐开发者和尤其是提交 pull request 的人使用）。

我们在 version_db_* 表中引入了一个作为主键字符串的字段，还有一个 'required_rev' 字段，你可以用它来建立版本之间的关联。

例如，你可以创建一个与版本 "Y" 相关联的版本 "X"，而不一定要求 "Y" 是紧邻的前一个版本。

目前我们使用这个 bash 命令来尽可能避免修订之间的冲突：

```bash
date +%s%N
```

如果发生冲突（极难发生），也很容易手动解决。

最终查询将是：

```sql
INSERT INTO `version_db_auth` (`sql_rev`, `required_rev`) VALUES ('1472557015805232200','1472557004102672900');
```

或者在没有 required_rev 的情况下：

```sql
INSERT INTO `version_db_auth` (`sql_rev`) VALUES ('1472557015805232200');
```

把它添加到你的 sql 的第一行，在重复导入时会产生错误；这与按时间顺序的版本管理类似。

在 pending_* 文件夹下有一个 bash 脚本，它会为你创建第一行带该行的 sql，并且会以我们的导入系统可识别的方式命名文件。我们强烈建议使用它。

## 待处理导入系统

如前所述，我们为 PR 提供了一个特殊的工作流，以便为开发者保持数据库数据的一致性。

它要求你的 PR 的 sql 做几件事，才能兼容我们的导入系统，并避免重复导入相同的查询。

具体操作方法在[如何创建 PR](how-to-create-a-pr)一文中描述。
