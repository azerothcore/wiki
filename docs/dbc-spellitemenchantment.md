# SpellItemEnchantment.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellItemEnchantment.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [spellitemenchantment_dbc](spellitemenchantment_dbc) table of the world database.

**Structure**

| Column | Field             | Type   | spellitemenchantment\_dbc column                                | Comment |
| :----: | :---------------- | :----- | :-------------------------------------------------------------- | :------ |
| 0      | ID                | uint32 | [ID](spellitemenchantment_dbc#id)                               |         |
| 1      | Charges           | uint32 | [Charges](spellitemenchantment_dbc#charges)                     |         |
| 2      | Effect_0          | uint32 | [Effect_1](spellitemenchantment_dbc#effect)                     |         |
| 3      | Effect_1          | uint32 | [Effect_2](spellitemenchantment_dbc#effect)                     |         |
| 4      | Effect_2          | uint32 | [Effect_3](spellitemenchantment_dbc#effect)                     |         |
| 5      | EffectPointsMin_0 | uint32 | [EffectPointsMin_1](spellitemenchantment_dbc#effectpointsmin)   |         |
| 6      | EffectPointsMin_1 | uint32 | [EffectPointsMin_2](spellitemenchantment_dbc#effectpointsmin)   |         |
| 7      | EffectPointsMin_2 | uint32 | [EffectPointsMin_3](spellitemenchantment_dbc#effectpointsmin)   |         |
| 8      | EffectPointsMax_0 | uint32 | [EffectPointsMax_1](spellitemenchantment_dbc#effectpointsmax)   |         |
| 9      | EffectPointsMax_1 | uint32 | [EffectPointsMax_2](spellitemenchantment_dbc#effectpointsmax)   |         |
| 10     | EffectPointsMax_2 | uint32 | [EffectPointsMax_3](spellitemenchantment_dbc#effectpointsmax)   |         |
| 11     | EffectArg_0       | uint32 | [EffectArg_1](spellitemenchantment_dbc#effectarg)               |         |
| 12     | EffectArg_1       | uint32 | [EffectArg_2](spellitemenchantment_dbc#effectarg)               |         |
| 13     | EffectArg_2       | uint32 | [EffectArg_3](spellitemenchantment_dbc#effectarg)               |         |
| 14     | Name_0            | string | [Name_Lang_enUS](spellitemenchantment_dbc#namelang)             |         |
| 15     | Name_1            | string | [Name_Lang_enGB](spellitemenchantment_dbc#namelang)             |         |
| 16     | Name_2            | string | [Name_Lang_koKR](spellitemenchantment_dbc#namelang)             |         |
| 17     | Name_3            | string | [Name_Lang_frFR](spellitemenchantment_dbc#namelang)             |         |
| 18     | Name_4            | string | [Name_Lang_deDE](spellitemenchantment_dbc#namelang)             |         |
| 19     | Name_5            | string | [Name_Lang_enCN](spellitemenchantment_dbc#namelang)             |         |
| 20     | Name_6            | string | [Name_Lang_zhCN](spellitemenchantment_dbc#namelang)             |         |
| 21     | Name_7            | string | [Name_Lang_enTW](spellitemenchantment_dbc#namelang)             |         |
| 22     | Name_8            | string | [Name_Lang_zhTW](spellitemenchantment_dbc#namelang)             |         |
| 23     | Name_9            | string | [Name_Lang_esES](spellitemenchantment_dbc#namelang)             |         |
| 24     | Name_10           | string | [Name_Lang_esMX](spellitemenchantment_dbc#namelang)             |         |
| 25     | Name_11           | string | [Name_Lang_ruRU](spellitemenchantment_dbc#namelang)             |         |
| 26     | Name_12           | string | [Name_Lang_ptPT](spellitemenchantment_dbc#namelang)             |         |
| 27     | Name_13           | string | [Name_Lang_ptBR](spellitemenchantment_dbc#namelang)             |         |
| 28     | Name_14           | string | [Name_Lang_itIT](spellitemenchantment_dbc#namelang)             |         |
| 29     | Name_15           | string | [Name_Lang_Unk](spellitemenchantment_dbc#namelang)              |         |
| 30     | Name_lang_mask    | uint32 | [Name_Lang_Mask](spellitemenchantment_dbc#namelang)             |         |
| 31     | ItemVisual        | uint32 | [ItemVisual](spellitemenchantment_dbc#itemvisual)               |         |
| 32     | Flags             | uint32 | [Flags](spellitemenchantment_dbc#flags)                         |         |
| 33     | SrcItemID         | uint32 | [Src_ItemID](spellitemenchantment_dbc#srcitemid)                |         |
| 34     | ConditionID       | uint32 | [Condition_Id](spellitemenchantment_dbc#conditionid)            |         |
| 35     | RequiredSkillID   | uint32 | [RequiredSkillID](spellitemenchantment_dbc#requiredskillid)     |         |
| 36     | RequiredSkillRank | uint32 | [RequiredSkillRank](spellitemenchantment_dbc#requiredskillrank) |         |
| 37     | MinLevel          | uint32 | [MinLevel](spellitemenchantment_dbc#minlevel)                   |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellItemEnchantment).
