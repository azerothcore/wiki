# lfg\_dungeon\_rewards

[<-Back-to:World](database-world.md)

**The \`lfg\_dungeon\_encounters\` table**

`table-no-description|0`

**Structure**

| Field              | Type       | Attributes | Key | Null | Default | Extra | Comment                                                                                         |
|--------------------|------------|------------|-----|------|---------|-------|-------------------------------------------------------------------------------------------------|
| [dungeonId][1]     | int(10)    | unsigned   | PRI | NO   | 0       |       | Dungeon entry from dbc                                                                          |
| [maxlevel][2]      | TINYINT(3) | unsigned   | PRI | NO   | 0       |       | Max level at which this reward is rewarded                                                      |
| [firstQuestId][3]  | int(10)    | unsigned   |     | NO   | 0       |       | Quest id with rewards for first dungeon this day                                                |
| [firstMoneyVar][4] | int(10)    | unsigned   |     | NO   | 0       |       | Money multiplier for completing the dungeon first time in a day with less players than max      |
| [firstXPVar][5]    | int(10)    | unsigned   |     | NO   | 0       |       | Experience multiplier for completing the dungeon first time in a day with less players than max |
| [otherQuestId][6]  | int(10)    | unsigned   |     | NO   | 0       |       | Quest id with rewards for Nth dungeon this day                                                  |
| [otherMoneyVar][7] | int(10)    | unsigned   |     | NO   | 0       |       | Money multiplier for completing the dungeon Nth time in a day with less players than max        |
| [otherXPVar][8]    | int(10)    | unsigned   |     | NO   | 0       |       | Experience multiplier for completing the dungeon Nth time in a day with less players than max   |

[1]: #dungeonid
[2]: #maxlevel
[3]: #firstquestid
[4]: #firstmoneyvar
[5]: #firstxpvar
[6]: #otherquestid
[7]: #othermoneyvar
[8]: #otherxpvar

**Description of the fields**

### dungeonId

Dungeon ID from LFGDungeons.dbc

### maxlevel

Max level at which this reward is rewarded

### firstQuestId

Quest\_template.id with rewards for first dungeon this day.

### firstMoneyVar

Money multiplier for completing the dungeon first time in a day with less players than max.

### firstXPVar

Experience multiplier for completing the dungeon first time in a day with less players than max.

### otherQuestId

Quest\_template.id with rewards for Nth dungeon this day

### otherMoneyVar

Money multiplier for completing the dungeon Nth time in a day with less players than max.

### otherXPVar

Experience multiplier for completing the dungeon Nth time in a day with less players than max.
