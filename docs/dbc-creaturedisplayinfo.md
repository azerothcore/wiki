# CreatureDisplayInfo.dbc

[`Back-to:DBC`](dbc-index)

**The \`CreatureDisplayInfo.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [creaturedisplayinfo_dbc](creaturedisplayinfo_dbc) table of the world database.

**Structure**

| Column | Field                 | Type   | creaturedisplayinfo\_dbc column                                        | Comment |
| :----: | :-------------------- | :----- | :--------------------------------------------------------------------- | :------ |
| 0      | ID                    | uint32 | [ID](creaturedisplayinfo_dbc#id)                                       |         |
| 1      | ModelID               | uint32 | [ModelID](creaturedisplayinfo_dbc#modelid)                             |         |
| 2      | SoundID               | uint32 | [SoundID](creaturedisplayinfo_dbc#soundid)                             |         |
| 3      | ExtendedDisplayInfoID | uint32 | [ExtendedDisplayInfoID](creaturedisplayinfo_dbc#extendeddisplayinfoid) |         |
| 4      | CreatureModelScale    | float  | [CreatureModelScale](creaturedisplayinfo_dbc#creaturemodelscale)       |         |
| 5      | CreatureModelAlpha    | uint32 | [CreatureModelAlpha](creaturedisplayinfo_dbc#creaturemodelalpha)       |         |
| 6      | TextureVariation_0    | string | [TextureVariation_1](creaturedisplayinfo_dbc#texturevariation)         |         |
| 7      | TextureVariation_1    | string | [TextureVariation_2](creaturedisplayinfo_dbc#texturevariation)         |         |
| 8      | TextureVariation_2    | string | [TextureVariation_3](creaturedisplayinfo_dbc#texturevariation)         |         |
| 9      | PortraitTextureName   | string | [PortraitTextureName](creaturedisplayinfo_dbc#portraittexturename)     |         |
| 10     | SizeClass             | uint32 | [BloodLevel](creaturedisplayinfo_dbc#bloodlevel)                       |         |
| 11     | BloodID               | uint32 | [BloodID](creaturedisplayinfo_dbc#bloodid)                             |         |
| 12     | NPCSoundID            | uint32 | [NPCSoundID](creaturedisplayinfo_dbc#npcsoundid)                       |         |
| 13     | ParticleColorID       | uint32 | [ParticleColorID](creaturedisplayinfo_dbc#particlecolorid)             |         |
| 14     | CreatureGeosetData    | uint32 | [CreatureGeosetData](creaturedisplayinfo_dbc#creaturegeosetdata)       |         |
| 15     | ObjectEffectPackageID | uint32 | [ObjectEffectPackageID](creaturedisplayinfo_dbc#objecteffectpackageid) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/CreatureDisplayInfo).
