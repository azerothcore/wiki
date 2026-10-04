# module\_string\_locale

[<-Back-to:World](database-world)

**The module_string_locale table**

This table holds information of string entries for modules.

**Table: module\_string\_locale's Structure**

| Field             | Type         |                                         | Null | Key | Default | Extra | Comment                                           |
| :---------------- | :----------- | :-------------------------------------- | :--: | :-: | :-----: | :---: | :------------------------------------------------ |
| [module](#module) | VARCHAR(255) |                                         | NO   | PRI |         |       | Corresponds to an existing entry in module_string |
| [id](#id)         | INT          | UNSIGNED                                | NO   | PRI |         |       | Corresponds to an existing entry in module_string |
| [locale](#locale) | ENUM         | koKR,frFR,deDE,zhCN,zhTW,esES,esMX,ruRU | NO   | PRI |         |       |                                                   |
| [string](#string) | TEXT         |                                         | NO   |     |         |       |                                                   |

**Description of the table's fields**

### module

Module identifier in [module_string.module](module_string#module).

### id

String id in [module_string.id](module_string#id).

### locale

Which locale to translate to.

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

The translated text of [module_string.string](module_string#string).
