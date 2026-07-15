# acore_string

[<-Volver a:World](database-world)

**Tabla \`acore_string\`**

Esta tabla contiene todas las cadenas (strings) usadas internamente por el servidor. Se proporciona con el propósito principal de la traducción.

Para ver a qué idiomas corresponden los IDs de localización, visita la página Localization\_lang.

**Estructura**

| Field                | Type      | Attributes | Key | Null | Default | Extra | Comment |
| -------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]           | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [content_default][2] | text      |            |     | NO   |         |       |         |
| [locale_koKR][3]     | text      |            |     | YES  |         |       |         |
| [locale_frFR][3]     | text      |            |     | YES  |         |       |         |
| [locale_deDE][3]     | text      |            |     | YES  |         |       |         |
| [locale_zhCN][3]     | text      |            |     | YES  |         |       |         |
| [locale_zhTW][3]     | text      |            |     | YES  |         |       |         |
| [locale_esES][3]     | text      |            |     | YES  |         |       |         |
| [locale_esMX][3]     | text      |            |     | YES  |         |       |         |
| [locale_ruRU][3]     | text      |            |     | YES  |         |       |         |

[1]: #entry
[2]: #content\_default
[3]: #locale\_nnNN

**Descripción de los campos**

### entry

El ID que el core usa para identificar una cadena. Estos IDs se contienen y se usan internamente y deben corresponder con lo que el core espera. El core no funcionará si no están todos los IDs en esta tabla.

### content\_default

La traducción al inglés (locale ID 0).

### locale\_nnNN

La traducción a otro idioma depende del nombre de la localización.
