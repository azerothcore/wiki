# corpse

[<-Back-to:Characters](database-characters.md)

**The \`corpse\` table**

**Structure**

| Field            | Type     | Attributes | Key | Null | Default | Extra  | Comment                            |
| ---------------- | -------- | ---------- | --- | ---- | ------- | ------ | ---------------------------------- |
| [guid][1]        | INT      | UNSIGNED   | PRI | NO   | 0       |        | Character Global Unique Identifier |
| [posX][2]        | FLOAT    | SIGNED     |     | NO   | 0       |        |                                    |
| [posY][3]        | FLOAT    | SIGNED     |     | NO   | 0       |        |                                    |
| [posZ][4]        | FLOAT    | SIGNED     |     | NO   | 0       |        |                                    |
| [orientation][5] | FLOAT    | SIGNED     |     | NO   | 0       |        |                                    |
| [mapId][6]       | SMALLINT | UNSIGNED   |     | NO   | 0       |        | Map Identifier                     |
| [phaseMask][7]   | INT      | UNSIGNED   |     | NO   | 1       |        |                                    |
| [displayId][8]   | INT      | UNSIGNED   |     | NO   | 0       |        |                                    |
| [itemCache][9]   | TEXT     | SIGNED     |     | NO   |         |        |                                    |
| [bytes1][10]     | INT      | UNSIGNED   |     | NO   | 0       |        |                                    |
| [bytes2][11]     | INT      | UNSIGNED   |     | NO   | 0       |        |                                    |
| [guildId][12]    | INT      | UNSIGNED   |     | NO   | 0       |        |                                    |
| [flags][13]      | TINYINT  | UNSIGNED   |     | NO   | 0       |        |                                    |
| [dynFlags][14]   | TINYINT  | UNSIGNED   |     | NO   | 0       |        |                                    |
| [time][15]       | INT      | UNSIGNED   |     | NO   | 0       |        |                                    |
| [corpseType][16] | TINYINT  | UNSIGNED   |     | NO   | 0       |        |                                    |
| [instanceId][17] | INT      | UNSIGNED   |     | NO   | 0       |        | Instance Identifier                |

[1]: #guid
[2]: #posx
[3]: #posy
[4]: #posz
[5]: #orientation
[6]: #mapid
[7]: #phasemask
[8]: #displayid
[9]: #itemcache
[10]: #bytes1
[11]: #bytes2
[12]: #guildid
[13]: #flags
[14]: #dynFlags
[15]: #time
[16]: #corpsetype
[17]: #instanceid

**Description of the fields**

### guid

The character guid. See [characters.guid](characters#guid).

### posX

`field-no-description|2`

### posY

`field-no-description|3`

### posZ

`field-no-description|4`

### orientation

`field-no-description|5`

### mapId

`field-no-description|6`

### phaseMask

`field-no-description|7`

### displayId

`field-no-description|8`

### itemCache

`field-no-description|9`

### bytes1

`field-no-description|10`

### bytes2

`field-no-description|11`

### guildId

`field-no-description|12`

### flags

`field-no-description|13`

### dynFlags

`field-no-description|14`

### time

`field-no-description|15`

### corpseType

`field-no-description|16`

### instanceId

`field-no-description|17`