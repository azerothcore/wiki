# arena_season_reward_group

[<-返回:World](database-world)

**\`arena_season_reward_group\` 表**

`table-no-description`

**表结构**

| Field                                            | Type         | Attributes | Key | Null | Default | Extra          | Comment                                                                                                                                                |
| ------------------------------------------------ | ------------ | ---------- | --- | ---- | ------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [id](#id)                                        | INT          |            | PRI |      |         | AUTO_INCREMENT |                                                                                                                                                        |
| [arena_season](#arenaseason)                     | TINYINT      | UNSIGNED   |     | NO   |         |                |                                                                                                                                                        |
| [criteria_type](#criteriatype)                   | ENUM         | pct,abs    |     | NO   | pct     |                | 决定排名的评估方式："pct" - 基于百分比（例如，天梯前 20%），"abs" - 基于绝对名次（例如，前 10 名玩家）。 |
| [min_criteria](#mincriteria)                     | FLOAT        |            |     | NO   |         |                |                                                                                                                                                        |
| [max_criteria](#maxcriteria)                     | FLOAT        |            |     | NO   |         |                |                                                                                                                                                        |
| [reward_mail_template_id](#rewardmailtemplateid) | INT          | UNSIGNED   |     | NO   |         |                |                                                                                                                                                        |
| [reward_mail_subject](#rewardmailsubject)        | VARCHAR(255) |            |     |      |         |                |                                                                                                                                                        |
| [reward_mail_body](#rewardmailbody)              | TEXT         |            |     |      |         |                |                                                                                                                                                        |
| [gold_reward](#goldreward)                       | INT          | UNSIGNED   |     | NO   |         |                |                                                                                                                                                        |


## 字段说明

### id

自动递增的 ID。

### arena_season

竞技场赛季 ID

### criteria_type

决定排名的评估方式

| value | comment                                        |
| ----- | ---------------------------------------------- |
| pct   | 基于百分比（例如，天梯前 20%） |
| abs   | 基于绝对名次（例如，前 10 名玩家） |

### min_criteria

`field-no-description|4`

### max_criteria

`field-no-description|5`

### reward_mail_template_id

`field-no-description|6`

### reward_mail_subject

`field-no-description|7`

### reward_mail_body

`field-no-description|8`

### gold_reward

以铜币计的金币奖励。
