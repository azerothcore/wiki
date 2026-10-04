# page\_text\_locale

[<-Back-to:World](database-world)

**The \`page\_text\_locale\` table**

This table is used to provide localized clients with localized strings for page_texts.

**Table: page\_text\_locale's Structure**

| Field                           | Type       |          | Null | Key | Default | Extra | Comment |
| :------------------------------ | :--------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                       | INT        | UNSIGNED | NO   | PRI | 0       |       |         |
| [locale](#locale)               | VARCHAR(4) |          | NO   | PRI |         |       |         |
| [Text](#text)                   | TEXT       |          | YES  |     | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### ID

This must match [page_text.ID](page_text#id).

### locale

The locale (language code) for this row. There is one row per non-default locale, so a single record can have up to 8 translated variants here. Valid values: `koKR`, `frFR`, `deDE`, `zhCN`, `zhTW`, `esES`, `esMX`, `ruRU`. The default `enUS` text is stored in the base table, not here.

### Text

Translated [page_text.Text](page_text#text) for this locale.

### VerifiedBuild

Client build this row was verified against (from WDB/ADB extraction). `NULL` if not applicable.
