# ItemSet.dbc

[`Back-to:DBC`](dbc-index)

**The \`ItemSet.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [itemset_dbc](itemset_dbc) table of the world database.

**Structure**

| Column | Field             | Type   | itemset\_dbc column                                | Comment                                         |
| :----: | :---------------- | :----- | :------------------------------------------------- | :---------------------------------------------- |
| 0      | ID                | uint32 | [ID](itemset_dbc#id)                               |                                                 |
| 1      | Name_0            | string | [Name_Lang_enUS](itemset_dbc#namelangenus)         | Assumed enUS                                    |
| 2      | Name_1            | string | [Name_Lang_enGB](itemset_dbc#namelangengb)         | Assumed enGB, not used in 3.3.5a                |
| 3      | Name_2            | string | [Name_Lang_koKR](itemset_dbc#namelangkokr)         | Assumed koKR                                    |
| 4      | Name_3            | string | [Name_Lang_frFR](itemset_dbc#namelangfrfr)         | Assumed frFR                                    |
| 5      | Name_4            | string | [Name_Lang_deDE](itemset_dbc#namelangdede)         | Assumed deDE                                    |
| 6      | Name_5            | string | [Name_Lang_enCN](itemset_dbc#namelangencn)         | Assumed enCN, not used in 3.3.5a                |
| 7      | Name_6            | string | [Name_Lang_zhCN](itemset_dbc#namelangzhcn)         | Assumed zhCN                                    |
| 8      | Name_7            | string | [Name_Lang_enTW](itemset_dbc#namelangentw)         | Assumed enTW, not used in 3.3.5a                |
| 9      | Name_8            | string | [Name_Lang_zhTW](itemset_dbc#namelangzhtw)         | Assumed zhTW                                    |
| 10     | Name_9            | string | [Name_Lang_esES](itemset_dbc#namelangeses)         | Assumed esES                                    |
| 11     | Name_10           | string | [Name_Lang_esMX](itemset_dbc#namelangesmx)         | Assumed esMX                                    |
| 12     | Name_11           | string | [Name_Lang_ruRU](itemset_dbc#namelangruru)         | Assumed ruRU                                    |
| 13     | Name_12           | string | [Name_Lang_ptPT](itemset_dbc#namelangptpt)         | Assumed ptPT, not used in 3.3.5a                |
| 14     | Name_13           | string | [Name_Lang_ptBR](itemset_dbc#namelangptbr)         | Assumed ptBR, not used in 3.3.5a                |
| 15     | Name_14           | string | [Name_Lang_itIT](itemset_dbc#namelangitit)         | Assumed itIT, not used in 3.3.5a                |
| 16     | Name_15           | string | [Name_Lang_Unk](itemset_dbc#namelangunk)           | Unknown language, unsure of the usage in 3.3.5a |
| 17     | Name_lang_mask    | uint32 | [Name_Lang_Mask](itemset_dbc#namelangmask)         | Assumed flags of the localized text             |
| 18     | ItemID_0          | uint32 | [ItemID_1](itemset_dbc#itemid1)                    | ID in [Item.dbc](dbc-item)                      |
| 19     | ItemID_1          | uint32 | [ItemID_2](itemset_dbc#itemid2)                    | ID in [Item.dbc](dbc-item)                      |
| 20     | ItemID_2          | uint32 | [ItemID_3](itemset_dbc#itemid3)                    | ID in [Item.dbc](dbc-item)                      |
| 21     | ItemID_3          | uint32 | [ItemID_4](itemset_dbc#itemid4)                    | ID in [Item.dbc](dbc-item)                      |
| 22     | ItemID_4          | uint32 | [ItemID_5](itemset_dbc#itemid5)                    | ID in [Item.dbc](dbc-item)                      |
| 23     | ItemID_5          | uint32 | [ItemID_6](itemset_dbc#itemid6)                    | ID in [Item.dbc](dbc-item)                      |
| 24     | ItemID_6          | uint32 | [ItemID_7](itemset_dbc#itemid7)                    | ID in [Item.dbc](dbc-item)                      |
| 25     | ItemID_7          | uint32 | [ItemID_8](itemset_dbc#itemid8)                    | ID in [Item.dbc](dbc-item)                      |
| 26     | ItemID_8          | uint32 | [ItemID_9](itemset_dbc#itemid9)                    | ID in [Item.dbc](dbc-item)                      |
| 27     | ItemID_9          | uint32 | [ItemID_10](itemset_dbc#itemid10)                  | ID in [Item.dbc](dbc-item)                      |
| 28     | ItemID_10         | uint32 | [ItemID_11](itemset_dbc#itemid11)                  |                                                 |
| 29     | ItemID_11         | uint32 | [ItemID_12](itemset_dbc#itemid12)                  |                                                 |
| 30     | ItemID_12         | uint32 | [ItemID_13](itemset_dbc#itemid13)                  |                                                 |
| 31     | ItemID_13         | uint32 | [ItemID_14](itemset_dbc#itemid14)                  |                                                 |
| 32     | ItemID_14         | uint32 | [ItemID_15](itemset_dbc#itemid15)                  |                                                 |
| 33     | ItemID_15         | uint32 | [ItemID_16](itemset_dbc#itemid16)                  |                                                 |
| 34     | ItemID_16         | uint32 | [ItemID_17](itemset_dbc#itemid17)                  |                                                 |
| 35     | SetSpellID_0      | uint32 | [SetSpellID_1](itemset_dbc#setspellid1)            | ID in [Spell.dbc](spell)                        |
| 36     | SetSpellID_1      | uint32 | [SetSpellID_2](itemset_dbc#setspellid2)            | ID in [Spell.dbc](spell)                        |
| 37     | SetSpellID_2      | uint32 | [SetSpellID_3](itemset_dbc#setspellid3)            | ID in [Spell.dbc](spell)                        |
| 38     | SetSpellID_3      | uint32 | [SetSpellID_4](itemset_dbc#setspellid4)            | ID in [Spell.dbc](spell)                        |
| 39     | SetSpellID_4      | uint32 | [SetSpellID_5](itemset_dbc#setspellid5)            | ID in [Spell.dbc](spell)                        |
| 40     | SetSpellID_5      | uint32 | [SetSpellID_6](itemset_dbc#setspellid6)            | ID in [Spell.dbc](spell)                        |
| 41     | SetSpellID_6      | uint32 | [SetSpellID_7](itemset_dbc#setspellid7)            | ID in [Spell.dbc](spell)                        |
| 42     | SetSpellID_7      | uint32 | [SetSpellID_8](itemset_dbc#setspellid8)            | ID in [Spell.dbc](spell)                        |
| 43     | SetThreshold_0    | uint32 | [SetThreshold_1](itemset_dbc#setthreshold1)        |                                                 |
| 44     | SetThreshold_1    | uint32 | [SetThreshold_2](itemset_dbc#setthreshold2)        |                                                 |
| 45     | SetThreshold_2    | uint32 | [SetThreshold_3](itemset_dbc#setthreshold3)        |                                                 |
| 46     | SetThreshold_3    | uint32 | [SetThreshold_4](itemset_dbc#setthreshold4)        |                                                 |
| 47     | SetThreshold_4    | uint32 | [SetThreshold_5](itemset_dbc#setthreshold5)        |                                                 |
| 48     | SetThreshold_5    | uint32 | [SetThreshold_6](itemset_dbc#setthreshold6)        |                                                 |
| 49     | SetThreshold_6    | uint32 | [SetThreshold_7](itemset_dbc#setthreshold7)        |                                                 |
| 50     | SetThreshold_7    | uint32 | [SetThreshold_8](itemset_dbc#setthreshold8)        |                                                 |
| 51     | RequiredSkill     | uint32 | [RequiredSkill](itemset_dbc#requiredskill)         | ID in [SkillLine.dbc](skillline)                |
| 52     | RequiredSkillRank | uint32 | [RequiredSkillRank](itemset_dbc#requiredskillrank) |                                                 |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ItemSet).
