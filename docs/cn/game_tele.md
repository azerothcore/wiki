# game\_tele

[<-返回:世界](database-world)

**表结构**

该表包含一系列传送位置，可在游戏内通过 *.tele* 命令使用。该表中的条目可以手动添加/删除，也可以通过 *.tele add* 和 *.tele delete* 命令进行添加/删除。

| 字段 (Field)        | 类型 (Type)   | 属性 (Attributes) | 键 (Key) | 空 (Null) | 默认 (Default) | 额外 (Extra)      |
| ------------------- | ------------- | ----------------- | -------- | --------- | -------------- | ----------------- |
| [id][1]             | MEDIUMINT     | UNSIGNED          | PRI      | NO        | NULL           | Auto increment    |
| [position_x][2]     | FLOAT         | SIGNED            |          | NO        | 0              |                   |
| [position_y][3]     | FLOAT         | SIGNED            |          | NO        | 0              |                   |
| [position_z][4]     | FLOAT         | SIGNED            |          | NO        | 0              |                   |
| [orientation][5]    | FLOAT         | SIGNED            |          | NO        | 0              |                   |
| [map][6]            | SMALLINT      | UNSIGNED          |          | NO        | 0              |                   |
| [name][7]           | VARCHAR(100)  | SIGNED            |          | NO        | NULL           |                   |

[1]: #id
[2]: #positionx
[3]: #positiony
[4]: #positionz
[5]: #orientation
[6]: #map
[7]: #name

**字段说明**

### id

传送位置的 ID。该编号对每个已添加的位置都是唯一的。

### position\_x

传送位置的 x 轴坐标。可以通过使用 *.gps* 命令获得。

### position\_y

传送位置的 y 轴坐标。可以通过使用 *.gps* 命令获得。

### position\_z

传送位置的 z 轴坐标。可以通过使用 *.gps* 命令获得。

### orientation

玩家到达传送位置后将面对的方向。可以通过使用 *.gps* 命令获得。

（北 = 0，南 = 3.14159）

### map

该位置的地图 ID。所有区域的 ID 参见 [Map DBC 文件](map)。

### name

传送位置的描述性名称。名称中*不能*包含任何空格。同时也不建议使用句点、逗号、斜杠等特殊字符……

### 示例

| id  | position_x | position_y | position_z | orientation | map | name         |
| --- | ---------- | ---------- | ---------- | ----------- | --- | ------------ |
| 10  | 2799.46    | 847.549    | 111.842    | 0.509892    | 0   | AgamandMills |
| 11  | -7040.08   | -3342.15   | 241.667    | 0.82338     | 0   | AgmondsEnd   |
| 12  | 451.572    | -3342.23   | 119.689    | 0.772541    | 0   | AgolWatha    |
| 13  | -2681.4    | -4787.21   | 16.0751    | 4.69276     | 1   | AlcazIsland  |
| 14  | -1746.58   | 5780.03    | 146.44     | 1.30629     | 530 | AldorRise    |
