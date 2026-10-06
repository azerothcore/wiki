# SpellVisualKitModelAttach.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellVisualKitModelAttach.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                   | Type   | Comment                                                      |
| :----: | :---------------------- | :----- | :----------------------------------------------------------- |
| 0      | ID                      | uint32 |                                                              |
| 1      | ParentSpellVisualKitID  | uint32 | ID in [SpellVisualKit.dbc](dbc-spellvisualkit)               |
| 2      | SpellVisualEffectNameID | uint32 | ID in [SpellVisualEffectName.dbc](dbc-spellvisualeffectname) |
| 3      | AttachmentID            | int32  |                                                              |
| 4      | Offset_X                | float  |                                                              |
| 5      | Offset_Y                | float  |                                                              |
| 6      | Offset_Z                | float  |                                                              |
| 7      | Yaw                     | float  |                                                              |
| 8      | Pitch                   | float  |                                                              |
| 9      | Roll                    | float  |                                                              |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellVisualKitModelAttach).
