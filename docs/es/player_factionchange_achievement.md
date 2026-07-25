# player_factionchange_achievement

[<-Volver a:World](database-world)

**Tabla \`player_factionchange_achievement\`**

Básicamente todos los cambios de logros que se hacen cuando un jugador cambia de facción.

**Estructura**

| Field                                | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------------ | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id](#allianceid)           | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [alliance_comment](#alliancecomment) | TEXT |            |     | YES  | NULL    |       |         |
| [horde_id](#hordeid)                 | INT  | SIGNED     | PRI | NO   |         |       |         |
| [horde_comment](#hordecomment)       | TEXT |            |     | YES  | NULL    |       |         |

**Descripción de los campos**

### alliance_id

Este es el ID del logro de la Alianza. Si te conviertes a la Horda y tus logros tienen un registro en esta tabla, se convertirán a [\#horde_id](##hordeid)

### alliance_comment

comentario

### horde_id

Este es el ID del logro de la Horda. Si te conviertes a la Alianza y tus logros tienen un registro en esta tabla, se convertirán a [\#alliance_id](#allianceid)

### horde_comment

comentario
