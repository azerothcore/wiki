# points\_of\_interest

[<-Volver a:World](database-world)

**Tabla \`points\_of\_interest\`**

`tabla-sin-descripción`

**Estructura**

| Field           | Type      | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]      | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [x][2]          | FLOAT     | SIGNED     |     | NO   | 0       |       |         |
| [y][3]          | FLOAT     | SIGNED     |     | NO   | 0       |       |         |
| [icon][4]       | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [flags][5]      | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [Importance][6] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [icon_name][7]  | text      |            |     | NO   | NULL    |       |         |

[1]: #entry
[2]: #x
[3]: #y
[4]: #icon
[5]: #flags
[6]: #importance
[7]: #icon_name

**Descripción de los campos**

### entry

`campo-sin-descripción|1`

### x

`campo-sin-descripción|2`

### y

`campo-sin-descripción|3`

### icon

| Icon                      | Value | Description                    |
| ------------------------- | ----- | ------------------------------ |
| ICON\_POI\_BLANK          | 0     | En blanco (no visible)         |
| ICON\_POI\_GREY\_AV\_MINE | 1     | Vagoneta de mina gris          |
| ICON\_POI\_RED\_AV\_MINE  | 2     | Vagoneta de mina roja          |
| ICON\_POI\_BLUE\_AV\_MINE | 3     | Vagoneta de mina azul          |
| ICON\_POI\_BWTOMB         | 4     | Lápida azul y blanca           |
| ICON\_POI\_SMALL\_HOUSE   | 5     | Casa pequeña                   |
| ICON\_POI\_GREYTOWER      | 6     | Torre gris                     |
| ICON\_POI\_REDFLAG        | 7     | Bandera roja con ! amarillo    |
| ICON\_POI\_TOMBSTONE      | 8     | Lápida normal (marrón)         |
| ICON\_POI\_BWTOWER        | 9     | Torre azul y blanca            |
| ICON\_POI\_REDTOWER       | 10    | Torre roja                     |
| ICON\_POI\_BLUETOWER      | 11    | Torre azul                     |
| ICON\_POI\_RWTOWER        | 12    | Torre roja y blanca            |
| ICON\_POI\_REDTOMB        | 13    | Lápida roja                    |
| ICON\_POI\_RWTOMB         | 14    | Lápida roja y blanca           |
| ICON\_POI\_BLUETOMB       | 15    | Lápida azul                    |
| ICON\_POI\_16             | 16    | ¿Gris?                         |
| ICON\_POI\_17             | 17    | ¿Azul/blanco?                  |
| ICON\_POI\_18             | 18    | ¿Azul?                         |
| ICON\_POI\_19             | 19    | ¿Rojo y blanco?                |
| ICON\_POI\_20             | 20    | ¿Rojo?                         |
| ICON\_POI\_GREYLOGS       | 21    | Troncos de madera grises       |
| ICON\_POI\_BWLOGS         | 22    | Troncos de madera azules y blancos |
| ICON\_POI\_BLUELOGS       | 23    | Troncos de madera azules       |
| ICON\_POI\_RWLOGS         | 24    | Troncos de madera rojos y blancos |
| ICON\_POI\_REDLOGS        | 25    | Troncos de madera rojos        |
| ICON\_POI\_26             | 26    | ¿Gris?                         |
| ICON\_POI\_27             | 27    | ¿Azul y blanco?                |
| ICON\_POI\_28             | 28    | ¿Azul?                         |
| ICON\_POI\_29             | 29    | ¿Rojo y blanco?                |
| ICON\_POI\_30             | 30    | ¿Rojo?                         |
| ICON\_POI\_GREYHOUSE      | 31    | Casa gris                      |
| ICON\_POI\_BWHOUSE        | 32    | Casa azul y blanca             |
| ICON\_POI\_BLUEHOUSE      | 33    | Casa azul                      |
| ICON\_POI\_RWHOUSE        | 34    | Casa roja y blanca             |
| ICON\_POI\_REDHOUSE       | 35    | Casa roja                      |
| ICON\_POI\_GREYHORSE      | 36    | Caballo gris                   |
| ICON\_POI\_BWHORSE        | 37    | Caballo azul y blanco          |
| ICON\_POI\_BLUEHORSE      | 38    | Caballo azul                   |
| ICON\_POI\_RWHORSE        | 39    | Caballo rojo y blanco          |
| ICON\_POI\_REDHORSE       | 40    | Caballo rojo                   |

### flags

`campo-sin-descripción|5`

### Importance

`campo-sin-descripción|6`

### icon

`campo-sin-descripción|7`
