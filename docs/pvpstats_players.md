# pvpstats\_players

[<-Back-to:Characters](database-characters.md)

**The \`[pvpstats\_players](http://collab.kpsn.org/pages/createpage.action?spaceKey=tc&title=pvpstats_battlegrounds&linkCreation=true&fromPageId=331580)\` table**

This table holds datas about BattleGrounds scores. To enable storing this kind of informations, set **Battleground . StoreStatistics . Enable = 1** in **worldserver.config** file.

**Structure**

| Field                      | Type      | Attributes | Key | Null | Default | Extra | Comment |
|----------------------------|-----------|------------|-----|------|---------|-------|---------|
| [battleground_id][1]       | BIGINT    | unsigned   | PRI | NO   |         |       |         |
| [character_guid][2]        | int       | unsigned   | PRI | NO   |         |       |         |
| [win][3]                   | bit       |            |     |      |         |       |         |
| [score_killing_blows][4]   | mediumint | unsigned   |     | NO   |         |       |         |
| [score_deaths][5]          | mediumint | unsigned   |     | NO   |         |       |         |
| [score_honorable_kills][6] | mediumint | unsigned   |     | NO   |         |       |         |
| [score_bonus_honor][7]     | mediumint | unsigned   |     | NO   |         |       |         |
| [score_damage_done][8]     | mediumint | unsigned   |     | NO   |         |       |         |
| [score_healing_done][9]    | mediumint | unsigned   |     | NO   |         |       |         |
| [attr_1][10]               | mediumint | unsigned   |     | NO   | 0       |       |         |
| [attr_2][11]               | mediumint | unsigned   |     | NO   | 0       |       |         |
| [attr_3][12]               | mediumint | unsigned   |     | NO   | 0       |       |         |
| [attr_4][13]               | mediumint | unsigned   |     | NO   | 0       |       |         |
| [attr_5][14]               | mediumint | unsigned   |     | NO   | 0       |       |         |

[1]: #battleground_id
[2]: #character_guid
[3]: #win
[4]: #score_killing_blows
[5]: #score_deaths
[6]: #score_honorable_kills
[7]: #score_bonus_honor
[8]: #score_damage_done
[9]: #score_healing_done
[10]: #attr_1
[11]: #attr_2
[12]: #attr_3
[13]: #attr_4
[14]: #attr_5

**Description of the fields**

### battleground\_id

Link to pvpstats\_battlegrounds.id

### character\_guid

Link to characters.guid

### winner

1 when player has won the BG, 0 otherwise

### score\_\*

All scores which are in common between all BattleGrounds

### attr\_\*

All scores which are not in common between all BattleGrounds. This fields changes their mean according to pvpstats\_battlegrounds.type
