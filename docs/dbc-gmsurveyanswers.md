# GMSurveyAnswers.dbc

[`Back-to:DBC`](dbc-index)

**The \`GMSurveyAnswers.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field              | Type   | Comment                                              |
| :----: | :----------------- | :----- | :--------------------------------------------------- |
| 0      | ID                 | uint32 |                                                      |
| 1      | Sort_Index         | uint32 |                                                      |
| 2      | GMSurveyQuestionID | uint32 | ID in [GMSurveyQuestions.dbc](dbc-gmsurveyquestions) |
| 3      | Answer_0           | string | Assumed enUS                                         |
| 4      | Answer_1           | string | Assumed enGB, not used in 3.3.5a                     |
| 5      | Answer_2           | string | Assumed koKR                                         |
| 6      | Answer_3           | string | Assumed frFR                                         |
| 7      | Answer_4           | string | Assumed deDE                                         |
| 8      | Answer_5           | string | Assumed enCN, not used in 3.3.5a                     |
| 9      | Answer_6           | string | Assumed zhCN                                         |
| 10     | Answer_7           | string | Assumed enTW, not used in 3.3.5a                     |
| 11     | Answer_8           | string | Assumed zhTW                                         |
| 12     | Answer_9           | string | Assumed esES                                         |
| 13     | Answer_10          | string | Assumed esMX                                         |
| 14     | Answer_11          | string | Assumed ruRU                                         |
| 15     | Answer_12          | string | Assumed ptPT, not used in 3.3.5a                     |
| 16     | Answer_13          | string | Assumed ptBR, not used in 3.3.5a                     |
| 17     | Answer_14          | string | Assumed itIT, not used in 3.3.5a                     |
| 18     | Answer_15          | string | Unknown language, unsure of the usage in 3.3.5a      |
| 19     | Answer_lang_mask   | uint32 | Assumed flags of the localized text                  |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/GMSurveyAnswers).
