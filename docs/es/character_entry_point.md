# character\_entry\_point

[<-Volver a:Characters](database-characters)

**Tabla \`character\_entry\_point\`**

**Estructura**

| Campo           | Tipo  | Atributos | Llave | Nulo | Por defecto | Extra | Comentario                 |
| --------------- | ----- | --------- | ----- | ---- | ----------- | ----- | -------------------------- |
| [guid][1]       | INT   | UNSIGNED  | PRI   | NO   | 0           |       | Identificador único global |
| [joinX][2]      | FLOAT | SIGNED    |       | NO   | 0           |       |                            |
| [joinY][3]      | FLOAT | SIGNED    |       | NO   | 0           |       |                            |
| [joinZ][4]      | FLOAT | SIGNED    |       | NO   | 0           |       |                            |
| [joinO][5]      | FLOAT | SIGNED    |       | NO   | 0           |       |                            |
| [joinMapId][6]  | INT   | UNSIGNED  |       | YES  | 0           |       | Identificador de mapa      |
| [taxiPath][7]   | TEXT  | SIGNED    |       | NO   | 0           |       |                            |
| [mountSpell][8] | INT   | UNSIGNED  |       | NO   | 0           |       |                            |

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

`field-no-description|2`

### joinY

`field-no-description|3`

### joinZ

`field-no-description|4`

### joinO

`field-no-description|5`

### joinMapId

Identificador de mapa.

### taxiPath

`field-no-description|7`

### mountSpell

`field-no-description|8`