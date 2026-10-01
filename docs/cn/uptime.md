# uptime

[<-返回:Auth](database-auth)

**\`uptime\` 表**

此表保存服务器的运行时间。核心会自动更新最新记录的值，直到崩溃后新增一条记录。

**表结构**

| Field           | Type         | Attributes | Key | Null | Default     | Extra | Comment |
| --------------- | ------------ | ---------- | --- | ---- | ----------- | ----- | ------- |
| [realmid][1]    | INT          | UNSIGNED   | PRI | NO   |             |       |         |
| [starttime][2]  | INT          | UNSIGNED   | PRI | NO   | 0           |       |         |
| [uptime][3]     | INT          | UNSIGNED   |     | NO   | 0           |       |         |
| [maxplayers][4] | SMALLINT     | UNSIGNED   |     | NO   | 0           |       |         |
| [revision][5]   | VARCHAR(255) | SIGNED     |     | NO   | AzerothCore |       |         |

[1]: #realmid
[2]: #starttime
[3]: #uptime
[4]: #maxplayers
[5]: #revision

**字段描述**

### realmid

realm 的 ID。参见 [realmlist.id](realmlist#id)。

### starttime

服务器启动的时间，以 Unix 时间表示。

### uptime

服务器的运行时间，以秒为单位。

### maxplayers

已连接玩家的最大数量。

### revision

worldserver 的详细修订版本。
