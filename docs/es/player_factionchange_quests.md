# player_factionchange_quest

[<-Volver a:World](database-world)

**Tabla \`player_factionchange_quest\`**

Determina qué quest debería cambiarse durante un cambio de facción.

**Estructura**

| Field                      | Type | Attributes | Key        | Null | Default | Extra | Comment |
| -------------------------- | ---- | ---------- | ---------- | ---- | ------- | ----- | ------- |
| [alliance_id](#allianceid) | INT  | UNSIGNED   | PRI UNIQUE | NO   |         |       |         |
| [horde_id](#hordeid)       | INT  | UNSIGNED   | PRI UNIQUE | NO   |         |       |         |

**Descripción de los campos**

### alliance_id

[quest_template.id](quest_template#id).

### horde_id

[quest_template.id](quest_template#id).
