# lfg_dungeon_template

[<-Back-to:World](database-world)

**The \`lfg_dungeon_template\` table**

Used to give NPC spells cooldowns for mindcontroll.

**Table Structure**

| Field                           | Type         | Attributes | Key | Null | Default | Extra | Comment                        |
| ------------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------------ |
| [dungeonId](#dungeonid)         | INT          | UNSIGNED   | PRI | NO   | 0       |       | Unique id from LFGDungeons.dbc |
| [name](#name)                   | VARCHAR(255) |            |     | YES  | NULL    |       |                                |
| [position_x](#positionx)        | FLOAT        |            |     | NO   | 0       |       |                                |
| [position_y](#positiony)        | FLOAT        |            |     | NO   | 0       |       |                                |
| [position_z](#positionz)        | FLOAT        |            |     | NO   | 0       |       |                                |
| [orientation](#orientation)     | FLOAT        |            |     | NO   | 0       |       |                                |
| [VerifiedBuild](#verifiedbuild) | INT          |            |     | YES  | NULL    |       |                                |

**Description of the fields**

### DungionId

Unique id from LFGDungeons.dbc

### name

Dungeon Name

### poisition_x

`field-no-description|3`

### poisition_y

`field-no-description|4`

### poisition_z

`field-no-description|5`

### orientation

`field-no-description|6`

### VerifiedBuild

This field is used to determine if the data originates from verified sniffs.

If value is 0 then it has not been parsed yet or it has been inherited from an older DB or another Core.

If value is above 0 then it has been parsed with sniffs from that specific client build.

If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.
