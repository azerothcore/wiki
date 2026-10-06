# SpellShapeshiftForm.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellShapeshiftForm.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [spellshapeshiftform_dbc](spellshapeshiftform_dbc) table of the world database.

**Structure**

| Column | Field               | Type   | spellshapeshiftform\_dbc column                                  | Comment                                                  |
| :----: | :------------------ | :----- | :--------------------------------------------------------------- | :------------------------------------------------------- |
| 0      | ID                  | uint32 | [ID](spellshapeshiftform_dbc#id)                                 |                                                          |
| 1      | BonusActionBar      | uint32 | [BonusActionBar](spellshapeshiftform_dbc#bonusactionbar)         |                                                          |
| 2      | Name_0              | string | [Name_Lang_enUS](spellshapeshiftform_dbc#namelang)               | Assumed enUS                                             |
| 3      | Name_1              | string | [Name_Lang_enGB](spellshapeshiftform_dbc#namelang)               | Assumed enGB, not used in 3.3.5a                         |
| 4      | Name_2              | string | [Name_Lang_koKR](spellshapeshiftform_dbc#namelang)               | Assumed koKR                                             |
| 5      | Name_3              | string | [Name_Lang_frFR](spellshapeshiftform_dbc#namelang)               | Assumed frFR                                             |
| 6      | Name_4              | string | [Name_Lang_deDE](spellshapeshiftform_dbc#namelang)               | Assumed deDE                                             |
| 7      | Name_5              | string | [Name_Lang_enCN](spellshapeshiftform_dbc#namelang)               | Assumed enCN, not used in 3.3.5a                         |
| 8      | Name_6              | string | [Name_Lang_zhCN](spellshapeshiftform_dbc#namelang)               | Assumed zhCN                                             |
| 9      | Name_7              | string | [Name_Lang_enTW](spellshapeshiftform_dbc#namelang)               | Assumed enTW, not used in 3.3.5a                         |
| 10     | Name_8              | string | [Name_Lang_zhTW](spellshapeshiftform_dbc#namelang)               | Assumed zhTW                                             |
| 11     | Name_9              | string | [Name_Lang_esES](spellshapeshiftform_dbc#namelang)               | Assumed esES                                             |
| 12     | Name_10             | string | [Name_Lang_esMX](spellshapeshiftform_dbc#namelang)               | Assumed esMX                                             |
| 13     | Name_11             | string | [Name_Lang_ruRU](spellshapeshiftform_dbc#namelang)               | Assumed ruRU                                             |
| 14     | Name_12             | string | [Name_Lang_ptPT](spellshapeshiftform_dbc#namelang)               | Assumed ptPT, not used in 3.3.5a                         |
| 15     | Name_13             | string | [Name_Lang_ptBR](spellshapeshiftform_dbc#namelang)               | Assumed ptBR, not used in 3.3.5a                         |
| 16     | Name_14             | string | [Name_Lang_itIT](spellshapeshiftform_dbc#namelang)               | Assumed itIT, not used in 3.3.5a                         |
| 17     | Name_15             | string | [Name_Lang_Unk](spellshapeshiftform_dbc#namelang)                | Unknown language, unsure of the usage in 3.3.5a          |
| 18     | Name_lang_mask      | uint32 | [Name_Lang_Mask](spellshapeshiftform_dbc#namelang)               | Assumed flags of the localized text                      |
| 19     | Flags               | uint32 | [Flags](spellshapeshiftform_dbc#flags)                           |                                                          |
| 20     | CreatureType        | int32  | [CreatureType](spellshapeshiftform_dbc#creaturetype)             | ID in [CreatureType.dbc](dbc-creaturetype)               |
| 21     | AttackIconID        | uint32 | [AttackIconID](spellshapeshiftform_dbc#attackiconid)             | ID in [SpellIcon.dbc](dbc-spellicon)                     |
| 22     | CombatRoundTime     | uint32 | [CombatRoundTime](spellshapeshiftform_dbc#combatroundtime)       |                                                          |
| 23     | CreatureDisplayID_0 | uint32 | [CreatureDisplayID_1](spellshapeshiftform_dbc#creaturedisplayid) | ID in [CreatureDisplayInfo.dbc](dbc-creaturedisplayinfo) |
| 24     | CreatureDisplayID_1 | uint32 | [CreatureDisplayID_2](spellshapeshiftform_dbc#creaturedisplayid) | ID in [CreatureDisplayInfo.dbc](dbc-creaturedisplayinfo) |
| 25     | CreatureDisplayID_2 | uint32 | [CreatureDisplayID_3](spellshapeshiftform_dbc#creaturedisplayid) |                                                          |
| 26     | CreatureDisplayID_3 | uint32 | [CreatureDisplayID_4](spellshapeshiftform_dbc#creaturedisplayid) |                                                          |
| 27     | PresetSpellID_0     | uint32 | [PresetSpellID_1](spellshapeshiftform_dbc#presetspellid)         | ID in [Spell.dbc](spell)                                 |
| 28     | PresetSpellID_1     | uint32 | [PresetSpellID_2](spellshapeshiftform_dbc#presetspellid)         | ID in [Spell.dbc](spell)                                 |
| 29     | PresetSpellID_2     | uint32 | [PresetSpellID_3](spellshapeshiftform_dbc#presetspellid)         | ID in [Spell.dbc](spell)                                 |
| 30     | PresetSpellID_3     | uint32 | [PresetSpellID_4](spellshapeshiftform_dbc#presetspellid)         | ID in [Spell.dbc](spell)                                 |
| 31     | PresetSpellID_4     | uint32 | [PresetSpellID_5](spellshapeshiftform_dbc#presetspellid)         | ID in [Spell.dbc](spell)                                 |
| 32     | PresetSpellID_5     | uint32 | [PresetSpellID_6](spellshapeshiftform_dbc#presetspellid)         | ID in [Spell.dbc](spell)                                 |
| 33     | PresetSpellID_6     | uint32 | [PresetSpellID_7](spellshapeshiftform_dbc#presetspellid)         | ID in [Spell.dbc](spell)                                 |
| 34     | PresetSpellID_7     | uint32 | [PresetSpellID_8](spellshapeshiftform_dbc#presetspellid)         | ID in [Spell.dbc](spell)                                 |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellShapeshiftForm).
