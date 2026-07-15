# arena_season_reward_group

[<-Volver a:World](database-world)

**Tabla \`arena_season_reward_group\`**

`tabla-sin-descripción`

**Estructura**

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


## Descripción de los campos

### id

ID autoincrementado.

### arena_season

ID de la temporada de arena

### criteria_type

Determina cómo se evalúan las clasificaciones

| value | comment                                            |
| ----- | -------------------------------------------------- |
| pct   | basado en porcentaje (p. ej., el 20% superior de la clasificación) |
| abs   | basado en posición absoluta (p. ej., los 10 primeros jugadores) |

### min_criteria

`campo-sin-descripción|4`

### max_criteria

`campo-sin-descripción|5`

### reward_mail_template_id

`campo-sin-descripción|6`

### reward_mail_subject

`campo-sin-descripción|7`

### reward_mail_body

`campo-sin-descripción|8`

### gold_reward

Recompensa de oro en cobre.
