# SpellRuneCost.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellRuneCost.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [spellrunecost_dbc](spellrunecost_dbc) table of the world database.

**Structure**

| Column | Field      | Type   | spellrunecost\_dbc column                  | Comment |
| :----: | :--------- | :----- | :----------------------------------------- | :------ |
| 0      | ID         | uint32 | [ID](spellrunecost_dbc#id)                 |         |
| 1      | RuneCost_0 | uint32 | [Blood](spellrunecost_dbc#blood)           |         |
| 2      | RuneCost_1 | uint32 | [Unholy](spellrunecost_dbc#unholy)         |         |
| 3      | RuneCost_2 | uint32 | [Frost](spellrunecost_dbc#frost)           |         |
| 4      | RunicPower | uint32 | [RunicPower](spellrunecost_dbc#runicpower) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellRuneCost).
