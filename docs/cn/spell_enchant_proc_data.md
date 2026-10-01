# spell\_enchant\_proc\_data

[<-返回至:World](database-world)

**\`spell\_enchant\_proc\` 表**

`table-no-description`

**表结构**

| Field             | Type  | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ----- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]        | INT   | UNSIGNED   |     | NO   | NULL    |       |         |
| [customChance][2] | INT   | UNSIGNED   |     | NO   | 0       |       |         |
| [PPMChance][3]    | FLOAT | UNSIGNED   |     | NO   | 0       |       |         |
| [procEx][4]       | INT   | UNSIGNED   |     | NO   | 0       |       |         |
| [attributeMask][5] | INT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #entry
[2]: #customchance
[3]: #ppmchance
[4]: #procex
[5]: #attributemask

**字段说明**

### entry

来自 SpellItemEnchantment.dbc 的附魔 ID

### customChance

`field-no-description|2`

### PPMChance

值必须 >=0。如果该值不满足条件，SQL 将在 `spell_enchant_proc_data_chk_1` 上失败。

### procEx

`field-no-description|4`

### attributeMask

`field-no-description|5`
