# creature_questitem

[<-Volver a: World](database-world)

**Tabla \`creature_questitem\`**

Contiene las relaciones de NPCs que finalizan misiones: qué NPCs finalizan qué misiones.

**Estructura**

| Field                           | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [CreatureEntry](#creatureEntry) | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Idx](#idx)                     | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [ItemId](#itemid)               | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild](#verifiedbuild) | INT  |            |     | YES  | NULL    |       |         |

**Descripción de los campos**

### CreatureEntry

[creature_template.entry](creature_template#entry).

### Idx

Índice 0-3

### ItemId

[item_template.entry](item_template#entry).

### VerifiedBuild

Este campo se usa para determinar si los datos provienen de sniffs verificados.

Si el valor es 0, entonces aún no ha sido analizado o se ha heredado de una BD más antigua o de otro Core.

Si el valor es mayor que 0, entonces ha sido analizado con sniffs de esa build específica del cliente.

Si el valor es -Client Build, entonces se analizó con archivos WDB de esa build específica del cliente y se editó manualmente más tarde por alguna necesidad especial.
