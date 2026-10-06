# LiquidType.dbc

[`Back-to:DBC`](dbc-index)

**The \`LiquidType.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [liquidtype_dbc](liquidtype_dbc) table of the world database.

**Structure**

| Column | Field              | Type   | liquidtype\_dbc column                                  | Comment                                        |
| :----: | :----------------- | :----- | :------------------------------------------------------ | :--------------------------------------------- |
| 0      | ID                 | uint32 | [ID](liquidtype_dbc#id)                                 |                                                |
| 1      | Name               | string | [Name](liquidtype_dbc#name)                             |                                                |
| 2      | Flags              | uint32 | [Flags](liquidtype_dbc#flags)                           |                                                |
| 3      | SoundBank          | uint32 | [Type](liquidtype_dbc#type)                             |                                                |
| 4      | SoundID            | uint32 | [SoundID](liquidtype_dbc#soundid)                       | ID in [SoundEntries.dbc](dbc-soundentries)     |
| 5      | SpellID            | uint32 | [SpellID](liquidtype_dbc#spellid)                       |                                                |
| 6      | MaxDarkenDepth     | float  | [MaxDarkenDepth](liquidtype_dbc#maxdarkendepth)         |                                                |
| 7      | FogDarkenIntensity | float  | [FogDarkenintensity](liquidtype_dbc#fogdarkenintensity) |                                                |
| 8      | AmbDarkenIntensity | float  | [AmbDarkenintensity](liquidtype_dbc#ambdarkenintensity) |                                                |
| 9      | DirDarkenIntensity | float  | [DirDarkenintensity](liquidtype_dbc#dirdarkenintensity) |                                                |
| 10     | LightID            | uint32 | [LightID](liquidtype_dbc#lightid)                       | ID in [Light.dbc](dbc-light)                   |
| 11     | ParticleScale      | float  | [ParticleScale](liquidtype_dbc#particlescale)           |                                                |
| 12     | ParticleMovement   | uint32 | [ParticleMovement](liquidtype_dbc#particlemovement)     |                                                |
| 13     | ParticleTexSlots   | uint32 | [ParticleTexSlots](liquidtype_dbc#particletexslots)     |                                                |
| 14     | MaterialID         | uint32 | [MaterialID](liquidtype_dbc#materialid)                 | ID in [LiquidMaterial.dbc](dbc-liquidmaterial) |
| 15     | Texture_0          | string | [Texture_1](liquidtype_dbc#texture)                     |                                                |
| 16     | Texture_1          | string | [Texture_2](liquidtype_dbc#texture)                     |                                                |
| 17     | Texture_2          | string | [Texture_3](liquidtype_dbc#texture)                     |                                                |
| 18     | Texture_3          | string | [Texture_4](liquidtype_dbc#texture)                     |                                                |
| 19     | Texture_4          | string | [Texture_5](liquidtype_dbc#texture)                     |                                                |
| 20     | Texture_5          | string | [Texture_6](liquidtype_dbc#texture)                     |                                                |
| 21     | Color_0            | uint32 | [Color_1](liquidtype_dbc#color)                         |                                                |
| 22     | Color_1            | uint32 | [Color_2](liquidtype_dbc#color)                         |                                                |
| 23     | Unk1_0             | float  | [Float_1](liquidtype_dbc#float)                         |                                                |
| 24     | Unk1_1             | float  | [Float_2](liquidtype_dbc#float)                         |                                                |
| 25     | Unk1_2             | float  | [Float_3](liquidtype_dbc#float)                         |                                                |
| 26     | Unk1_3             | float  | [Float_4](liquidtype_dbc#float)                         |                                                |
| 27     | Unk1_4             | float  | [Float_5](liquidtype_dbc#float)                         |                                                |
| 28     | Unk1_5             | float  | [Float_6](liquidtype_dbc#float)                         |                                                |
| 29     | Unk1_6             | float  | [Float_7](liquidtype_dbc#float)                         |                                                |
| 30     | Unk1_7             | float  | [Float_8](liquidtype_dbc#float)                         |                                                |
| 31     | Unk1_8             | float  | [Float_9](liquidtype_dbc#float)                         |                                                |
| 32     | Unk1_9             | float  | [Float_10](liquidtype_dbc#float)                        |                                                |
| 33     | Unk1_10            | float  | [Float_11](liquidtype_dbc#float)                        |                                                |
| 34     | Unk1_11            | float  | [Float_12](liquidtype_dbc#float)                        |                                                |
| 35     | Unk1_12            | float  | [Float_13](liquidtype_dbc#float)                        |                                                |
| 36     | Unk1_13            | float  | [Float_14](liquidtype_dbc#float)                        |                                                |
| 37     | Unk1_14            | float  | [Float_15](liquidtype_dbc#float)                        |                                                |
| 38     | Unk1_15            | float  | [Float_16](liquidtype_dbc#float)                        |                                                |
| 39     | Unk1_16            | float  | [Float_17](liquidtype_dbc#float)                        |                                                |
| 40     | Unk1_17            | float  | [Float_18](liquidtype_dbc#float)                        |                                                |
| 41     | Unk2_0             | uint32 | [Int_1](liquidtype_dbc#int)                             |                                                |
| 42     | Unk2_1             | uint32 | [Int_2](liquidtype_dbc#int)                             |                                                |
| 43     | Unk2_2             | uint32 | [Int_3](liquidtype_dbc#int)                             |                                                |
| 44     | Unk2_3             | uint32 | [Int_4](liquidtype_dbc#int)                             |                                                |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/LiquidType).
