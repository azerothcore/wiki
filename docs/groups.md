# groups

[<-Back-to:Characters](database-characters.md)

**The \`groups\` table**

This table holds basic info about groups.

**Structure**

| Field                | Type       | Attributes | Key | Null | Default | Extra | Comment |
|----------------------|------------|------------|-----|------|---------|-------|---------|
| [guid][1]            | INT(10)    | UNSIGNED   | PRI | NO   |         |       |         |
| [leaderGuid][2]      | INT(10)    | UNSIGNED   |     | NO   |         |       |         |
| [lootMethod][3]      | TINYINT(3) | UNSIGNED   |     | NO   |         |       |         |
| [looterGuid][4]      | INT(10)    | UNSIGNED   |     | NO   |         |       |         |
| [lootThreshold][5]   | TINYINT(3) | UNSIGNED   |     | NO   |         |       |         |
| [icon1][6]           | INT(10)    | UNSIGNED   |     | NO   |         |       |         |
| [icon2][7]           | INT(10)    | UNSIGNED   |     | NO   |         |       |         |
| [icon3][8]           | INT(10)    | UNSIGNED   |     | NO   |         |       |         |
| [icon4][9]           | INT(10)    | UNSIGNED   |     | NO   |         |       |         |
| [icon5][10]          | INT(10)    | UNSIGNED   |     | NO   |         |       |         |
| [icon6][11]          | INT(10)    | UNSIGNED   |     | NO   |         |       |         |
| [icon7][12]          | INT(10)    | UNSIGNED   |     | NO   |         |       |         |
| [icon8][13]          | INT(10)    | UNSIGNED   |     | NO   |         |       |         |
| [groupType][14]      | TINYINT(3) | UNSIGNED   |     | NO   |         |       |         |
| [difficulty][15]     | TINYINT(3) | UNSIGNED   |     | NO   | 0       |       |         |
| [raiddifficulty][16] | TINYINT(3) | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #leaderguid
[3]: #lootmethod
[4]: #looterguid
[5]: #lootthreshold
[6]: #icon1
[7]: #icon2
[8]: #icon3
[9]: #icon4
[10]: #icon5
[11]: #icon6
[12]: #icon7
[13]: #icon8
[14]: #grouptype
[15]: #difficulty
[16]: #raiddifficulty

**Description of the fields**

### guid

The ID of the group. This number is unique to each group and is the main method to identify a group.

### leaderGuid

The GUID of the character. See characters.guid

### lootMethod

| Value | Name              | Comments |
|-------|-------------------|----------|
| 0     | FREE_FOR_ALL      |          |
| 1     | ROUND_ROBIN       |          |
| 2     | MASTER_LOOT       |          |
| 3     | GROUP_LOOT        |          |
| 4     | NEED_BEFORE_GREED |          |

### looterGuid

Master looter's guid. See characters.guid
If [lootMethod](#groups-lootMethod) is not 2, then it's group leader's guid.

### lootThreshold

`field-no-description|5`

### icon1-8

`field-no-description|6`

### groupType

| Value | Name             | Comments                               |
|-------|------------------|----------------------------------------|
| 0     | GROUPTYPE_NORMAL |                                        |
| 1     | GROUPTYPE_BG     |                                        |
| 2     | GROUPTYPE_RAID   |                                        |
| 3     | GROUPTYPE_BGRAID | GROUPTYPE_BG + GROUPTYPE_RAID, // mask |
| 4     | GROUPTYPE_UNK1   |                                        |
| 8     | GROUPTYPE_LFG    |                                        |

### difficulty

`field-no-description|8`

### raiddifficulty

`field-no-description|9`
