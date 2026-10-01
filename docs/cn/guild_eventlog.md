# guild\_eventlog

[<-返回至:Characters](database-characters)

**\`guild\_eventlog\` 表**

**表结构**

| Field            | Type    | Attributes | Key | Null | Default | Extra | Comment                |
| ---------------- | ------- | ---------- | --- | ---- | ------- | ----- | ---------------------- |
| [guildid][1]     | INT     | UNSIGNED   | PRI | NO   |         |       | 公会标识符             |
| [LogGuid][2]     | INT     | UNSIGNED   | PRI | NO   |         |       | 日志记录标识符 - 辅助列 |
| [EventType][3]   | TINYINT | UNSIGNED   |     | NO   |         |       | 事件类型               |
| [PlayerGuid1][4] | INT     | UNSIGNED   |     | NO   |         |       | 玩家 1                 |
| [PlayerGuid2][5] | INT     | UNSIGNED   |     | NO   |         |       | 玩家 2                 |
| [NewRank][6]     | TINYINT | UNSIGNED   |     | NO   |         |       | 新职位（用于晋升/降级的情况） |
| [timestamp][7]   | BIGINT  | UNSIGNED   |     | NO   |         |       | 事件的 UNIX 时间       |

[1]: #guildid
[2]: #logguid
[3]: #eventtype
[4]: #playerguid1
[5]: #playerguid2
[6]: #newrank
[7]: #timestamp

**字段说明**

### guildid

公会标识符。

### LogGuid

日志记录标识符 - 辅助列。

### EventType

| 值   | 描述                            |
| ---- | ------------------------------- |
| 1    | GUILD\_EVENT\_LOG\_INVITE\_PLAYER |
| 2    | GUILD\_EVENT\_LOG\_JOIN\_GUILD  |
| 3    | GUILD\_EVENT\_LOG\_PROMOTE\_PLAYER |
| 4    | GUILD\_EVENT\_LOG\_DEMOTE\_PLAYER |
| 5    | GUILD\_EVENT\_LOG\_UNINVITE\_PLAYER |
| 6    | GUILD\_EVENT\_LOG\_LEAVE\_GUILD |

### PlayerGuid1

玩家 1 的 GUID。

### PlayerGuid2

玩家 2 的 GUID。

### NewRank

新职位（用于晋升/降级的情况）。

### timestamp

事件的 UNIX 时间。
