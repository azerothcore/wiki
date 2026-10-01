# arena\_team\_member

[<-返回:Characters](database-characters)

**\`arena\_team\_member\` 表**

该表保存了具体战队成员的竞技场信息。所有 arena\_team 的成员都会在此表中有一条记录。

**表结构**

| Field               | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [arenaTeamId][1]    | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [guid][2]           | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [weekGames][3]      | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [weekWins][4]       | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [seasonGames][5]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [seasonWins][6]     | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [personalRating][7] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #arenateamid
[2]: #guid
[3]: #weekgames
[4]: #weekwins
[5]: #seasongames
[6]: #seasonwins
[7]: #personalrating

**字段说明**

### arenaTeamId

竞技场战队的 ID。参见 [arena\_team#arenateamid]。

### guid

玩家的 GUID。参见 [characters.guid](characters#guid)。

### weekGames

本**周**已进行的比赛场数。

### weekWins

本**周**已获胜的比赛场数。

### seasonGames

本**赛季**已进行的比赛场数。

### seasonWins

本**赛季**已获胜的比赛场数。

### personalrating

玩家的个人竞技场评级。
