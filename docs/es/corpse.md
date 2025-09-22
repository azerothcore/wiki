# corpse

[<-Volver a:Characters](database-characters)

**Tabla \`corpse\`**

**Estructura**

| Campo            | Tipo     | Atributos | Llave | Nulo | Por defecto | Extra  | Comentario                             |
| ---------------- | -------- | --------- | ----- | ---- | ----------- | ------ | -------------------------------------- |
| [guid][1]        | INT      | UNSIGNED  | PRI   | NO   | 0           |        | Identificador único global de carácter |
| [posX][2]        | FLOAT    | SIGNED    |       | NO   | 0           |        |                                        |
| [posY][3]        | FLOAT    | SIGNED    |       | NO   | 0           |        |                                        |
| [posZ][4]        | FLOAT    | SIGNED    |       | NO   | 0           |        |                                        |
| [orientation][5] | FLOAT    | SIGNED    |       | NO   | 0           |        |                                        |
| [mapId][6]       | SMALLINT | UNSIGNED  |       | NO   | 0           |        | Identificador de mapa                  |
| [phaseMask][7]   | INT      | UNSIGNED  |       | NO   | 1           |        |                                        |
| [displayId][8]   | INT      | UNSIGNED  |       | NO   | 0           |        |                                        |
| [itemCache][9]   | TEXT     | SIGNED    |       | NO   |             |        |                                        |
| [bytes1][10]     | INT      | UNSIGNED  |       | NO   | 0           |        |                                        |
| [bytes2][11]     | INT      | UNSIGNED  |       | NO   | 0           |        |                                        |
| [guildId][12]    | INT      | UNSIGNED  |       | NO   | 0           |        |                                        |
| [flags][13]      | TINYINT  | UNSIGNED  |       | NO   | 0           |        |                                        |
| [dynFlags][14]   | TINYINT  | UNSIGNED  |       | NO   | 0           |        |                                        |
| [time][15]       | INT      | UNSIGNED  |       | NO   | 0           |        |                                        |
| [corpseType][16] | TINYINT  | UNSIGNED  |       | NO   | 0           |        |                                        |
| [instanceId][17] | INT      | UNSIGNED  |       | NO   | 0           |        | Identificador de instancia             |

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

**Descripción de los campos**

### guid

El guid del personaje. See [characters.guid](characters#guid).

### posX

`campo-sin-descripción|2`

### posY

`campo-sin-descripción|3`

### posZ

`campo-sin-descripción|4`

### orientation

`campo-sin-descripción|5`

### mapId

`campo-sin-descripción|6`

### phaseMask

`campo-sin-descripción|7`

### displayId

`campo-sin-descripción|8`

### itemCache

`campo-sin-descripción|9`

### bytes1

`campo-sin-descripción|10`

### bytes2

`campo-sin-descripción|11`

### guildId

`campo-sin-descripción|12`

### flags

`campo-sin-descripción|13`

### dynFlags

`campo-sin-descripción|14`

### time

`campo-sin-descripción|15`

### corpseType

`campo-sin-descripción|16`

### instanceId

`campo-sin-descripción|17`
