# world_state

[<-返回至:Characters](database-characters)

**\`world_state\` 表**

持久化服务器全局的世界状态值，使其在服务器重启后仍然保留。每一行保存一个按内部保存 `Id` 键控的、序列化的世界状态数据块。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Id](#id) | INT | UNSIGNED | PRI | NO |  |  | 内部保存 ID |
| [Data](#data) | LONGTEXT |  |  | YES | (NULL) |  |  |

**字段说明**

### Id

内部世界状态保存标识符。

### Data

序列化的世界状态数据。
