# spell\_target\_position

[<-Back-to:World](database-world)

**The \`spell\_target\_position\` table**

This table holds coordinate information on where the player should be teleported to when a spell with target type: TARGET\_DST\_DB(17).

**Table Structure**

| Field                   | Type      | Attributes | Key | Null | Default | Extra | Comment    |
| ----------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------- |
| [id][1]            | INT       | UNSIGNED   | PRI | NO   | 0       |       | Identifier |
| [EffectIndex][7]   | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |            |
| [MapID][2]         | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |            |
| [PositionX][3]     | FLOAT     |            |     | NO   | 0       |       |            |
| [PositionY][4]     | FLOAT     |            |     | NO   | 0       |       |            |
| [PositionZ][5]     | FLOAT     |            |     | NO   | 0       |       |            |
| [Orientation][6]   | FLOAT     |            |     | NO   | 0       |       |            |
| [VerifiedBuild][8] | INT       |            |     | YES  | NULL    |       |            |

[1]: #id
[2]: #mapid
[3]: #positionx
[4]: #positiony
[5]: #positionz
[6]: #orientation
[7]: #effectindex
[8]: #verifiedbuild

**Description of the fields**

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
