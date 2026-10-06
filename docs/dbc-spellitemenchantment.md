# SpellItemEnchantment.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellItemEnchantment.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [spellitemenchantment_dbc](spellitemenchantment_dbc) table of the world database.

**Structure**

| Column | Field             | Type   | spellitemenchantment\_dbc column                                | Comment                                                                      |
| :----: | :---------------- | :----- | :-------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| 0      | ID                | uint32 | [ID](spellitemenchantment_dbc#id)                               |                                                                              |
| 1      | Charges           | uint32 | [Charges](spellitemenchantment_dbc#charges)                     |                                                                              |
| 2      | Effect_0          | uint32 | [Effect_1](spellitemenchantment_dbc#effect)                     |                                                                              |
| 3      | Effect_1          | uint32 | [Effect_2](spellitemenchantment_dbc#effect)                     |                                                                              |
| 4      | Effect_2          | uint32 | [Effect_3](spellitemenchantment_dbc#effect)                     |                                                                              |
| 5      | EffectPointsMin_0 | uint32 | [EffectPointsMin_1](spellitemenchantment_dbc#effectpointsmin)   |                                                                              |
| 6      | EffectPointsMin_1 | uint32 | [EffectPointsMin_2](spellitemenchantment_dbc#effectpointsmin)   |                                                                              |
| 7      | EffectPointsMin_2 | uint32 | [EffectPointsMin_3](spellitemenchantment_dbc#effectpointsmin)   |                                                                              |
| 8      | EffectPointsMax_0 | uint32 | [EffectPointsMax_1](spellitemenchantment_dbc#effectpointsmax)   |                                                                              |
| 9      | EffectPointsMax_1 | uint32 | [EffectPointsMax_2](spellitemenchantment_dbc#effectpointsmax)   |                                                                              |
| 10     | EffectPointsMax_2 | uint32 | [EffectPointsMax_3](spellitemenchantment_dbc#effectpointsmax)   |                                                                              |
| 11     | EffectArg_0       | uint32 | [EffectArg_1](spellitemenchantment_dbc#effectarg)               |                                                                              |
| 12     | EffectArg_1       | uint32 | [EffectArg_2](spellitemenchantment_dbc#effectarg)               |                                                                              |
| 13     | EffectArg_2       | uint32 | [EffectArg_3](spellitemenchantment_dbc#effectarg)               |                                                                              |
| 14     | Name_0            | string | [Name_Lang_enUS](spellitemenchantment_dbc#namelang)             | Assumed enUS                                                                 |
| 15     | Name_1            | string | [Name_Lang_enGB](spellitemenchantment_dbc#namelang)             | Assumed enGB, not used in 3.3.5a                                             |
| 16     | Name_2            | string | [Name_Lang_koKR](spellitemenchantment_dbc#namelang)             | Assumed koKR                                                                 |
| 17     | Name_3            | string | [Name_Lang_frFR](spellitemenchantment_dbc#namelang)             | Assumed frFR                                                                 |
| 18     | Name_4            | string | [Name_Lang_deDE](spellitemenchantment_dbc#namelang)             | Assumed deDE                                                                 |
| 19     | Name_5            | string | [Name_Lang_enCN](spellitemenchantment_dbc#namelang)             | Assumed enCN, not used in 3.3.5a                                             |
| 20     | Name_6            | string | [Name_Lang_zhCN](spellitemenchantment_dbc#namelang)             | Assumed zhCN                                                                 |
| 21     | Name_7            | string | [Name_Lang_enTW](spellitemenchantment_dbc#namelang)             | Assumed enTW, not used in 3.3.5a                                             |
| 22     | Name_8            | string | [Name_Lang_zhTW](spellitemenchantment_dbc#namelang)             | Assumed zhTW                                                                 |
| 23     | Name_9            | string | [Name_Lang_esES](spellitemenchantment_dbc#namelang)             | Assumed esES                                                                 |
| 24     | Name_10           | string | [Name_Lang_esMX](spellitemenchantment_dbc#namelang)             | Assumed esMX                                                                 |
| 25     | Name_11           | string | [Name_Lang_ruRU](spellitemenchantment_dbc#namelang)             | Assumed ruRU                                                                 |
| 26     | Name_12           | string | [Name_Lang_ptPT](spellitemenchantment_dbc#namelang)             | Assumed ptPT, not used in 3.3.5a                                             |
| 27     | Name_13           | string | [Name_Lang_ptBR](spellitemenchantment_dbc#namelang)             | Assumed ptBR, not used in 3.3.5a                                             |
| 28     | Name_14           | string | [Name_Lang_itIT](spellitemenchantment_dbc#namelang)             | Assumed itIT, not used in 3.3.5a                                             |
| 29     | Name_15           | string | [Name_Lang_Unk](spellitemenchantment_dbc#namelang)              | Unknown language, unsure of the usage in 3.3.5a                              |
| 30     | Name_lang_mask    | uint32 | [Name_Lang_Mask](spellitemenchantment_dbc#namelang)             | Assumed flags of the localized text                                          |
| 31     | ItemVisual        | uint32 | [ItemVisual](spellitemenchantment_dbc#itemvisual)               | ID in [ItemVisuals.dbc](dbc-itemvisuals)                                     |
| 32     | Flags             | uint32 | [Flags](spellitemenchantment_dbc#flags)                         |                                                                              |
| 33     | SrcItemID         | uint32 | [Src_ItemID](spellitemenchantment_dbc#srcitemid)                | ID in [Item.dbc](dbc-item)                                                   |
| 34     | ConditionID       | uint32 | [Condition_Id](spellitemenchantment_dbc#conditionid)            | ID in [SpellItemEnchantmentCondition.dbc](dbc-spellitemenchantmentcondition) |
| 35     | RequiredSkillID   | uint32 | [RequiredSkillID](spellitemenchantment_dbc#requiredskillid)     | ID in [SkillLine.dbc](skillline)                                             |
| 36     | RequiredSkillRank | uint32 | [RequiredSkillRank](spellitemenchantment_dbc#requiredskillrank) |                                                                              |
| 37     | MinLevel          | uint32 | [MinLevel](spellitemenchantment_dbc#minlevel)                   |                                                                              |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellItemEnchantment).
