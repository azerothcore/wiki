# ChrRaces.dbc

This dbc contains all possible races, some of which are unused and unavailable to players.

**Version is : 3.3.5a**

### Structure

| Column | Field             | Type         | Notes                                           |
|--------|-------------------|--------------|-------------------------------------------------|
| 1      | RaceID            | Integer      |                                                 |
| 2      | [Flags](#flags)             | Integer      |                                                 |
| 3      | FactionID         | Integer      | Faction ID                                      |
| 4      | ExplorationSoundID| Integer      |                                                 |
| 5      | model_m           | Integer      | Male display ID, used for character creation    |
| 6      | model_f           | Integer      | Female display ID, used for character creation  |
| 7      | ClientPrefix      | String       |                                                 |
| 8      | TeamID            | Integer      | 7=Alliance, 1=Horde                             |
| 9      | CreatureType      | Integer      | 7=Humanoid                                      |
| 10     | ResSicknessSpellID| Integer      | Spell to use for res sickness                   |
| 11     | SplashSoundID     | Integer      | Sound to use for splashing                      |
| 12     | ClientFilestring  | String       |                                                 |
| 13     | CinematicSequence | Integer      | ID from CinematicSequence.dbc                   |
| 14     | Alliance          | Integer      | Faction (0=Alliance, 1=Horde, 2=Not available)  |
| 15-30  | name              | String + Loc | Used for DBC language detection/selection       |
| 31     | NameLangMask      | Integer      | String flags, unused                            |
| 32-47  | nameFemale        | String + Loc | If different from base case, otherwise unused   |
| 48     | fNameLangMask     | Integer      | String flags, unused                            |
| 49-64  | nameMale          | String + Loc | If different from base case, otherwise unused   |
| 65     | mNameLangMask     | Integer      | String flags, unused                            |
| 66-68  | CustomizationNames| String       | Strings to use for customization in creation    |
| 69     | expansion         | Integer      | 0=Original race, 1=TBC race                     |

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
