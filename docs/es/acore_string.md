# acore_string

[<-Back-to:World](database-world)

**La \`acore_string\` tabla**

Esta tabla contiene todas las cadenas utilizadas internamente por el servidor. Se proporciona principalmente para la traducción.

Para ver qué ID de configuración regional corresponden a qué idiomas, visita la página Localization\_lang.

**Estructura de la tabla**

| Campo                | Tipo      | Atributos  | Llave | Llave | Por defecto | Extra | Comentario |
| -------------------- | --------- | ---------- | ----- | ----- | ----------- | ----- | ---------- |
| [entry][1]           | MEDIUMINT | UNSIGNED   | PRI   | NO    | 0           |       |            |
| [content_default][2] | text      |            |       | NO    |             |       |            |
| [locale_koKR][3]     | text      |            |       | YES   |             |       |            |
| [locale_frFR][3]     | text      |            |       | YES   |             |       |            |
| [locale_deDE][3]     | text      |            |       | YES   |             |       |            |
| [locale_zhCN][3]     | text      |            |       | YES   |             |       |            |
| [locale_zhTW][3]     | text      |            |       | YES   |             |       |            |
| [locale_esES][3]     | text      |            |       | YES   |             |       |            |
| [locale_esMX][3]     | text      |            |       | YES   |             |       |            |
| [locale_ruRU][3]     | text      |            |       | YES   |             |       |            |

[1]: #entry
[2]: #content\_default
[3]: #locale\_nnNN

**Descripción de los campos**

### entry

El ID que el núcleo utiliza para identificar una cadena. Estos ID se contienen y se utilizan internamente, y deben corresponder a lo que el núcleo espera. El núcleo no funcionará si no todos los ID están en esta tabla.

### content\_default

La traducción al inglés (ID de configuración regional 0).

### locale\_nnNN

La traducción a otro idioma depende del nombre regional.
