# TalentTab.dbc

[`Back-to:DBC`](dbc-index)

**The \`TalentTab.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [talenttab_dbc](talenttab_dbc) table of the world database.

**Structure**

| Column | Field          | Type   | talenttab\_dbc column                          | Comment                                                                                                           |
| :----: | :------------- | :----- | :--------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- |
| 0      | ID             | uint32 | [ID](talenttab_dbc#id)                         |                                                                                                                   |
| 1      | Name_0         | string | [Name_Lang_enUS](talenttab_dbc#namelang)       | Assumed enUS                                                                                                      |
| 2      | Name_1         | string | [Name_Lang_enGB](talenttab_dbc#namelang)       | Assumed enGB, not used in 3.3.5a                                                                                  |
| 3      | Name_2         | string | [Name_Lang_koKR](talenttab_dbc#namelang)       | Assumed koKR                                                                                                      |
| 4      | Name_3         | string | [Name_Lang_frFR](talenttab_dbc#namelang)       | Assumed frFR                                                                                                      |
| 5      | Name_4         | string | [Name_Lang_deDE](talenttab_dbc#namelang)       | Assumed deDE                                                                                                      |
| 6      | Name_5         | string | [Name_Lang_enCN](talenttab_dbc#namelang)       | Assumed enCN, not used in 3.3.5a                                                                                  |
| 7      | Name_6         | string | [Name_Lang_zhCN](talenttab_dbc#namelang)       | Assumed zhCN                                                                                                      |
| 8      | Name_7         | string | [Name_Lang_enTW](talenttab_dbc#namelang)       | Assumed enTW, not used in 3.3.5a                                                                                  |
| 9      | Name_8         | string | [Name_Lang_zhTW](talenttab_dbc#namelang)       | Assumed zhTW                                                                                                      |
| 10     | Name_9         | string | [Name_Lang_esES](talenttab_dbc#namelang)       | Assumed esES                                                                                                      |
| 11     | Name_10        | string | [Name_Lang_esMX](talenttab_dbc#namelang)       | Assumed esMX                                                                                                      |
| 12     | Name_11        | string | [Name_Lang_ruRU](talenttab_dbc#namelang)       | Assumed ruRU                                                                                                      |
| 13     | Name_12        | string | [Name_Lang_ptPT](talenttab_dbc#namelang)       | Assumed ptPT, not used in 3.3.5a                                                                                  |
| 14     | Name_13        | string | [Name_Lang_ptBR](talenttab_dbc#namelang)       | Assumed ptBR, not used in 3.3.5a                                                                                  |
| 15     | Name_14        | string | [Name_Lang_itIT](talenttab_dbc#namelang)       | Assumed itIT, not used in 3.3.5a                                                                                  |
| 16     | Name_15        | string | [Name_Lang_Unk](talenttab_dbc#namelang)        | Unknown language, unsure of the usage in 3.3.5a                                                                   |
| 17     | Name_lang_mask | uint32 | [Name_Lang_Mask](talenttab_dbc#namelang)       | Assumed flags of the localized text                                                                               |
| 18     | SpellIconID    | uint32 | [SpellIconID](talenttab_dbc#spelliconid)       | ID in [SpellIcon.dbc](dbc-spellicon)                                                                              |
| 19     | RaceMask       | uint32 | [RaceMask](talenttab_dbc#racemask)             | Race mask (1 of 2 values used here also set bits that are not in that file). See [ChrRaces.dbc](chrraces#content) |
| 20     | ClassMask      | uint32 | [ClassMask](talenttab_dbc#classmask)           | Class mask. See [ChrClasses.dbc](chrclasses#content)                                                              |
| 21     | PetTalentMask  | uint32 | [PetTalentMask](talenttab_dbc#pettalentmask)   | ID in [CreatureFamily.dbc](dbc-creaturefamily)                                                                    |
| 22     | OrderIndex     | uint32 | [OrderIndex](talenttab_dbc#orderindex)         |                                                                                                                   |
| 23     | BackgroundFile | string | [BackgroundFile](talenttab_dbc#backgroundfile) |                                                                                                                   |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/TalentTab).
