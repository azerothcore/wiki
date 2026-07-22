# creature_template_locale

[<-Back-to:World](database-world)

**The \`creature_template_locale\` table**

This table is used to provide localized clients with localized strings for creatures.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry](#entry) | INT | UNSIGNED | PRI | NO | 0 |  |  |
| [locale](#locale) | VARCHAR(4) |  | PRI | NO |  |  |  |
| [Name](#name) | TEXT |  |  | YES |  |  |  |
| [Title](#title) | TEXT |  |  | YES |  |  |  |
| [VerifiedBuild](#verifiedbuild) | INT |  |  | YES | NULL |  |  |

**Description of the fields**

### entry

This must match [creature_template.entry](creature_template#creature_template-entry). The row provides localization for that creature_template record.

### locale

The locale (language code) for this row. There is one row per non-default locale, so a single record can have up to 8 translated variants here. Valid values: `koKR`, `frFR`, `deDE`, `zhCN`, `zhTW`, `esES`, `esMX`, `ruRU`. The default `enUS` text is stored in the base table, not here.

### Name

Translated [creature_template.name](creature_template#name) for this locale.

### Title

Translated [creature_template.subname](creature_template#subname) (title) for this locale.

### VerifiedBuild

Client build this row was verified against (from WDB/ADB extraction). `NULL` if not applicable.
