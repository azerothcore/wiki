# CreatureSpellData.dbc

[`Back-to:DBC`](dbc-index)

**The \`CreatureSpellData.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [creaturespelldata_dbc](creaturespelldata_dbc) table of the world database.

**Structure**

| Column | Field          | Type   | creaturespelldata\_dbc column                        | Comment                                                                      |
| :----: | :------------- | :----- | :--------------------------------------------------- | :--------------------------------------------------------------------------- |
| 0      | ID             | uint32 | [ID](creaturespelldata_dbc#id)                       |                                                                              |
| 1      | Spells_0       | uint32 | [Spells_1](creaturespelldata_dbc#spells)             | ID in [Spell.dbc](spell) (5 of the 52 values used here are not in that file) |
| 2      | Spells_1       | uint32 | [Spells_2](creaturespelldata_dbc#spells)             | ID in [Spell.dbc](spell) (6 of the 64 values used here are not in that file) |
| 3      | Spells_2       | uint32 | [Spells_3](creaturespelldata_dbc#spells)             |                                                                              |
| 4      | Spells_3       | uint32 | [Spells_4](creaturespelldata_dbc#spells)             | ID in [Spell.dbc](spell)                                                     |
| 5      | Availability_0 | uint32 | [Availability_1](creaturespelldata_dbc#availability) |                                                                              |
| 6      | Availability_1 | uint32 | [Availability_2](creaturespelldata_dbc#availability) |                                                                              |
| 7      | Availability_2 | uint32 | [Availability_3](creaturespelldata_dbc#availability) |                                                                              |
| 8      | Availability_3 | uint32 | [Availability_4](creaturespelldata_dbc#availability) |                                                                              |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/CreatureSpellData).
