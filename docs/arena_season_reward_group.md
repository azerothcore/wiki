# arena\_season\_reward\_group

[<-Back-to:World](database-world)

**The \`arena\_season\_reward\_group\` table**

Defines which arena teams get rewards at the end of an arena season. Teams need at least 30 games in the season, and members need to have played at least 30% of their team's games. The rewards of each group are in [arena\_season\_reward](arena_season_reward).

**Table: arena\_season\_reward\_group's Structure**

| Field                                            | Type         |          | Null | Key | Default | Extra          | Comment                                                                                                                                                |
| :----------------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                                        | INT          |          | NO   | PRI |         | AUTO_INCREMENT |                                                                                                                                                        |
| [arena_season](#arenaseason)                     | TINYINT      | UNSIGNED | NO   |     |         |                |                                                                                                                                                        |
| [criteria_type](#criteriatype)                   | ENUM         | pct,abs  | NO   |     | pct     |                | Determines how rankings are evaluated: "pct" - percentage-based (e.g., top 20% of the ladder), "abs" - absolute position-based (e.g., top 10 players). |
| [min_criteria](#mincriteria)                     | FLOAT        |          | NO   |     |         |                |                                                                                                                                                        |
| [max_criteria](#maxcriteria)                     | FLOAT        |          | NO   |     |         |                |                                                                                                                                                        |
| [reward_mail_template_id](#rewardmailtemplateid) | INT          | UNSIGNED | YES  |     | NULL    |                |                                                                                                                                                        |
| [reward_mail_subject](#rewardmailsubject)        | VARCHAR(255) |          | YES  |     | NULL    |                |                                                                                                                                                        |
| [reward_mail_body](#rewardmailbody)              | TEXT         |          | YES  |     | NULL    |                |                                                                                                                                                        |
| [gold_reward](#goldreward)                       | INT          | UNSIGNED | YES  |     | NULL    |                |                                                                                                                                                        |


**Description of the table's fields**

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

Start of the ranking range. With `pct`, a percentage of all teams sorted by rating, for example 0 for the top of the ladder. With `abs`, the rank of the first team, for example 1 for the best team.

### max_criteria

End of the ranking range. With `pct`, a percentage of all teams, for example 0.5 for the top 0.5%. With `abs`, the rank of the last team to get the reward.

### reward_mail_template_id

ID from MailTemplate.dbc of the mail that sends the item and money rewards. If 0, [reward\_mail\_subject](#rewardmailsubject) and [reward\_mail\_body](#rewardmailbody) are used.

### reward_mail_subject

Subject of the reward mail, if no [reward\_mail\_template\_id](#rewardmailtemplateid) is set.

### reward_mail_body

Text of the reward mail, if no [reward\_mail\_template\_id](#rewardmailtemplateid) is set.

### gold_reward

Gold reward in copper.
