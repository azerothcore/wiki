# recovery\_item

[<-Volver a:Characters](database-characters.md)

Leer en: [English :gb:](../recovery_item) [Spanish :es:](recovery_item)

**Tabla \`recovery\_item\`**

Esta tabla contiene información sobre la clasificación de emparejamiento de personajes en todos los tipos de equipos.

**Estructura**

| Field          | Type      | Attributes | Key | Null | Default | Extra          | Comment |
| -------------- | --------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [Id][1]        | INT       | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [Guid][2]      | INT       | UNSIGNED   |     | NO   | 0       |                |         |
| [ItemEntry][3] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |                |         |
| [Count][4]     | INT       | UNSIGNED   |     | NO   | 0       |                |         |

[1]: #id
[2]: #guid
[3]: #itementry
[4]: #count

**Descripción de los campos**

### Id

`campo-sin-descripción|1`

### Guid

`campo-sin-descripción|2`

### ItemEntry

Ver [item_template.entry](item_template#entry).

### Count

La cantidad de artículos.
