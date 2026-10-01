# areatrigger

[<-返回:World](database-world)

**\`areatrigger\` 表**

此表包含地图中特定坐标处事件的触发器点。

[如何将 DBC 数据导入我的数据库](how-to-import-dbc-data-in-db)

**表结构**

| Field       | Type  | Attributes | Key | Null | Default | Extra          | Comment                                              |
| ----------- | ----- | ---------- | --- | ---- | ------- | -------------- | ---------------------------------------------------- |
| entry       | INT   | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |                                                      |
| map         | INT   | UNSIGNED   |     | NO   | 0       |                |                                                      |
| x           | FLOAT |            |     | NO   | 0       |                |                                                      |
| y           | FLOAT |            |     | NO   | 0       |                |                                                      |
| z           | FLOAT |            |     | NO   | 0       |                |                                                      |
| radius      | FLOAT |            |     | NO   | 0       |                | 似乎是一个以 x,y,z 为中心、以码为单位大小的盒体        |
| length      | FLOAT |            |     | NO   | 0       |                | 最常在 size 为 0 时使用，但并非总是如此                |
| width       | FLOAT |            |     | NO   | 0       |                | 最常在 size 为 0 时使用，但并非总是如此                |
| height      | FLOAT |            |     | NO   | 0       |                | 最常在 size 为 0 时使用，但并非总是如此                |
| orientation | FLOAT |            |     | NO   | 0       |                | 最常在 size 为 0 时使用，但并非总是如此                |

**字段描述**

### Entry

这只是一个自动计数器，为每个触发器分配一个值以便对其进行编号。

### Map

此字段根据 ID 引用某个特定地图（例如，ID 30 引用艾尔文森林 Elwynn Forest）

### X、Y 和 Z

包含三个 3D 维度的坐标。

### Radius

包含触发器的激活半径。

### Length、Width、Height 和 Orientation

这些字段包含某个给定触发器的物理和行为值。

### 示例

| entry | map | x        | y        | z       | radius | length | width | height | orientation |
| ----- | --- | -------- | -------- | ------- | ------ | ------ | ----- | ------ | ----------- |
| 45    | 0   | 2924.38  | -798.429 | 161.611 | 8      | 0      | 0     | 0      | 0           |
| 71    | 0   | -10645.9 | 1179.06  | 48.1781 | 27     | 0      | 0     | 0      | 0           |
| 78    | 0   | -11208.5 | 1685.34  | 25.7612 | 7      | 0      | 0     | 0      | 0           |
| 84    | 0   | 16449.9  | 16393.2  | 69.4444 | 15     | 0      | 0     | 0      | 0           |
| 87    | 0   | -9077.34 | -552.925 | 60.3476 | 30     | 0      | 0     | 0      | 0           |
