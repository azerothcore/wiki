# dungeon\_access\_template

[<-返回:世界](database-world)

**\`dungeon\_access\_template\` 表**

**表结构**

| 字段                   | 类型         | 属性 | 键 | 空 | 默认值        | 额外                                         | 注释 |
| ----------------------- | ------------ | ---------- | --- | ---- | -------------- | --------------------------------------------- | ------- |
| [id][1]                 | TINYINT      | UNSIGNED   | PRI | NO   | AUTO_INCREMENT |                                               |         |
| [map_id][2]             | MEDIUMINT    | UNSIGNED   | KEY | NO   |                | FK_dungeon_access_template__instance_template |         |
| [difficulty][3]         | TINYINT      | UNSIGNED   |     | NO   | 0              |                                               |         |
| [min_level][4]          | TINYINT      | UNSIGNED   |     | YES  | NULL           |                                               |         |
| [max_level][5]          | TINYINT      | UNSIGNED   |     | YES  | NULL           |                                               |         |
| [min_avg_item_level][6] | SMALLINT     | UNSIGNED   |     | YES  | NULL           |                                               |         |
| [comment][7]            | VARCHAR(255) |            |     | YES  | NULL           |                                               |         |

[1]: #id
[2]: #mapid
[3]: #difficulty
[4]: #minlevel
[5]: #maxlevel
[6]: #minavgitemlevel
[7]: #comment

**字段说明**

### id

副本模板 ID

### map_id

来自 [instance_template.map](instance_template#map) 的地图 ID。

### difficulty

- 5 人：0 = 普通，1 = 英雄，2 = 史诗 (Mythic，在 3.3.5 中未实现)

- 10 人：0 = 普通，2 = 英雄

- 25 人：1 = 普通，3 = 英雄

### min_level

进入副本所需的最低等级。

### max_level

进入副本所允许的最高等级。

### min_avg_item_level

进入副本所需的最低平均物品等级。

- 所有 WotLK 英雄副本至少需要 180 的平均物品等级。

- 冠军的试炼、萨隆矿坑和灵魂洪炉需要 200 的平均物品等级。

- 映像大厅需要 219 的平均物品等级。

**注意：** 此要求仅适用于地下城查找器和团队查找器，不适用于副本/团队传送门（这是仿暴雪的设定）。这也意味着一个公会可以在装备不足的情况下尝试打通团队副本 :)

### comment
