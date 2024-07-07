# lag\_reports

[<-Volver a:Characters](database-characters)

**Tabla `\lag\_reports\`**

La tabla alberga aquellos informes de lag realizados por jugadores dentro del juego (cuando hacen clic en "Solicitud de Ayuda").

**Estructura**

| Field           | Type     | Attributes | Key | Null | Default | Extra          | Comment |
| --------------- | -------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [reportId][1]   | INT      | UNSIGNED   | PRI | NO   |         | Auto Increment |         |
| [guid][2]       | INT      | UNSIGNED   |     | NO   | 0       |                |         |
| [lagType][3]    | TINYINT  | UNSIGNED   |     | NO   | 0       |                |         |
| [mapId][4]      | SMALLINT | UNSIGNED   |     | NO   | 0       |                |         |
| [posX][5]       | FLOAT    | SIGNED     |     | NO   | 0       |                |         |
| [posY][6]       | FLOAT    | SIGNED     |     | NO   | 0       |                |         |
| [posZ][7]       | FLOAT    | SIGNED     |     | NO   | 0       |                |         |
| [latency][8]    | INT      | UNSIGNED   |     | NO   | 0       |                |         |
| [createTime][9] | INT      | UNSIGNED   |     | NO   | 0       |                |         |

[1]: #reportid
[2]: #guid
[3]: #lagtype
[4]: #mapid
[5]: #posx
[6]: #posy
[7]: #posz
[8]: #latency
[9]: #createtime

**Descripción de los Campos**

### reportId

ID del reporte actual.

### guid

GUID o Identificador Global Único del jugador. Véase [characters.guid](characters#guid)

### lagType

* 0 = Relacionado con el Botín.
* 1 = Relacionado con la Casa de Subastas.
* 2 = Relacionado con el Correo.
* 3 = Relacionado con el Chat.
* 4 = Relacionado con el movimiento.
* 5 = Relacionado con hechizos y habilidades.

### mapId

ID del mapa dónde fue creado el reporte. Véase [Map.dbc](map).

### posX

Posición cartesiana en X donde se hizo el reporte.

### posY

Posición cartesiana en Y donde se hizo el reporte.

### posZ

Posición cartesiana en Z donde se hizo el reporte.

### latency

Latencia del jugador en el momento que se hizo el reporte.

### createTime

Fecha de creación en tiempo Unix. (TODO: Debería cambiarse al sistema de conteo de mysql).
