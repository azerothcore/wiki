# profanity_name

[<-返回至:Characters](database-characters)

**\`profanity_name\` 表**

不当言论（脏话）名称过滤器中使用的禁用名称片段列表，用于拒绝角色、宠物等类似名称。关于完全保留（禁用）的名称，另请参阅 [reserved_name](reserved_name)。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [name](#name) | VARCHAR(12) |  | PRI | NO |  |  |  |

**字段说明**

### name

被不当言论过滤器屏蔽的禁用名称片段（不区分大小写）。
