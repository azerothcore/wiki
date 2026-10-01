# guild\_bank\_eventlog

[<-返回至:Characters](database-characters)

**\`guild\_bank\_eventlog\` 表**

**表结构**

| Field               | Type     | Attributes | Key | Null | Default | Extra | Comment              |
| ------------------- | -------- | ---------- | --- | ---- | ------- | ----- | -------------------- |
| [guildid][1]        | INT      | UNSIGNED   | PRI | NO   | 0       |       | 公会标识符           |
| [LogGuid][2]        | INT      | UNSIGNED   | PRI | NO   | 0       |       | 日志记录标识符 - 辅助列 |
| [TabId][3]          | TINYINT  | UNSIGNED   | PRI | NO   | 0       |       | 公会银行标签页 ID    |
| [EventType][4]      | TINYINT  | UNSIGNED   |     | NO   | 0       |       | 事件类型             |
| [PlayerGuid][5]     | INT      | UNSIGNED   |     | NO   | 0       |       |                      |
| [ItemOrMoney][6]    | INT      | UNSIGNED   |     | NO   | 0       |       |                      |
| [ItemStackCount][7] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                      |
| [DestTabId][8]      | TINYINT  | UNSIGNED   |     | NO   | 0       |       | 目标标签页 ID        |
| [TimeStamp][9]      | INT      | UNSIGNED   |     | NO   | 0       |       | 事件的 UNIX 时间     |

[1]: #guildid
[2]: #logguid
[3]: #tabid
[4]: #eventtype
[5]: #playerguid
[6]: #itemormoney
[7]: #itemstackcount
[8]: #desttabid
[9]: #timestamp

**字段说明**

### guildid

公会标识符。

### LogGuid

日志记录标识符 - 辅助列。

### TabId

公会银行标签页 ID。

### EventType

| 值   | 描述                            |
| ---- | ------------------------------- |
| 1    | GUILD\_BANK\_LOG\_DEPOSIT\_ITEM |
| 2    | GUILD\_BANK\_LOG\_WITHDRAW\_ITEM |
| 3    | GUILD\_BANK\_LOG\_MOVE\_ITEM    |
| 4    | GUILD\_BANK\_LOG\_DEPOSIT\_MONEY |
| 5    | GUILD\_BANK\_LOG\_WITHDRAW\_MONEY |
| 6    | GUILD\_BANK\_LOG\_REPAIR\_MONEY |
| 7    | GUILD\_BANK\_LOG\_MOVE\_ITEM2   |
| 8    | GUILD\_BANK\_LOG\_UNK1          |
| 9    | GUILD\_BANK\_LOG\_BUY\_SLOT     |

### PlayerGuid

玩家的 GUID。

### ItemOrMoney

`field-no-description|6`

### ItemStackCount

`field-no-description|7`

### DestTabId

目标标签页 ID。

### TimeStamp

事件的 UNIX 时间。
