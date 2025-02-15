# active_arena_season

[<-Back-to:Characters](database-characters)

**The \`active_arena_season\` table**

Holds information about the current arena season.

**Table Structure**

| Field                        | Type    | Attributes | Key | Null | Default | Extra | Comment                                            |
| ---------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | -------------------------------------------------- |
| [season_id](#seasonid)       | TINYINT | UNSIGNED   |     | NO   |         |       |                                                    |
| [season_state](#seasonstate) | TINYINT | UNSIGNED   |     | NO   |         |       | Supported 2 states: 0 - disabled; 1 - in progress. |

**Description of the fields**

### season_id

Current season id.

### season_state

| value | comment     |
| ----- | ----------- |
| 0     | disabled    |
| 1     | in progress |
