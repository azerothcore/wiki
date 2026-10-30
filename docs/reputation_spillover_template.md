# reputation\_spillover\_template

[<-Back-to:World](database-world)

**The \`reputation\_spillover\_template\` table**

When a player gains or loses reputation with a faction, this table lets a part of it spill over to other factions. A row here replaces the spillover defined in Faction.dbc for that faction.

**Table: reputation\_spillover\_template's Structure**

| Field                   | Type     |          | Null | Key | Default | Extra | Comment                                         |
| :---------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :---------------------------------------------- |
| [faction](#faction)     | SMALLINT | UNSIGNED | NO   | PRI | 0       |       | faction entry                                   |
| [faction1](#faction1-6) | SMALLINT | UNSIGNED | NO   |     | 0       |       | faction to give spillover for                   |
| [rate_1](#rate1-6)      | FLOAT    |          | NO   |     | 0       |       | the given rep points * rate                     |
| [rank_1](#rank1-6)      | TINYINT  | UNSIGNED | NO   |     | 0       |       | max rank,above this will not give any spillover |
| [faction2](#faction1-6) | SMALLINT | UNSIGNED | NO   |     | 0       |       |                                                 |
| [rate_2](#rate1-6)      | FLOAT    |          | NO   |     | 0       |       |                                                 |
| [rank_2](#rank1-6)      | TINYINT  | UNSIGNED | NO   |     | 0       |       |                                                 |
| [faction3](#faction1-6) | SMALLINT | UNSIGNED | NO   |     | 0       |       |                                                 |
| [rate_3](#rate1-6)      | FLOAT    |          | NO   |     | 0       |       |                                                 |
| [rank_3](#rank1-6)      | TINYINT  | UNSIGNED | NO   |     | 0       |       |                                                 |
| [faction4](#faction1-6) | SMALLINT | UNSIGNED | NO   |     | 0       |       |                                                 |
| [rate_4](#rate1-6)      | FLOAT    |          | NO   |     | 0       |       |                                                 |
| [rank_4](#rank1-6)      | TINYINT  | UNSIGNED | NO   |     | 0       |       |                                                 |
| [faction5](#faction1-6) | SMALLINT | UNSIGNED | NO   |     | 0       |       |                                                 |
| [rate_5](#rate1-6)      | FLOAT    |          | NO   |     | 0       |       |                                                 |
| [rank_5](#rank1-6)      | TINYINT  | UNSIGNED | NO   |     | 0       |       |                                                 |
| [faction6](#faction1-6) | SMALLINT | UNSIGNED | NO   |     | 0       |       |                                                 |
| [rate_6](#rate1-6)      | FLOAT    |          | NO   |     | 0       |       |                                                 |
| [rank_6](#rank1-6)      | TINYINT  | UNSIGNED | NO   |     | 0       |       |                                                 |

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
