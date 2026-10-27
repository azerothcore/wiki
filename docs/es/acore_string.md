# acore_string

[<-Volver a:World](database-world)

**Tabla \`acore_string\`**

Esta tabla contiene todas las cadenas (strings) usadas internamente por el servidor. Se proporciona con el propósito principal de la traducción.

Las traducciones a otros idiomas están en [acore\_string\_locale](acore_string_locale).

**Estructura**

| Field                | Type | Attributes | Key | Null | Default | Extra | Comment |
| -------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]           | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [content_default][2] | text |            |     | NO   |         |       |         |

[1]: #entry
[2]: #contentdefault

**Descripción de los campos**

### entry

El ID que el core usa para identificar una cadena. Estos IDs se contienen y se usan internamente y deben corresponder con lo que el core espera. El core no funcionará si no están todos los IDs en esta tabla.

### content\_default

La traducción al inglés (locale ID 0).
