# reputation\_spillover\_template

[<-Back-to:World](database-world)

**The \`reputation\_spillover\_rate\` table**

`table-no-description|0`

**Table Structure**

| Field          | Type     | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [faction][1]   | SMALLINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [faction1][2]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [rate_1][3]    | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| [rank1][4]     | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [faction2][5]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [rate_2][6]    | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| [rank_2][7]    | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [faction3][8]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [rate_3][9]    | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| [rank_3][10]   | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [faction4][11] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [rate_4][12]   | FLOAT    | SIGNED     |     | NO   | 0       |       |         |
| [rank_4][13]   | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #faction
[2]: #faction1-4
[3]: #rate1-4
[4]: #rank1-4
[5]: #faction1-4
[6]: #rate1-4
[7]: #rank1-4
[8]: #faction1-4
[9]: #rate1-4
[10]: #rank1-4
[11]: #faction1-4
[12]: #rate1-4
[13]: #rank1-4

**Description of the fields**

### faction

Faction entry (from FactionTemplate) to where the reputation was supposed to be rewarded.

### faction1-4

Faction entry (from FactionTemplate) receiving the reputation spillover.

### rate1-4

Rate the given reputation points are multiplied by.

### rank1-4

Max reputation rank. The player will not be given any spillover above this rank.
