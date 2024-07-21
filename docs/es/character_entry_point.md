# character\_entry\_point

[<-Volver a:Characters](database-characters)

**Tabla \`character\_entry\_point\`**

**Estructura**

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

**Descripción de los Campos**

### guid

GUID o Identificador Global Único.

### joinX

Posición cartesiana en X.

### joinY

Posición cartesiana en Y.

### joinZ

Posición cartesiana en Z.

### joinO

Orientación del personaje (Según las medidas de pi: 3.1415...).

### joinMapId

ID del mapa en cuestión. Véase [Map.dbc](map) columna número 1.

### taxiPath

Identificador (ID) del TaxiPath, véase TaxiPath.dbc columna número 1.

### mountSpell

ID del aura de la montura.
