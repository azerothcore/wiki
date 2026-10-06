# SpellVisual.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellVisual.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [spellvisual_dbc](spellvisual_dbc) table of the world database.

**Structure**

| Column | Field                        | Type   | spellvisual\_dbc column                                                      | Comment                                                                                                           |
| :----: | :--------------------------- | :----- | :--------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- |
| 0      | ID                           | uint32 | [ID](spellvisual_dbc#id)                                                     |                                                                                                                   |
| 1      | PrecastKit                   | uint32 | [PrecastKit](spellvisual_dbc#precastkit)                                     | ID in [SpellVisualKit.dbc](dbc-spellvisualkit) (2 of the 740 values used here are not in that file)               |
| 2      | CastKit                      | uint32 | [CastKit](spellvisual_dbc#castkit)                                           | ID in [SpellVisualKit.dbc](dbc-spellvisualkit)                                                                    |
| 3      | ImpactKit                    | uint32 | [ImpactKit](spellvisual_dbc#impactkit)                                       | ID in [SpellVisualKit.dbc](dbc-spellvisualkit) (1 of the 1362 values used here are not in that file)              |
| 4      | StateKit                     | uint32 | [StateKit](spellvisual_dbc#statekit)                                         | ID in [SpellVisualKit.dbc](dbc-spellvisualkit)                                                                    |
| 5      | StateDoneKit                 | uint32 | [StateDoneKit](spellvisual_dbc#statedonekit)                                 | ID in [SpellVisualKit.dbc](dbc-spellvisualkit)                                                                    |
| 6      | ChannelKit                   | uint32 | [ChannelKit](spellvisual_dbc#channelkit)                                     | ID in [SpellVisualKit.dbc](dbc-spellvisualkit)                                                                    |
| 7      | HasMissile                   | uint32 | [HasMissile](spellvisual_dbc#hasmissile)                                     |                                                                                                                   |
| 8      | MissileModel                 | int32  | [MissileModel](spellvisual_dbc#missilemodel)                                 | ID in [SpellVisualEffectName.dbc](dbc-spellvisualeffectname) (6 of the 623 values used here are not in that file) |
| 9      | MissilePathType              | uint32 | [MissilePathType](spellvisual_dbc#missilepathtype)                           |                                                                                                                   |
| 10     | MissileDestinationAttachment | uint32 | [MissileDestinationAttachment](spellvisual_dbc#missiledestinationattachment) |                                                                                                                   |
| 11     | MissileSound                 | uint32 | [MissileSound](spellvisual_dbc#missilesound)                                 | ID in [SoundEntries.dbc](dbc-soundentries)                                                                        |
| 12     | AnimEventSoundID             | uint32 | [AnimEventSoundID](spellvisual_dbc#animeventsoundid)                         | ID in [SoundEntries.dbc](dbc-soundentries)                                                                        |
| 13     | Flags                        | uint32 | [Flags](spellvisual_dbc#flags)                                               |                                                                                                                   |
| 14     | CasterImpactKit              | uint32 | [CasterImpactKit](spellvisual_dbc#casterimpactkit)                           | ID in [SpellVisualKit.dbc](dbc-spellvisualkit)                                                                    |
| 15     | TargetImpactKit              | uint32 | [TargetImpactKit](spellvisual_dbc#targetimpactkit)                           | ID in [SpellVisualKit.dbc](dbc-spellvisualkit)                                                                    |
| 16     | MissileAttachment            | int32  | [MissileAttachment](spellvisual_dbc#missileattachment)                       |                                                                                                                   |
| 17     | MissileFollowGroundHeight    | uint32 | [MissileFollowGroundHeight](spellvisual_dbc#missilefollowgroundheight)       |                                                                                                                   |
| 18     | MissileFollowGroundDropSpeed | uint32 | [MissileFollowGroundDropSpeed](spellvisual_dbc#missilefollowgrounddropspeed) |                                                                                                                   |
| 19     | MissileFollowGroundApproach  | uint32 | [MissileFollowGroundApproach](spellvisual_dbc#missilefollowgroundapproach)   |                                                                                                                   |
| 20     | MissileFollowGroundFlags     | uint32 | [MissileFollowGroundFlags](spellvisual_dbc#missilefollowgroundflags)         |                                                                                                                   |
| 21     | MissileMotion                | uint32 | [MissileMotion](spellvisual_dbc#missilemotion)                               |                                                                                                                   |
| 22     | MissileTargetingKit          | uint32 | [MissileTargetingKit](spellvisual_dbc#missiletargetingkit)                   | ID in [SpellVisualKit.dbc](dbc-spellvisualkit)                                                                    |
| 23     | InstantAreaKit               | uint32 | [InstantAreaKit](spellvisual_dbc#instantareakit)                             | ID in [SpellVisualKit.dbc](dbc-spellvisualkit)                                                                    |
| 24     | ImpactAreaKit                | uint32 | [ImpactAreaKit](spellvisual_dbc#impactareakit)                               | ID in [SpellVisualKit.dbc](dbc-spellvisualkit)                                                                    |
| 25     | PersistentAreaKit            | uint32 | [PersistentAreaKit](spellvisual_dbc#persistentareakit)                       | ID in [SpellVisualKit.dbc](dbc-spellvisualkit)                                                                    |
| 26     | MissileCastOffset_X          | float  | [MissileCastOffsetX](spellvisual_dbc#missilecastoffsetx)                     |                                                                                                                   |
| 27     | MissileCastOffset_Y          | float  | [MissileCastOffsetY](spellvisual_dbc#missilecastoffsety)                     |                                                                                                                   |
| 28     | MissileCastOffset_Z          | float  | [MissileCastOffsetZ](spellvisual_dbc#missilecastoffsetz)                     |                                                                                                                   |
| 29     | MissileImpactOffset_X        | float  | [MissileImpactOffsetX](spellvisual_dbc#missileimpactoffsetx)                 |                                                                                                                   |
| 30     | MissileImpactOffset_Y        | float  | [MissileImpactOffsetY](spellvisual_dbc#missileimpactoffsety)                 |                                                                                                                   |
| 31     | MissileImpactOffset_Z        | float  | [MissileImpactOffsetZ](spellvisual_dbc#missileimpactoffsetz)                 |                                                                                                                   |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellVisual).
