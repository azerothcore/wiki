# player\_factionchange\_items

[<-Volver a:World](database-world)

**Tabla \`player\_factionchange\_items\`**

Básicamente todos los cambios de items que se hacen cuando un jugador cambia de facción.

**Estructura**

| Field            | Type | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [race_A][1]      | INT  | SIGNED     |     | NO   |         |       |         |
| [alliance_id][2] | INT  | SIGNED     | PRI | NO   |         |       |         |
| [commentA][3]    | tex  | SIGNED     |     |      |         |       |         |
| [race_H][4]      | INT  | SIGNED     |     | NO   |         |       |         |
| [horde_id][5]    | INT  | SIGNED     | PRI | NO   |         |       |         |
| [commentH][6]    | INT  | SIGNED     |     |      |         |       |         |

[1]: #race_a
[2]: #alliance_id
[3]: #commenta
[4]: #race_h
[5]: #horde_id
[6]: #commenth

**Descripción de los campos**

### race\_A

No implementado.

Ver item\_template.AllowableRace

### alliance\_id

Este es el ID del item de la Alianza. Si te conviertes a la Horda y tus items tienen un registro en esta tabla, se convertirán a [\#horde\_id](#hordeid)

### commentA

Esto sirve para identificar fácilmente el nombre del item. El estilo del comentario debería ser nombre(ItemLevel)

### race\_H

No implementado.

Ver [item\_template.AllowableRace](item_template#allowablerace)

### horde\_id

Este es el ID del item de la Horda. Si te conviertes a la Alianza y tus items tienen un registro en esta tabla, se convertirán a [\#alliance\_id](#allianceid)

### commentH

Esto sirve para identificar fácilmente el nombre del item. El estilo del comentario debería ser nombre (ItemLevel)
