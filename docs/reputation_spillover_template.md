# reputation\_spillover\_template

[<-Back-to:World](database-world)

**The \`reputation\_spillover\_template\` table**

When a player gains or loses reputation with a faction, this table lets a part of it spill over to other factions. A row here replaces the spillover defined in Faction.dbc for that faction.

**Table: reputation\_spillover\_template's Structure**

| Field          | Type     | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [faction][1]   | SMALLINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [faction1][2]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [rate_1][3]    | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| [rank_1][4]    | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [faction2][5]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [rate_2][6]    | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| [rank_2][7]    | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [faction3][8]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [rate_3][9]    | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| [rank_3][10]   | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [faction4][11] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [rate_4][12]   | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| [rank_4][13]   | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [faction5][14] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [rate_5][15]   | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| [rank_5][16]   | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [faction6][17] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [rate_6][18]   | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| [rank_6][19]   | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #faction
[2]: #faction1-6
[3]: #rate1-6
[4]: #rank1-6
[5]: #faction1-6
[6]: #rate1-6
[7]: #rank1-6
[8]: #faction1-6
[9]: #rate1-6
[10]: #rank1-6
[11]: #faction1-6
[12]: #rate1-6
[13]: #rank1-6
[14]: #faction1-6
[15]: #rate1-6
[16]: #rank1-6
[17]: #faction1-6
[18]: #rate1-6
[19]: #rank1-6

**Description of the table's fields**

### faction

ID from Faction.dbc of the faction the player gains or loses reputation with.

### faction1-6

`faction1` to `faction6`. ID from Faction.dbc of a faction that receives part of the reputation. 0 if not used.

### rate1-6

`rate_1` to `rate_6`. The reputation is multiplied by this rate before it is given to the matching faction. For example, 0.5 gives half of the reputation.

### rank1-6

`rank_1` to `rank_6`. Highest reputation rank with the matching faction at which the player still gets the spillover.

| Value | Rank       |
| ----- | ---------- |
| 0     | Hated      |
| 1     | Hostile    |
| 2     | Unfriendly |
| 3     | Neutral    |
| 4     | Friendly   |
| 5     | Honored    |
| 6     | Revered    |
| 7     | Exalted    |
