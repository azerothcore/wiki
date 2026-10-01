# gossip_menu_option_locale

[<-返回至:World](database-world)

**\`gossip_menu_option_locale\` 表**

此表用于为本地化客户端提供对话菜单选项的本地化字符串。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [MenuID](#menuid) | INT | UNSIGNED | PRI | NO | 0 |  |  |
| [OptionID](#optionid) | SMALLINT | UNSIGNED | PRI | NO | 0 |  |  |
| [Locale](#locale) | VARCHAR(4) |  | PRI | NO |  |  |  |
| [OptionText](#optiontext) | TEXT |  |  | YES |  |  |  |
| [BoxText](#boxtext) | TEXT |  |  | YES |  |  |  |

**字段说明**

### MenuID

此值必须与 [gossip_menu_option.MenuID](gossip_menu_option#menuid) 相匹配。

### OptionID

此值必须与 [gossip_menu_option.OptionID](gossip_menu_option#optionid) 相匹配。它与 MenuID 一起用于标识要本地化的选项。

### Locale

此行所对应的语言区域（语言代码）。每个非默认语言区域对应一行，因此一条记录在这里最多可以有 8 个翻译变体。有效值：`koKR`、`frFR`、`deDE`、`zhCN`、`zhTW`、`esES`、`esMX`、`ruRU`。默认的 `enUS` 文本存储在基础表中，而不是这里。

### OptionText

针对此语言区域翻译后的 [gossip_menu_option.OptionText](gossip_menu_option#optiontext)。

### BoxText

针对此语言区域翻译后的 [gossip_menu_option.BoxText](gossip_menu_option#boxtext)。
