# pvpstats\_players

[<-返回至:Characters](database-characters)

**\`pvpstats\_players\` 表**

此表保存关于战场（BattleGround）得分的数据。要启用此类信息的存储，请在 **worldserver.config.dist** 文件中设置 **Battleground.StoreStatistics.Enable = 1**。

**表结构**

| Field                      | Type      | Attributes | Key | Null | Default | Extra | Comment |
| -------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [battleground_id][1]       | BIGINT    | UNSIGNED   | PRI | NO   |         |       |         |
| [character_guid][2]        | INT       | UNSIGNED   | PRI | NO   |         |       |         |
| [winner][3]                | BIT       | SIGNED     |     | NO   |         |       |         |
| [score_killing_blows][4]   | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [score_deaths][5]          | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [score_honorable_kills][6] | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [score_bonus_honor][7]     | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [score_damage_done][8]     | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [score_healing_done][9]    | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [attr_1][10]               | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [attr_2][11]               | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [attr_3][12]               | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [attr_4][13]               | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [attr_5][14]               | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #battlegroundid
[2]: #characterguid
[3]: #winner
[4]: #score
[5]: #score
[6]: #score
[7]: #score
[8]: #score
[9]: #score
[10]: #attr
[11]: #attr
[12]: #attr
[13]: #attr
[14]: #attr

**字段说明**

### battleground\_id

指向 [pvpstats\_battlegrounds.id](pvpstats_battlegrounds#id)。

### character\_guid

指向 [characters.guid](characters#guid)。

### winner

玩家赢得该战场（BG）时为 1，否则为 0。

### score\_\*

所有战场（BattleGround）之间通用的得分。

### attr\_\*

所有战场（BattleGround）之间不通用的得分。这些字段的含义会根据 [pvpstats\_battlegrounds.type](pvpstats_battlegrounds#type) 而改变。
