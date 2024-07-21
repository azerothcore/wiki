# pvpstats\_players

[<-Back-to:Characters](database-characters)

**The \`pvpstats\_players\` table**

This table holds datas about BattleGrounds scores. To enable storing this kind of informations, set **Battleground.StoreStatistics.Enable = 1** in **worldserver.config.dist** file.

**Table Structure**

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

**Description of the fields**

### battleground\_id

Link to [pvpstats\_battlegrounds.id](pvpstats_battlegrounds#id).

### character\_guid

Link to [characters.guid](characters#guid).

### winner

1 when player has won the BG, 0 otherwise.

### score\_\*

All scores which are in common between all BattleGrounds.

### attr\_\*

All scores which are not in common between all BattleGrounds. This fields changes their mean according to [pvpstats\_battlegrounds.type](pvpstats_battlegrounds#type).
