# player_totem_model

[<-Volver a:World](database-world)

**Tabla \`player_totem_model\`**

Esta tabla contiene la información sobre qué valores se usan para los modelos de tótem del chamán, según el tótem y la raza del personaje del jugador.

**Estructura**

| Field               | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [TotemID](#totemid) | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [RaceID](#raceid)   | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [ModelID](#modelid) | INT     | UNSIGNED   |     | NO   |         |       |         |

**Descripción de los campos**

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

Para `RaceID` puedes consultar la columna "ID" de [chrraces](chrraces).

### ModelID

Consulta [creature_model_info](#creature_model_info#displayid)
