# module_string_locale

[<-Volver a:World](database-world)

**Tabla module_string_locale**

Esta tabla contiene información de las entradas de cadenas (strings) para los módulos.

**Estructura**

| Field             | Type         | Attributes                              | Key | Null | Default | Extra | Comment                      |
| ----------------- | ------------ | --------------------------------------- | --- | ---- | ------- | ----- | ---------------------------- |
| [module](#module) | VARCHAR(255) |                                         | PRI | NO   |         |       | module dir name, eg mod-cfbg |
| [id](#id)         | INT          | UNSIGNED                                | PRI | NO   |         |       |                              |
| [locale](#locale) | ENUM         | koKR,frFR,deDE,zhCN,zhTW,esES,esMX,ruRU | PRI | NO   |         |       |                              |
| [string](#string) | TEXT         |                                         |     | NO   |         |       |                              |

**Descripción de los campos**

### module

Identificador del módulo en [module_string.module](module_string#module).

### id

Id de la cadena en [module_string.id](module_string#id).

### locale

A qué localización traducir.

| Locale |
| ------ |
| koKR   |
| frFR   |
| deDE   |
| zhCN   |
| zhTW   |
| esES   |
| esMX   |
| ruRU   |

### string

El texto traducido de [module_string.string](module_string#string).
