# LanguageWords.dbc

[`Back-to:DBC`](dbc-index)

**The \`LanguageWords.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field      | Type   | Comment                          |
| :----: | :--------- | :----- | :------------------------------- |
| 0      | ID         | uint32 |                                  |
| 1      | LanguageID | uint32 | ID in [Languages.dbc](languages) |
| 2      | Word       | string |                                  |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/LanguageWords).
