# arena_season_reward

[<-Voler a:World](database-world)

**La \`arena_season_reward\` table**

`table-no-description`

**Estructura**

| Campo                | Tipo | Atributos        | Llave | Nulo | Por defecto | Extra | Comentario                                                                              |
| -------------------- | ---- | ---------------- | ----- | ---- | ----------- | ----- | --------------------------------------------------------------------------------------- |
| [group_id](#groupid) | INT  |                  | PRI   | NO   |             |       | id de la tabla arena_season_reward_group                                                |
| [type](#type)        | ENUM | logro, artículo  | PRI   | NO   | achievement |       |                                                                                         |
| [entry](#entry)      | INT  | UNSIGNED         | PRI   | NO   | pct         |       | Para el tipo de artículo: entrada de artículo, para el logro: identificación del logro. |


## Descripción de los campos

### group_id

[arena_season_reward_group.id](arena_season_reward_group#id)

### type

- logro
- artículo

### entry

- ID de logro
- [item_tempalte.entry](item_template#entry)
