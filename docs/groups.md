# groups

[<-Back-to:Characters](database-characters.md)

**The \`groups\` table**

This table holds basic info about groups.

**Structure**

| Field                  | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]              | INT     | UNSIGNED   | PRI | NO   |         |       |         |
| [leaderGuid][2]        | INT     | UNSIGNED   |     | NO   |         |       |         |
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
| [raiddifficulty][16]   | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
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

**Description of the fields**

### guid

The ID of the group. This number is unique to each group and is the main method to identify a group.

### leaderGuid

The GUID of the character. See [characters.guid](characters#guid).

### lootMethod

| Value | Name              | Comments |
|-------|-------------------|----------|
| 0     | FREE_FOR_ALL      |          |
| 1     | ROUND_ROBIN       |          |
| 2     | MASTER_LOOT       |          |
| 3     | GROUP_LOOT        |          |
| 4     | NEED_BEFORE_GREED |          |

### looterGuid

Master looter's guid. See [characters.guid](characters#guid).
If [lootMethod](groups#lootmethod) is not 2, then it's group leader's guid.

### lootThreshold

`field-no-description|5`

### icon

`field-no-description|6-13`

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

`field-no-description|15`

### raiddifficulty

`field-no-description|16`

### masterLooterGuid

`field-no-description|17`