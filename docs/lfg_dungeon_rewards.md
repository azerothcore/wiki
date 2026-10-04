# lfg\_dungeon\_rewards

[<-Back-to:World](database-world)

**The \`lfg\_dungeon\_rewards\` table**

The quests that give the rewards for finishing a random dungeon in the Dungeon Finder, by level.

**Table: lfg\_dungeon\_rewards's Structure**

| Field                         | Type    |          | Null | Key | Default | Extra | Comment                                          |
| :---------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :----------------------------------------------- |
| [dungeonId](#dungeonid)       | INT     | UNSIGNED | NO   | PRI | 0       |       | Dungeon entry from dbc                           |
| [maxLevel](#maxlevel)         | TINYINT | UNSIGNED | NO   | PRI | 0       |       | Max level at which this reward is rewarded       |
| [firstQuestId](#firstquestid) | INT     | UNSIGNED | NO   |     | 0       |       | Quest id with rewards for first dungeon this day |
| [otherQuestId](#otherquestid) | INT     | UNSIGNED | NO   |     | 0       |       | Quest id with rewards for Nth dungeon this day   |

**Description of the table's fields**

### dungeonId

Dungeon ID from LFGDungeons.dbc

### maxlevel

Max level at which this reward is rewarded

### firstQuestId

Quest\_template.id with rewards for first dungeon this day.

### otherQuestId

Quest\_template.id with rewards for Nth dungeon this day
