# player_factionchange_titles

[<-Volver a:World](database-world)

**Tabla \`spell_cooldown_overrides\`**

Determina qué título debería intercambiarse durante un cambio de facción.

**Estructura**

| Field                                | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------------ | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id](#allianceid)           | INT  |            | PRI | NO   |         |       |         |
| [alliance_comment](#alliancecomment) | TEXT |            | PRI | YES  | NULL    |       |         |
| [horde_id](#hordeid)                 | INT  |            | PRI | NO   |         |       |         |
| [horde_comment](#hordecomment)       | TEXT |            | PRI | YES  | NULL    |       |         |

**Descripción de los campos**

### alliance_id

ID de Titles.dbc

### alliance_comment

Nombre del título

### horde_id

ID de Titles.dbc

### horde_comment

Nombre del título
