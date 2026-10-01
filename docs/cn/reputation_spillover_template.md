# reputation\_spillover\_template

[<-返回至:World](database-world)

**`reputation\_spillover\_template` 表**

`table-no-description|0`

**表结构**

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
[14]: #faction1-4
[15]: #rate1-4
[16]: #rank1-4
[17]: #faction1-4
[18]: #rate1-4
[19]: #rank1-4

**字段说明**

### faction

原本应获得声望的阵营条目（来自 FactionTemplate）。

### faction1-4

接收声望溢出的阵营条目（来自 FactionTemplate）。

### rate1-4

给定声望点数所乘的倍率。

### rank1-4

最大声望等级。玩家在此等级之上不会获得任何溢出声望。
