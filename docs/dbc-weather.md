# Weather.dbc

[`Back-to:DBC`](dbc-index)

**The \`Weather.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field            | Type   | Comment                                    |
| :----: | :--------------- | :----- | :----------------------------------------- |
| 0      | ID               | uint32 |                                            |
| 1      | AmbienceSoundID  | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) |
| 2      | EffectType       | uint32 |                                            |
| 3      | TransitionSkyBox | float  |                                            |
| 4      | EffectColor_R    | float  |                                            |
| 5      | EffectColor_G    | float  |                                            |
| 6      | EffectColor_B    | float  |                                            |
| 7      | EffectTexture    | string |                                            |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/Weather).
