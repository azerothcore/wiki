# arena_season_reward

[<-Back-to:World](database-world)

**The \`arena_season_reward\` table**

`table-no-description`

**Table Structure**

| Field                | Type | Attributes       | Key | Null | Default     | Extra | Comment                                                      |
| -------------------- | ---- | ---------------- | --- | ---- | ----------- | ----- | ------------------------------------------------------------ |
| [group_id](#groupid) | INT  |                  | PRI | NO   |             |       | id from arena_season_reward_group table                      |
| [type](#type)        | ENUM | achievement,item | PRI | NO   | achievement |       |                                                              |
| [entry](#entry)      | INT  | UNSIGNED         | PRI | NO   | pct         |       | For item type - item entry, for achievement - achevement id. |


## Description of the fields

### group_id

[arena_season_reward_group.id](arena_season_reward_group#id)

### type

- achievement
- item

### entry

- achievement ID
- [item_tempalte.entry](item_template#entry)
