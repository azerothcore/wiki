# ChrRaces.dbc

[`Back-to:DBC`](dbc-index.md)

This DBC contains all possible races, some of which are unused and unavailable to players.

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db.md)  

### Structure

| Column | Field                   | Type         | Notes                                                                                |
|--------|-------------------------|--------------|--------------------------------------------------------------------------------------|
| 1      | ID                      | Integer      |                                                                                      |
| 2      | [Flags](#flags)         | Integer      |                                                                                      |
| 3      | FactionID               | iRefID       | Faction template ID. The order in the creation screen depends on this.               |
| 4      | Exploration             | iRefID       | Played on exploring zones with SMSG_EXPLORATION_EXPERIENCE.                          |
| 5      | MaleModel               | iRefID       | Only used for the character creation/selection screen. Server sets the model ingame. |
| 6      | FemaleModel             | iRefID       | Only used for the character creation/selection screen. Server sets the model ingame. |
| 7      | ClientPrefix            | String       | A short form of the name. Used for helmet models.                                    |
| 8      | BaseLanguage            | Integer      | 1 = Horde, 7 = Alliance & Not playable.                                              |
| 9      | creatureType            | iRefID       | Always 7 (Humanoid).                                                                 |
| 10     | ResSicknessSpellID      | Integer      | Always 15007.                                                                        |
| 11     | SplashSoundID           | Integer      | 1090 for dwarfs, 1096 for the others. Getting stored in CGUnit at CGUnit::PostInit.  |
| 12     | clientFilestring        | String       | Same as the one used in model filepaths.                                             |
| 13     | cinematicSequenceID     | iRefID       | Used for the opening cinematic.                                                      |
| 14     | alliance                | Integer      | Faction (0 = Alliance, 1 = Horde, 2 = Not available)                                 |
| 15-30  | RaceNameNeutral         | Loc          | A name to display.                                                                   |
| 31     | NameLangMask            | Integer      | String flags, unused                                                                 |
| 32-47  | RaceNameFemale          | Loc          | If different from base case, otherwise unused. Always NULL for zhCN.                 |
| 48     | NameFemaleLangMask      | Integer      | String flags, unused                                                                 |
| 49-64  | RaceNameMale            | Loc          | If different from base case, otherwise unused. Always NULL for zhCN.                 |
| 65     | NameMaleLangMask        | Integer      | String flags, unused                                                                 |
| 66     | facialHairCustomization | String       | Internal names for the facial features.                                              |
| 67     | facialHairCustomization | String       | The localized ones are in luas.                                                      |
| 68     | hairCustomization       | String       | Internal name for the hair customizations.  Horns for tauren, normal for the others. |
| 69     | required_expansion      | Integer      | 0 = Classic & Not playable, 1 = Burning Crusade                                      |

### Content

| ID | Value    | Name                    |
|----|----------|-------------------------|
| 1  | 1        | Human                   |
| 2  | 2        | Orc                     |
| 3  | 4        | Dwarf                   |
| 4  | 8        | Night Elf               |
| 5  | 16       | Undead                  |
| 6  | 32       | Tauren                  |
| 7  | 64       | Gnome                   |
| 8  | 128      | Troll                   |
| 9  | 256      | Goblin                  |
| 10 | 512      | Blood Elf               |
| 11 | 1024     | Draenei                 |
| 12 | 2048     | Fel Orc                 |
| 13 | 4096     | Naga                    |
| 14 | 8192     | Broken                  |
| 15 | 16384    | Skeleton                |
| 16 | 32768    | Vrykul                  |
| 17 | 65536    | Tuskarr                 |
| 18 | 131072   | Forest Troll            |
| 19 | 262144   | Taunka                  |
| 20 | 524288   | Northrend Skeleton      |
| 21 | 1048576  | Ice Troll               |

### Flags

| Flag | Description           |
|------|-----------------------|
| 1    | Not playable          |
| 2    | Bare feet             |
| 4    | Can mount             |
| 8    | Has bald              |


### Faction values

Alliance only = 1101
Horde only = 690
Both factions = 1791 (0 may work)


### How do I get the values?

If you want to learn how bits work you can read the [bit-and-bytes tutorial](Bit-and_bytes-tutorial).
