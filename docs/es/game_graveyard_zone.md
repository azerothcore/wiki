# game_graveyard_zone

[<-Volver a:World](database-world)

**Tabla \`game_graveyard_zone\`**

| Field           | Type      | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]         | MEDIUMINT | unasigned  | PRI | NO   | 0       |       |         |
| [ghost_zone][2] | MEDIUMINT | unasigned  | PRI | NO   | 0       |       |         |
| [faction][3]    | SMALLINT  | unasigned  |     | NO   | 0       |       |         |

[1]: #id
[2]: #ghostzone
[3]: #faction

**Descripción de los campos**

### id
ID del cementerio. Ver [WorldSafeLocs.dbc](worldsafelocs)

### ghost_zone
ID de la zona de la posición del fantasma antes de la teletransportación al cementerio. Ver [AreaTable.dbc](areatable)

### faction
Bando del cementerio.

0 - Cualquier bando aceptado

469 - Solo bando Alianza

67 - Solo bando Horda
