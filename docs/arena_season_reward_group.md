# arena_season_reward_group

[<-Back-to:World](database-world)

**The \`arena_season_reward_group\` table**

`table-no-description`

**Table Structure**

| Field                                            | Type         | Attributes | Key | Null | Default | Extra          | Comment                                                                                                                                                |
| ------------------------------------------------ | ------------ | ---------- | --- | ---- | ------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [id](#id)                                        | INT          |            | PRI |      |         | AUTO_INCREMENT |                                                                                                                                                        |
| [arena_season](#arenaseason)                     | TINYINT      | UNSIGNED   |     | NO   |         |                |                                                                                                                                                        |
| [criteria_type](#criteriatype)                   | ENUM         | pct,abs    |     | NO   | pct     |                | Determines how rankings are evaluated: "pct" - percentage-based (e.g., top 20% of the ladder), "abs" - absolute position-based (e.g., top 10 players). |
| [min_criteria](#mincriteria)                     | FLOAT        |            |     | NO   |         |                |                                                                                                                                                        |
| [max_criteria](#maxcriteria)                     | FLOAT        |            |     | NO   |         |                |                                                                                                                                                        |
| [reward_mail_template_id](#rewardmailtemplateid) | INT          | UNSIGNED   |     | NO   |         |                |                                                                                                                                                        |
| [reward_mail_subject](#rewardmailsubject)        | VARCHAR(255) |            |     |      |         |                |                                                                                                                                                        |
| [reward_mail_body](#rewardmailbody)              | TEXT         |            |     |      |         |                |                                                                                                                                                        |
| [gold_reward](#goldreward)                       | INT          | UNSIGNED   |     | NO   |         |                |                                                                                                                                                        |


## Description of the fields

### id

ID auto incremented.

### arena_season

Arena season ID

### criteria_type

Determines how rankings are evaluated

| value | comment                                        |
| ----- | ---------------------------------------------- |
| pct   | percentage-based (e.g., top 20% of the ladder) |
| abs   | absolute position-based (e.g., top 10 players) |

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

Gold reward in copper.
