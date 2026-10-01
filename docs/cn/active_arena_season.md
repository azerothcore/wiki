# active_arena_season

[<-返回:Characters](database-characters)

**\`active_arena_season\` 表**

保存有关当前竞技场赛季的信息。

**表结构**

| Field                        | Type    | Attributes | Key | Null | Default | Extra | Comment                                            |
| ---------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | -------------------------------------------------- |
| [season_id](#seasonid)       | TINYINT | UNSIGNED   |     | NO   |         |       |                                                    |
| [season_state](#seasonstate) | TINYINT | UNSIGNED   |     | NO   |         |       | 支持 2 种状态：0 - 已禁用；1 - 进行中。 |

**字段描述**

### season_id

当前赛季 ID。

### season_state

| value | comment     |
| ----- | ----------- |
| 0     | 已禁用      |
| 1     | 进行中      |
