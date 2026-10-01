# areatrigger\_tavern

[<-Volver a:World](database-world)

**Tabla \`areatrigger\_tavern\`**

Activa un trigger cuando el jugador entra en una ciudad o taberna. Esto hace que el jugador entre en un estado de descanso.

**Estructura**

| Field     | Type      | Attributes | Key | Null | Default | Extra | Comment    |
| --------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------- |
| [id][1]   | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Identifier |
| [name][2] | text      |            |     | YES  |         |       |            |

[1]: #id
[2]: #name

**Descripción de los campos**

### id

Este es el identificador del trigger, ver [AreaTrigger.dbc](DBC-AreaTrigger)

### name

Nombre de la ciudad o taberna. Esto es puramente con fines descriptivos.

### Example

| id  | name                                         |
| --- | -------------------------------------------- |
| 71  | Westfall - Sentinel Hill Inn                 |
| 98  | Nesingwary's Expedition                      |
| 178 | Strahnbrad                                   |
| 562 | Elwynn Forest - Goldshire - Lion's Pride Inn |
| 682 | Redridge Mountains - Lakeshire Inn           |
