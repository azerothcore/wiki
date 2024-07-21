# gameobject_addon

[<-Back-to:World](database-world)

**The \`gameobject_addon\` table**

| Field                  | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]              | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [invisibilityType][2]  | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [invisibilityValue][3] | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #invisibilitytype
[3]: #invisibilityvalue

**Description of the fields**

### guid

[gameobject.guid](gameobject#guid)

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

field-no-description|3
