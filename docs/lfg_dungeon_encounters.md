# lfg\_dungeon\_encounters

[<-Back-to:World](database-world)

**The \`lfg\_dungeon\_encounters\` table**

**Table Structure**

| Field              | Type | Attributes | Key | Null | Default | Extra | Comment                                   |
| ------------------ | ---- | ---------- | --- | ---- | ------- | ----- | ----------------------------------------- |
| [achievementId][1] | INT  | UNSIGNED   | PRI | NO   | 0       |       | Achievement marking final boss completion |
| [dungeonId][2]     | INT  | UNSIGNED   |     | NO   | 0       |       | Dungeon entry from dbc                    |

[1]: #achievementid
[2]: #dungeonid

**Description of the fields**

### achievementId

Don't know, but surely taken from [Achievement.dbc](achievement)

### dungeonId

Dungeon ID from LFGDungeons.dbc
