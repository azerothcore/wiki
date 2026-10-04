# ChatChannels.dbc

[`Back-to:DBC`](dbc-index)

**The \`ChatChannels.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [chatchannels_dbc](chatchannels_dbc) table of the world database.

**Structure**

| Column | Field              | Type   | chatchannels\_dbc column                            | Comment |
| :----: | :----------------- | :----- | :-------------------------------------------------- | :------ |
| 0      | ID                 | uint32 | [ID](chatchannels_dbc#id)                           |         |
| 1      | Flags              | uint32 | [Flags](chatchannels_dbc#flags)                     |         |
| 2      | FactionGroup       | uint32 | [FactionGroup](chatchannels_dbc#factiongroup)       |         |
| 3      | Name_0             | string | [Name_Lang_enUS](chatchannels_dbc#namelang)         |         |
| 4      | Name_1             | string | [Name_Lang_enGB](chatchannels_dbc#namelang)         |         |
| 5      | Name_2             | string | [Name_Lang_koKR](chatchannels_dbc#namelang)         |         |
| 6      | Name_3             | string | [Name_Lang_frFR](chatchannels_dbc#namelang)         |         |
| 7      | Name_4             | string | [Name_Lang_deDE](chatchannels_dbc#namelang)         |         |
| 8      | Name_5             | string | [Name_Lang_enCN](chatchannels_dbc#namelang)         |         |
| 9      | Name_6             | string | [Name_Lang_zhCN](chatchannels_dbc#namelang)         |         |
| 10     | Name_7             | string | [Name_Lang_enTW](chatchannels_dbc#namelang)         |         |
| 11     | Name_8             | string | [Name_Lang_zhTW](chatchannels_dbc#namelang)         |         |
| 12     | Name_9             | string | [Name_Lang_esES](chatchannels_dbc#namelang)         |         |
| 13     | Name_10            | string | [Name_Lang_esMX](chatchannels_dbc#namelang)         |         |
| 14     | Name_11            | string | [Name_Lang_ruRU](chatchannels_dbc#namelang)         |         |
| 15     | Name_12            | string | [Name_Lang_ptPT](chatchannels_dbc#namelang)         |         |
| 16     | Name_13            | string | [Name_Lang_ptBR](chatchannels_dbc#namelang)         |         |
| 17     | Name_14            | string | [Name_Lang_itIT](chatchannels_dbc#namelang)         |         |
| 18     | Name_15            | string | [Name_Lang_Unk](chatchannels_dbc#namelang)          |         |
| 19     | Name_lang_mask     | uint32 | [Name_Lang_Mask](chatchannels_dbc#namelang)         |         |
| 20     | Shortcut_0         | string | [Shortcut_Lang_enUS](chatchannels_dbc#shortcutlang) |         |
| 21     | Shortcut_1         | string | [Shortcut_Lang_enGB](chatchannels_dbc#shortcutlang) |         |
| 22     | Shortcut_2         | string | [Shortcut_Lang_koKR](chatchannels_dbc#shortcutlang) |         |
| 23     | Shortcut_3         | string | [Shortcut_Lang_frFR](chatchannels_dbc#shortcutlang) |         |
| 24     | Shortcut_4         | string | [Shortcut_Lang_deDE](chatchannels_dbc#shortcutlang) |         |
| 25     | Shortcut_5         | string | [Shortcut_Lang_enCN](chatchannels_dbc#shortcutlang) |         |
| 26     | Shortcut_6         | string | [Shortcut_Lang_zhCN](chatchannels_dbc#shortcutlang) |         |
| 27     | Shortcut_7         | string | [Shortcut_Lang_enTW](chatchannels_dbc#shortcutlang) |         |
| 28     | Shortcut_8         | string | [Shortcut_Lang_zhTW](chatchannels_dbc#shortcutlang) |         |
| 29     | Shortcut_9         | string | [Shortcut_Lang_esES](chatchannels_dbc#shortcutlang) |         |
| 30     | Shortcut_10        | string | [Shortcut_Lang_esMX](chatchannels_dbc#shortcutlang) |         |
| 31     | Shortcut_11        | string | [Shortcut_Lang_ruRU](chatchannels_dbc#shortcutlang) |         |
| 32     | Shortcut_12        | string | [Shortcut_Lang_ptPT](chatchannels_dbc#shortcutlang) |         |
| 33     | Shortcut_13        | string | [Shortcut_Lang_ptBR](chatchannels_dbc#shortcutlang) |         |
| 34     | Shortcut_14        | string | [Shortcut_Lang_itIT](chatchannels_dbc#shortcutlang) |         |
| 35     | Shortcut_15        | string | [Shortcut_Lang_Unk](chatchannels_dbc#shortcutlang)  |         |
| 36     | Shortcut_lang_mask | uint32 | [Shortcut_Lang_Mask](chatchannels_dbc#shortcutlang) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ChatChannels).
