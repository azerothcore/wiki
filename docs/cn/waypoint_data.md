# waypoint\_data

[<-返回至:World](database-world)

**\`waypoint\_data\` 表**

该表包含生物在其 creature addon 定义中直接使用的、用于路径点和路径点脚本的所有路径数据。关于路径点的通用信息，另请参见 [路径点信息](waypoints-information)。

**表结构**

| Field                                 | Type      | Attributes | Key | Null | Default |
| ------------------------------------- | --------- | ---------- | --- | ---- | ------- |
| [id](#id)                             | INT       | UNSIGNED   | PRI | NO   | 0       |
| [point](#point)                       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |
| [position\_x](#positionx)             | FLOAT     |            |     | NO   | 0       |
| [position\_y](#positiony)             | FLOAT     |            |     | NO   | 0       |
| [position\_z](#positionz)             | FLOAT     |            |     | NO   | 0       |
| [orientation](#orientation)           | FLOAT     |            |     | YES  | NULL    |
| [velocity](#velocity)                 | FLOAT     |            |     | NO   | 0       |
| [delay](#delay)                       | INT       | UNSIGNED   |     | NO   | 0       |
| [smoothTransition](#smoothtransition) | TINYINT   |            |     | NO   | 0       |
| [move\_type](#movetype)               | INT       |            |     | NO   | 0       |
| [action](#action)                     | INT       |            |     | NO   | 0       |
| [action\_chance](#actionchance)       | SMALLINT  |            |     | NO   | 100     |
| [wpguid](#wpguid)                     | INT       | UNSIGNED   |     | NO   | 0       |

**字段说明**

### id

每条路径的唯一 ID。

*TDB 分配 ID 的标准做法是将生物 GUID 乘以 10。*

*因此，对于 GUID 为 1234 的生物，其路径 ID 应为 12340。任何提交给 TDB 的路径点都应遵循这一标准。*

*不过，在创建自己的路径点时，这只是一个建议。只要为生物设置的 creature\_addon.path\_id 与这里选择的 ID 一致，这个 ID 可以是任何你想要的数值。*

### point

路径中每个点的唯一点 ID。从 1 开始，并随每条路径递增。

### position\_x

目标路径点的 X 坐标。

### position\_y

目标路径点的 Y 坐标。

### position\_z

目标路径点的 Z 坐标。

### orientation

生物的面朝方向。（北 = 0.0；南 = π（3.14159））

### velocity

覆盖生物在该路径点上的默认移动速度。设置为 `0` 以使用默认速度。

### delay

每个点之间的等待时间（以毫秒为单位）。

### smoothTransition

启用后，生物会沿着平滑的 catmullrom 样条曲线穿过路径点，而不是在每个点急停急转。可以通过 [waypoint\_data\_addon](waypoint_data_addon) 表添加自定义的中间样条点。

| 值    | 描述                                            |
| ----- | ----------------------------------------------- |
| 0     | 已禁用（默认）——生物在每个路径点处停留           |
| 1     | 已启用——路径点之间使用平滑的样条曲线             |

### move\_type

| 值    | 名称    | 描述                                                  |
| ----- | ------- | ----------------------------------------------------- |
| 0     | Walk    | 生物以步行速度移动。                                   |
| 1     | Run     | 生物以奔跑速度移动（默认）。                           |
| 2     | Land    | 将动画层级设置为地面（用于从飞行中降落时）。           |
| 3     | Takeoff | 将动画层级设置为悬停（用于起飞时）。                   |

### action

要执行的动作 ID。参见 [waypoint\_scripts.id](scripts#id)。

### action\_chance

动作发生的百分比（0-100%）。

### wpguid

该字段由核心使用，**不可**手动设置。

该字段保存的是当您为路径点启用可视化模式时，路径点视觉效果的 GUID。

### 示例行

| Id    | Point | Position\_x | Position\_y | Position\_z | Orientation | Velocity | Delay | SmoothTransition | Move\_type | Action | Action\_chance | wpguid |
| ----- | ----- | ----------- | ----------- | ----------- | ----------- | -------- | ----- | ---------------- | ---------- | ------ | -------------- | ------ |
| 20160 | 1     | -4998       | -1167       | 501657      | 0           | 0        | 10000 | 0                | 0          | 0      | 100            | 0      |
| 20160 | 2     | -4958.38    | -1199.34    | 501659      | 0           | 0        | 0     | 0                | 0          | 0      | 100            | 0      |
