# channels

[<-返回至:Characters](database-characters)

**\`channels\` 表**

游戏内基于玩家的聊天频道的信息和设置（不影响默认系统频道）。

**表结构**

| Field           | Type         | Attributes | Key | Null | Default | Extra          | Comment |
| --------------- | ------------ | ---------- | --- | ---- | ------- | -------------- | ------- |
| [channelId][1]  | INT          | SIGNED     | PRI | NO   |         | AUTO_INCREMENT |         |
| [name][2]       | VARCHAR(128) | SIGNED     |     | NO   |         |                |         |
| [team][3]       | INT          | UNSIGNED   |     | NO   |         |                |         |
| [announce][4]   | TINYINT      | UNSIGNED   |     | NO   | 1       |                |         |
| [ownership][5]  | TINYINT      | UNSIGNED   |     | NO   | 1       |                |         |
| [password][6]   | VARCHAR(32)  | SIGNED     |     | YES  |         |                |         |
| [lastUsed][7]   | INT          | UNSIGNED   |     | NO   |         |                |         |

[1]: #channelid
[2]: #name
[3]: #team
[4]: #announce
[5]: #ownership
[6]: #password
[7]: #lastused

**字段说明**

### channelId

频道的 ID。

### name

频道的名称。

### team

允许通过指定的玩家阵营 ID 访问频道。

对于多阵营频道，必须存在两个（或更多）独立的条目，除本字段外所有字段的设置必须完全相同（本字段需要不同的 `team id`）。

| 阵营   | 值   |
| ------ | ---- |
| 部落   | 67   |
| 联盟   | 469  |

### announce

频道公告（0/1）。

- 0 = 不会发送频道加入/离开动作
- 1 = 会发送频道加入/离开动作

### ownership

频道所有权。

- 0 = 永远没有人成为所有者。
- 1 = 频道中的第一个人成为所有者。

### password

频道密码。

为空，或是一个标准的字符串密码（不允许空格）。

### lastUsed

用于自动清理数据库中不使用的频道。时间为 Unix 时间。
