# lfg\_dungeon\_rewards

[<-Back-to:World](database-world)

**The \`lfg\_dungeon\_rewards\` table**

`table-no-description|0`

**Table Structure**

| Field              | Type    | Attributes | Key | Null | Default | Extra | Comment                                                                                         |
| ------------------ | ------- | ---------- | --- | ---- | ------- | ----- | ----------------------------------------------------------------------------------------------- |
| [dungeonId][1]     | INT     | UNSIGNED   | PRI | NO   | 0       |       | Dungeon entry from dbc                                                                          |
| [maxlevel][2]      | TINYINT | UNSIGNED   | PRI | NO   | 0       |       | Max level at which this reward is rewarded                                                      |
| [firstQuestId][3]  | INT     | UNSIGNED   |     | NO   | 0       |       | Quest id with rewards for first dungeon this day                                                |
| [otherQuestId][6]  | INT     | UNSIGNED   |     | NO   | 0       |       | Quest id with rewards for Nth dungeon this day                                                  |

[1]: #dungeonid
[2]: #maxlevel
[3]: #firstquestid
[6]: #otherquestid

**Description of the fields**

### dungeonId

Dungeon ID from LFGDungeons.dbc

### maxlevel

Max level at which this reward is rewarded

### firstQuestId

Quest\_template.id with rewards for first dungeon this day.

### otherQuestId

Quest\_template.id with rewards for Nth dungeon this day
