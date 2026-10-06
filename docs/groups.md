# groups

[<-Back-to:Characters](database-characters)

**The \`groups\` table**

This table holds basic info about groups.

**Table: groups's Structure**

| Field                                 | Type    |          | Null | Key | Default | Extra | Comment |
| :------------------------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid)                         | INT     | UNSIGNED | NO   | PRI |         |       |         |
| [leaderGuid](#leaderguid)             | INT     | UNSIGNED | NO   | MUL |         |       |         |
| [lootMethod](#lootmethod)             | TINYINT | UNSIGNED | NO   |     |         |       |         |
| [looterGuid](#looterguid)             | INT     | UNSIGNED | NO   |     |         |       |         |
| [lootThreshold](#lootthreshold)       | TINYINT | UNSIGNED | NO   |     |         |       |         |
| [icon1](#icon)                        | BIGINT  | UNSIGNED | NO   |     |         |       |         |
| [icon2](#icon)                        | BIGINT  | UNSIGNED | NO   |     |         |       |         |
| [icon3](#icon)                        | BIGINT  | UNSIGNED | NO   |     |         |       |         |
| [icon4](#icon)                        | BIGINT  | UNSIGNED | NO   |     |         |       |         |
| [icon5](#icon)                        | BIGINT  | UNSIGNED | NO   |     |         |       |         |
| [icon6](#icon)                        | BIGINT  | UNSIGNED | NO   |     |         |       |         |
| [icon7](#icon)                        | BIGINT  | UNSIGNED | NO   |     |         |       |         |
| [icon8](#icon)                        | BIGINT  | UNSIGNED | NO   |     |         |       |         |
| [groupType](#grouptype)               | TINYINT | UNSIGNED | NO   |     |         |       |         |
| [difficulty](#difficulty)             | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [raidDifficulty](#raiddifficulty)     | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [masterLooterGuid](#masterlooterguid) | INT     | UNSIGNED | NO   |     |         |       |         |

**Description of the table's fields**

### guid

The ID of the group. This number is unique to each group and is the main method to identify a group.

### leaderGuid

The GUID of the character. See [characters.guid](characters#guid).

### lootMethod

| Value | Name              | Comments |
| ----- | ----------------- | -------- |
| 0     | FREE_FOR_ALL      |          |
| 1     | ROUND_ROBIN       |          |
| 2     | MASTER_LOOT       |          |
| 3     | GROUP_LOOT        |          |
| 4     | NEED_BEFORE_GREED |          |

### looterGuid

Master looter's guid. See [characters.guid](characters#guid).
If [lootMethod](groups#lootmethod) is not 2, then it's group leader's guid.

### lootThreshold

The lowest item quality that is rolled for. See [item\_template.Quality](item_template#quality).

### icon

`icon1` to `icon8`. GUID of the unit marked with each raid target icon (star, circle, diamond, triangle, moon, square, cross and skull).

### groupType

| Value | Hex    | Flag                     | Comment                                                                                                                                                                                                                                                  |
| :---- | :----: | :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0     | `0x00` | GROUPTYPE_NORMAL         | Normal party                                                                                                                                                                                                                                             |
| 1     | `0x01` | GROUPTYPE_BG             | Battleground group                                                                                                                                                                                                                                       |
| 2     | `0x02` | GROUPTYPE_RAID           | Raid group                                                                                                                                                                                                                                               |
| 3     | `0x03` | GROUPTYPE_BGRAID         | GROUPTYPE_BG + GROUPTYPE_RAID, // mask                                                                                                                                                                                                                   |
| 4     | `0x04` | GROUPTYPE_LFG_RESTRICTED | Group with LFG restrictions                                                                                                                                                                                                                              |
| 8     | `0x08` | GROUPTYPE_LFG            | Group made by the dungeon finder                                                                                                                                                                                                                         |
| 16    | `0x10` | GROUP_FLAG_DESTROYED     | Not in the core. Named in [cmangos](https://github.com/cmangos/mangos-wotlk/blob/master/src/game/Groups/Group.h); [WowPacketParser](https://github.com/TrinityCore/WowPacketParser/blob/master/WowPacketParser/Enums/GroupTypeFlag.cs) has it as unknown |

### difficulty

| Value | Dungeon difficulty |
| ----- | ------------------ |
| 0     | Normal             |
| 1     | Heroic             |

### raiddifficulty

| Value | Raid difficulty   |
| ----- | ----------------- |
| 0     | 10 player         |
| 1     | 25 player         |
| 2     | 10 player heroic  |
| 3     | 25 player heroic  |

### masterLooterGuid

GUID of the master looter, if the loot method is master loot. See [characters.guid](characters#guid).
