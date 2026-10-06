# OverrideSpellData.dbc

[`Back-to:DBC`](dbc-index)

**The \`OverrideSpellData.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [overridespelldata_dbc](overridespelldata_dbc) table of the world database.

**Structure**

| Column | Field    | Type   | overridespelldata\_dbc column             | Comment                  |
| :----: | :------- | :----- | :---------------------------------------- | :----------------------- |
| 0      | ID       | uint32 | [ID](overridespelldata_dbc#id)            |                          |
| 1      | Spells_0 | uint32 | [Spells_1](overridespelldata_dbc#spells)  | ID in [Spell.dbc](spell) |
| 2      | Spells_1 | uint32 | [Spells_2](overridespelldata_dbc#spells)  | ID in [Spell.dbc](spell) |
| 3      | Spells_2 | uint32 | [Spells_3](overridespelldata_dbc#spells)  | ID in [Spell.dbc](spell) |
| 4      | Spells_3 | uint32 | [Spells_4](overridespelldata_dbc#spells)  | ID in [Spell.dbc](spell) |
| 5      | Spells_4 | uint32 | [Spells_5](overridespelldata_dbc#spells)  |                          |
| 6      | Spells_5 | uint32 | [Spells_6](overridespelldata_dbc#spells)  | ID in [Spell.dbc](spell) |
| 7      | Spells_6 | uint32 | [Spells_7](overridespelldata_dbc#spells)  |                          |
| 8      | Spells_7 | uint32 | [Spells_8](overridespelldata_dbc#spells)  |                          |
| 9      | Spells_8 | uint32 | [Spells_9](overridespelldata_dbc#spells)  |                          |
| 10     | Spells_9 | uint32 | [Spells_10](overridespelldata_dbc#spells) |                          |
| 11     | Flags    | uint32 | [Flags](overridespelldata_dbc#flags)      |                          |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/OverrideSpellData).
