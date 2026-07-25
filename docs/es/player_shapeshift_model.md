# player_shapeshift_model

[<-Volver a:World](database-world)

**Tabla \`player_shapeshift_model\`**

Esta tabla contiene la información sobre qué valores se usan para los modelos de forma cambiante (shapeshift) del druida, según la forma, la raza, la personalización del personaje y el género del personaje del jugador.

**Estructura**

| Field                               | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ShapeshiftID](#shapeshiftid)       | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [RaceID](#raceid)                   | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [CustomizationID](#customizationid) | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [GenderID](#genderid)               | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [ModelID](#modelid)                 | INT     | UNSIGNED   |     | NO   |         |       |         |

**Descripción de los campos**

### ShapeshiftID

| FormID | Description      |
| ------ | ---------------- |
| 1      | Cat Form         |
| 5      | Bear Form        |
| 8      | Dire Bear Form   |
| 27     | Epic Flight Form |
| 29     | Flight Form      |

### RaceID

| RaceID | Description |
| ------ | ----------- |
| 4      | Night Elf   |
| 6      | Tauren      |

Para `RaceID` puedes consultar la columna "ID" de [chrraces](chrraces).

### CustomizationID

Si eres un personaje de la Alianza (solo elfos de la noche con razas estándar), el ID de personalización se basa en el [color de pelo](characters#haircolor) de tu personaje.

Si eres un personaje de la Horda (solo taurens con razas estándar), el ID de personalización se basa en el [color de piel](characters#skin) de tu personaje.

### GenderID

| [GenderID](characters#gender) | Description      |
| ----------------------------- | ---------------- |
| 0                             | Masculino        |
| 1                             | Femenino         |
| 2                             | Cualquier género |

### ModelID

Consulta [creature_model_info](#creature_model_info#displayid)
