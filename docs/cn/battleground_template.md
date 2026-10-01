# battleground\_template

[<-返回:World](database-world)

**\`battleground\_template\` 表**

包含不同战场的信息，例如开始需要多少玩家、同一战场内最多能容纳多少玩家，以及双方各自开始的位置。

**表结构**

| Field                  | Type      | Atributes | Key | Null | Default | Extra | Comment |
| ---------------------- | --------- | --------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]                | MEDIUMINT | UNSIGNED  | PRI | NO   | 0       |       |         |
| [MinPlayersPerTeam][2] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [MaxPlayersPerTeam][3] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [MinLvl][4]            | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [MaxLvl][5]            | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [AllianceStartLoc][6]  | MEDIUMINT | UNSIGNED  |     | NO   |         |       |         |
| [AllianceStartO][7]    | FLOAT     | SIGNED    |     | NO   |         |       |         |
| [HordeStartLoc][8]     | MEDIUMINT | UNSIGNED  |     | NO   |         |       |         |
| [HordeStartO][9]       | FLOAT     | SIGNED    |     | NO   |         |       |         |
| [StartMaxDist][10]     | FLOAT     | SIGNED    |     | NO   | 0       |       |         |
| [Weight][11]           | TINYINT   | UNSIGNED  |     | NO   | 1       |       |         |
| [ScriptName][12]       | char(64)  |           |     | NO   |         |       |         |
| [Comment][13]          | char(38)  |           |     | NO   |         |       |         |

[1]: #id
[2]: #minplayersperteam
[3]: #maxplayersperteam
[4]: #minlvl
[5]: #maxlvl
[6]: #alliancestartloc
[7]: #alliancestarto
[8]: #hordestartloc
[9]: #hordestarto
[10]: #startmaxdist
[11]: #weight
[12]: #scriptname
[13]: #comment

**字段说明**

### id

战场 ID。

| ID  | Type                   |
| --- | ---------------------- |
| 1   | Alterac Valley         |
| 2   | Warsong Gulch          |
| 3   | Arathi Basin           |
| 4   | Nagrand Arena          |
| 5   | Blade's Edge Arena     |
| 6   | All Arena              |
| 7   | Eye of the Storm       |
| 8   | Ruins of Lordaeron     |
| 9   | Strand of the Ancients |
| 10  | Dalaran Sewers         |
| 11  | The Ring of Valor      |
| 30  | Isle of Conquest       |
| 32  | Random battleground    |

### MinPlayersPerTeam

控制战场开始前，每个阵营需要加入战场的最少玩家数量。战场要开始，所有角色（介于最小和最大玩家数之间）必须处于同一等级段。等级段按 10 级一个区间划分，但 80 级除外。因此第一个等级段是 10-19，接下来是 20-29、30-39、40-49、50-59、60-69、70-79，最后是 80。如果不同等级段的角色都加入排队，他们会进入各自等级段的队列，并等待同等级段的更多玩家加入队列。不同等级段的角色永远不会进入同一个战场。

### MaxPlayersPerTeam

控制每个阵营可以加入战场的玩家人数。

注意2：如果保持为 0，trinity 将使用默认的 DBC 值。

### MinLvl

玩家加入战场所需的最低等级。

注意：如果保持为 0，trinity 将使用默认的 DBC 值。

### MaxLvl

玩家进入战场所允许的最高等级。

注意：如果保持为 0，trinity 将使用默认的 DBC 值。

### AllianceStartLoc

战场首次开始时，联盟玩家被传送到的位置。参见 WorldSafeLocs.dbc

### AllianceStartO

联盟玩家传送到战场时的朝向。北为 0，南为 Pi（3.14159）。

### HordeStartLoc

战场首次开始时，部落玩家被传送到的位置。参见 WorldSafeLocs.dbc

### HordeStartO

部落玩家传送到战场时的朝向。北为 0，南为 Pi（3.14159）。

### Weight

决定使用随机战场时哪些战场会更频繁地被选中。
例如：如果你希望 AV 被选中的频率更低，就给 AV 设为 2，其他战场设为 3。

### 示例

| ID  | MinPlayersPerTeam | MaxPlayersPerTeam | MinLvl | MaxLvl | AllianceStartLoc | AllianceStartO | HordeStartLoc | HordeStartO | StartMaxDist | Weight | ScriptName | Comment                                |
| --- | ----------------- | ----------------- | ------ | ------ | ---------------- | -------------- | ------------- | ----------- | ------------ | ------ | ---------- | -------------------------------------- |
| 1   | 20                | 40                | 51     | 80     | 611              | 3.16312        | 610           | 0.715504    | 100          | 1      |            | Alterac Valley (战场)          |
| 2   | 5                 | 10                | 10     | 80     | 769              | 3.14159        | 770           | 0.151581    | 75           | 1      |            | Warsong Gulch (战场)           |
| 3   | 8                 | 15                | 20     | 80     | 890              | 3.91571        | 889           | 0.813671    | 75           | 1      |            | Arathi Basin (战场)            |
| 4   | 0                 | 5                 | 10     | 80     | 929              | 0              | 936           | 3.14159     | 0            | 1      |            | Nagrand Arena / Ring of Trials (竞技场) |
| 5   | 0                 | 5                 | 10     | 80     | 939              | 0              | 940           | 3.14159     | 0            | 1      |            | Blades's Edge Arena (竞技场)            |
