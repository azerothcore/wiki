# player_totem_model

[<-返回至:World](database-world)

**`player_totem_model` 表**

该表保存了用于萨满祭司图腾模型的值信息，这些值基于图腾和玩家角色的种族。

**表结构**

| Field               | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [TotemID](#totemid) | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [RaceID](#raceid)   | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [ModelID](#modelid) | INT     | UNSIGNED   |     | NO   |         |       |         |

**字段说明**

### TotemID

| TotemID | Description |
| ------- | ----------- |
| 1       | 火焰图腾     |
| 2       | 大地图腾     |
| 3       | 水图腾       |
| 4       | 空气图腾     |

### RaceID

| RaceID | Description |
| ------ | :---------- |
| 2      | 兽人         |
| 3      | 矮人         |
| 6      | 牛头人       |
| 8      | 巨魔         |
| 11     | 德莱尼       |

对于 `RaceID`，你可以参考 [chrraces](chrraces) 的“ID”列。

### ModelID

请参阅 [creature_model_info](creature_model_info#displayid)
