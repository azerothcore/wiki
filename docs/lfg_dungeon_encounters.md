# lfg\_dungeon\_encounters

[<-Back-to:World](database-world.md)

**The \`lfg\_dungeon\_encounters\` table**

**Structure**

| Field              | Type    | Attributes | Key | Null | Default | Extra | Comment                                   |
|--------------------|---------|------------|-----|------|---------|-------|-------------------------------------------|
| [achievementId][1] | int(10) | unsigned   | PRI | NO   | 0       |       | Achievement marking final boss completion |
| [dungeonId][2]     | int(10) | unsigned   |     | NO   | 0       |       | Dungeon entry from dbc                    |

[1]: #achievementid
[2]: #dungeonid

**Description of the fields**

### achievementId

Don't know, but surely taken from [Achievement.dbc](Achievement)

### dungeonId

Dungeon ID from LFGDungeons.dbc
