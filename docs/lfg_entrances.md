# lfg\_entrances

[<-Back-to:World](database-world)

**The \`lfg\_entrances\` table**

Used by LFG system to teleport players on specified position. This table should be used instead of \`areatrigger_teleport\` tabe for all dungeons in the future.

**Table Structure**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment                |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ---------------------- |
| [dungeonId][1]   | INT          | UNSIGNED   | PRI | NO   | 0       |       | Dungeon entry from dbc |
| [name][2]        | VARCHAR(255) |            |     | YES  | NULL    |       | Dungeon name from dbc  |
| [position_x][3]  | FLOAT        |            |     | NO   | 0       |       |                        |
| [position_y][4]  | FLOAT        |            |     | NO   | 0       |       |                        |
| [position_z][5]  | FLOAT        |            |     | NO   | 0       |       |                        |
| [orientation][6] | FLOAT        |            |     | NO   | 0       |       |                        |

[1]: #dungeonid
[2]: #name
[3]: #position_x
[4]: #position_y
[5]: #position_z
[6]: #orientation

**Description of the fields**

### dungeonId

Dungeon ID from LFGDungeons.dbc

### name

Dungeon name from LFGDungeons.dbc

### position\_x

X coordinate for the entrance position

### position\_y

Y coordinate for the entrance position

### position\_z

Z coordinate for the entrance position

### orientation

Orientation the player will get when appearing at this location
