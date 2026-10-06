# CreatureFamily.dbc

[`Back-to:DBC`](dbc-index)

**The \`CreatureFamily.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [creaturefamily_dbc](creaturefamily_dbc) table of the world database.

**Structure**

| Column | Field          | Type   | creaturefamily\_dbc column                          | Comment                                                                          |
| :----: | :------------- | :----- | :-------------------------------------------------- | :------------------------------------------------------------------------------- |
| 0      | ID             | uint32 | [ID](creaturefamily_dbc#id)                         |                                                                                  |
| 1      | MinScale       | float  | [MinScale](creaturefamily_dbc#minscale)             |                                                                                  |
| 2      | MinScaleLevel  | uint32 | [MinScaleLevel](creaturefamily_dbc#minscalelevel)   |                                                                                  |
| 3      | MaxScale       | float  | [MaxScale](creaturefamily_dbc#maxscale)             |                                                                                  |
| 4      | MaxScaleLevel  | uint32 | [MaxScaleLevel](creaturefamily_dbc#maxscalelevel)   |                                                                                  |
| 5      | SkillLine_0    | uint32 | [SkillLine_1](creaturefamily_dbc#skillline)         | ID in [SkillLine.dbc](skillline)                                                 |
| 6      | SkillLine_1    | uint32 | [SkillLine_2](creaturefamily_dbc#skillline)         | ID in [SkillLine.dbc](skillline)                                                 |
| 7      | PetFoodMask    | uint32 | [PetFoodMask](creaturefamily_dbc#petfoodmask)       | Bitmask of pet food types (bit = ID - 1). See [ItemPetFood.dbc](dbc-itempetfood) |
| 8      | PetTalentType  | int32  | [PetTalentType](creaturefamily_dbc#pettalenttype)   |                                                                                  |
| 9      | CategoryEnumID | int32  | [CategoryEnumID](creaturefamily_dbc#categoryenumid) |                                                                                  |
| 10     | Name_0         | string | [Name_Lang_enUS](creaturefamily_dbc#namelang)       | Assumed enUS                                                                     |
| 11     | Name_1         | string | [Name_Lang_enGB](creaturefamily_dbc#namelang)       | Assumed enGB, not used in 3.3.5a                                                 |
| 12     | Name_2         | string | [Name_Lang_koKR](creaturefamily_dbc#namelang)       | Assumed koKR                                                                     |
| 13     | Name_3         | string | [Name_Lang_frFR](creaturefamily_dbc#namelang)       | Assumed frFR                                                                     |
| 14     | Name_4         | string | [Name_Lang_deDE](creaturefamily_dbc#namelang)       | Assumed deDE                                                                     |
| 15     | Name_5         | string | [Name_Lang_enCN](creaturefamily_dbc#namelang)       | Assumed enCN, not used in 3.3.5a                                                 |
| 16     | Name_6         | string | [Name_Lang_zhCN](creaturefamily_dbc#namelang)       | Assumed zhCN                                                                     |
| 17     | Name_7         | string | [Name_Lang_enTW](creaturefamily_dbc#namelang)       | Assumed enTW, not used in 3.3.5a                                                 |
| 18     | Name_8         | string | [Name_Lang_zhTW](creaturefamily_dbc#namelang)       | Assumed zhTW                                                                     |
| 19     | Name_9         | string | [Name_Lang_esES](creaturefamily_dbc#namelang)       | Assumed esES                                                                     |
| 20     | Name_10        | string | [Name_Lang_esMX](creaturefamily_dbc#namelang)       | Assumed esMX                                                                     |
| 21     | Name_11        | string | [Name_Lang_ruRU](creaturefamily_dbc#namelang)       | Assumed ruRU                                                                     |
| 22     | Name_12        | string | [Name_Lang_ptPT](creaturefamily_dbc#namelang)       | Assumed ptPT, not used in 3.3.5a                                                 |
| 23     | Name_13        | string | [Name_Lang_ptBR](creaturefamily_dbc#namelang)       | Assumed ptBR, not used in 3.3.5a                                                 |
| 24     | Name_14        | string | [Name_Lang_itIT](creaturefamily_dbc#namelang)       | Assumed itIT, not used in 3.3.5a                                                 |
| 25     | Name_15        | string | [Name_Lang_Unk](creaturefamily_dbc#namelang)        | Unknown language, unsure of the usage in 3.3.5a                                  |
| 26     | Name_lang_mask | uint32 | [Name_Lang_Mask](creaturefamily_dbc#namelang)       | Assumed flags of the localized text                                              |
| 27     | IconFile       | string | [IconFile](creaturefamily_dbc#iconfile)             |                                                                                  |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/CreatureFamily).
