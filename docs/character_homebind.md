# character\_homebind

[<-Back-to:Characters](database-characters)

**The \`character\_homebind\` table**

Contains information on the location where characters get teleported when they use their Hearthstone.

**Table Structure**

| Field       | Type        | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]   | INT         | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [mapId][2]  | SMALLINT    | UNSIGNED   |     | NO   | 0       |       | Map Identifier           |
| [zoneId][3] | SMALLINT    | UNSIGNED   |     | NO   | 0       |       | Zone Identifier          |
| [posX][4]   | FLOAT       | SIGNED     |     | NO   | 0       |       |                          |
| [posY][5]   | FLOAT       | SIGNED     |     | NO   | 0       |       |                          |
| [posZ][6]   | FLOAT       | SIGNED     |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #mapid
[3]: #zoneid
[4]: #posx
[5]: #posy
[6]: #posz

**Description of the fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### mapId

The map ID where the character gets teleported to. See [Map.dbc](map) column 1.

### zoneId

The zone ID where the character gets teleported to. See [AreaTable.dbc](areatable) column 1.

### posX

The X position where the character gets teleported to.

### posY

The Y position where the character gets teleported to.

### posZ

The Z position where the character gets teleported to.
