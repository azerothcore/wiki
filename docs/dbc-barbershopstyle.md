# BarberShopStyle.dbc

[`Back-to:DBC`](dbc-index)

**The \`BarberShopStyle.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [barbershopstyle_dbc](barbershopstyle_dbc) table of the world database.

**Structure**

| Column | Field                 | Type   | barbershopstyle\_dbc column                                  | Comment |
| :----: | :-------------------- | :----- | :----------------------------------------------------------- | :------ |
| 0      | ID                    | uint32 | [ID](barbershopstyle_dbc#id)                                 |         |
| 1      | Type                  | uint32 | [Type](barbershopstyle_dbc#type)                             |         |
| 2      | DisplayName_0         | string | [DisplayName_Lang_enUS](barbershopstyle_dbc#displaynamelang) |         |
| 3      | DisplayName_1         | string | [DisplayName_Lang_enGB](barbershopstyle_dbc#displaynamelang) |         |
| 4      | DisplayName_2         | string | [DisplayName_Lang_koKR](barbershopstyle_dbc#displaynamelang) |         |
| 5      | DisplayName_3         | string | [DisplayName_Lang_frFR](barbershopstyle_dbc#displaynamelang) |         |
| 6      | DisplayName_4         | string | [DisplayName_Lang_deDE](barbershopstyle_dbc#displaynamelang) |         |
| 7      | DisplayName_5         | string | [DisplayName_Lang_enCN](barbershopstyle_dbc#displaynamelang) |         |
| 8      | DisplayName_6         | string | [DisplayName_Lang_zhCN](barbershopstyle_dbc#displaynamelang) |         |
| 9      | DisplayName_7         | string | [DisplayName_Lang_enTW](barbershopstyle_dbc#displaynamelang) |         |
| 10     | DisplayName_8         | string | [DisplayName_Lang_zhTW](barbershopstyle_dbc#displaynamelang) |         |
| 11     | DisplayName_9         | string | [DisplayName_Lang_esES](barbershopstyle_dbc#displaynamelang) |         |
| 12     | DisplayName_10        | string | [DisplayName_Lang_esMX](barbershopstyle_dbc#displaynamelang) |         |
| 13     | DisplayName_11        | string | [DisplayName_Lang_ruRU](barbershopstyle_dbc#displaynamelang) |         |
| 14     | DisplayName_12        | string | [DisplayName_Lang_ptPT](barbershopstyle_dbc#displaynamelang) |         |
| 15     | DisplayName_13        | string | [DisplayName_Lang_ptBR](barbershopstyle_dbc#displaynamelang) |         |
| 16     | DisplayName_14        | string | [DisplayName_Lang_itIT](barbershopstyle_dbc#displaynamelang) |         |
| 17     | DisplayName_15        | string | [DisplayName_Lang_Unk](barbershopstyle_dbc#displaynamelang)  |         |
| 18     | DisplayName_lang_mask | uint32 | [DisplayName_Lang_Mask](barbershopstyle_dbc#displaynamelang) |         |
| 19     | Description_0         | string | [Description_Lang_enUS](barbershopstyle_dbc#descriptionlang) |         |
| 20     | Description_1         | string | [Description_Lang_enGB](barbershopstyle_dbc#descriptionlang) |         |
| 21     | Description_2         | string | [Description_Lang_koKR](barbershopstyle_dbc#descriptionlang) |         |
| 22     | Description_3         | string | [Description_Lang_frFR](barbershopstyle_dbc#descriptionlang) |         |
| 23     | Description_4         | string | [Description_Lang_deDE](barbershopstyle_dbc#descriptionlang) |         |
| 24     | Description_5         | string | [Description_Lang_enCN](barbershopstyle_dbc#descriptionlang) |         |
| 25     | Description_6         | string | [Description_Lang_zhCN](barbershopstyle_dbc#descriptionlang) |         |
| 26     | Description_7         | string | [Description_Lang_enTW](barbershopstyle_dbc#descriptionlang) |         |
| 27     | Description_8         | string | [Description_Lang_zhTW](barbershopstyle_dbc#descriptionlang) |         |
| 28     | Description_9         | string | [Description_Lang_esES](barbershopstyle_dbc#descriptionlang) |         |
| 29     | Description_10        | string | [Description_Lang_esMX](barbershopstyle_dbc#descriptionlang) |         |
| 30     | Description_11        | string | [Description_Lang_ruRU](barbershopstyle_dbc#descriptionlang) |         |
| 31     | Description_12        | string | [Description_Lang_ptPT](barbershopstyle_dbc#descriptionlang) |         |
| 32     | Description_13        | string | [Description_Lang_ptBR](barbershopstyle_dbc#descriptionlang) |         |
| 33     | Description_14        | string | [Description_Lang_itIT](barbershopstyle_dbc#descriptionlang) |         |
| 34     | Description_15        | string | [Description_Lang_Unk](barbershopstyle_dbc#descriptionlang)  |         |
| 35     | Description_lang_mask | uint32 | [Description_Lang_Mask](barbershopstyle_dbc#descriptionlang) |         |
| 36     | CostModifier          | float  | [Cost_Modifier](barbershopstyle_dbc#costmodifier)            |         |
| 37     | Race                  | uint32 | [Race](barbershopstyle_dbc#race)                             |         |
| 38     | Sex                   | uint32 | [Sex](barbershopstyle_dbc#sex)                               |         |
| 39     | Data                  | uint32 | [Data](barbershopstyle_dbc#data)                             |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/BarberShopStyle).
