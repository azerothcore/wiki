# gossip\_menu\_option\_locale

[<-Back-to:World](database-world)

**The \`gossip\_menu\_option\_locale\` table**

This table is used to provide localized clients with localized strings for gossip menu options.

**Table: gossip\_menu\_option\_locale's Structure**

| Field                     | Type       |          | Null | Key | Default | Extra | Comment |
| :------------------------ | :--------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [MenuID](#menuid)         | INT        | UNSIGNED | NO   | PRI | 0       |       |         |
| [OptionID](#optionid)     | SMALLINT   | UNSIGNED | NO   | PRI | 0       |       |         |
| [Locale](#locale)         | VARCHAR(4) |          | NO   | PRI |         |       |         |
| [OptionText](#optiontext) | TEXT       |          | YES  |     | NULL    |       |         |
| [BoxText](#boxtext)       | TEXT       |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### MenuID

This must match [gossip_menu_option.MenuID](gossip_menu_option#menuid).

### OptionID

This must match [gossip_menu_option.OptionID](gossip_menu_option#optionid). Together with MenuID it identifies the option to localize.

### Locale

The locale (language code) for this row. There is one row per non-default locale, so a single record can have up to 8 translated variants here. Valid values: `koKR`, `frFR`, `deDE`, `zhCN`, `zhTW`, `esES`, `esMX`, `ruRU`. The default `enUS` text is stored in the base table, not here.

### OptionText

Translated [gossip_menu_option.OptionText](gossip_menu_option#optiontext) for this locale.

### BoxText

Translated [gossip_menu_option.BoxText](gossip_menu_option#boxtext) for this locale.
