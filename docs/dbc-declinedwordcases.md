# DeclinedWordCases.dbc

[`Back-to:DBC`](dbc-index)

**The \`DeclinedWordCases.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field          | Type   | Comment                                    |
| :----: | :------------- | :----- | :----------------------------------------- |
| 0      | ID             | uint32 |                                            |
| 1      | DeclinedWordID | uint32 | ID in [DeclinedWord.dbc](dbc-declinedword) |
| 2      | CaseIndex      | uint32 |                                            |
| 3      | DeclinedWord   | string |                                            |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/DeclinedWordCases).
