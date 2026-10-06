# SheatheSoundLookups.dbc

[`Back-to:DBC`](dbc-index)

**The \`SheatheSoundLookups.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field            | Type   | Comment                                    |
| :----: | :--------------- | :----- | :----------------------------------------- |
| 0      | ID               | uint32 |                                            |
| 1      | ClassID          | uint32 | ID in [ItemSubClass.dbc](dbc-itemsubclass) |
| 2      | SubClassID       | uint32 | ID in [ItemSubClass.dbc](dbc-itemsubclass) |
| 3      | MaterialID       | uint32 | ID in [Material.dbc](dbc-material)         |
| 4      | CheckMaterial    | uint32 |                                            |
| 5      | SheatheSoundID   | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) |
| 6      | UnsheatheSoundID | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SheatheSoundLookups).
