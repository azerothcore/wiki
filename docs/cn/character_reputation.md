# character\_reputation

[<-返回:Characters](database-characters)

**\`character\_reputation\` 表**

该表保存每个角色的声望信息。

**表结构**

| Field         | Type        | Attributes | Key | Null | Default | Extra | Comment                  |
| ------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]     | INT         | UNSIGNED   | PRI | NO   | 0       |       | 全局唯一标识符           |
| [faction][2]  | SMALLINT    | UNSIGNED   | PRI | NO   | 0       |       |                          |
| [standing][3] | INT         | SIGNED     |     | NO   | 0       |       |                          |
| [flags][4]    | SMALLINT    | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #faction
[3]: #standing
[4]: #flags

**字段说明**

### guid

角色 GUID。参见 [characters.guid](characters#guid)。

### faction

角色在该阵营中拥有上述声望的阵营 ID。参见 [Faction.dbc](faction)。

### standing

角色当前拥有的声望值。

### flags

该字段是一个位掩码，包含应用于该阵营以及其在角色面前显示方式的标志。与任何标志字段一样，你可以通过将标志相加来组合它们。如果该字段为 0，则不会显示在游戏内的声望列表中。

| Flag | Name                          | Comments                                                                 |
|----- | ----------------------------- | ------------------------------------------------------------------------ |
| 1    | FACTION_FLAG_VISIBLE          | 显示在声望选项卡中                                                        |
| 2    | FACTION_FLAG_AT_WAR           | 当玩家勾选“交战”（at war）复选框时处于激活状态                           |
| 4    | FACTION_FLAG_HIDDEN           | 在客户端的声望面板中隐藏该阵营                                            |
| 8    | FACTION_FLAG_INVISIBLE_FORCED | 始终覆盖 FACTION_FLAG_VISIBLE，并在声望列表中隐藏该阵营                   |
| 16   | FACTION_FLAG_PEACE_FORCED     | 始终覆盖 FACTION_FLAG_AT_WAR                                              |
| 32   | FACTION_FLAG_INACTIVE         |                                                                           |
| 64   | FACTION_FLAG_RIVAL            | 用于两个相互竞争的外域阵营的标志                                          |
| 128  | FACTION_FLAG_SPECIAL          | 部落和联盟的主城及其诺森德盟友拥有此标志                                  |
