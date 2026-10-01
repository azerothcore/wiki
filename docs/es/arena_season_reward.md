# arena_season_reward

[<-Volver a:World](database-world)

**Tabla \`arena_season_reward\`**

`tabla-sin-descripción`

**Estructura**

| Field                | Type | Attributes       | Key | Null | Default     | Extra | Comment                                                      |
| -------------------- | ---- | ---------------- | --- | ---- | ----------- | ----- | ------------------------------------------------------------ |
| [group_id](#groupid) | INT  |                  | PRI | NO   |             |       | id from arena_season_reward_group table                      |
| [type](#type)        | ENUM | achievement,item | PRI | NO   | achievement |       |                                                              |
| [entry](#entry)      | INT  | UNSIGNED         | PRI | NO   | pct         |       | For item type - item entry, for achievement - achevement id. |


## Descripción de los campos

### group_id

[arena_season_reward_group.id](arena_season_reward_group#id)

### type

- achievement
- item

### entry

- ID del logro (achievement)
- [item_tempalte.entry](item_template#entry)
