# spell\_pet\_auras

[<-Back-to:World](database-world.md)

**The \`spell\_pet\_auras\` table**

`table-no-description`

| Field         | Type         | Attributes | Key | Null | Default | Extra | Comment         |
|---------------|--------------|------------|-----|------|---------|-------|-----------------|
| [spell][1]    | MEDIUMINT(8) | unsigned   | PRI | NO   | NULL    |       | dummy spell id  |
| [effectId][2] | tinyint(3)   | unsigned   | PRI | NO   | 0       |       |                 |
| [pet][3]      | MEDIUMINT(8) | unsigned   | PRI | NO   | 0       |       | pet id; 0 = all |
| [aura][4]     | MEDIUMINT(8) | unsigned   |     | NO   | NULL    |       | pet aura id     |

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
