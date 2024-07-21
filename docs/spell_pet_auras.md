# spell\_pet\_auras

[<-Back-to:World](database-world)

**The \`spell\_pet\_auras\` table**

`table-no-description`

**Table Structure**

| Field         | Type      | Attributes | Key | Null | Default | Extra | Comment         |
| ------------- | --------- | ---------- | --- | ---- | ------- | ----- | --------------- |
| [spell][1]    | MEDIUMINT | UNSIGNED   | PRI | NO   | NULL    |       | dummy spell id  |
| [effectId][2] | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |                 |
| [pet][3]      | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | pet id; 0 = all |
| [aura][4]     | MEDIUMINT | UNSIGNED   |     | NO   | NULL    |       | pet aura id     |

[1]: #spell
[2]: #effectid
[3]: #pet
[4]: #aura

**Description of the fields**

### spell

`field-no-description|1`

### effectId

`field-no-description|2`

### pet

`field-no-description|3`

### aura

`field-no-description|4`
