# points\_of\_interest

[<-返回至:World](database-world)

**\`points\_of\_interest\` 表**

`table-no-description`

**表结构**

| Field           | Type      | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]         | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [PositionX][2]  | FLOAT     | SIGNED     |     | NO   | 0       |       |         |
| [PositionY][3]  | FLOAT     | SIGNED     |     | NO   | 0       |       |         |
| [Icon][4]       | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [Flags][5]      | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [Importance][6] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [Name][7]       | text      |            |     | NO   | NULL    |       |         |

[1]: #id
[2]: #positionx
[3]: #positiony
[4]: #icon
[5]: #flags
[6]: #importance
[7]: #name

**字段说明**

### ID

`field-no-description|1`

### PositionX

`field-no-description|2`

### PositionY

`field-no-description|3`

### icon

| Icon                      | Value | Description           |
| ------------------------- | ----- | ------------------------- |
| ICON\_POI\_BLANK          | 0     | 空白（不可见）        |
| ICON\_POI\_GREY\_AV\_MINE | 1     | 灰色矿车              |
| ICON\_POI\_RED\_AV\_MINE  | 2     | 红色矿车              |
| ICON\_POI\_BLUE\_AV\_MINE | 3     | 蓝色矿车              |
| ICON\_POI\_BWTOMB         | 4     | 蓝白墓碑              |
| ICON\_POI\_SMALL\_HOUSE   | 5     | 小房子                |
| ICON\_POI\_GREYTOWER      | 6     | 灰色塔                |
| ICON\_POI\_REDFLAG        | 7     | 带黄色感叹号的红旗    |
| ICON\_POI\_TOMBSTONE      | 8     | 普通墓碑（棕色）      |
| ICON\_POI\_BWTOWER        | 9     | 蓝白塔                |
| ICON\_POI\_REDTOWER       | 10    | 红塔                  |
| ICON\_POI\_BLUETOWER      | 11    | 蓝塔                  |
| ICON\_POI\_RWTOWER        | 12    | 红白塔                |
| ICON\_POI\_REDTOMB        | 13    | 红色墓碑              |
| ICON\_POI\_RWTOMB         | 14    | 红白墓碑              |
| ICON\_POI\_BLUETOMB       | 15    | 蓝色墓碑              |
| ICON\_POI\_16             | 16    | 灰色 ?                |
| ICON\_POI\_17             | 17    | 蓝白 ?                |
| ICON\_POI\_18             | 18    | 蓝色 ?                |
| ICON\_POI\_19             | 19    | 红白 ?                |
| ICON\_POI\_20             | 20    | 红色 ?                |
| ICON\_POI\_GREYLOGS       | 21    | 灰色原木              |
| ICON\_POI\_BWLOGS         | 22    | 蓝白原木              |
| ICON\_POI\_BLUELOGS       | 23    | 蓝色原木              |
| ICON\_POI\_RWLOGS         | 24    | 红白原木              |
| ICON\_POI\_REDLOGS        | 25    | 红色原木              |
| ICON\_POI\_26             | 26    | 灰色 ?                |
| ICON\_POI\_27             | 27    | 蓝白 ?                |
| ICON\_POI\_28             | 28    | 蓝色 ?                |
| ICON\_POI\_29             | 29    | 红白 ?                |
| ICON\_POI\_30             | 30    | 红色 ?                |
| ICON\_POI\_GREYHOUSE      | 31    | 灰色房屋              |
| ICON\_POI\_BWHOUSE        | 32    | 蓝白房屋              |
| ICON\_POI\_BLUEHOUSE      | 33    | 蓝色房屋              |
| ICON\_POI\_RWHOUSE        | 34    | 红白房屋              |
| ICON\_POI\_REDHOUSE       | 35    | 红色房屋              |
| ICON\_POI\_GREYHORSE      | 36    | 灰马                  |
| ICON\_POI\_BWHORSE        | 37    | 蓝白马                |
| ICON\_POI\_BLUEHORSE      | 38    | 蓝马                  |
| ICON\_POI\_RWHORSE        | 39    | 红白马                |
| ICON\_POI\_REDHORSE       | 40    | 红马                  |

### Flags

`field-no-description|5`

### Importance

`field-no-description|6`

### Name

显示给玩家的兴趣点名称。
