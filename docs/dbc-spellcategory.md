# SpellCategory.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellCategory.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [spellcategory_dbc](spellcategory_dbc) table of the world database.

**Structure**

| Column | Field | Type   | spellcategory\_dbc column        | Comment |
| :----: | :---- | :----- | :------------------------------- | :------ |
| 0      | ID    | uint32 | [ID](spellcategory_dbc#id)       |         |
| 1      | Flags | uint32 | [Flags](spellcategory_dbc#flags) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellCategory).
