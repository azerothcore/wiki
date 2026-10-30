# WMOAreaTable.dbc

[`Back-to:DBC`](dbc-index)

**The \`WMOAreaTable.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [wmoareatable_dbc](wmoareatable_dbc) table of the world database.

**Structure**

| Column | Field                       | Type   | wmoareatable\_dbc column                                                    | Comment                                                                                                      |
| :----: | :-------------------------- | :----- | :-------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| 0      | ID                          | uint32 | [ID](wmoareatable_dbc#id)                                                   |                                                                                                              |
| 1      | WMOID                       | uint32 | [WMOID](wmoareatable_dbc#wmoid)                                             |                                                                                                              |
| 2      | NameSetID                   | int32  | [NameSetID](wmoareatable_dbc#namesetid)                                     |                                                                                                              |
| 3      | WMOGroupID                  | int32  | [WMOGroupID](wmoareatable_dbc#wmogroupid)                                   |                                                                                                              |
| 4      | SoundProviderPref           | int32  | [SoundProviderPref](wmoareatable_dbc#soundproviderpref)                     |                                                                                                              |
| 5      | SoundProviderPrefUnderwater | uint32 | [SoundProviderPrefUnderwater](wmoareatable_dbc#soundproviderprefunderwater) | ID in [SoundProviderPreferences.dbc](dbc-soundproviderpreferences)                                           |
| 6      | AmbienceID                  | uint32 | [AmbienceID](wmoareatable_dbc#ambienceid)                                   | ID in [SoundAmbience.dbc](dbc-soundambience)                                                                 |
| 7      | ZoneMusic                   | uint32 | [ZoneMusic](wmoareatable_dbc#zonemusic)                                     | ID in [ZoneMusic.dbc](dbc-zonemusic) (3 of the 236 values used here are not in that file)                    |
| 8      | IntroSound                  | int32  | [IntroSound](wmoareatable_dbc#introsound)                                   | ID in [ZoneIntroMusicTable.dbc](dbc-zoneintromusictable) (5 of the 74 values used here are not in that file) |
| 9      | Flags                       | uint32 | [Flags](wmoareatable_dbc#flags)                                             |                                                                                                              |
| 10     | AreaTableID                 | uint32 | [AreaTableID](wmoareatable_dbc#areatableid)                                 | ID in [AreaTable.dbc](areatable)                                                                             |
| 11     | AreaName_0                  | string | [AreaName_Lang_enUS](wmoareatable_dbc#areanamelang)                         | Assumed enUS                                                                                                 |
| 12     | AreaName_1                  | string | [AreaName_Lang_enGB](wmoareatable_dbc#areanamelang)                         | Assumed enGB, not used in 3.3.5a                                                                             |
| 13     | AreaName_2                  | string | [AreaName_Lang_koKR](wmoareatable_dbc#areanamelang)                         | Assumed koKR                                                                                                 |
| 14     | AreaName_3                  | string | [AreaName_Lang_frFR](wmoareatable_dbc#areanamelang)                         | Assumed frFR                                                                                                 |
| 15     | AreaName_4                  | string | [AreaName_Lang_deDE](wmoareatable_dbc#areanamelang)                         | Assumed deDE                                                                                                 |
| 16     | AreaName_5                  | string | [AreaName_Lang_enCN](wmoareatable_dbc#areanamelang)                         | Assumed enCN, not used in 3.3.5a                                                                             |
| 17     | AreaName_6                  | string | [AreaName_Lang_zhCN](wmoareatable_dbc#areanamelang)                         | Assumed zhCN                                                                                                 |
| 18     | AreaName_7                  | string | [AreaName_Lang_enTW](wmoareatable_dbc#areanamelang)                         | Assumed enTW, not used in 3.3.5a                                                                             |
| 19     | AreaName_8                  | string | [AreaName_Lang_zhTW](wmoareatable_dbc#areanamelang)                         | Assumed zhTW                                                                                                 |
| 20     | AreaName_9                  | string | [AreaName_Lang_esES](wmoareatable_dbc#areanamelang)                         | Assumed esES                                                                                                 |
| 21     | AreaName_10                 | string | [AreaName_Lang_esMX](wmoareatable_dbc#areanamelang)                         | Assumed esMX                                                                                                 |
| 22     | AreaName_11                 | string | [AreaName_Lang_ruRU](wmoareatable_dbc#areanamelang)                         | Assumed ruRU                                                                                                 |
| 23     | AreaName_12                 | string | [AreaName_Lang_ptPT](wmoareatable_dbc#areanamelang)                         | Assumed ptPT, not used in 3.3.5a                                                                             |
| 24     | AreaName_13                 | string | [AreaName_Lang_ptBR](wmoareatable_dbc#areanamelang)                         | Assumed ptBR, not used in 3.3.5a                                                                             |
| 25     | AreaName_14                 | string | [AreaName_Lang_itIT](wmoareatable_dbc#areanamelang)                         | Assumed itIT, not used in 3.3.5a                                                                             |
| 26     | AreaName_15                 | string | [AreaName_Lang_Unk](wmoareatable_dbc#areanamelang)                          | Unknown language, unsure of the usage in 3.3.5a                                                              |
| 27     | AreaName_lang_mask          | uint32 | [AreaName_Lang_Mask](wmoareatable_dbc#areanamelang)                         | Assumed flags of the localized text                                                                          |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/WMOAreaTable).
