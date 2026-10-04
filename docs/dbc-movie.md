# Movie.dbc

[`Back-to:DBC`](dbc-index)

**The \`Movie.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [movie_dbc](movie_dbc) table of the world database.

**Structure**

| Column | Field    | Type   | movie\_dbc column              | Comment |
| :----: | :------- | :----- | :----------------------------- | :------ |
| 0      | ID       | uint32 | [ID](movie_dbc#id)             |         |
| 1      | Filename | string | [Filename](movie_dbc#filename) |         |
| 2      | Volume   | uint32 | [Volume](movie_dbc#volume)     |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/Movie).
