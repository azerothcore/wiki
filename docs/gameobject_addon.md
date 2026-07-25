# gameobject_addon

[<-Back-to:World](database-world)

**The \`gameobject_addon\` table**

| Field                          | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------ | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]                      | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [parent_rotation0][2]          | FLOAT   |            |     | NO   | 0       |       |         |
| [parent_rotation1][3]          | FLOAT   |            |     | NO   | 0       |       |         |
| [parent_rotation2][4]          | FLOAT   |            |     | NO   | 0       |       |         |
| [parent_rotation3][5]          | FLOAT   |            |     | NO   | 1       |       |         |
| [invisibilityType][6]          | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [invisibilityValue][7]         | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #parent_rotation0
[3]: #parent_rotation1
[4]: #parent_rotation2
[5]: #parent_rotation3
[6]: #invisibilitytype
[7]: #invisibilityvalue

**Description of the fields**

### guid

[gameobject.guid](gameobject#guid)

### parent_rotation0

The X component of the quaternion rotation applied to the GameObject. Together with `parent_rotation1`, `parent_rotation2`, and `parent_rotation3`, this defines the object's orientation as a unit quaternion. Valid range: -1.0 to 1.0. Default is 0.

### parent_rotation1

The Y component of the quaternion rotation. Default is 0.

### parent_rotation2

The Z component of the quaternion rotation. Default is 0.

### parent_rotation3

The W (scalar) component of the quaternion rotation. Default is 1, which together with the other components set to 0 represents the identity quaternion (no rotation).

### invisibilityType

| Name                 | Value |
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

The detection value required to see this invisible gameobject. Works in conjunction with [invisibilityType](#invisibilitytype).
