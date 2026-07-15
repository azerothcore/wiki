# playercreateinfo

[<-Volver a:World](database-world)

**Tabla \`playercreateinfo\`**

Esta tabla contiene las posiciones de inicio de cada combinación clase-raza para todos los personajes recién creados.

**Estructura**

| Field            | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [race][1]        | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |         |
| [class][2]       | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |         |
| [map][3]         | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [zone][4]        | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [position_x][5]  | FLOAT     | SIGNED     |     | NO   | 0       |       |         |
| [position_y][6]  | FLOAT     | SIGNED     |     | NO   | 0       |       |         |
| [position_z][7]  | FLOAT     | SIGNED     |     | NO   | 0       |       |         |
| [orientation][8] | FLOAT     | SIGNED     |     | NO   | 0       |       |         |

[1]: #race
[2]: #class
[3]: #map
[4]: #zone
[5]: #position_x
[6]: #position_y
[7]: #position_z
[8]: #orientation

**Descripción de los campos**

### race

La raza del personaje. `ChrRaces.dbc`

### class

La clase del personaje. `ChrClasses.dbc`

### map

El ID del mapa. Ver [Map.dbc](map)

### zone

El ID de la zona. Ver [AreaTable.dbc](areatable)

### position\_x

La posición X.

### position\_y

La posición Y.

### position\_z

La posición Z.

### orientation

La orientación.
