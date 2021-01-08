# character\_homebind

[<-Back-to:Characters](database-characters.md)

**The \`character\_homebind\` table**

Contains information on the location where characters get teleported when they use their Hearthstone.

**Structure**

| Field       | Type        | Attributes | Key | Null | Default | Extra | Comment                  |
|-------------|-------------|------------|-----|------|---------|-------|--------------------------|
| [guid][1]   | int(10)     | unsigned   | PRI | NO   | 0       |       | Global Unique Identifier |
| [mapId][2]  | smallint(5) | unsigned   |     | NO   | 0       |       | Map Identifier           |
| [zoneId][3] | smallint(5) | unsigned   |     | NO   | 0       |       | Zone Identifier          |
| [posX][4]   | float       | signed     |     | NO   | 0       |       | Coordinate x             |
| [posY][5]   | float       | signed     |     | NO   | 0       |       | Coordinate y             |
| [posZ][6]   | float       | signed     |     | NO   | 0       |       | Coordinate z             |

[1]: #guid
[2]: #mapid
[3]: #zoneid
[4]: #posx
[5]: #posy
[6]: #posz

**Description of the fields**

### guid

The GUID of the character. See [characters.guid](2129969.html#characters(table)-guid)

### mapId

The map ID where the character gets teleported to. See Map.dbc column 1

### zoneId

The zone ID where the character gets teleported to. See AreaTable.dbc column 1

### posX

The X position where the character gets teleported to.

### posY

The Y position where the character gets teleported to.

### posZ

The Z position where the character gets teleported to.
