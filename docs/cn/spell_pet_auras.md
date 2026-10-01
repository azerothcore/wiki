# spell\_pet\_auras

[<-返回至:World](database-world)

**\`spell\_pet\_auras\` 表**

`table-no-description`

**表结构**

| Field         | Type      | Attributes | Key | Null | Default | Extra | Comment         |
| ------------- | --------- | ---------- | --- | ---- | ------- | ----- | --------------- |
| [spell][1]    | MEDIUMINT | UNSIGNED   | PRI | NO   | NULL    |       | 假法术（dummy spell）id |
| [effectId][2] | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |                 |
| [pet][3]      | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | 宠物 id；0 = 所有 |
| [aura][4]     | MEDIUMINT | UNSIGNED   |     | NO   | NULL    |       | 宠物光环 id     |

[1]: #spell
[2]: #effectid
[3]: #pet
[4]: #aura

**字段说明**

### spell

`field-no-description|1`

### effectId

`field-no-description|2`

### pet

`field-no-description|3`

### aura

`field-no-description|4`
