# log\_encounter

[<-Back-to:Characters](database-characters)

**The \`log\_encounter\` table**

**Table Structure**

| Field            | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [time][1]        | DATATIME | SIGNED     |     | NO   |         |       |         |
| [map][2]         | SMALLINT | UNSIGNED   |     | NO   |         |       |         |
| [difficulty][3]  | TINYINT  | UNSIGNED   |     | NO   |         |       |         |
| [creditType][4]  | TINYINT  | UNSIGNED   |     | NO   |         |       |         |
| [creditEntry][5] | INT      | UNSIGNED   |     | NO   |         |       |         |
| [playersInfo][6] | TEXT     | SIGNED     |     | NO   |         |       |         |

[1]: #time
[2]: #map
[3]: #difficulty
[4]: #credittype
[5]: #creditentry
[6]: #playersinfo

**Description of the fields**

### time

The date and time the boss was killed.

### map

The map of the encounter. See [Map.dbc](map).

### difficulty

The difficulty of the map.

### creditType

0 if the encounter was credited by killing a creature, 1 if it was credited by a spell.

### creditEntry

The creature entry or spell ID that credited the encounter.

### playersInfo

One line per player in the map, with the name, GUID, account, IP, guild, position and the auras on the player as `spell(effectMask)`.
