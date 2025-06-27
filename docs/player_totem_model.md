# player_totem_model

[<-Back-to:World](database-world)

**The \`player_totem_model\` table**

This table holds the information on what values are used for the shaman totem models, based on the totem and race of the player character.

**Table Structure**

| Field               | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [TotemID](#totemid) | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [RaceID](#raceid)   | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [ModelID](#modelid) | INT     | UNSIGNED   |     | NO   |         |       |         |

**Description of the fields**

### TotemID

| TotemID | Description |
| ------- | ----------- |
| 1       | Fire Totem  |
| 2       | Earth Totem |
| 3       | Water Totem |
| 4       | Air Totem   |

### RaceID

| RaceID | Description |
| ------ | :---------- |
| 2      | Orc         |
| 3      | Dwarf       |
| 6      | Tauren      |
| 8      | Troll       |
| 11     | Draenei     |

For `RaceID` you can refer to the [chrraces](chrraces) "ID" column.

### ModelID

Refer to [creature_model_info](#creature_model_info#displayid)
