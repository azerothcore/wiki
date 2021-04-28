# reputation\_spillover\_template

[<-Back-to:World](database-world.md)

**The \`reputation\_spillover\_rate\` table**

`field-no-description|0`

**Structure**

| Field          | Type        | Attributes | Key | Null | Default | Extra | Comment |
|----------------|-------------|------------|-----|------|---------|-------|---------|
| [faction][1]   | smallint(6) | unsigned   | PRI | NO   | 0       |       |         |
| [faction1][2]  | smallint(6) | unsigned   |     | NO   | 0       |       |         |
| [rate_1][3]    | FLOAT       | signed     |     | NO   | 0       |       |         |
| [rank1][4]     | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| [faction2][5]  | smallint(6) | unsigned   |     | NO   | 0       |       |         |
| [rate_2][6]    | FLOAT       | signed     |     | NO   | 0       |       |         |
| [rank_2][7]    | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| [faction3][8]  | smallint(6) | unsigned   |     | NO   | 0       |       |         |
| [rate_3][9]    | FLOAT       | signed     |     | NO   | 0       |       |         |
| [rank_3][10]   | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |
| [faction4][11] | smallint(6) | unsigned   |     | NO   | 0       |       |         |
| [rate_4][12]   | FLOAT       | signed     |     | NO   | 0       |       |         |
| [rank_4][13]   | tinyint(3)  | unsigned   |     | NO   | 0       |       |         |

[1]: #faction
[2]: #faction1
[3]: #rate_1
[4]: #rank1
[5]: #faction2
[6]: #rate_2
[7]: #rank_2
[8]: #faction3
[9]: #rate_3
[10]: #rank_3
[11]: #faction4
[12]: #rate_4
[13]: #rank_4

**Description of the fields**

### faction

Faction entry (from FactionTemplate) to where the reputation was supposed to be rewarded.

### faction1-4

Faction entry (from FactionTemplate) receiving the reputation spillover.

### rate1-4

Rate the given reputation points are multiplied by.

### rank1-4

Max reputation rank. The player will not be given any spillover above this rank.
