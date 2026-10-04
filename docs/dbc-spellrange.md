# SpellRange.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellRange.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [spellrange_dbc](spellrange_dbc) table of the world database.

**Structure**

| Column | Field                      | Type   | spellrange\_dbc column                                            | Comment |
| :----: | :------------------------- | :----- | :---------------------------------------------------------------- | :------ |
| 0      | ID                         | uint32 | [ID](spellrange_dbc#id)                                           |         |
| 1      | RangeMin_0                 | float  | [RangeMin_1](spellrange_dbc#rangemin)                             |         |
| 2      | RangeMin_1                 | float  | [RangeMin_2](spellrange_dbc#rangemin)                             |         |
| 3      | RangeMax_0                 | float  | [RangeMax_1](spellrange_dbc#rangemax)                             |         |
| 4      | RangeMax_1                 | float  | [RangeMax_2](spellrange_dbc#rangemax)                             |         |
| 5      | Flags                      | uint32 | [Flags](spellrange_dbc#flags)                                     |         |
| 6      | DisplayName_0              | string | [DisplayName_Lang_enUS](spellrange_dbc#displaynamelang)           |         |
| 7      | DisplayName_1              | string | [DisplayName_Lang_enGB](spellrange_dbc#displaynamelang)           |         |
| 8      | DisplayName_2              | string | [DisplayName_Lang_koKR](spellrange_dbc#displaynamelang)           |         |
| 9      | DisplayName_3              | string | [DisplayName_Lang_frFR](spellrange_dbc#displaynamelang)           |         |
| 10     | DisplayName_4              | string | [DisplayName_Lang_deDE](spellrange_dbc#displaynamelang)           |         |
| 11     | DisplayName_5              | string | [DisplayName_Lang_enCN](spellrange_dbc#displaynamelang)           |         |
| 12     | DisplayName_6              | string | [DisplayName_Lang_zhCN](spellrange_dbc#displaynamelang)           |         |
| 13     | DisplayName_7              | string | [DisplayName_Lang_enTW](spellrange_dbc#displaynamelang)           |         |
| 14     | DisplayName_8              | string | [DisplayName_Lang_zhTW](spellrange_dbc#displaynamelang)           |         |
| 15     | DisplayName_9              | string | [DisplayName_Lang_esES](spellrange_dbc#displaynamelang)           |         |
| 16     | DisplayName_10             | string | [DisplayName_Lang_esMX](spellrange_dbc#displaynamelang)           |         |
| 17     | DisplayName_11             | string | [DisplayName_Lang_ruRU](spellrange_dbc#displaynamelang)           |         |
| 18     | DisplayName_12             | string | [DisplayName_Lang_ptPT](spellrange_dbc#displaynamelang)           |         |
| 19     | DisplayName_13             | string | [DisplayName_Lang_ptBR](spellrange_dbc#displaynamelang)           |         |
| 20     | DisplayName_14             | string | [DisplayName_Lang_itIT](spellrange_dbc#displaynamelang)           |         |
| 21     | DisplayName_15             | string | [DisplayName_Lang_Unk](spellrange_dbc#displaynamelang)            |         |
| 22     | DisplayName_lang_mask      | uint32 | [DisplayName_Lang_Mask](spellrange_dbc#displaynamelang)           |         |
| 23     | DisplayNameShort_0         | string | [DisplayNameShort_Lang_enUS](spellrange_dbc#displaynameshortlang) |         |
| 24     | DisplayNameShort_1         | string | [DisplayNameShort_Lang_enGB](spellrange_dbc#displaynameshortlang) |         |
| 25     | DisplayNameShort_2         | string | [DisplayNameShort_Lang_koKR](spellrange_dbc#displaynameshortlang) |         |
| 26     | DisplayNameShort_3         | string | [DisplayNameShort_Lang_frFR](spellrange_dbc#displaynameshortlang) |         |
| 27     | DisplayNameShort_4         | string | [DisplayNameShort_Lang_deDE](spellrange_dbc#displaynameshortlang) |         |
| 28     | DisplayNameShort_5         | string | [DisplayNameShort_Lang_enCN](spellrange_dbc#displaynameshortlang) |         |
| 29     | DisplayNameShort_6         | string | [DisplayNameShort_Lang_zhCN](spellrange_dbc#displaynameshortlang) |         |
| 30     | DisplayNameShort_7         | string | [DisplayNameShort_Lang_enTW](spellrange_dbc#displaynameshortlang) |         |
| 31     | DisplayNameShort_8         | string | [DisplayNameShort_Lang_zhTW](spellrange_dbc#displaynameshortlang) |         |
| 32     | DisplayNameShort_9         | string | [DisplayNameShort_Lang_esES](spellrange_dbc#displaynameshortlang) |         |
| 33     | DisplayNameShort_10        | string | [DisplayNameShort_Lang_esMX](spellrange_dbc#displaynameshortlang) |         |
| 34     | DisplayNameShort_11        | string | [DisplayNameShort_Lang_ruRU](spellrange_dbc#displaynameshortlang) |         |
| 35     | DisplayNameShort_12        | string | [DisplayNameShort_Lang_ptPT](spellrange_dbc#displaynameshortlang) |         |
| 36     | DisplayNameShort_13        | string | [DisplayNameShort_Lang_ptBR](spellrange_dbc#displaynameshortlang) |         |
| 37     | DisplayNameShort_14        | string | [DisplayNameShort_Lang_itIT](spellrange_dbc#displaynameshortlang) |         |
| 38     | DisplayNameShort_15        | string | [DisplayNameShort_Lang_Unk](spellrange_dbc#displaynameshortlang)  |         |
| 39     | DisplayNameShort_lang_mask | uint32 | [DisplayNameShort_Lang_Mask](spellrange_dbc#displaynameshortlang) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellRange).
