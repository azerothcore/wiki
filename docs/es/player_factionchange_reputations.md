# player_factionchange_reputations

[<-Volver a:World](database-world)

**Tabla \`player_factionchange_reputations\`**

Básicamente todos los cambios de facción/reputación que se hacen cuando un jugador cambia de facción.

**Estructura**

| Field                                | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------------ | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id](#allianceid)           | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [alliance_comment](#alliancecomment) | TEXT |            |     | YES  | NULL    |       |         |
| [horde_id](#hordeid)                 | INT  | SIGNED     | PRI | NO   |         |       |         |
| [horde_comment](#hordecomment)       | TEXT |            |     | YES  | NULL    |       |         |

**Descripción de los campos**

### alliance_id

Este es el ID de reputación de la Alianza. Si te conviertes a la Horda y tus reputaciones tienen un registro en esta tabla, se convertirán a [\#horde_id](#hordeid)

Ver [character_reputation.faction](character_reputation#faction)

### alliance_comment

comentario

### horde_id

Este es el ID de reputación de la Horda. Si te conviertes a la Alianza y tus reputaciones tienen un registro en esta tabla, se convertirán a [\#alliance_id](#allianceid)

Ver [character_reputation.faction](character_reputation#faction)

### horde_comment

comentario
