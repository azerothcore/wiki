# lfg\_data

[<-返回至:Characters](database-characters)

**\`lfg\_data\` 表**

此表包含 LFG 的已保存数据。该表由核心（core）持续使用。

**表结构**

| Field        | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
| ------------ | ------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]    | INT     | UNSIGNED   | PRI | NO   | 0       |       | 全局唯一标识符 |
| [dungeon][2] | INT     | UNSIGNED   |     | NO   | 0       |       |                          |
| [state][3]   | TINYINT | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #dungeon
[3]: #state

**字段说明**

### guid

此队伍的 guid。

### dungeon

来自 dbc 的副本（dungeon）ID。

### state

此队伍/副本的状态。
