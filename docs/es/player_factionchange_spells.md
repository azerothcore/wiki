# player\_factionchange\_spells

[<-Volver a:World](database-world)

**Tabla \`player\_factionchange\_spells\`**

Básicamente todos los cambios de spells que se hacen cuando un jugador cambia de facción.

**Estructura**

| Field            | Type | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [alliance_id][1] | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [horde_id][2]    | INT  | SIGNED     | PRI | NO   |         |       |         |

[1]: #alliance_id
[2]: #horde_id

**Descripción de los campos**

### alliance\_id

Este es el ID del spell de la Alianza. Si te conviertes a la Horda y tus spells tienen un registro en esta tabla, se convertirán a [\#horde\_id](#hordeid)

### horde\_id

Este es el ID del spell de la Horda. Si te conviertes a la Alianza y tus spells tienen un registro en esta tabla, se convertirán a [\#alliance\_id](#allianceid)
