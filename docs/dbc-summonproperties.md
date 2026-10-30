# SummonProperties.dbc

[`Back-to:DBC`](dbc-index)

**The \`SummonProperties.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [summonproperties_dbc](summonproperties_dbc) table of the world database.

**Structure**

| Column | Field   | Type   | summonproperties\_dbc column            | Comment                                      |
| :----: | :------ | :----- | :-------------------------------------- | :------------------------------------------- |
| 0      | ID      | uint32 | [ID](summonproperties_dbc#id)           |                                              |
| 1      | Control | uint32 | [Control](summonproperties_dbc#control) |                                              |
| 2      | Faction | uint32 | [Faction](summonproperties_dbc#faction) | ID in [FactionTemplate.dbc](factiontemplate) |
| 3      | Title   | uint32 | [Title](summonproperties_dbc#title)     |                                              |
| 4      | Slot    | uint32 | [Slot](summonproperties_dbc#slot)       |                                              |
| 5      | Flags   | uint32 | [Flags](summonproperties_dbc#flags)     |                                              |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SummonProperties).
