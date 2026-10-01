# character_settings

[<-返回:Characters](database-characters)

**\`character_settings\` 表**

存储任意按角色划分的键值设置数据块。模块和子系统使用此表来持久化它们自己角色作用域的配置。\`guid\` 引用 \`characters.guid\`。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid](#guid) | INT | UNSIGNED | PRI | NO |  |  |  |
| [source](#source) | VARCHAR(40) |  | PRI | NO |  |  |  |
| [data](#data) | TEXT |  |  | YES | (NULL) |  |  |

**字段说明**

### guid

引用 \`characters.guid\` – 该设置所属的角色。

### source

拥有此行数据的设置组 / 模块的标识符。

### data

针对给定 \`source\` 的序列化设置负载。
