# script\_waypoint

[<-返回至:World](database-world)

**`script\_waypoint` 表**

此表包含由脚本化 AI（`CreatureAI`）驱动的生物所使用的路径点路径。它是 [waypoint\_data](waypoint_data)（供生物通过其 [creature\_addon](creature_addon) 使用）和 [waypoints](waypoints)（供 [SmartAI](smart_scripts) 使用）的脚本化 AI 对应表。有关路径点的一般信息，另请参阅 [路径点信息](waypoints-information)。

**表结构**

| Field                             | Type | Attributes | Key | Null | Default |
| --------------------------------- | ---- | ---------- | --- | ---- | ------- |
| [entry](#entry)                   | INT  | UNSIGNED   | PRI | NO   | 0       |
| [pointid](#pointid)               | INT  | UNSIGNED   | PRI | NO   | 0       |
| [location\_x](#locationx)         | FLOAT |           |     | NO   | 0       |
| [location\_y](#locationy)         | FLOAT |           |     | NO   | 0       |
| [location\_z](#locationz)         | FLOAT |           |     | NO   | 0       |
| [waittime](#waittime)             | INT  | UNSIGNED   |     | NO   | 0       |
| [point\_comment](#pointcomment)   | TEXT |            |     | YES  | NULL    |

**字段说明**

### entry

此路径所属生物的 [creature\_template.entry](creature_template#entry)。它与 `pointid` 共同构成主键。

### pointid

此点在路径内的顺序编号，从 1 开始。它与 `entry` 共同构成主键。

### location_x

路径点的 X 坐标。

### location_y

路径点的 Y 坐标。

### location_z

路径点的 Z 坐标。

### waittime

生物在移动到下一个点之前，在此路径点等待的毫秒数。

### point_comment

描述该路径点的可选自由文本注释。
