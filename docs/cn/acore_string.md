# acore_string

[<-返回:World](database-world)

**\`acore_string\` 表**

此表保存了服务器内部使用的所有字符串。它主要是为翻译目的而提供的。

要查看哪个 locale ID 对应哪种语言，请访问 Localization\_lang 页面。

**表结构**

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
[2]: #contentdefault
[3]: #localennnn

**字段描述**

### entry

核心用于标识字符串的 ID。这些 ID 在内部保存和使用，并且必须与核心所期望的对应。如果此表中不包含全部 ID，核心将无法运行。

### content\_default

英文翻译（locale ID 0）。

### locale\_nnNN

其他语言的翻译，取决于 locale 名称。
