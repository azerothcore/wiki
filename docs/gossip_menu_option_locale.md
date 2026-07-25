# gossip_menu_option_locale

[<-Back-to:World](database-world)

**The \`gossip_menu_option_locale\` table**

This table is used to provide localized clients with localized strings for gossip menu options.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [MenuID](#menuid) | INT | UNSIGNED | PRI | NO | 0 |  |  |
| [OptionID](#optionid) | SMALLINT | UNSIGNED | PRI | NO | 0 |  |  |
| [Locale](#locale) | VARCHAR(4) |  | PRI | NO |  |  |  |
| [OptionText](#optiontext) | TEXT |  |  | YES |  |  |  |
| [BoxText](#boxtext) | TEXT |  |  | YES |  |  |  |

**Description of the fields**

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
