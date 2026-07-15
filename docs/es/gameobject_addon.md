# gameobject_addon

[<-Volver a: World](database-world)

**Tabla \`gameobject_addon\`**

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

**Descripción de los campos**

### guid

[gameobject.guid](gameobject#guid)

### parent_rotation0

El componente X de la rotación cuaternión aplicada al GameObject. Junto con `parent_rotation1`, `parent_rotation2` y `parent_rotation3`, esto define la orientación del objeto como un cuaternión unitario. Rango válido: -1.0 a 1.0. El valor por defecto es 0.

### parent_rotation1

El componente Y de la rotación cuaternión. El valor por defecto es 0.

### parent_rotation2

El componente Z de la rotación cuaternión. El valor por defecto es 0.

### parent_rotation3

El componente W (escalar) de la rotación cuaternión. El valor por defecto es 1, que junto con los demás componentes puestos a 0 representa el cuaternión identidad (sin rotación).

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

El valor de detección requerido para ver este gameobject invisible. Funciona en conjunto con [invisibilityType](#invisibilitytype).
