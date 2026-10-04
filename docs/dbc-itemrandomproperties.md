# ItemRandomProperties.dbc

[`Back-to:DBC`](dbc-index)

**The \`ItemRandomProperties.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [itemrandomproperties_dbc](itemrandomproperties_dbc) table of the world database.

**Structure**

| Column | Field          | Type   | itemrandomproperties\_dbc column                      | Comment |
| :----: | :------------- | :----- | :---------------------------------------------------- | :------ |
| 0      | ID             | uint32 | [ID](itemrandomproperties_dbc#id)                     |         |
| 1      | InternalName   | string | [Name](itemrandomproperties_dbc#name)                 |         |
| 2      | Enchantment_0  | uint32 | [Enchantment_1](itemrandomproperties_dbc#enchantment) |         |
| 3      | Enchantment_1  | uint32 | [Enchantment_2](itemrandomproperties_dbc#enchantment) |         |
| 4      | Enchantment_2  | uint32 | [Enchantment_3](itemrandomproperties_dbc#enchantment) |         |
| 5      | Enchantment_3  | uint32 | [Enchantment_4](itemrandomproperties_dbc#enchantment) |         |
| 6      | Enchantment_4  | uint32 | [Enchantment_5](itemrandomproperties_dbc#enchantment) |         |
| 7      | Name_0         | string | [Name_Lang_enUS](itemrandomproperties_dbc#namelang)   |         |
| 8      | Name_1         | string | [Name_Lang_enGB](itemrandomproperties_dbc#namelang)   |         |
| 9      | Name_2         | string | [Name_Lang_koKR](itemrandomproperties_dbc#namelang)   |         |
| 10     | Name_3         | string | [Name_Lang_frFR](itemrandomproperties_dbc#namelang)   |         |
| 11     | Name_4         | string | [Name_Lang_deDE](itemrandomproperties_dbc#namelang)   |         |
| 12     | Name_5         | string | [Name_Lang_enCN](itemrandomproperties_dbc#namelang)   |         |
| 13     | Name_6         | string | [Name_Lang_zhCN](itemrandomproperties_dbc#namelang)   |         |
| 14     | Name_7         | string | [Name_Lang_enTW](itemrandomproperties_dbc#namelang)   |         |
| 15     | Name_8         | string | [Name_Lang_zhTW](itemrandomproperties_dbc#namelang)   |         |
| 16     | Name_9         | string | [Name_Lang_esES](itemrandomproperties_dbc#namelang)   |         |
| 17     | Name_10        | string | [Name_Lang_esMX](itemrandomproperties_dbc#namelang)   |         |
| 18     | Name_11        | string | [Name_Lang_ruRU](itemrandomproperties_dbc#namelang)   |         |
| 19     | Name_12        | string | [Name_Lang_ptPT](itemrandomproperties_dbc#namelang)   |         |
| 20     | Name_13        | string | [Name_Lang_ptBR](itemrandomproperties_dbc#namelang)   |         |
| 21     | Name_14        | string | [Name_Lang_itIT](itemrandomproperties_dbc#namelang)   |         |
| 22     | Name_15        | string | [Name_Lang_Unk](itemrandomproperties_dbc#namelang)    |         |
| 23     | Name_lang_mask | uint32 | [Name_Lang_Mask](itemrandomproperties_dbc#namelang)   |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ItemRandomProperties).
