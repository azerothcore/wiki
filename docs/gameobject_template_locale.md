# gameobject_template_locale

[<-Back-to:World](database-world)

**The \`gameobject_template_locale\` table**

This table is used to provide localized clients with localized strings for gameobjects.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry](#entry) | INT | UNSIGNED | PRI | NO | 0 |  |  |
| [locale](#locale) | VARCHAR(4) |  | PRI | NO |  |  |  |
| [name](#name) | TEXT |  |  | YES |  |  |  |
| [castBarCaption](#castbarcaption) | TEXT |  |  | YES |  |  |  |
| [VerifiedBuild](#verifiedbuild) | INT |  |  | YES | NULL |  |  |

**Description of the fields**

### entry

This must match [gameobject_template.entry](gameobject_template#entry). The row provides localization for that gameobject_template record.

### locale

The locale (language code) for this row. There is one row per non-default locale, so a single record can have up to 8 translated variants here. Valid values: `koKR`, `frFR`, `deDE`, `zhCN`, `zhTW`, `esES`, `esMX`, `ruRU`. The default `enUS` text is stored in the base table, not here.

### name

Translated [gameobject_template.name](gameobject_template#name) for this locale.

### castBarCaption

Translated [gameobject_template.castBarCaption](gameobject_template#castbarcaption) for this locale.

### VerifiedBuild

Client build this row was verified against (from WDB/ADB extraction). `NULL` if not applicable.
