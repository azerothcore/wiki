# module_string

[<-返回:World](database-world)

**\`module_string\` 表**

此表保存模块的字符串条目信息。

**表结构**

| Field             | Type         | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [module](#module) | VARCHAR(255) |            | PRI | NO   |         |       | 模块目录名称，例如 mod-cfbg |
| [id](#id)         | INT          | UNSIGNED   | PRI | NO   |         |       |                          |
| [string](#string) | TEXT         |            |     | NO   |         |       |                          |

**字段说明**

### module

模块标识符

### id

字符串 ID

### string

英文文本
