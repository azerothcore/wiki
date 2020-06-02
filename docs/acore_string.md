# acore_string

[<-Back-to:World](database-world.md)

**The \`acore_string\` table**

This table holds all of the strings used internally by the server. This table is provided with the main purpose of translation in mind.

To see which locale IDs correspond to what languages, visit the Localization\_lang page.

NOTE: The % arguments need to stay in the exact same order as they are provided by default in the English translation.

**Structure**

| Field                  | Type      | Attributes | Key | Null | Default | Comment |
|:-----------------------|:----------|:-----------|:----|:-----|:--------|:--------|
| [entry][1]             | mediumint | unsigned   | PRI | NO   | 0       |         |
| [content\_default][2]  | text      | signed     |     | NO   |         |         |
| [locale\_koKR][3]      | text      | signed     |     | YES  |         |         |
| [locale\_frFR][3]      | text      | signed     |     | YES  |         |         |
| [locale\_deDE][3]      | text      | signed     |     | YES  |         |         |
| [locale\_zhCN][3]      | text      | signed     |     | YES  |         |         |
| [locale\_zhTW][3]      | text      | signed     |     | YES  |         |         |
| [locale\_esES][3]      | text      | signed     |     | YES  |         |         |
| [locale\_esMX][3]      | text      | signed     |     | YES  |         |         |
| [locale\_ruRU][3]      | text      | signed     |     | YES  |         |         |

[1]: #entry
[2]: #content\_default
[3]: #locale\_nnNN

**Description of the fields**

### entry

The ID that the core uses to identify a string. These IDs are contained and used internally and need to correspond to what the core expects. The core will not operate if all IDs aren't in this table.

### content\_default

The English translation (locale ID 0).

### locale\_nnNN

The translation in another language depending on the locale name.
