# ChrRaces.dbc

[`Back-to:DBC`](dbc-index)

This DBC contains all possible races, some of which are unused and unavailable to players.

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)  

**Table Structure**

| Column | Field                   | Type    | Notes                                                                                |
| ------ | ----------------------- | ------- | ------------------------------------------------------------------------------------ |
| 1      | ID                      | Integer |                                                                                      |
| 2      | [Flags](#flags)         | Integer |                                                                                      |
| 3      | FactionID               | iRefID  | Faction template ID. The order in the creation screen depends on this.               |
| 4      | Exploration             | iRefID  | Played on exploring zones with SMSG_EXPLORATION_EXPERIENCE.                          |
| 5      | MaleModel               | iRefID  | Only used for the character creation/selection screen. Server sets the model ingame. |
| 6      | FemaleModel             | iRefID  | Only used for the character creation/selection screen. Server sets the model ingame. |
| 7      | ClientPrefix            | String  | A short form of the name. Used for helmet models.                                    |
| 8      | BaseLanguage            | Integer | 1 = Horde, 7 = Alliance & Not playable.                                              |
| 9      | creatureType            | iRefID  | Always 7 (Humanoid).                                                                 |
| 10     | ResSicknessSpellID      | Integer | Always 15007.                                                                        |
| 11     | SplashSoundID           | Integer | 1090 for dwarfs, 1096 for the others. Getting stored in CGUnit at CGUnit::PostInit.  |
| 12     | clientFilestring        | String  | Same as the one used in model filepaths.                                             |
| 13     | cinematicSequenceID     | iRefID  | Used for the opening cinematic.                                                      |
| 14     | alliance                | Integer | Faction (0 = Alliance, 1 = Horde, 2 = Not available)                                 |
| 15-30  | RaceNameNeutral         | Loc     | A name to display.                                                                   |
| 31     | NameLangMask            | Integer | String flags, unused                                                                 |
| 32-47  | RaceNameFemale          | Loc     | If different from base case, otherwise unused. Always NULL for zhCN.                 |
| 48     | NameFemaleLangMask      | Integer | String flags, unused                                                                 |
| 49-64  | RaceNameMale            | Loc     | If different from base case, otherwise unused. Always NULL for zhCN.                 |
| 65     | NameMaleLangMask        | Integer | String flags, unused                                                                 |
| 66     | facialHairCustomization | String  | Internal names for the facial features.                                              |
| 67     | facialHairCustomization | String  | The localized ones are in luas.                                                      |
| 68     | hairCustomization       | String  | Internal name for the hair customizations.  Horns for tauren, normal for the others. |
| 69     | required_expansion      | Integer | 0 = Classic & Not playable, 1 = Burning Crusade                                      |

### Content

| Value   | Hex        | Flag               | Race ID |
| :------ | :--------: | :----------------- | :------ |
| 1       | 0x00000001 | Human              | 1       |
| 2       | 0x00000002 | Orc                | 2       |
| 4       | 0x00000004 | Dwarf              | 3       |
| 8       | 0x00000008 | Night Elf          | 4       |
| 16      | 0x00000010 | Undead             | 5       |
| 32      | 0x00000020 | Tauren             | 6       |
| 64      | 0x00000040 | Gnome              | 7       |
| 128     | 0x00000080 | Troll              | 8       |
| 256     | 0x00000100 | Goblin             | 9       |
| 512     | 0x00000200 | Blood Elf          | 10      |
| 1024    | 0x00000400 | Draenei            | 11      |
| 2048    | 0x00000800 | Fel Orc            | 12      |
| 4096    | 0x00001000 | Naga               | 13      |
| 8192    | 0x00002000 | Broken             | 14      |
| 16384   | 0x00004000 | Skeleton           | 15      |
| 32768   | 0x00008000 | Vrykul             | 16      |
| 65536   | 0x00010000 | Tuskarr            | 17      |
| 131072  | 0x00020000 | Forest Troll       | 18      |
| 262144  | 0x00040000 | Taunka             | 19      |
| 524288  | 0x00080000 | Northrend Skeleton | 20      |
| 1048576 | 0x00100000 | Ice Troll          | 21      |

### Flags

| Value | Hex  | Flag         | Comment |
| :---- | :--: | :----------- | :------ |
| 1     | 0x01 | Not playable |         |
| 2     | 0x02 | Bare feet    |         |
| 4     | 0x04 | Can mount    |         |
| 8     | 0x08 | Has bald     |         |


### Faction values

Alliance only = 1101
Horde only = 690
Both factions = 1791 (0 may work)


### How do I get the values?

If you want to learn how bits work you can read the [bit-and-bytes tutorial](bit-and-bytes-tutorial).
