# page\_text\_locale

[<-Volver a:World](database-world)

**Tabla \`page\_text\_locale\`**

Esta tabla se usa para proporcionar a los clientes localizados la cadena localizada de los page\_texts.

**Estructura**

| Field                          | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------ | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                      | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [locale](#locale)              | longtext  | SIGNED     |     | YES  | NULL    |       |         |
| [Name](#name) | longtext  | SIGNED     |     | YES  | NULL    |       |         |

**Descripción de los campos**

### ID

Este entry debe ser el mismo que [page\_text.entry](#page_text#entry) y entonces la fila se usará para proporcionar soporte de localización para este registro de page\_text.

### locale

`campo-sin-descripción|2`

### Name

Contenido traducido del campo [page\_text.text](#page_text#text) para el idioma X.
