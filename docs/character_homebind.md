# character\_homebind

[<-Back-to:Characters](database-characters)

**The \`character\_homebind\` table**

Contains information on the location where characters get teleported when they use their Hearthstone.

**Table: character\_homebind's Structure**

| Field             | Type     |          | Null | Key | Default | Extra | Comment                  |
| :---------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)     | INT      | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [mapId](#mapid)   | SMALLINT | UNSIGNED | NO   |     | 0       |       | Map Identifier           |
| [zoneId](#zoneid) | SMALLINT | UNSIGNED | NO   |     | 0       |       | Zone Identifier          |
| [posX](#posx)     | FLOAT    |          | NO   |     | 0       |       |                          |
| [posY](#posy)     | FLOAT    |          | NO   |     | 0       |       |                          |
| [posZ](#posz)     | FLOAT    |          | NO   |     | 0       |       |                          |

**Description of the table's fields**

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
