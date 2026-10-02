# character\_entry\_point

[<-Back-to:Characters](database-characters)

**The \`character\_entry\_point\` table**

Stores where a character was before the core teleported it into a battleground or a Dungeon Finder dungeon: position, map, taxi path and mount. The core uses it to send the character back afterwards.

**Table: character\_entry\_point's Structure**

| Field           | Type  | Attributes | Key | Null | Default | Extra | Comment                  |
| --------------- | ----- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]       | INT   | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [joinX][2]      | FLOAT | SIGNED     |     | NO   | 0       |       |                          |
| [joinY][3]      | FLOAT | SIGNED     |     | NO   | 0       |       |                          |
| [joinZ][4]      | FLOAT | SIGNED     |     | NO   | 0       |       |                          |
| [joinO][5]      | FLOAT | SIGNED     |     | NO   | 0       |       |                          |
| [joinMapId][6]  | INT   | UNSIGNED   |     | NO   | 0       |       | Map Identifier           |
| [taxiPath0][7]  | INT   | UNSIGNED   |     | NO   | 0       |       |                          |
| [taxiPath1][9]  | INT   | UNSIGNED   |     | NO   | 0       |       |                          |
| [mountSpell][8] | INT   | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #joinx
[3]: #joiny
[4]: #joinz
[5]: #joino
[6]: #joinmapid
[7]: #taxipath0
[9]: #taxipath1
[8]: #mountspell

**Description of the table's fields**

### guid

Global Unique Identifier.

### joinX

X position the character is sent back to.

### joinY

Y position the character is sent back to.

### joinZ

Z position the character is sent back to.

### joinO

Orientation the character is sent back to.

### joinMapId

Map Identifier.

### taxiPath0

The source node of the taxi (flight) path the character was on when the entry point was saved.

### taxiPath1

The destination node of the taxi (flight) path the character was on when the entry point was saved.

### mountSpell

The mount spell the character was using, which is cast again when they return.
