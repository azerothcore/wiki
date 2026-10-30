# ItemRandomSuffix.dbc

[`Back-to:DBC`](dbc-index)

**The \`ItemRandomSuffix.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [itemrandomsuffix_dbc](itemrandomsuffix_dbc) table of the world database.

**Structure**

| Column | Field           | Type   | itemrandomsuffix\_dbc column                          | Comment                                                    |
| :----: | :-------------- | :----- | :---------------------------------------------------- | :--------------------------------------------------------- |
| 0      | ID              | uint32 | [ID](itemrandomsuffix_dbc#id)                         |                                                            |
| 1      | Name_0          | string | [Name_Lang_enUS](itemrandomsuffix_dbc#namelang)       | Assumed enUS                                               |
| 2      | Name_1          | string | [Name_Lang_enGB](itemrandomsuffix_dbc#namelang)       | Assumed enGB, not used in 3.3.5a                           |
| 3      | Name_2          | string | [Name_Lang_koKR](itemrandomsuffix_dbc#namelang)       | Assumed koKR                                               |
| 4      | Name_3          | string | [Name_Lang_frFR](itemrandomsuffix_dbc#namelang)       | Assumed frFR                                               |
| 5      | Name_4          | string | [Name_Lang_deDE](itemrandomsuffix_dbc#namelang)       | Assumed deDE                                               |
| 6      | Name_5          | string | [Name_Lang_enCN](itemrandomsuffix_dbc#namelang)       | Assumed enCN, not used in 3.3.5a                           |
| 7      | Name_6          | string | [Name_Lang_zhCN](itemrandomsuffix_dbc#namelang)       | Assumed zhCN                                               |
| 8      | Name_7          | string | [Name_Lang_enTW](itemrandomsuffix_dbc#namelang)       | Assumed enTW, not used in 3.3.5a                           |
| 9      | Name_8          | string | [Name_Lang_zhTW](itemrandomsuffix_dbc#namelang)       | Assumed zhTW                                               |
| 10     | Name_9          | string | [Name_Lang_esES](itemrandomsuffix_dbc#namelang)       | Assumed esES                                               |
| 11     | Name_10         | string | [Name_Lang_esMX](itemrandomsuffix_dbc#namelang)       | Assumed esMX                                               |
| 12     | Name_11         | string | [Name_Lang_ruRU](itemrandomsuffix_dbc#namelang)       | Assumed ruRU                                               |
| 13     | Name_12         | string | [Name_Lang_ptPT](itemrandomsuffix_dbc#namelang)       | Assumed ptPT, not used in 3.3.5a                           |
| 14     | Name_13         | string | [Name_Lang_ptBR](itemrandomsuffix_dbc#namelang)       | Assumed ptBR, not used in 3.3.5a                           |
| 15     | Name_14         | string | [Name_Lang_itIT](itemrandomsuffix_dbc#namelang)       | Assumed itIT, not used in 3.3.5a                           |
| 16     | Name_15         | string | [Name_Lang_Unk](itemrandomsuffix_dbc#namelang)        | Unknown language, unsure of the usage in 3.3.5a            |
| 17     | Name_lang_mask  | uint32 | [Name_Lang_Mask](itemrandomsuffix_dbc#namelang)       | Assumed flags of the localized text                        |
| 18     | InternalName    | string | [InternalName](itemrandomsuffix_dbc#internalname)     |                                                            |
| 19     | Enchantment_0   | uint32 | [Enchantment_1](itemrandomsuffix_dbc#enchantment)     | ID in [SpellItemEnchantment.dbc](dbc-spellitemenchantment) |
| 20     | Enchantment_1   | uint32 | [Enchantment_2](itemrandomsuffix_dbc#enchantment)     | ID in [SpellItemEnchantment.dbc](dbc-spellitemenchantment) |
| 21     | Enchantment_2   | uint32 | [Enchantment_3](itemrandomsuffix_dbc#enchantment)     | ID in [SpellItemEnchantment.dbc](dbc-spellitemenchantment) |
| 22     | Enchantment_3   | uint32 | [Enchantment_4](itemrandomsuffix_dbc#enchantment)     | ID in [SpellItemEnchantment.dbc](dbc-spellitemenchantment) |
| 23     | Enchantment_4   | uint32 | [Enchantment_5](itemrandomsuffix_dbc#enchantment)     | ID in [SpellItemEnchantment.dbc](dbc-spellitemenchantment) |
| 24     | AllocationPct_0 | uint32 | [AllocationPct_1](itemrandomsuffix_dbc#allocationpct) |                                                            |
| 25     | AllocationPct_1 | uint32 | [AllocationPct_2](itemrandomsuffix_dbc#allocationpct) |                                                            |
| 26     | AllocationPct_2 | uint32 | [AllocationPct_3](itemrandomsuffix_dbc#allocationpct) |                                                            |
| 27     | AllocationPct_3 | uint32 | [AllocationPct_4](itemrandomsuffix_dbc#allocationpct) |                                                            |
| 28     | AllocationPct_4 | uint32 | [AllocationPct_5](itemrandomsuffix_dbc#allocationpct) |                                                            |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ItemRandomSuffix).
