# page_text_locale

[<-Back-to:World](database-world)

**The \`page_text_locale\` table**

This table is used to provide localized clients with localized strings for page_texts.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id) | INT | UNSIGNED | PRI | NO | 0 |  |  |
| [locale](#locale) | VARCHAR(4) |  | PRI | NO |  |  |  |
| [Text](#text) | TEXT |  |  | YES |  |  |  |
| [VerifiedBuild](#verifiedbuild) | INT |  |  | YES | NULL |  |  |

**Description of the fields**

### ID

This must match [page_text.ID](page_text#id).

### locale

The locale (language code) for this row. There is one row per non-default locale, so a single record can have up to 8 translated variants here. Valid values: `koKR`, `frFR`, `deDE`, `zhCN`, `zhTW`, `esES`, `esMX`, `ruRU`. The default `enUS` text is stored in the base table, not here.

### Text

Translated [page_text.Text](page_text#text) for this locale.

### VerifiedBuild

Client build this row was verified against (from WDB/ADB extraction). `NULL` if not applicable.
