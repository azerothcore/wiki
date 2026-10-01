# graveyard\_zone

[<-Volver a:World](database-world)

**Tabla \`graveyard\_zone\`**

Contiene información sobre las zonas conectadas a los cementerios del mundo.

Esta tabla se usa para establecer qué facciones aceptará un cementerio dado, y también para especificar el cementerio más cercano a una zona dada.

Para una lista de todas las zonas de cementerio existentes y sus respectivos IDs, consulta WorldSafeLocs.dbc

**Estructura**

| Field                   | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)               | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [GhostZone](#ghostzone) | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Faction](#faction)     | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [Comment](#comment)     | TEXT      |            |     |      |         |       |         |

**Descripción de los campos**

### ID

ID del cementerio. Ver WorldSafeLocs.dbc

### GhostZone

ID de la zona de la posición del fantasma antes de la teletransportación al cementerio. Ver AreaTable.dbc

### Faction

Bando del cementerio.

0 - Cualquier bando aceptado

469 - Solo bando Alianza

67 - Solo bando Horda

### Comment

Un comentario legible que describe esta entrada de zona de cementerio.
