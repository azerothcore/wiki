# playercreateinfo

[<-返回至:World](database-world)

**`playercreateinfo` 表**

该表保存了所有新建角色每种种族-职业组合的起始位置。

**表结构**

| Field            | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [race][1]        | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |         |
| [class][2]       | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |         |
| [map][3]         | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [zone][4]        | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [position_x][5]  | FLOAT     | SIGNED     |     | NO   | 0       |       |         |
| [position_y][6]  | FLOAT     | SIGNED     |     | NO   | 0       |       |         |
| [position_z][7]  | FLOAT     | SIGNED     |     | NO   | 0       |       |         |
| [orientation][8] | FLOAT     | SIGNED     |     | NO   | 0       |       |         |

[1]: #race
[2]: #class
[3]: #map
[4]: #zone
[5]: #positionx
[6]: #positiony
[7]: #positionz
[8]: #orientation

**字段说明**

### race

角色种族。`ChrRaces.dbc`

### class

角色职业。`ChrClasses.dbc`

### map

地图 ID。参见 [Map.dbc](map)

### zone

区域 ID。参见 [AreaTable.dbc](areatable)

### position_x

X 坐标。

### position_y

Y 坐标。

### position_z

Z 坐标。

### orientation

朝向。
