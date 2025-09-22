# creature_questitem

[<-Volver a:World](database-world)

**Tabla \`creature_questitem\`**

Contiene las relaciones de finalización de misiones de los NPC sobre qué NPC finalizan qué misiones.
| Campo                           | Tipo | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ------------------------------- | ---- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [CreatureEntry](#creatureEntry) | INT  | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [Idx](#idx)                     | INT  | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [ItemId](#itemid)               | INT  | UNSIGNED  |       | NO   | 0           |       |            |
| [VerifiedBuild](#verifiedbuild) | INT  |           |       | Si   | NULL        |       |            |

**Descripción de los campos**

### CreatureEntry

[creature_template.entry](creature_template#entry).

### Idx

Índice 0-3

### ItemId

[item_template.entry](item_template#entry).

### VerifiedBuild

Este campo se utiliza para determinar si los datos provienen de rastreos verificados.

Si el valor es 0, entonces no se ha analizado todavía o se ha heredado de una base de datos más antigua u otro núcleo.

Si el valor es superior a 0, se ha analizado con rastreos de esa compilación de cliente específica.

Si el valor es -Client Build, entonces se analizó con archivos WDB de esa compilación de cliente específica y luego se editó manualmente para satisfacer alguna necesidad especial.
