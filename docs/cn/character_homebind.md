# character\_homebind

[<-返回:Characters](database-characters)

**\`character\_homebind\` 表**

包含角色使用炉石（Hearthstone）时被传送到的位置信息。

**表结构**

| Field       | Type        | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]   | INT         | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [mapId][2]  | SMALLINT    | UNSIGNED   |     | NO   | 0       |       | Map Identifier           |
| [zoneId][3] | SMALLINT    | UNSIGNED   |     | NO   | 0       |       | Zone Identifier          |
| [posX][4]   | FLOAT       | SIGNED     |     | NO   | 0       |       |                          |
| [posY][5]   | FLOAT       | SIGNED     |     | NO   | 0       |       |                          |
| [posZ][6]   | FLOAT       | SIGNED     |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #mapid
[3]: #zoneid
[4]: #posx
[5]: #posy
[6]: #posz

**字段说明**

### guid

角色的 GUID。参见 [characters.guid](characters#guid)。

### mapId

角色被传送到的地图 ID。参见 [Map.dbc](map) 第 1 列。

### zoneId

角色被传送到的区域 ID。参见 [AreaTable.dbc](areatable) 第 1 列。

### posX

角色被传送到的 X 坐标。

### posY

角色被传送到的 Y 坐标。

### posZ

角色被传送到的 Z 坐标。
