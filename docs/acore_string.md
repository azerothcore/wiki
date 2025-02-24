# acore_string

[<-Back-to:World](database-world)

**The \`acore_string\` table**

This table holds all of the strings used internally by the server. It is provided for the main purpose of translation.

To see which locale IDs correspond to what languages, visit the Localization\_lang page.

**Table Structure**

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

**Description of the fields**

### entry

The ID that the core uses to identify a string. These IDs are contained and used internally and must correspond to what the core expects. The core will not operate if all IDs aren't in this table.

### content\_default

The English translation (locale ID 0).

### locale\_nnNN

The translation in another language depends on the locale name.
