# groups

[<-Back-to:Characters](database-characters)

**The \`groups\` table**

This table holds basic info about groups.

**Table: groups's Structure**

| Field                  | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]              | INT     | UNSIGNED   | PRI | NO   |         |       |         |
| [leaderGuid][2]        | INT     | UNSIGNED   | MUL | NO   |         |       |         |
| [lootMethod][3]        | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [looterGuid][4]        | INT     | UNSIGNED   |     | NO   |         |       |         |
| [lootThreshold][5]     | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [icon1][6]             | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [icon2][7]             | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [icon3][8]             | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [icon4][9]             | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [icon5][10]            | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [icon6][11]            | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [icon7][12]            | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [icon8][13]            | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [groupType][14]        | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [difficulty][15]       | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [raidDifficulty][16]   | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [masterLooterGuid][17] | INT     | UNSIGNED   |     | NO   |         |       |         |

[1]: #guid
[2]: #leaderguid
[3]: #lootmethod
[4]: #looterguid
[5]: #lootthreshold
[6]: #icon
[7]: #icon
[8]: #icon
[9]: #icon
[10]: #icon
[11]: #icon
[12]: #icon
[13]: #icon
[14]: #grouptype
[15]: #difficulty
[16]: #raiddifficulty
[17]: #masterlooterguid

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

| Value | Name             | Comments                               |
| ----- | ---------------- | -------------------------------------- |
| 0     | GROUPTYPE_NORMAL |                                        |
| 1     | GROUPTYPE_BG     |                                        |
| 2     | GROUPTYPE_RAID   |                                        |
| 3     | GROUPTYPE_BGRAID | GROUPTYPE_BG + GROUPTYPE_RAID, // mask |
| 4     | GROUPTYPE_UNK1   |                                        |
| 8     | GROUPTYPE_LFG    |                                        |

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
