# arena_season_reward

[<-返回:World](database-world)

**\`arena_season_reward\` 表**

`table-no-description`

**表结构**

| Field                | Type | Attributes       | Key | Null | Default     | Extra | Comment                                                      |
| -------------------- | ---- | ---------------- | --- | ---- | ----------- | ----- | ------------------------------------------------------------ |
| [group_id](#groupid) | INT  |                  | PRI | NO   |             |       | 来自 arena_season_reward_group 表的 id                      |
| [type](#type)        | ENUM | achievement,item | PRI | NO   | achievement |       |                                                              |
| [entry](#entry)      | INT  | UNSIGNED         | PRI | NO   | pct         |       | 对于 item 类型为物品 entry，对于 achievement 类型为成就 id。 |


## 字段说明

### group_id

[arena_season_reward_group.id](arena_season_reward_group#id)

### type

- achievement
- item

### entry

- 成就 ID
- [item_tempalte.entry](item_template#entry)
