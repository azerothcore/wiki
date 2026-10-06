# arena\_season\_reward

[<-Back-to:World](database-world)

**The \`arena\_season\_reward\` table**

The rewards of each [arena\_season\_reward\_group](arena_season_reward_group). Items are sent by mail, achievements are completed for every member of the team who gets the reward.

**Table: arena\_season\_reward's Structure**

| Field                | Type |                  | Null | Key | Default     | Extra | Comment                                                      |
| :------------------- | :--- | :--------------- | :--: | :-: | :---------: | :---: | :----------------------------------------------------------- |
| [group_id](#groupid) | INT  |                  | NO   | PRI |             |       | id from arena_season_reward_group table                      |
| [type](#type)        | ENUM | achievement,item | NO   | PRI | achievement |       |                                                              |
| [entry](#entry)      | INT  | UNSIGNED         | NO   | PRI |             |       | For item type - item entry, for achievement - achevement id. |


**Description of the table's fields**

### group_id

[arena_season_reward_group.id](arena_season_reward_group#id)

### type

- achievement
- item

### entry

- achievement ID
- [item_tempalte.entry](item_template#entry)
