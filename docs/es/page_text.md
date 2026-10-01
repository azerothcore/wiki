# page\_text

[<-Volver a:World](database-world)

**Tabla \`page\_text\`**

Esta tabla contiene el texto de los items tipo carta o de cualquier item que, al pasar el ratón por encima, convierte el cursor en una lupa y al hacer click derecho abre una ventana donde puedes leer el contenido de la carta.

**Estructura**

| Field              | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]            | INT       | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Text][2]          | LONGTEXT  | SIGNED     |     | NO   |         |       |         |
| [NextPageID][3]    | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild][4] | INT       | SIGNED     |     | YES  | NULL    |       |         |

[1]: #id
[2]: #text
[3]: #nextpageid
[4]: #verifiedbuild

**Descripción de los campos**

### ID

Identificador único

### Text

El texto en sí. El mensaje de este campo se mostrará como el texto de una página.

### NextPageID

El ID de la página siguiente. [page_text.id](#id).

### VerifiedBuild
