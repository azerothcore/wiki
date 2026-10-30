---
redirect_from: "/TotemCategory"
---

# TotemCategory

[`Back-to:DBC`](dbc-index)

**TotemCategory.dbc**

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)  

## Structure

| Column | Field             | Type   | totemcategory\_dbc column                                | Comment                                                                  |
| :----: | :---------------- | :----- | :------------------------------------------------------- | :----------------------------------------------------------------------- |
| 0      | ID                | uint32 | [ID](totemcategory_dbc#id)                               |                                                                          |
| 1      | Name_0            | string | [Name_Lang_enUS](totemcategory_dbc#namelang)             | Includes all kinds of component things.. not just totems. Assumed enUS   |
| 2      | Name_1            | string | [Name_Lang_enGB](totemcategory_dbc#namelang)             | Assumed enGB, not used in 3.3.5a                                         |
| 3      | Name_2            | string | [Name_Lang_koKR](totemcategory_dbc#namelang)             | Assumed koKR                                                             |
| 4      | Name_3            | string | [Name_Lang_frFR](totemcategory_dbc#namelang)             | Assumed frFR                                                             |
| 5      | Name_4            | string | [Name_Lang_deDE](totemcategory_dbc#namelang)             | Assumed deDE                                                             |
| 6      | Name_5            | string | [Name_Lang_enCN](totemcategory_dbc#namelang)             | Assumed enCN, not used in 3.3.5a                                         |
| 7      | Name_6            | string | [Name_Lang_zhCN](totemcategory_dbc#namelang)             | Assumed zhCN                                                             |
| 8      | Name_7            | string | [Name_Lang_enTW](totemcategory_dbc#namelang)             | Assumed enTW, not used in 3.3.5a                                         |
| 9      | Name_8            | string | [Name_Lang_zhTW](totemcategory_dbc#namelang)             | Assumed zhTW                                                             |
| 10     | Name_9            | string | [Name_Lang_esES](totemcategory_dbc#namelang)             | Assumed esES                                                             |
| 11     | Name_10           | string | [Name_Lang_esMX](totemcategory_dbc#namelang)             | Assumed esMX                                                             |
| 12     | Name_11           | string | [Name_Lang_ruRU](totemcategory_dbc#namelang)             | Assumed ruRU                                                             |
| 13     | Name_12           | string | [Name_Lang_ptPT](totemcategory_dbc#namelang)             | Assumed ptPT, not used in 3.3.5a                                         |
| 14     | Name_13           | string | [Name_Lang_ptBR](totemcategory_dbc#namelang)             | Assumed ptBR, not used in 3.3.5a                                         |
| 15     | Name_14           | string | [Name_Lang_itIT](totemcategory_dbc#namelang)             | Assumed itIT, not used in 3.3.5a                                         |
| 16     | Name_15           | string | [Name_Lang_Unk](totemcategory_dbc#namelang)              | Unknown language, unsure of the usage in 3.3.5a                          |
| 17     | Name_lang_mask    | uint32 | [Name_Lang_Mask](totemcategory_dbc#namelang)             | Assumed flags of the localized text                                      |
| 18     | TotemCategoryType | uint32 | [TotemCategoryType](totemcategory_dbc#totemcategorytype) | Which category the tool belongs to (1 = totems, 3 = enchanting rods etc) |
| 19     | TotemCategoryMask | uint32 | [TotemCategoryMask](totemcategory_dbc#totemcategorymask) | Which tools in the category the tool can be used as.                     |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

### For instance for totems:

| Bit | Description |
| --- | ----------- |
| 0   | earth       |
| 1   | air         |
| 2   | fire        |
| 3   | water       |

Master Totem has the bitmask 1111b, meaning it can be used instead of all four normal totems.

## **Content**

<details>
<summary>Show the content of TotemCategory.dbc</summary>

| ID  | Name                     |
| --- | ------------------------ |
| 1   | Skinning Knife (OLD)     |
| 2   | Earth Totem              |
| 3   | Air Totem                |
| 4   | Fire Totem               |
| 5   | Water Totem              |
| 6   | Runed Copper Rod         |
| 7   | Runed Silver Rod         |
| 8   | Runed Golden Rod         |
| 9   | Runed Truesilver Rod     |
| 10  | Runed Arcanite Rod       |
| 11  | Mining Pick (OLD)        |
| 12  | Philosopher's Stone      |
| 13  | Blacksmith Hammer (OLD)  |
| 14  | Arclight Spanner         |
| 15  | Gyromatic Micro-Adjustor |
| 21  | Master Totem             |
| 41  | Runed Fel Iron Rod       |
| 62  | Runed Adamantite Rod     |
| 63  | Runed Eternium Rod       |
| 81  | Hollow Quill             |
| 101 | Runed Azurite Rod        |
| 121 | Virtuoso Inking Set      |
| 141 | Drums                    |
| 161 | Gnomish Army Knife       |
| 162 | Blacksmith Hammer        |
| 165 | Mining Pick              |
| 166 | Skinning Knife           |
| 167 | Hammer Pick              |
| 168 | Bladed Pickaxe           |
| 169 | Flint and Tinder         |
| 189 | Runed Cobalt Rod         |
| 190 | Runed Titanium Rod       |

</details>
