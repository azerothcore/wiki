# character\_entry\_point

[<-Back-to:Characters](database-characters)

**The \`character\_entry\_point\` table**

Stores where a character was before the core teleported it into a battleground or a Dungeon Finder dungeon: position, map, taxi path and mount. The core uses it to send the character back afterwards.

**Table: character\_entry\_point's Structure**

| Field                     | Type  |          | Null | Key | Default | Extra | Comment                  |
| :------------------------ | :---- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)             | INT   | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [joinX](#joinx)           | FLOAT |          | NO   |     | 0       |       |                          |
| [joinY](#joiny)           | FLOAT |          | NO   |     | 0       |       |                          |
| [joinZ](#joinz)           | FLOAT |          | NO   |     | 0       |       |                          |
| [joinO](#joino)           | FLOAT |          | NO   |     | 0       |       |                          |
| [joinMapId](#joinmapid)   | INT   | UNSIGNED | NO   |     | 0       |       | Map Identifier           |
| [taxiPath0](#taxipath0)   | INT   | UNSIGNED | NO   |     | 0       |       |                          |
| [taxiPath1](#taxipath1)   | INT   | UNSIGNED | NO   |     | 0       |       |                          |
| [mountSpell](#mountspell) | INT   | UNSIGNED | NO   |     | 0       |       |                          |

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
