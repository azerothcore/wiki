# NamesProfanity.dbc

[`Back-to:DBC`](dbc-index)

**The \`NamesProfanity.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [namesprofanity_dbc](namesprofanity_dbc) table of the world database.

**Structure**

| Column | Field    | Type   | namesprofanity\_dbc column                    | Comment |
| :----: | :------- | :----- | :-------------------------------------------- | :------ |
| 0      | ID       | uint32 | [ID](namesprofanity_dbc#id)                   |         |
| 1      | Name     | string | [Pattern](namesprofanity_dbc#pattern)         |         |
| 2      | Language | int32  | [LanguagueID](namesprofanity_dbc#languagueid) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/NamesProfanity).
