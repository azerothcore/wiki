# item\_set\_names\_locale

[<-Back-to:World](database-world)

**The \`item\_set\_names\_locale\` table**

This table is used to provide localized clients with localized strings for item set names.

**Table: item\_set\_names\_locale's Structure**

| Field                           | Type       |          | Null | Key | Default | Extra | Comment |
| :------------------------------ | :--------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                       | INT        | UNSIGNED | NO   | PRI | 0       |       |         |
| [locale](#locale)               | VARCHAR(4) |          | NO   | PRI |         |       |         |
| [Name](#name)                   | TEXT       |          | YES  |     | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### ID

This must match [item_set_names.entry](item_set_names#entry).

### locale

The locale (language code) for this row. There is one row per non-default locale, so a single record can have up to 8 translated variants here. Valid values: `koKR`, `frFR`, `deDE`, `zhCN`, `zhTW`, `esES`, `esMX`, `ruRU`. The default `enUS` text is stored in the base table, not here.

### Name

Translated [item_set_names.name](item_set_names#name) for this locale.

### VerifiedBuild

Client build this row was verified against (from WDB/ADB extraction). `NULL` if not applicable.
