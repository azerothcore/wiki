# SpellVisualKit.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellVisualKit.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field             | Type   | Comment                                                                                                            |
| :----: | :---------------- | :----- | :----------------------------------------------------------------------------------------------------------------- |
| 0      | ID                | uint32 |                                                                                                                    |
| 1      | StartAnimID       | int32  | ID in [AnimationData.dbc](dbc-animationdata)                                                                       |
| 2      | AnimID            | int32  | ID in [AnimationData.dbc](dbc-animationdata)                                                                       |
| 3      | HeadEffect        | int32  | ID in [SpellVisualEffectName.dbc](dbc-spellvisualeffectname)                                                       |
| 4      | ChestEffect       | int32  | ID in [SpellVisualEffectName.dbc](dbc-spellvisualeffectname)                                                       |
| 5      | BaseEffect        | int32  | ID in [SpellVisualEffectName.dbc](dbc-spellvisualeffectname) (1 of the 1354 values used here are not in that file) |
| 6      | LeftHandEffect    | int32  | ID in [SpellVisualEffectName.dbc](dbc-spellvisualeffectname)                                                       |
| 7      | RightHandEffect   | int32  | ID in [SpellVisualEffectName.dbc](dbc-spellvisualeffectname) (2 of the 287 values used here are not in that file)  |
| 8      | BreathEffect      | int32  | ID in [SpellVisualEffectName.dbc](dbc-spellvisualeffectname) (1 of the 174 values used here are not in that file)  |
| 9      | LeftWeaponEffect  | int32  |                                                                                                                    |
| 10     | RightWeaponEffect | int32  |                                                                                                                    |
| 11     | SpecialEffect_0   | int32  |                                                                                                                    |
| 12     | SpecialEffect_1   | int32  |                                                                                                                    |
| 13     | SpecialEffect_2   | int32  |                                                                                                                    |
| 14     | WorldEffect       | int32  | ID in [SpellVisualEffectName.dbc](dbc-spellvisualeffectname)                                                       |
| 15     | SoundID           | int32  | ID in [SoundEntries.dbc](dbc-soundentries) (13 of the 913 values used here are not in that file)                   |
| 16     | ShakeID           | uint32 |                                                                                                                    |
| 17     | CharProc_0        | int32  |                                                                                                                    |
| 18     | CharProc_1        | int32  |                                                                                                                    |
| 19     | CharProc_2        | int32  |                                                                                                                    |
| 20     | CharProc_3        | int32  |                                                                                                                    |
| 21     | CharParamA_0      | float  |                                                                                                                    |
| 22     | CharParamA_1      | float  |                                                                                                                    |
| 23     | CharParamA_2      | float  |                                                                                                                    |
| 24     | CharParamA_3      | float  |                                                                                                                    |
| 25     | CharParamB_0      | float  |                                                                                                                    |
| 26     | CharParamB_1      | float  |                                                                                                                    |
| 27     | CharParamB_2      | float  |                                                                                                                    |
| 28     | CharParamB_3      | float  |                                                                                                                    |
| 29     | CharParamC_0      | float  |                                                                                                                    |
| 30     | CharParamC_1      | float  |                                                                                                                    |
| 31     | CharParamC_2      | float  |                                                                                                                    |
| 32     | CharParamC_3      | float  |                                                                                                                    |
| 33     | CharParamD_0      | float  |                                                                                                                    |
| 34     | CharParamD_1      | float  |                                                                                                                    |
| 35     | CharParamD_2      | float  |                                                                                                                    |
| 36     | CharParamD_3      | float  |                                                                                                                    |
| 37     | Flags             | uint32 |                                                                                                                    |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellVisualKit).
