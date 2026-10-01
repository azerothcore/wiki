# gameobject_addon

[<-返回:World](database-world)

**\`gameobject_addon\` 表**

| 字段                          | 类型    | 属性     | 键 | 空 | 默认值 | 额外 | 注释 |
| ------------------------------ | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]                      | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [parent_rotation0][2]          | FLOAT   |            |     | NO   | 0       |       |         |
| [parent_rotation1][3]          | FLOAT   |            |     | NO   | 0       |       |         |
| [parent_rotation2][4]          | FLOAT   |            |     | NO   | 0       |       |         |
| [parent_rotation3][5]          | FLOAT   |            |     | NO   | 1       |       |         |
| [invisibilityType][6]          | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [invisibilityValue][7]         | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #parentrotation0
[3]: #parentrotation1
[4]: #parentrotation2
[5]: #parentrotation3
[6]: #invisibilitytype
[7]: #invisibilityvalue

**字段说明**

### guid

[gameobject.guid](gameobject#guid)

### parent_rotation0

应用于游戏对象（GameObject）的四元数旋转的 X 分量。与 `parent_rotation1`、`parent_rotation2` 和 `parent_rotation3` 一起，以单位四元数的形式定义对象的朝向。有效范围：-1.0 到 1.0。默认值为 0。

### parent_rotation1

四元数旋转的 Y 分量。默认值为 0。

### parent_rotation2

四元数旋转的 Z 分量。默认值为 0。

### parent_rotation3

四元数旋转的 W（标量）分量。默认值为 1，当其他分量都设置为 0 时，表示单位四元数（无旋转）。

### invisibilityType

| 名称                 | 值 |
| :------------------- | :---- |
| INVISIBILITY_GENERAL | 0     |
| INVISIBILITY_UNK1    | 1     |
| INVISIBILITY_UNK2    | 2     |
| INVISIBILITY_TRAP    | 3     |
| INVISIBILITY_UNK4    | 4     |
| INVISIBILITY_UNK5    | 5     |
| INVISIBILITY_DRUNK   | 6     |
| INVISIBILITY_UNK7    | 7     |
| INVISIBILITY_UNK8    | 8     |
| INVISIBILITY_UNK9    | 9     |
| INVISIBILITY_UNK10   | 10    |
| INVISIBILITY_UNK11   | 11    |

### invisibilityValue

看见此隐形游戏对象所需的侦测值。与 [invisibilityType](#invisibilitytype) 配合使用。
