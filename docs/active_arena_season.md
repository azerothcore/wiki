# active\_arena\_season

[<-Back-to:Characters](database-characters)

**The \`active\_arena\_season\` table**

Holds information about the current arena season.

**Table: active\_arena\_season's Structure**

| Field                        | Type    |          | Null | Key | Default | Extra | Comment                                            |
| :--------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------------------------------------------------- |
| [season_id](#seasonid)       | TINYINT | UNSIGNED | NO   |     |         |       |                                                    |
| [season_state](#seasonstate) | TINYINT | UNSIGNED | NO   |     |         |       | Supported 2 states: 0 - disabled; 1 - in progress. |

**Description of the table's fields**

### season_id

Current season id.

### season_state

| value | comment     |
| ----- | ----------- |
| 0     | disabled    |
| 1     | in progress |
