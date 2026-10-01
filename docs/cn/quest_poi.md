# quest\_poi

[<-返回至:World](database-world)

**`quest\_poi` 表**

来源于嗅探（sniffs）。

**表结构**

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
| [VerifiedBuild][9]  | INT  |            |     | YES  | NULL    |       |         |

[1]: #questid
[2]: #id
[3]: #objectiveindex
[4]: #mapid
[5]: #worldmapareaid
[6]: #floor
[7]: #priority
[8]: #flags
[9]: #verifiedbuild

**字段说明**

### QuestID

来自 [quest\_template.id](quest_template#id) 的任务 ID。

### id

用于对 quest\_poi\_points.id 中的多条记录进行分组，它是 POI 的 ID。

### ObjectiveIndex

如果为 -1，则表示玩家可以完成任务时 NPC 的位置。

### MapID

来自 [Map.dbc](map) 的地图 ID。

### WorldMapAreaId

来自 [WorldMapArea.dbc](https://wowdev.wiki/DB/WorldMapArea) 的 ID。

### Floor

这是 POI 的 [AreaTable.dbc](areatable) 中的 ID。

### Priority

`field-no-description|7`

### Flags

`field-no-description|8`

### VerifiedBuild

验证此行所依据的客户端构建（来自 WDB/ADB 提取）。如不适用则为 `NULL`。
