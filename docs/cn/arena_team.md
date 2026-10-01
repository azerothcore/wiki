# arena\_team

[<-返回:Characters](database-characters)

**\`arena\_team\` 表**

该表保存了主要的竞技场战队（ArenaTeam）信息。所有已创建的战队，以及正在创建过程中的战队，都会在此表中有一条记录。

**表结构**

| Field                 | Type        | Attributes | Key | Null | Default | Extra  | Comment |
| --------------------- | ----------- | ---------- | --- | ---- | ------- | ------ | ------- |
| [arenaTeamId][1]      | INT         | UNSIGNED   | PRI | NO   | 0       | Unique |         |
| [name][2]             | VARCHAR(24) | SIGNED     |     | NO   |         |        |         |
| [captainGuid][3]      | INT         | UNSIGNED   |     | NO   | 0       |        |         |
| [type][4]             | TINYINT     | UNSIGNED   |     | NO   | 0       |        |         |
| [rating][5]           | SMALLINT    | UNSIGNED   |     | NO   | 0       |        |         |
| [seasonGames][6]      | SMALLINT    | UNSIGNED   |     | NO   | 0       |        |         |
| [seasonWins][7]       | SMALLINT    | UNSIGNED   |     | NO   | 0       |        |         |
| [weekGames][8]        | SMALLINT    | UNSIGNED   |     | NO   | 0       |        |         |
| [weekWins][9]         | SMALLINT    | UNSIGNED   |     | NO   | 0       |        |         |
| [rank][10]            | INT         | UNSIGNED   |     | NO   | 0       |        |         |
| [BackgroundColor][11] | INT         | UNSIGNED   |     | NO   | 0       |        |         |
| [emblemStyle][12]     | TINYINT     | UNSIGNED   |     | NO   | 0       |        |         |
| [emblemColor][13]     | INT         | UNSIGNED   |     | NO   | 0       |        |         |
| [borderStyle][14]     | TINYINT     | UNSIGNED   |     | NO   | 0       |        |         |
| [borderColor][15]     | INT         | UNSIGNED   |     | NO   | 0       |        |         |

[1]: #arenateamid
[2]: #name
[3]: #captainguid
[4]: #type
[5]: #rating
[6]: #seasongames
[7]: #seasonwins
[8]: #weekgames
[9]: #weekwins
[10]: #rank
[11]: #backgroundcolor
[12]: #emblemstyle
[13]: #emblemcolor
[14]: #borderstyle
[15]: #bordercolor

**字段说明**

### arenaTeamId

竞技场战队的 ID。该编号对每个战队都是唯一的，是识别战队的主要方式。

### name

竞技场战队的名称。

### captainGuid

创建竞技场战队的角色的 GUID。参见 [characters.guid](characters#guid)。

### type

定义竞技场类型（ArenaType）：

- 2 – 2v2 战队
- 3 – 3v3 战队
- 5 – 5v5 战队

### rating

竞技场战队的评级。

### seasonGames

本**赛季**已进行的比赛场数。

### seasonWins

本**赛季**已获胜的比赛场数。

### weekGames

本**周**已进行的比赛场数。

### weekWins

本**周**已获胜的比赛场数。

### rank

战队按评级在比赛中的排名。

### BackgroundColor

战队战袍的背景色（与公会战袍相同）。

### emblemStyle

战队战袍的徽章样式（与公会战袍相同）。

### emblemColor

战队战袍的徽章颜色（与公会战袍相同）。

### borderStyle

战队战袍的边框样式（与公会战袍相同）。

### borderColor

战队战袍的边框颜色（与公会战袍相同）。
