# guild\_rank

[<-返回:角色](database-characters)

**\`guild\_rank\` 表**

该表存储了公会中所有可用等级的信息，包括等级名称以及拥有该等级的人员所拥有的权限。

**表结构**

| Field                | Type        | Attributes | Key | Null | Default | Extra | Comment |
| -------------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guildid][1]         | INT         | UNSIGNED   | PRI | NO   | 0       |       |         |
| [rid][2]             | TINYINT     | UNSIGNED   | PRI | NO   |         |       |         |
| [rname][3]           | VARCHAR(20) | SIGNED     |     | NO   | "       |       |         |
| [rights][4]          | MEDIUMINT   | UNSIGNED   |     | NO   | 0       |       |         |
| [BankMoneyPerDay][5] | INT         | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guildid
[2]: #rid
[3]: #rname
[4]: #rights
[5]: #bankmoneyperday

**字段说明**

### guildid

该等级所属的公会 ID。参见 [guild.guildid](guild#guildid)。

### rid

特定的等级 ID。该编号在公会内的每个等级中必须是唯一的。

### rname

游戏中显示的等级名称。

### rights

拥有该等级的角色在公会中拥有的权限。这种情况下多个权限的计算方式略有不同，因为权限值并非都是 2^n 的值。要组合权限，你必须对两个标志进行 OR 运算（\|）。

| Flag    | Name                        | Comments                                                                  |
| ------- | --------------------------- | ------------------------------------------------------------------------- |
| 64      | GR_RIGHT_EMPTY              | 仅拥有此标志本身相当于没有任何权限。                                       |
| 65      | GR_RIGHT_GCHATLISTEN        | 角色可以读取公会普通聊天频道的消息。                                       |
| 66      | GR_RIGHT_GCHATSPEAK         | 角色可以在公会普通聊天频道输入消息。                                       |
| 68      | GR_RIGHT_OFFCHATLISTEN      | 角色可以读取公会官员频道的消息。                                           |
| 72      | GR_RIGHT_OFFCHATSPEAK       | 角色可以在公会官员频道输入消息。                                           |
| 80      | GR_RIGHT_INVITE             | 可以邀请其他玩家加入公会。                                                 |
| 96      | GR_RIGHT_REMOVE             | 可以将其他玩家踢出公会。                                                   |
| 192     | GR_RIGHT_PROMOTE            | 可以提升其他玩家。                                                         |
| 320     | GR_RIGHT_DEMOTE             | 可以降级其他玩家。                                                         |
| 4160    | GR_RIGHT_SETMOTD            | 可以修改公会的每日公告。                                                   |
| 8256    | GR_RIGHT_EPNOTE             | 可以编辑其他玩家的个人备注。                                               |
| 16448   | GR_RIGHT_VIEWOFFNOTE        | 可以查看其他玩家的官员备注。                                               |
| 32832   | GR_RIGHT_EOFFNOTE           | 可以编辑其他玩家的官员备注。                                               |
| 65600   | GR_RIGHT_MODIFY_GUILD_INFO  | 可以编辑公会信息。                                                         |
| 131072  | GR_RIGHT_WITHDRAW_GOLD_LOCK | 可以取消金币提取权限。                                                     |
| 262144  | GR_RIGHT_WITHDRAW_REPAIR    | 可以提取金币用于修理。                                                     |
| 524288  | GR_RIGHT_WITHDRAW_GOLD      | 可以提取金币。                                                             |
| 1048576 | GR_RIGHT_CREATE_GUILD_EVENT | 可以创建公会活动。                                                         |
| 1962495 | GR_RIGHT_ALL                | 拥有所有权限。                                                             |

### BankMoneyPerDay

拥有该等级的角色每天可以提取的金币总额（以铜币为单位）。使用 UNSIGNED INT 的最大值（4294967295）来指定无限额度。
