# QuestSort.dbc

[`Back-to:DBC`](dbc-index)

**The \`QuestSort.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [questsort_dbc](questsort_dbc) table of the world database.

**Structure**

| Column | Field              | Type   | questsort\_dbc column                            | Comment |
| :----: | :----------------- | :----- | :----------------------------------------------- | :------ |
| 0      | ID                 | uint32 | [ID](questsort_dbc#id)                           |         |
| 1      | SortName_0         | string | [SortName_Lang_enUS](questsort_dbc#sortnamelang) |         |
| 2      | SortName_1         | string | [SortName_Lang_enGB](questsort_dbc#sortnamelang) |         |
| 3      | SortName_2         | string | [SortName_Lang_koKR](questsort_dbc#sortnamelang) |         |
| 4      | SortName_3         | string | [SortName_Lang_frFR](questsort_dbc#sortnamelang) |         |
| 5      | SortName_4         | string | [SortName_Lang_deDE](questsort_dbc#sortnamelang) |         |
| 6      | SortName_5         | string | [SortName_Lang_enCN](questsort_dbc#sortnamelang) |         |
| 7      | SortName_6         | string | [SortName_Lang_zhCN](questsort_dbc#sortnamelang) |         |
| 8      | SortName_7         | string | [SortName_Lang_enTW](questsort_dbc#sortnamelang) |         |
| 9      | SortName_8         | string | [SortName_Lang_zhTW](questsort_dbc#sortnamelang) |         |
| 10     | SortName_9         | string | [SortName_Lang_esES](questsort_dbc#sortnamelang) |         |
| 11     | SortName_10        | string | [SortName_Lang_esMX](questsort_dbc#sortnamelang) |         |
| 12     | SortName_11        | string | [SortName_Lang_ruRU](questsort_dbc#sortnamelang) |         |
| 13     | SortName_12        | string | [SortName_Lang_ptPT](questsort_dbc#sortnamelang) |         |
| 14     | SortName_13        | string | [SortName_Lang_ptBR](questsort_dbc#sortnamelang) |         |
| 15     | SortName_14        | string | [SortName_Lang_itIT](questsort_dbc#sortnamelang) |         |
| 16     | SortName_15        | string | [SortName_Lang_Unk](questsort_dbc#sortnamelang)  |         |
| 17     | SortName_lang_mask | uint32 | [SortName_Lang_Mask](questsort_dbc#sortnamelang) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/QuestSort).
