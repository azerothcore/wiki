# CreatureSoundData.dbc

[`Back-to:DBC`](dbc-index)

**The \`CreatureSoundData.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                     | Type   | Comment                                                                                         |
| :----: | :------------------------ | :----- | :---------------------------------------------------------------------------------------------- |
| 0      | ID                        | uint32 |                                                                                                 |
| 1      | SoundExertionID           | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 2      | SoundExertionCriticalID   | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 3      | SoundInjuryID             | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 4      | SoundInjuryCriticalID     | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 5      | SoundInjuryCrushingBlowID | uint32 |                                                                                                 |
| 6      | SoundDeathID              | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) (1 of the 343 values used here are not in that file) |
| 7      | SoundStunID               | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 8      | SoundStandID              | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 9      | SoundFootstepID           | uint32 |                                                                                                 |
| 10     | SoundAggroID              | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 11     | SoundWingFlapID           | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 12     | SoundWingGlideID          | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 13     | SoundAlertID              | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) (1 of the 241 values used here are not in that file) |
| 14     | SoundFidget_0             | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 15     | SoundFidget_1             | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 16     | SoundFidget_2             | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 17     | SoundFidget_3             | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 18     | SoundFidget_4             | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 19     | CustomAttack_0            | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 20     | CustomAttack_1            | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 21     | CustomAttack_2            | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 22     | CustomAttack_3            | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 23     | NPCSoundID                | uint32 |                                                                                                 |
| 24     | LoopSoundID               | uint32 | ID in [SoundEntries.dbc](dbc-soundentries) (1 of the 76 values used here are not in that file)  |
| 25     | CreatureImpactType        | uint32 |                                                                                                 |
| 26     | SoundJumpStartID          | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 27     | SoundJumpEndID            | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 28     | SoundPetAttackID          | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 29     | SoundPetOrderID           | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 30     | SoundPetDismissID         | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 31     | FidgetDelaySecondsMin     | float  |                                                                                                 |
| 32     | FidgetDelaySecondsMax     | float  |                                                                                                 |
| 33     | BirthSoundID              | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 34     | SpellCastDirectedSoundID  | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 35     | SubmergeSoundID           | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 36     | SubmergedSoundID          | uint32 | ID in [SoundEntries.dbc](dbc-soundentries)                                                      |
| 37     | CreatureSoundDataIDPet    | uint32 |                                                                                                 |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/CreatureSoundData).
