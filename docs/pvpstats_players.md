# pvpstats\_players

[<-Back-to:Characters](database-characters.md)

**The \`pvpstats\_players\` table**

This table holds datas about BattleGrounds scores. To enable storing this kind of informations, set **Battleground.StoreStatistics.Enable = 1** in **worldserver.config.dist** file.

**Structure**

| Field                      | Type      | Attributes | Key | Null | Default | Extra | Comment |
|----------------------------|-----------|------------|-----|------|---------|-------|---------|
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

[1]: #battleground_id
[2]: #character_guid
[3]: #winner
[4]: #score_
[5]: #score_
[6]: #score_
[7]: #score_
[8]: #score_
[9]: #score_
[10]: #attr_
[11]: #attr_
[12]: #attr_
[13]: #attr_
[14]: #attr_

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