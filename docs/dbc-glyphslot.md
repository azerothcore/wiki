# GlyphSlot.dbc

[`Back-to:DBC`](dbc-index)

**The \`GlyphSlot.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [glyphslot_dbc](glyphslot_dbc) table of the world database.

**Structure**

| Column | Field   | Type   | glyphslot\_dbc column            | Comment |
| :----: | :------ | :----- | :------------------------------- | :------ |
| 0      | ID      | uint32 | [ID](glyphslot_dbc#id)           |         |
| 1      | Type    | uint32 | [Type](glyphslot_dbc#type)       |         |
| 2      | Tooltip | uint32 | [Tooltip](glyphslot_dbc#tooltip) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/GlyphSlot).
