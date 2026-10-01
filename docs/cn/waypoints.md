# waypoints

[<-返回至:World](database-world)

**\`waypoints\` 表**

由 [SAI](smart_scripts) 使用。

包含路径点数据，使生物能够移动到特定的 X、Y 和 Z 坐标。关于路径点的通用信息，另请参见 [路径点信息](waypoints-information)。

**表结构**

| Field                            | Type      | Attributes | Key | Null | Default |
| -------------------------------- | --------- | ---------- | --- | ---- | ------- |
| [entry](#entry)                  | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |
| [pointid](#pointid)              | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |
| [position\_x](#positionx)        | FLOAT     |            |     | NO   | 0       |
| [position\_y](#positiony)        | FLOAT     |            |     | NO   | 0       |
| [position\_z](#positionz)        | FLOAT     |            |     | NO   | 0       |
| [orientation](#orientation)      | FLOAT     |            |     | YES  | NULL    |
| [delay](#delay)                  | INT       | UNSIGNED   |     | NO   | 0       |
| [point\_comment](#pointcomment)  | text      |            |     | YES  | NULL    |

**字段说明**

#### entry

路径 ID。分配 ID 的标准做法是 [creature\_template.entry](creature_template#entry) * 100，但这里可以使用任意随机数字。

#### pointid

每个路径点的唯一 ID。从 1 开始，并随每个路径点递增。

#### position\_x

目标路径点的 X 坐标。

#### position\_y

目标路径点的 Y 坐标。

#### position\_z

目标路径点的 Z 坐标。

#### orientation

生物在该路径点处应有的朝向。`NULL` 表示保持朝向不变。

#### delay

生物在该路径点移动到下一个点之前等待的时间（以毫秒为单位）。

#### point\_comment

文本注释。

### 示例行

| entry | pointid | position\_x | position\_y | position\_z | point\_comment           |
| ----- | ------- | ----------- | ----------- | ----------- | ------------------------ |
| 16208 | 1       | 6647.83     | -6344.92    | 9.13345     | Apothecary Enith 点 1    |
| 16208 | 2       | 6657.92     | -6345.96    | 15.3468     | Apothecary Enith 点 2    |

ID 为 16208 的生物现在将有 2 个路径点，首先它会移动到 pointid 1，当它到达该 XYZ 位置后，会再移动到 pointid 2。注释有助于明确该 ID 属于哪个生物。
