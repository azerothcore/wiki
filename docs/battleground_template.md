# battleground\_template

[<-Back-to:World](database-world)

**The \`battleground\_template\` table**

Contains information about the different battlegrounds, like how many players are needed to start, how many can be inside the same one, and the locations where each side starts.

**Table Structure**

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

**Description of the fields**

### id

The battleground ID.

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

Controls the minimum number of players that need to join the battleground on each faction side for the battleground to start. For the battleground to start, all characters (between min and max player values) must be in the same tier. Tiers are set up in ranges of 10 levels except for level 80. So the first tier is 10-19, the next are 20-29, 30-39, 40-49, 50-59, 60-69, 70-79 and finally 80. If characters of different tiers all join the queue, they will join their respective tier's queue and wait for more players of their tier to join the queue. Characters in different tiers can never join the same battleground.

### MaxPlayersPerTeam

Controls how many players from each team can join the battleground.

NOTE2: If left to be 0, trinity will use the default DBC value.

### MinLvl

The minimum level that players need to be in order to join the battleground.

NOTE: If left to be 0, trinity will use the default DBC value.

### MaxLvl

The maximum level that players can be to enter the battleground.

NOTE: If left to be 0, trinity will use the default DBC value.

### AllianceStartLoc

The location where the alliance players get teleported to when the battleground first starts. See WorldSafeLocs.dbc

### AllianceStartO

The orientation of the alliance players upon teleport into the battleground. North is 0, south is Pi (3.14159).

### HordeStartLoc

The location where the horde players get teleported to when the battleground first starts. See WorldSafeLocs.dbc

### HordeStartO

The orientation of the horde players upon teleport into the battleground. North is 0, south is Pi (3.14159).

### Weight

Determines what battleground(s) will be more frequently chosen when using Random Battleground.
For example: If you want AV to be less often chosen, give 2 and for all other give 3.

### Example

| ID  | MinPlayersPerTeam | MaxPlayersPerTeam | MinLvl | MaxLvl | AllianceStartLoc | AllianceStartO | HordeStartLoc | HordeStartO | StartMaxDist | Weight | ScriptName | Comment                                |
| --- | ----------------- | ----------------- | ------ | ------ | ---------------- | -------------- | ------------- | ----------- | ------------ | ------ | ---------- | -------------------------------------- |
| 1   | 20                | 40                | 51     | 80     | 611              | 3.16312        | 610           | 0.715504    | 100          | 1      |            | Alterac Valley (battleground)          |
| 2   | 5                 | 10                | 10     | 80     | 769              | 3.14159        | 770           | 0.151581    | 75           | 1      |            | Warsong Gulch (battleground)           |
| 3   | 8                 | 15                | 20     | 80     | 890              | 3.91571        | 889           | 0.813671    | 75           | 1      |            | Arathi Basin (battleground)            |
| 4   | 0                 | 5                 | 10     | 80     | 929              | 0              | 936           | 3.14159     | 0            | 1      |            | Nagrand Arena / Ring of Trials (arena) |
| 5   | 0                 | 5                 | 10     | 80     | 939              | 0              | 940           | 3.14159     | 0            | 1      |            | Blades's Edge Arena (arena)            |
