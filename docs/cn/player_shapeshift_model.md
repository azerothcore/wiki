# player_shapeshift_model

[<-返回至:World](database-world)

**`player_shapeshift_model` 表**

该表保存了用于德鲁伊变形模型的值信息，这些值基于变形形态、种族、角色自定义以及玩家角色的性别。

**表结构**

| Field                               | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ShapeshiftID](#shapeshiftid)       | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [RaceID](#raceid)                   | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [CustomizationID](#customizationid) | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [GenderID](#genderid)               | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [ModelID](#modelid)                 | INT     | UNSIGNED   |     | NO   |         |       |         |

**字段说明**

### ShapeshiftID

| FormID | Description |
| ------ | ----------- |
| 1      | 猫形态       |
| 5      | 熊形态       |
| 8      | 巨熊形态     |
| 27     | 史诗飞行形态 |
| 29     | 飞行形态     |

### RaceID

| RaceID | Description |
| ------ | ----------- |
| 4      | 暗夜精灵     |
| 6      | 牛头人       |

对于 `RaceID`，你可以参考 [chrraces](chrraces) 的“ID”列。

### CustomizationID

如果你是联盟角色（仅限基础种族的暗夜精灵），自定义 ID 基于角色的[发色](characters#haircolor)。

如果你是部落角色（仅限基础种族的牛头人），自定义 ID 基于角色的[肤色](characters#skin)。

### GenderID

| [GenderID](characters#gender) | Description |
| ----------------------------- | ----------- |
| 0                             | 男性         |
| 1                             | 女性         |
| 2                             | 任意性别     |

### ModelID

请参阅 [creature_model_info](creature_model_info#displayid)
