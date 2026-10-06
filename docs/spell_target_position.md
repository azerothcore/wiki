# spell\_target\_position

[<-Back-to:World](database-world)

**The \`spell\_target\_position\` table**

This table holds coordinate information on where the player should be teleported to when a spell with target type: TARGET\_DEST\_DB(17).

**Table: spell\_target\_position's Structure**

| Field                           | Type     |          | Null | Key | Default | Extra | Comment    |
| :------------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :--------- |
| [ID](#id)                       | INT      | UNSIGNED | NO   | PRI | 0       |       | Identifier |
| [EffectIndex](#effectindex)     | TINYINT  | UNSIGNED | NO   | PRI | 0       |       |            |
| [MapID](#mapid)                 | SMALLINT | UNSIGNED | NO   |     | 0       |       |            |
| [PositionX](#positionx)         | FLOAT    |          | NO   |     | 0       |       |            |
| [PositionY](#positiony)         | FLOAT    |          | NO   |     | 0       |       |            |
| [PositionZ](#positionz)         | FLOAT    |          | NO   |     | 0       |       |            |
| [Orientation](#orientation)     | FLOAT    |          | NO   |     | 0       |       |            |
| [VerifiedBuild](#verifiedbuild) | INT      |          | YES  |     | NULL    |       |            |

**Description of the table's fields**

### id

The spell ID. See [Spell.dbc](spell)

### EffectIndex

The spell effect index this target position applies to.

### MapID

Map where the player should be teleported to. See [Map.dbc](map).

### PositionX

X coordinate for the target destination of the spell.

### PositionY

Y coordinate for the target destination of the spell.

### PositionZ

Z coordinate for the target destination of the spell.

### Orientation

Orientation the player will get when appearing at this location

### VerifiedBuild

Client build this row was verified against (from WDB/ADB extraction). `NULL` if not applicable.
