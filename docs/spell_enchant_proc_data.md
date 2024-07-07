# spell\_enchant\_proc\_data

[<-Back-to:World](database-world)

**The \`spell\_enchant\_proc\` table**

`table-no-description`

**Table Structure**

| Field             | Type  | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ----- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]        | INT   | UNSIGNED   |     | NO   | NULL    |       |         |
| [customChance][2] | INT   | UNSIGNED   |     | NO   | 0       |       |         |
| [PPMChance][3]    | FLOAT | UNSIGNED   |     | NO   | 0       |       |         |
| [proxEx][4]       | FLOAT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #entry
[2]: #customchance
[3]: #ppmchance
[4]: #proxex

**Description of the fields**

### entry

Enchantment ID from SpellItemEnchantment.dbc

### customChance

`field-no-description|2`

### PPMChance

Value must be >=0. If the value does not meet the condition the SQL will fail on `spell_enchant_proc_data_chk_1`.

### procEx

`field-no-description|4`
