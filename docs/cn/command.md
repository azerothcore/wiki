# command

[<-返回:世界库](database-world)

**`command` 表**

保存命令的帮助和安全信息。这张表并不会创建新命令，它只设置/覆盖安全级别并提供帮助。

**表结构**

| 字段         | 类型        | 属性 | 键 | 空 | 默认值 | 额外 | 备注 |
| ------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [name][1]     | VARCHAR(50) | SIGNED     | PRI | NO   | NULL    |       |         |
| [security][2] | TINYINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [help][3]     | longtext    | SIGNED     |     | YES  | NULL    |       |         |

[1]: #name
[2]: #security
[3]: #help

**字段说明**

### name

命令的名称。参见：[内置命令](gm-commands)

### security

使用该命令所需的安全级别。与 realm 数据库中的 account_access.gmlevel 对应。

### help

由 .help 命令显示的帮助文本。
