# lfg\_dungeon\_template

[<-Back-to:World](database-world)

**The \`lfg\_dungeon\_template\` table**

Used to give NPC spells cooldowns for mindcontroll.

**Table: lfg\_dungeon\_template's Structure**

| Field                           | Type         |          | Null | Key | Default | Extra | Comment                        |
| :------------------------------ | :----------- | :------- | :--: | :-: | :-----: | :---: | :----------------------------- |
| [dungeonId](#dungeonid)         | INT          | UNSIGNED | NO   | PRI | 0       |       | Unique id from LFGDungeons.dbc |
| [name](#name)                   | VARCHAR(255) |          | YES  |     | NULL    |       |                                |
| [position_x](#positionx)        | FLOAT        |          | NO   |     | 0       |       |                                |
| [position_y](#positiony)        | FLOAT        |          | NO   |     | 0       |       |                                |
| [position_z](#positionz)        | FLOAT        |          | NO   |     | 0       |       |                                |
| [orientation](#orientation)     | FLOAT        |          | NO   |     | 0       |       |                                |
| [VerifiedBuild](#verifiedbuild) | INT          |          | YES  |     | NULL    |       |                                |

**Description of the table's fields**

### dungeonId

Unique id from LFGDungeons.dbc

### name

Dungeon Name

### position_x

X position players are teleported to when the Dungeon Finder sends them into the dungeon.

### position_y

Y position players are teleported to.

### position_z

Z position players are teleported to.

### orientation

Orientation of players after the teleport.

### VerifiedBuild

This field is used to determine if the data originates from verified sniffs.

If value is 0 then it has not been parsed yet or it has been inherited from an older DB or another Core.

If value is above 0 then it has been parsed with sniffs from that specific client build.

If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.
