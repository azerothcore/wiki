# gameobject\_template\_locale

[<-Back-to:World](database-world)

**The \`gameobject\_template\_locale\` table**

This table is used to provide localized clients with localized strings for gameobjects.

**Table: gameobject\_template\_locale's Structure**

| Field                             | Type       |          | Null | Key | Default | Extra | Comment |
| :-------------------------------- | :--------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [entry](#entry)                   | INT        | UNSIGNED | NO   | PRI | 0       |       |         |
| [locale](#locale)                 | VARCHAR(4) |          | NO   | PRI |         |       |         |
| [name](#name)                     | TEXT       |          | YES  |     | NULL    |       |         |
| [castBarCaption](#castbarcaption) | TEXT       |          | YES  |     | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild)   | INT        |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

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
