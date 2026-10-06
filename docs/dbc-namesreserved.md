# NamesReserved.dbc

[`Back-to:DBC`](dbc-index)

**The \`NamesReserved.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [namesreserved_dbc](namesreserved_dbc) table of the world database.

**Structure**

| Column | Field    | Type   | namesreserved\_dbc column                    | Comment |
| :----: | :------- | :----- | :------------------------------------------- | :------ |
| 0      | ID       | uint32 | [ID](namesreserved_dbc#id)                   |         |
| 1      | Name     | string | [Pattern](namesreserved_dbc#pattern)         |         |
| 2      | Language | int32  | [LanguagueID](namesreserved_dbc#languagueid) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/NamesReserved).
