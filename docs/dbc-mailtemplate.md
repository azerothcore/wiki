# MailTemplate.dbc

[`Back-to:DBC`](dbc-index)

**The \`MailTemplate.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [mailtemplate_dbc](mailtemplate_dbc) table of the world database.

**Structure**

| Column | Field             | Type   | mailtemplate\_dbc column                          | Comment                                         |
| :----: | :---------------- | :----- | :------------------------------------------------ | :---------------------------------------------- |
| 0      | ID                | uint32 | [ID](mailtemplate_dbc#id)                         |                                                 |
| 1      | Subject_0         | string | [Subject_Lang_enUS](mailtemplate_dbc#subjectlang) | Assumed enUS                                    |
| 2      | Subject_1         | string | [Subject_Lang_enGB](mailtemplate_dbc#subjectlang) | Assumed enGB, not used in 3.3.5a                |
| 3      | Subject_2         | string | [Subject_Lang_koKR](mailtemplate_dbc#subjectlang) | Assumed koKR                                    |
| 4      | Subject_3         | string | [Subject_Lang_frFR](mailtemplate_dbc#subjectlang) | Assumed frFR                                    |
| 5      | Subject_4         | string | [Subject_Lang_deDE](mailtemplate_dbc#subjectlang) | Assumed deDE                                    |
| 6      | Subject_5         | string | [Subject_Lang_enCN](mailtemplate_dbc#subjectlang) | Assumed enCN, not used in 3.3.5a                |
| 7      | Subject_6         | string | [Subject_Lang_zhCN](mailtemplate_dbc#subjectlang) | Assumed zhCN                                    |
| 8      | Subject_7         | string | [Subject_Lang_enTW](mailtemplate_dbc#subjectlang) | Assumed enTW, not used in 3.3.5a                |
| 9      | Subject_8         | string | [Subject_Lang_zhTW](mailtemplate_dbc#subjectlang) | Assumed zhTW                                    |
| 10     | Subject_9         | string | [Subject_Lang_esES](mailtemplate_dbc#subjectlang) | Assumed esES                                    |
| 11     | Subject_10        | string | [Subject_Lang_esMX](mailtemplate_dbc#subjectlang) | Assumed esMX                                    |
| 12     | Subject_11        | string | [Subject_Lang_ruRU](mailtemplate_dbc#subjectlang) | Assumed ruRU                                    |
| 13     | Subject_12        | string | [Subject_Lang_ptPT](mailtemplate_dbc#subjectlang) | Assumed ptPT, not used in 3.3.5a                |
| 14     | Subject_13        | string | [Subject_Lang_ptBR](mailtemplate_dbc#subjectlang) | Assumed ptBR, not used in 3.3.5a                |
| 15     | Subject_14        | string | [Subject_Lang_itIT](mailtemplate_dbc#subjectlang) | Assumed itIT, not used in 3.3.5a                |
| 16     | Subject_15        | string | [Subject_Lang_Unk](mailtemplate_dbc#subjectlang)  | Unknown language, unsure of the usage in 3.3.5a |
| 17     | Subject_lang_mask | uint32 | [Subject_Lang_Mask](mailtemplate_dbc#subjectlang) | Assumed flags of the localized text             |
| 18     | Body_0            | string | [Body_Lang_enUS](mailtemplate_dbc#bodylang)       | Assumed enUS                                    |
| 19     | Body_1            | string | [Body_Lang_enGB](mailtemplate_dbc#bodylang)       | Assumed enGB, not used in 3.3.5a                |
| 20     | Body_2            | string | [Body_Lang_koKR](mailtemplate_dbc#bodylang)       | Assumed koKR                                    |
| 21     | Body_3            | string | [Body_Lang_frFR](mailtemplate_dbc#bodylang)       | Assumed frFR                                    |
| 22     | Body_4            | string | [Body_Lang_deDE](mailtemplate_dbc#bodylang)       | Assumed deDE                                    |
| 23     | Body_5            | string | [Body_Lang_enCN](mailtemplate_dbc#bodylang)       | Assumed enCN, not used in 3.3.5a                |
| 24     | Body_6            | string | [Body_Lang_zhCN](mailtemplate_dbc#bodylang)       | Assumed zhCN                                    |
| 25     | Body_7            | string | [Body_Lang_enTW](mailtemplate_dbc#bodylang)       | Assumed enTW, not used in 3.3.5a                |
| 26     | Body_8            | string | [Body_Lang_zhTW](mailtemplate_dbc#bodylang)       | Assumed zhTW                                    |
| 27     | Body_9            | string | [Body_Lang_esES](mailtemplate_dbc#bodylang)       | Assumed esES                                    |
| 28     | Body_10           | string | [Body_Lang_esMX](mailtemplate_dbc#bodylang)       | Assumed esMX                                    |
| 29     | Body_11           | string | [Body_Lang_ruRU](mailtemplate_dbc#bodylang)       | Assumed ruRU                                    |
| 30     | Body_12           | string | [Body_Lang_ptPT](mailtemplate_dbc#bodylang)       | Assumed ptPT, not used in 3.3.5a                |
| 31     | Body_13           | string | [Body_Lang_ptBR](mailtemplate_dbc#bodylang)       | Assumed ptBR, not used in 3.3.5a                |
| 32     | Body_14           | string | [Body_Lang_itIT](mailtemplate_dbc#bodylang)       | Assumed itIT, not used in 3.3.5a                |
| 33     | Body_15           | string | [Body_Lang_Unk](mailtemplate_dbc#bodylang)        | Unknown language, unsure of the usage in 3.3.5a |
| 34     | Body_lang_mask    | uint32 | [Body_Lang_Mask](mailtemplate_dbc#bodylang)       | Assumed flags of the localized text             |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/MailTemplate).
