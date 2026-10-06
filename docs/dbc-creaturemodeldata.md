# CreatureModelData.dbc

[`Back-to:DBC`](dbc-index)

**The \`CreatureModelData.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [creaturemodeldata_dbc](creaturemodeldata_dbc) table of the world database.

**Structure**

| Column | Field                  | Type   | creaturemodeldata\_dbc column                                          | Comment                                                                                                    |
| :----: | :--------------------- | :----- | :--------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| 0      | ID                     | uint32 | [ID](creaturemodeldata_dbc#id)                                         |                                                                                                            |
| 1      | Flags                  | uint32 | [Flags](creaturemodeldata_dbc#flags)                                   |                                                                                                            |
| 2      | ModelName              | string | [ModelName](creaturemodeldata_dbc#modelname)                           |                                                                                                            |
| 3      | SizeClass              | uint32 | [SizeClass](creaturemodeldata_dbc#sizeclass)                           |                                                                                                            |
| 4      | ModelScale             | float  | [ModelScale](creaturemodeldata_dbc#modelscale)                         |                                                                                                            |
| 5      | BloodID                | int32  | [BloodID](creaturemodeldata_dbc#bloodid)                               | ID in [UnitBloodLevels.dbc](dbc-unitbloodlevels)                                                           |
| 6      | FootprintTextureID     | int32  | [FootprintTextureID](creaturemodeldata_dbc#footprinttextureid)         | ID in [FootprintTextures.dbc](dbc-footprinttextures)                                                       |
| 7      | FootprintTextureLength | float  | [FootprintTextureLength](creaturemodeldata_dbc#footprinttexturelength) |                                                                                                            |
| 8      | FootprintTextureWidth  | float  | [FootprintTextureWidth](creaturemodeldata_dbc#footprinttexturewidth)   |                                                                                                            |
| 9      | FootprintParticleScale | float  | [FootprintParticleScale](creaturemodeldata_dbc#footprintparticlescale) |                                                                                                            |
| 10     | FoleyMaterialID        | uint32 | [FoleyMaterialID](creaturemodeldata_dbc#foleymaterialid)               |                                                                                                            |
| 11     | FootstepShakeSize      | uint32 | [FootstepShakeSize](creaturemodeldata_dbc#footstepshakesize)           |                                                                                                            |
| 12     | DeathThudShakeSize     | uint32 | [DeathThudShakeSize](creaturemodeldata_dbc#deaththudshakesize)         |                                                                                                            |
| 13     | SoundID                | uint32 | [SoundID](creaturemodeldata_dbc#soundid)                               | ID in [CreatureSoundData.dbc](dbc-creaturesounddata) (2 of the 1023 values used here are not in that file) |
| 14     | CollisionWidth         | float  | [CollisionWidth](creaturemodeldata_dbc#collisionwidth)                 |                                                                                                            |
| 15     | CollisionHeight        | float  | [CollisionHeight](creaturemodeldata_dbc#collisionheight)               |                                                                                                            |
| 16     | MountHeight            | float  | [MountHeight](creaturemodeldata_dbc#mountheight)                       |                                                                                                            |
| 17     | GeoBoxMin_X            | float  | [GeoBoxMinX](creaturemodeldata_dbc#geoboxminx)                         |                                                                                                            |
| 18     | GeoBoxMin_Y            | float  | [GeoBoxMinY](creaturemodeldata_dbc#geoboxminy)                         |                                                                                                            |
| 19     | GeoBoxMin_Z            | float  | [GeoBoxMinZ](creaturemodeldata_dbc#geoboxminz)                         |                                                                                                            |
| 20     | GeoBoxMax_X            | float  | [GeoBoxMaxX](creaturemodeldata_dbc#geoboxmaxx)                         |                                                                                                            |
| 21     | GeoBoxMax_Y            | float  | [GeoBoxMaxY](creaturemodeldata_dbc#geoboxmaxy)                         |                                                                                                            |
| 22     | GeoBoxMax_Z            | float  | [GeoBoxMaxZ](creaturemodeldata_dbc#geoboxmaxz)                         |                                                                                                            |
| 23     | WorldEffectScale       | float  | [WorldEffectScale](creaturemodeldata_dbc#worldeffectscale)             |                                                                                                            |
| 24     | AttachedEffectScale    | float  | [AttachedEffectScale](creaturemodeldata_dbc#attachedeffectscale)       |                                                                                                            |
| 25     | MissileCollisionRadius | float  | [MissileCollisionRadius](creaturemodeldata_dbc#missilecollisionradius) |                                                                                                            |
| 26     | MissileCollisionPush   | float  | [MissileCollisionPush](creaturemodeldata_dbc#missilecollisionpush)     |                                                                                                            |
| 27     | MissileCollisionRaise  | float  | [MissileCollisionRaise](creaturemodeldata_dbc#missilecollisionraise)   |                                                                                                            |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/CreatureModelData).
