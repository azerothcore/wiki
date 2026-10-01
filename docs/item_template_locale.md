# item_template_locale

[<-Back-to:World](database-world)

**The \`item_template_locale\` table**

This table is used to provide localized clients with localized strings for items.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id) | INT | UNSIGNED | PRI | NO | 0 |  |  |
| [locale](#locale) | VARCHAR(4) |  | PRI | NO |  |  |  |
| [Name](#name) | TEXT |  |  | YES |  |  |  |
| [Description](#description) | TEXT |  |  | YES |  |  |  |
| [VerifiedBuild](#verifiedbuild) | INT |  |  | YES | NULL |  |  |

**Description of the fields**

### ID

This must match [item_template.entry](item_template#entry).

### locale

The locale (language code) for this row. There is one row per non-default locale, so a single record can have up to 8 translated variants here. Valid values: `koKR`, `frFR`, `deDE`, `zhCN`, `zhTW`, `esES`, `esMX`, `ruRU`. The default `enUS` text is stored in the base table, not here.

### Name

Translated [item_template.name](item_template#name) for this locale.

### Description

Translated [item_template.description](item_template#description) for this locale.

### VerifiedBuild

Client build this row was verified against (from WDB/ADB extraction). `NULL` if not applicable.
