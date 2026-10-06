# SpellRadius.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellRadius.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [spellradius_dbc](spellradius_dbc) table of the world database.

**Structure**

| Column | Field          | Type   | spellradius\_dbc column                          | Comment |
| :----: | :------------- | :----- | :----------------------------------------------- | :------ |
| 0      | ID             | uint32 | [ID](spellradius_dbc#id)                         |         |
| 1      | Radius         | float  | [Radius](spellradius_dbc#radius)                 |         |
| 2      | RadiusPerLevel | float  | [RadiusPerLevel](spellradius_dbc#radiusperlevel) |         |
| 3      | RadiusMax      | float  | [RadiusMax](spellradius_dbc#radiusmax)           |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellRadius).
