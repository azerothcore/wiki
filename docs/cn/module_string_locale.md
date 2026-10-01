# module_string_locale

[<-返回:World](database-world)

**\`module_string_locale\` 表**

此表保存模块的字符串条目信息。

**表结构**

| Field             | Type         | Attributes                              | Key | Null | Default | Extra | Comment                  |
| ----------------- | ------------ | --------------------------------------- | --- | ---- | ------- | ----- | ------------------------ |
| [module](#module) | VARCHAR(255) |                                         | PRI | NO   |         |       | 模块目录名称，例如 mod-cfbg |
| [id](#id)         | INT          | UNSIGNED                                | PRI | NO   |         |       |                          |
| [locale](#locale) | ENUM         | koKR,frFR,deDE,zhCN,zhTW,esES,esMX,ruRU | PRI | NO   |         |       |                          |
| [string](#string) | TEXT         |                                         |     | NO   |         |       |                          |

**字段说明**

### module

[module_string.module](module_string#module) 中的模块标识符。

### id

[module_string.id](module_string#id) 中的字符串 ID。

### locale

要翻译成的语言（locale）。

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

[module_string.string](module_string#string) 的翻译文本。
