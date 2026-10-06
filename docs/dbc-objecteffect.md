# ObjectEffect.dbc

[`Back-to:DBC`](dbc-index)

**The \`ObjectEffect.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                  | Type   | Comment                                                    |
| :----: | :--------------------- | :----- | :--------------------------------------------------------- |
| 0      | ID                     | uint32 |                                                            |
| 1      | Name                   | string |                                                            |
| 2      | ObjectEffectGroupID    | uint32 | ID in [ObjectEffectGroup.dbc](dbc-objecteffectgroup)       |
| 3      | TriggerType            | uint32 |                                                            |
| 4      | EventType              | uint32 |                                                            |
| 5      | EffectRecType          | uint32 |                                                            |
| 6      | SoundKitID             | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                 |
| 7      | Attachment             | uint32 |                                                            |
| 8      | Offset_X               | float  |                                                            |
| 9      | Offset_Y               | float  |                                                            |
| 10     | Offset_Z               | float  |                                                            |
| 11     | ObjectEffectModifierID | uint32 | ID in [ObjectEffectModifier.dbc](dbc-objecteffectmodifier) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ObjectEffect).
