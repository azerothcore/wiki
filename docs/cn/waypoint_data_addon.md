# waypoint\_data\_addon

[<-返回至:World](database-world)

**\`waypoint\_data\_addon\` 表**

为在 [waypoint\_data](waypoint_data) 中设置了 `smoothTransition = 1` 的路径点路径提供自定义的中间样条插值点。这些点决定了生物在主路径点之间所遵循的 catmullrom 样条曲线的形状。

**表结构**

| Field                                   | Type | Attributes | Key | Null | Default |
| --------------------------------------- | ---- | ---------- | --- | ---- | ------- |
| [PathID](#pathid)                       | INT  | UNSIGNED   | PRI | NO   |         |
| [PointID](#pointid)                     | INT  | UNSIGNED   | PRI | NO   |         |
| [SplinePointIndex](#splinepointindex)   | INT  | UNSIGNED   | PRI | NO   |         |
| [PositionX](#positionx)                 | FLOAT |           |     | NO   | 0       |
| [PositionY](#positiony)                 | FLOAT |           |     | NO   | 0       |
| [PositionZ](#positionz)                 | FLOAT |           |     | NO   | 0       |

**字段说明**

### PathID

路径点路径 ID。引用 [waypoint\_data.id](waypoint_data#id)。

### PointID

路径点编号。引用 [waypoint\_data.point](waypoint_data#point)。

### SplinePointIndex

该中间样条点在所引用的路径点与其下一个路径点之间这一段内的索引。通过递增此索引，可以为每个路径点段定义多个中间点。

### PositionX

中间样条点的 X 坐标。

### PositionY

中间样条点的 Y 坐标。

### PositionZ

中间样条点的 Z 坐标。
