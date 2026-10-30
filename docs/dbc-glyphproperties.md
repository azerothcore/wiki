# GlyphProperties.dbc

[`Back-to:DBC`](dbc-index)

**The \`GlyphProperties.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [glyphproperties_dbc](glyphproperties_dbc) table of the world database.

**Structure**

| Column | Field          | Type   | glyphproperties\_dbc column                          | Comment                              |
| :----: | :------------- | :----- | :--------------------------------------------------- | :----------------------------------- |
| 0      | ID             | uint32 | [ID](glyphproperties_dbc#id)                         |                                      |
| 1      | SpellID        | uint32 | [SpellID](glyphproperties_dbc#spellid)               | ID in [Spell.dbc](spell)             |
| 2      | GlyphSlotFlags | uint32 | [GlyphSlotFlags](glyphproperties_dbc#glyphslotflags) |                                      |
| 3      | SpellIconID    | uint32 | [SpellIconID](glyphproperties_dbc#spelliconid)       | ID in [SpellIcon.dbc](dbc-spellicon) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/GlyphProperties).
