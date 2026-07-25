# quest\_poi

[<-Volver a: World](database-world)

**Tabla \`quest\_poi\`**

Proviene de sniffs.

**Estructura**

| Field               | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [QuestID][1]        | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [id][2]             | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [ObjectiveIndex][3] | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [MapID][4]          | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [WorldMapAreaId][5] | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [Floor][6]          | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [Priority][7]       | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [Flags][8]          | INT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #questid
[2]: #id
[3]: #objectiveindex
[4]: #mapid
[5]: #worldmapareaid
[6]: #floor
[7]: #priority
[8]: #flags

**Descripción de los campos**

### QuestID

El ID de misión de [quest\_template.id](quest_template#id)

### id

Se usa para agrupar múltiples entradas de quest\_poi\_points.id; es el id del POI.

### ObjectiveIndex

si es -1, entonces es la posición del npc donde puedes completar la misión

### MapID

El id del mapa de [Map.dbc](map)

### WorldMapAreaId

El ID de [WorldMapArea.dbc](worldmaparea).

### Floor

Este es el ID de [AreaTable.dbc](areatable) del POI.

### Priority

`campo-sin-descripción|7`

### Flags

`campo-sin-descripción|8`
