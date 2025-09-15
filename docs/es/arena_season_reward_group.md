# arena_season_reward_group

[<-Voler a:World](database-world)

**La \`arena_season_reward_group\` tabla**

`table-no-description`

**Estructura**

| Campo                                            | Tipo         | Atributos | Llave | Nulo | Por defecto | Extra          | Comentario                                                                                                                                                                                                   |
| ------------------------------------------------ | ------------ | --------- | ----- | ---- | ----------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [id](#id)                                        | INT          |           | PRI   |      |             | AUTO_INCREMENT |                                                                                                                                                                                                              |
| [arena_season](#arenaseason)                     | TINYINT      | UNSIGNED  |       | NO   |             |                |                                                                                                                                                                                                              |
| [criteria_type](#criteriatype)                   | ENUM         | pct,abs   |       | NO   | pct         |                | Determina cómo se evalúan las clasificaciones: "pct" - basado en porcentaje (por ejemplo, el 20% superior de la clasificación), "abs" - basado en posición absoluta (por ejemplo, los 10 mejores jugadores). |
| [min_criteria](#mincriteria)                     | FLOAT        |           |       | NO   |             |                |                                                                                                                                                                                                              |
| [max_criteria](#maxcriteria)                     | FLOAT        |           |       | NO   |             |                |                                                                                                                                                                                                              |
| [reward_mail_template_id](#rewardmailtemplateid) | INT          | UNSIGNED  |       | NO   |             |                |                                                                                                                                                                                                              |
| [reward_mail_subject](#rewardmailsubject)        | VARCHAR(255) |           |       |      |             |                |                                                                                                                                                                                                              |
| [reward_mail_body](#rewardmailbody)              | TEXT         |           |       |      |             |                |                                                                                                                                                                                                              |
| [gold_reward](#goldreward)                       | INT          | UNSIGNED  |       | NO   |             |                |                                                                                                                                                                                                              |


## Descripción de los campos

### id

ID incrementado automáticamente.

### arena_season

Identificación de la temporada de Arena

### criteria_type

Determina cómo se evalúan las clasificaciones

| Avaluar | comentario                                                             |
| ------- | ---------------------------------------------------------------------- |
| pct     | basado en porcentajes (por ejemplo, el 20% superior de la escala)      |
| abs     | Basado en la posición absoluta (por ejemplo, los 10 mejores jugadores) |

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

Recompensa de oro en cobre.
