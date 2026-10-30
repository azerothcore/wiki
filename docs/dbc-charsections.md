# CharSections.dbc

[`Back-to:DBC`](dbc-index)

**The \`CharSections.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [charsections_dbc](charsections_dbc) table of the world database.

**Structure**

| Column | Field          | Type   | charsections\_dbc column                                                 | Comment                        |
| :----: | :------------- | :----- | :----------------------------------------------------------------------- | :----------------------------- |
| 0      | ID             | uint32 | [ID](charsections_dbc#id)                                                |                                |
| 1      | RaceID         | uint32 | [RaceID](charsections_dbc#raceid)                                        | ID in [ChrRaces.dbc](chrraces) |
| 2      | SexID          | uint32 | [SexID](charsections_dbc#sexid)                                          |                                |
| 3      | BaseSection    | uint32 | [BaseSection](charsections_dbc#basesection)                              |                                |
| 4      | TextureName_0  | string | [TextureName_1](charsections_dbc#texturename1-texturename2-texturename3) |                                |
| 5      | TextureName_1  | string | [TextureName_2](charsections_dbc#texturename1-texturename2-texturename3) |                                |
| 6      | TextureName_2  | string | [TextureName_3](charsections_dbc#texturename1-texturename2-texturename3) |                                |
| 7      | Flags          | uint32 | [Flags](charsections_dbc#flags)                                          |                                |
| 8      | VariationIndex | uint32 | [VariationIndex](charsections_dbc#variationindex)                        |                                |
| 9      | ColorIndex     | uint32 | [ColorIndex](charsections_dbc#colorindex)                                |                                |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/CharSections).
