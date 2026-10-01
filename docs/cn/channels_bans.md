# channels\_bans

[<-返回至:Characters](database-characters)

**\`channels\_bans\` 表**

**表结构**

| Field           | Type  | Attributes | Key | Null | Default | Extra  | Comment |
| --------------- | ----- | ---------- | --- | ---- | ------- | ------ | ------- |
| [channelId][1]  | INT   | UNSIGNED   | PRI | NO   |         |        |         |
| [playerGUID][2] | INT   | UNSIGNED   | PRI | NO   |         |        |         |
| [banTime][3]    | INT   | UNSIGNED   |     | NO   |         |        |         |

[1]: #channelid
[2]: #playerguid
[3]: #banTime

**字段说明**

### channelId

[channel.id](channels#channelid)。

### playerGUID

被禁言玩家的 GUID。参见 [characters.guid](characters#guid)。

### banTime

该[频道](channels#channelId)的封禁时间。
