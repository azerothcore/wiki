# ChrRaces.dbc

This dbc contains all possible races, some of which are unused and unavailable to players.

**Version is : 3.3.5a**

### Structure

| Column | Field             | Type         | Notes                                           |
|--------|-------------------|--------------|-------------------------------------------------|
| 1      | RaceID            | Integer      |                                                 |
| 2      | Flags             | Integer      |                                                 |
| 3      | FactionID         | Integer      | faction template id                             |
| 4      |                   |              | unused                                          |
| 5      | model_m           | Integer      |                                                 |
| 6      | model_f           | Integer      |                                                 |
| 7      |                   |              | unused                                          |
| 8      | TeamID            | Integer      | (7-Alliance 1-Horde)                            |
| 9-12   |                   |              | unused                                          |
| 13     | CinematicSequence | Integer      | id from CinematicSequence.dbc                   |
| 14     | unk_322           |              | faction (0 Alliance, 1 Horde, 2 not available?) |
| 15-30  | name              | String + Loc | used for DBC language detection/selection       |
| 31     |                   |              | string flags, unused                            |
| 32-47  | nameFemale        | String + Loc | if different from base (male) case              |
| 48     |                   |              | string flags, unused                            |
| 49-64  |                   |              | if different from base (male) case              |
| 65     |                   |              | string flags, unused                            |
| 66-68  |                   |              | unused                                          |
| 69     | expansion         | Integer      | (0 - original race, 1 - tbc addon, ...)         |

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
| 9  | 256      | Goblin (4.x)            |
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
| 22 | 2097152  | Worgen (4.x)            |
| 24 | 8388608  | Pandaren Neutral (5.x)  |
| 25 | 16777216 | Pandaren Alliance (5.x) |
| 26 | 33554432 | Pandaren Horde (5.x)    |


### Faction values

On WOTLK:
Alliance only = 1101
Horde only = 690
Both factions = 0


### How do I get the values?

If you want to learn how bits work you can read the tutorial here [bit-and_bytes-tutorial](Bit-and_bytes-tutorial)
