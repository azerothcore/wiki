# guild\_member

[<-返回至:Characters](database-characters)

**\`guild\_member\` 表**

此表保存了所有公会成员的信息、他们在公会中的职位，以及由他们或公会官员所作的备注。

**表结构**

| Field        | Type        | Attributes | Key    | Null | Default | Extra | Comment      |
| ------------ | ----------- | ---------- | ------ | ---- | ------- | ----- | ------------ |
| [guildid][1] | INT         | UNSIGNED   |        | NO   |         |       | 公会标识符   |
| [guid][2]    | INT         | UNSIGNED   | Unique | NO   |         |       |              |
| [rank][3]    | TINYINT     | UNSIGNED   |        | NO   |         |       |              |
| [pnote][4]   | VARCHAR(31) | SIGNED     |        | NO   |         |       |              |
| [offnote][5] | VARCHAR(31) | SIGNED     |        | NO   |         |       |              |

[1]: #guildid
[2]: #guid
[3]: #rank
[4]: #pnote
[5]: #offnote

**字段说明**

### guildid

成员所属公会的 ID。参见 [guild.guildid](guild#guildid)。

### guid

玩家的 GUID。参见 [characters.guid](characters#guid)。

### rank

玩家在公会中所拥有的职位。参见 [guild\_rank.rid](guild_rank#rid)。

### pnote

由玩家设置的备注，所有人都可以阅读。

### offnote

由公会官员设置的备注，只有公会中的其他官员才能阅读。
