# pvpstats\_players

[<-Back-to:Characters](database-characters)

**The \`pvpstats\_players\` table**

This table holds datas about BattleGrounds scores. To enable storing this kind of informations, set **Battleground.StoreStatistics.Enable = 1** in **worldserver.config.dist** file.

**Table: pvpstats\_players's Structure**

| Field                              | Type   |          | Null | Key | Default | Extra | Comment |
| :--------------------------------- | :----- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [battleground_id](#battlegroundid) | BIGINT | UNSIGNED | NO   | PRI |         |       |         |
| [character_guid](#characterguid)   | INT    | UNSIGNED | NO   | PRI |         |       |         |
| [winner](#winner)                  | BIT(1) |          | NO   |     |         |       |         |
| [score_killing_blows](#score)      | INT    | UNSIGNED | YES  |     | NULL    |       |         |
| [score_deaths](#score)             | INT    | UNSIGNED | YES  |     | NULL    |       |         |
| [score_honorable_kills](#score)    | INT    | UNSIGNED | YES  |     | NULL    |       |         |
| [score_bonus_honor](#score)        | INT    | UNSIGNED | YES  |     | NULL    |       |         |
| [score_damage_done](#score)        | INT    | UNSIGNED | YES  |     | NULL    |       |         |
| [score_healing_done](#score)       | INT    | UNSIGNED | YES  |     | NULL    |       |         |
| [attr_1](#attr)                    | INT    | UNSIGNED | YES  |     | 0       |       |         |
| [attr_2](#attr)                    | INT    | UNSIGNED | YES  |     | 0       |       |         |
| [attr_3](#attr)                    | INT    | UNSIGNED | YES  |     | 0       |       |         |
| [attr_4](#attr)                    | INT    | UNSIGNED | YES  |     | 0       |       |         |
| [attr_5](#attr)                    | INT    | UNSIGNED | YES  |     | 0       |       |         |

**Description of the table's fields**

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
