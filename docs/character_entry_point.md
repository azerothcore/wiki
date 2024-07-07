# character\_entry\_point

[<-Back-to:Characters](database-characters)

**The \`character\_entry\_point\` table**

**Table Structure**

| Field           | Type  | Attributes | Key | Null | Default | Extra | Comment                  |
| --------------- | ----- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]       | INT   | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [joinX][2]      | FLOAT | SIGNED     |     | NO   | 0       |       |                          |
| [joinY][3]      | FLOAT | SIGNED     |     | NO   | 0       |       |                          |
| [joinZ][4]      | FLOAT | SIGNED     |     | NO   | 0       |       |                          |
| [joinO][5]      | FLOAT | SIGNED     |     | NO   | 0       |       |                          |
| [joinMapId][6]  | INT   | UNSIGNED   |     | YES  | 0       |       | Map Identifier           |
| [taxiPath][7]   | TEXT  | SIGNED     |     | NO   | 0       |       |                          |
| [mountSpell][8] | INT   | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #joinx
[3]: #joiny
[4]: #joinz
[5]: #joino
[6]: #joinmapid
[7]: #taxipath
[8]: #mountspell

**Description of the fields**

### guid

Global Unique Identifier.

### joinX

`field-no-description|2`

### joinY

`field-no-description|3`

### joinZ

`field-no-description|4`

### joinO

`field-no-description|5`

### joinMapId

Map Identifier.

### taxiPath

`field-no-description|7`

### mountSpell

`field-no-description|8`
