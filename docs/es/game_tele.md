# game\_tele

[<-Volver a:World](database-world)

**Estructura**

Esta tabla contiene una lista de ubicaciones de teletransporte que se pueden usar con el comando *.tele* dentro del juego. Las entradas de esta tabla se pueden añadir/eliminar manualmente o con los comandos *.tele add* y *.tele delete*.

| Field            | Type         | Attributes | Key | Null | Default | Extra          |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | -------------- |
| [id][1]          | MEDIUMINT    | UNSIGNED   | PRI | NO   | NULL    | Auto increment |
| [position_x][2]  | FLOAT        | SIGNED     |     | NO   | 0       |                |
| [position_y][3]  | FLOAT        | SIGNED     |     | NO   | 0       |                |
| [position_z][4]  | FLOAT        | SIGNED     |     | NO   | 0       |                |
| [orientation][5] | FLOAT        | SIGNED     |     | NO   | 0       |                |
| [map][6]         | SMALLINT     | UNSIGNED   |     | NO   | 0       |                |
| [name][7]        | VARCHAR(100) | SIGNED     |     | NO   | NULL    |                |

[1]: #id
[2]: #position_x
[3]: #position_y
[4]: #position_z
[5]: #orientation
[6]: #map
[7]: #name

**Descripción de los campos**

### id

El ID de la ubicación de teletransporte. Este número es único para cada ubicación añadida.

### position\_x

La coordenada del eje x de la ubicación de teletransporte. Se puede obtener usando el comando *.gps*.

### position\_y

La coordenada del eje y de la ubicación de teletransporte. Se puede obtener usando el comando *.gps*.

### position\_z

La coordenada del eje z de la ubicación de teletransporte. Se puede obtener usando el comando *.gps*.

### orientation

La dirección hacia la que mirará el jugador tras llegar a la ubicación de teletransporte. Se puede obtener usando el comando *.gps*.

(Norte = 0, Sur = 3.14159)

### map

El ID del mapa de la ubicación. Consulta el [archivo Map DBC](map) para los IDs de todas las zonas.

### name

Un nombre descriptivo para la ubicación de teletransporte. El nombre *no puede* tener espacios. Tampoco se recomienda usar caracteres especiales como puntos, comas, barras, etc...

### Examples

| id  | position_x | position_y | position_z | orientation | map | name         |
| --- | ---------- | ---------- | ---------- | ----------- | --- | ------------ |
| 10  | 2799.46    | 847.549    | 111.842    | 0.509892    | 0   | AgamandMills |
| 11  | -7040.08   | -3342.15   | 241.667    | 0.82338     | 0   | AgmondsEnd   |
| 12  | 451.572    | -3342.23   | 119.689    | 0.772541    | 0   | AgolWatha    |
| 13  | -2681.4    | -4787.21   | 16.0751    | 4.69276     | 1   | AlcazIsland  |
| 14  | -1746.58   | 5780.03    | 146.44     | 1.30629     | 530 | AldorRise    |
