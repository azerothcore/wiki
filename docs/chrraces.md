# ChrRaces.dbc

[`Back-to:DBC`](dbc-index)

This DBC contains all possible races, some of which are unused and unavailable to players.

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)  

**Table Structure**

| Column | Field                     | Type   | chrraces\_dbc column                                              | Comment                                                                                                                                       |
| :----: | :------------------------ | :----- | :---------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| 0      | ID                        | uint32 | [ID](chrraces_dbc#id)                                             |                                                                                                                                               |
| 1      | Flags                     | uint32 | [Flags](chrraces_dbc#flags)                                       | [Flags](#flags)                                                                                                                               |
| 2      | FactionID                 | uint32 | [FactionID](chrraces_dbc#factionid)                               | Faction template ID. The order in the creation screen depends on this. ID in [FactionTemplate.dbc](factiontemplate)                           |
| 3      | ExplorationSoundID        | uint32 | [ExplorationSoundID](chrraces_dbc#explorationsoundid)             | Played on exploring zones with SMSG_EXPLORATION_EXPERIENCE. ID in [SoundEntries.dbc](dbc-soundentries)                                        |
| 4      | MaleDisplayID             | uint32 | [MaleDisplayId](chrraces_dbc#maledisplayid)                       | Only used for the character creation/selection screen. Server sets the model ingame. ID in [CreatureDisplayInfo.dbc](dbc-creaturedisplayinfo) |
| 5      | FemaleDisplayID           | uint32 | [FemaleDisplayId](chrraces_dbc#femaledisplayid)                   | Only used for the character creation/selection screen. Server sets the model ingame. ID in [CreatureDisplayInfo.dbc](dbc-creaturedisplayinfo) |
| 6      | ClientPrefix              | string | [ClientPrefix](chrraces_dbc#clientprefix)                         | A short form of the name. Used for helmet models.                                                                                             |
| 7      | BaseLanguage              | uint32 | [BaseLanguage](chrraces_dbc#baselanguage)                         | 1 = Horde, 7 = Alliance & Not playable. ID in [Languages.dbc](languages)                                                                      |
| 8      | CreatureType              | uint32 | [CreatureType](chrraces_dbc#creaturetype)                         | Always 7 (Humanoid). ID in [CreatureType.dbc](dbc-creaturetype)                                                                               |
| 9      | ResSicknessSpellID        | uint32 | [ResSicknessSpellID](chrraces_dbc#ressicknessspellid)             | Always 15007. ID in [Spell.dbc](spell)                                                                                                        |
| 10     | SplashSoundID             | uint32 | [SplashSoundID](chrraces_dbc#splashsoundid)                       | 1090 for dwarfs, 1096 for the others. Getting stored in CGUnit at CGUnit::PostInit. ID in [SoundEntries.dbc](dbc-soundentries)                |
| 11     | ClientFileString          | string | [ClientFilestring](chrraces_dbc#clientfilestring)                 | Same as the one used in model filepaths.                                                                                                      |
| 12     | CinematicSequenceID       | uint32 | [CinematicSequenceID](chrraces_dbc#cinematicsequenceid)           | Used for the opening cinematic. ID in [CinematicSequences.dbc](dbc-cinematicsequences)                                                        |
| 13     | Alliance                  | uint32 | [Alliance](chrraces_dbc#alliance)                                 | Faction (0 = Alliance, 1 = Horde, 2 = Not available)                                                                                          |
| 14     | Name_0                    | string | [Name_Lang_enUS](chrraces_dbc#namelang)                           | A name to display. Assumed enUS                                                                                                               |
| 15     | Name_1                    | string | [Name_Lang_enGB](chrraces_dbc#namelang)                           | Assumed enGB, not used in 3.3.5a                                                                                                              |
| 16     | Name_2                    | string | [Name_Lang_koKR](chrraces_dbc#namelang)                           | Assumed koKR                                                                                                                                  |
| 17     | Name_3                    | string | [Name_Lang_frFR](chrraces_dbc#namelang)                           | Assumed frFR                                                                                                                                  |
| 18     | Name_4                    | string | [Name_Lang_deDE](chrraces_dbc#namelang)                           | Assumed deDE                                                                                                                                  |
| 19     | Name_5                    | string | [Name_Lang_enCN](chrraces_dbc#namelang)                           | Assumed enCN, not used in 3.3.5a                                                                                                              |
| 20     | Name_6                    | string | [Name_Lang_zhCN](chrraces_dbc#namelang)                           | Assumed zhCN                                                                                                                                  |
| 21     | Name_7                    | string | [Name_Lang_enTW](chrraces_dbc#namelang)                           | Assumed enTW, not used in 3.3.5a                                                                                                              |
| 22     | Name_8                    | string | [Name_Lang_zhTW](chrraces_dbc#namelang)                           | Assumed zhTW                                                                                                                                  |
| 23     | Name_9                    | string | [Name_Lang_esES](chrraces_dbc#namelang)                           | Assumed esES                                                                                                                                  |
| 24     | Name_10                   | string | [Name_Lang_esMX](chrraces_dbc#namelang)                           | Assumed esMX                                                                                                                                  |
| 25     | Name_11                   | string | [Name_Lang_ruRU](chrraces_dbc#namelang)                           | Assumed ruRU                                                                                                                                  |
| 26     | Name_12                   | string | [Name_Lang_ptPT](chrraces_dbc#namelang)                           | Assumed ptPT, not used in 3.3.5a                                                                                                              |
| 27     | Name_13                   | string | [Name_Lang_ptBR](chrraces_dbc#namelang)                           | Assumed ptBR, not used in 3.3.5a                                                                                                              |
| 28     | Name_14                   | string | [Name_Lang_itIT](chrraces_dbc#namelang)                           | Assumed itIT, not used in 3.3.5a                                                                                                              |
| 29     | Name_15                   | string | [Name_Lang_Unk](chrraces_dbc#namelang)                            | Unknown language, unsure of the usage in 3.3.5a                                                                                               |
| 30     | Name_lang_mask            | uint32 | [Name_Lang_Mask](chrraces_dbc#namelang)                           | String flags, unused. Assumed flags of the localized text                                                                                     |
| 31     | NameFemale_0              | string | [Name_Female_Lang_enUS](chrraces_dbc#namefemalelang)              | If different from base case, otherwise unused. Always NULL for zhCN. Assumed enUS                                                             |
| 32     | NameFemale_1              | string | [Name_Female_Lang_enGB](chrraces_dbc#namefemalelang)              | Assumed enGB, not used in 3.3.5a                                                                                                              |
| 33     | NameFemale_2              | string | [Name_Female_Lang_koKR](chrraces_dbc#namefemalelang)              | Assumed koKR                                                                                                                                  |
| 34     | NameFemale_3              | string | [Name_Female_Lang_frFR](chrraces_dbc#namefemalelang)              | Assumed frFR                                                                                                                                  |
| 35     | NameFemale_4              | string | [Name_Female_Lang_deDE](chrraces_dbc#namefemalelang)              | Assumed deDE                                                                                                                                  |
| 36     | NameFemale_5              | string | [Name_Female_Lang_enCN](chrraces_dbc#namefemalelang)              | Assumed enCN, not used in 3.3.5a                                                                                                              |
| 37     | NameFemale_6              | string | [Name_Female_Lang_zhCN](chrraces_dbc#namefemalelang)              | Assumed zhCN                                                                                                                                  |
| 38     | NameFemale_7              | string | [Name_Female_Lang_enTW](chrraces_dbc#namefemalelang)              | Assumed enTW, not used in 3.3.5a                                                                                                              |
| 39     | NameFemale_8              | string | [Name_Female_Lang_zhTW](chrraces_dbc#namefemalelang)              | Assumed zhTW                                                                                                                                  |
| 40     | NameFemale_9              | string | [Name_Female_Lang_esES](chrraces_dbc#namefemalelang)              | Assumed esES                                                                                                                                  |
| 41     | NameFemale_10             | string | [Name_Female_Lang_esMX](chrraces_dbc#namefemalelang)              | Assumed esMX                                                                                                                                  |
| 42     | NameFemale_11             | string | [Name_Female_Lang_ruRU](chrraces_dbc#namefemalelang)              | Assumed ruRU                                                                                                                                  |
| 43     | NameFemale_12             | string | [Name_Female_Lang_ptPT](chrraces_dbc#namefemalelang)              | Assumed ptPT, not used in 3.3.5a                                                                                                              |
| 44     | NameFemale_13             | string | [Name_Female_Lang_ptBR](chrraces_dbc#namefemalelang)              | Assumed ptBR, not used in 3.3.5a                                                                                                              |
| 45     | NameFemale_14             | string | [Name_Female_Lang_itIT](chrraces_dbc#namefemalelang)              | Assumed itIT, not used in 3.3.5a                                                                                                              |
| 46     | NameFemale_15             | string | [Name_Female_Lang_Unk](chrraces_dbc#namefemalelang)               | Unknown language, unsure of the usage in 3.3.5a                                                                                               |
| 47     | NameFemale_lang_mask      | uint32 | [Name_Female_Lang_Mask](chrraces_dbc#namefemalelang)              | String flags, unused. Assumed flags of the localized text                                                                                     |
| 48     | NameMale_0                | string | [Name_Male_Lang_enUS](chrraces_dbc#namemalelang)                  | If different from base case, otherwise unused. Always NULL for zhCN. Assumed enUS                                                             |
| 49     | NameMale_1                | string | [Name_Male_Lang_enGB](chrraces_dbc#namemalelang)                  | Assumed enGB, not used in 3.3.5a                                                                                                              |
| 50     | NameMale_2                | string | [Name_Male_Lang_koKR](chrraces_dbc#namemalelang)                  | Assumed koKR                                                                                                                                  |
| 51     | NameMale_3                | string | [Name_Male_Lang_frFR](chrraces_dbc#namemalelang)                  | Assumed frFR                                                                                                                                  |
| 52     | NameMale_4                | string | [Name_Male_Lang_deDE](chrraces_dbc#namemalelang)                  | Assumed deDE                                                                                                                                  |
| 53     | NameMale_5                | string | [Name_Male_Lang_enCN](chrraces_dbc#namemalelang)                  | Assumed enCN, not used in 3.3.5a                                                                                                              |
| 54     | NameMale_6                | string | [Name_Male_Lang_zhCN](chrraces_dbc#namemalelang)                  | Assumed zhCN                                                                                                                                  |
| 55     | NameMale_7                | string | [Name_Male_Lang_enTW](chrraces_dbc#namemalelang)                  | Assumed enTW, not used in 3.3.5a                                                                                                              |
| 56     | NameMale_8                | string | [Name_Male_Lang_zhTW](chrraces_dbc#namemalelang)                  | Assumed zhTW                                                                                                                                  |
| 57     | NameMale_9                | string | [Name_Male_Lang_esES](chrraces_dbc#namemalelang)                  | Assumed esES                                                                                                                                  |
| 58     | NameMale_10               | string | [Name_Male_Lang_esMX](chrraces_dbc#namemalelang)                  | Assumed esMX                                                                                                                                  |
| 59     | NameMale_11               | string | [Name_Male_Lang_ruRU](chrraces_dbc#namemalelang)                  | Assumed ruRU                                                                                                                                  |
| 60     | NameMale_12               | string | [Name_Male_Lang_ptPT](chrraces_dbc#namemalelang)                  | Assumed ptPT, not used in 3.3.5a                                                                                                              |
| 61     | NameMale_13               | string | [Name_Male_Lang_ptBR](chrraces_dbc#namemalelang)                  | Assumed ptBR, not used in 3.3.5a                                                                                                              |
| 62     | NameMale_14               | string | [Name_Male_Lang_itIT](chrraces_dbc#namemalelang)                  | Assumed itIT, not used in 3.3.5a                                                                                                              |
| 63     | NameMale_15               | string | [Name_Male_Lang_Unk](chrraces_dbc#namemalelang)                   | Unknown language, unsure of the usage in 3.3.5a                                                                                               |
| 64     | NameMale_lang_mask        | uint32 | [Name_Male_Lang_Mask](chrraces_dbc#namemalelang)                  | String flags, unused. Assumed flags of the localized text                                                                                     |
| 65     | FacialHairCustomization_0 | string | [FacialHairCustomization_1](chrraces_dbc#facialhaircustomization) | Internal names for the facial features.                                                                                                       |
| 66     | FacialHairCustomization_1 | string | [FacialHairCustomization_2](chrraces_dbc#facialhaircustomization) | The localized ones are in luas.                                                                                                               |
| 67     | HairCustomization         | string | [HairCustomization](chrraces_dbc#haircustomization)               | Internal name for the hair customizations.  Horns for tauren, normal for the others.                                                          |
| 68     | RequiredExpansion         | uint32 | [Required_Expansion](chrraces_dbc#requiredexpansion)              | 0 = Classic & Not playable, 1 = Burning Crusade                                                                                               |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

### Content

| Value   | Hex          | Flag               | Race ID |
| :------ | :----------: | :----------------- | :------ |
| 1       | `0x00000001` | Human              | 1       |
| 2       | `0x00000002` | Orc                | 2       |
| 4       | `0x00000004` | Dwarf              | 3       |
| 8       | `0x00000008` | Night Elf          | 4       |
| 16      | `0x00000010` | Undead             | 5       |
| 32      | `0x00000020` | Tauren             | 6       |
| 64      | `0x00000040` | Gnome              | 7       |
| 128     | `0x00000080` | Troll              | 8       |
| 256     | `0x00000100` | Goblin             | 9       |
| 512     | `0x00000200` | Blood Elf          | 10      |
| 1024    | `0x00000400` | Draenei            | 11      |
| 2048    | `0x00000800` | Fel Orc            | 12      |
| 4096    | `0x00001000` | Naga               | 13      |
| 8192    | `0x00002000` | Broken             | 14      |
| 16384   | `0x00004000` | Skeleton           | 15      |
| 32768   | `0x00008000` | Vrykul             | 16      |
| 65536   | `0x00010000` | Tuskarr            | 17      |
| 131072  | `0x00020000` | Forest Troll       | 18      |
| 262144  | `0x00040000` | Taunka             | 19      |
| 524288  | `0x00080000` | Northrend Skeleton | 20      |
| 1048576 | `0x00100000` | Ice Troll          | 21      |

### Flags

| Value | Hex    | Flag         | Comment |
| :---- | :----: | :----------- | :------ |
| 1     | `0x01` | Not playable |         |
| 2     | `0x02` | Bare feet    |         |
| 4     | `0x04` | Can mount    |         |
| 8     | `0x08` | Has bald     |         |

### Faction values

Alliance only = 1101
Horde only = 690
Both factions = 1791 (0 may work)

### How do I get the values?

If you want to learn how bits work you can read the [bit-and-bytes tutorial](bit-and-bytes-tutorial).
