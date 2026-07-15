# spell\_enchant\_proc\_data

[<-Volver a: World](database-world)

**Tabla \`spell\_enchant\_proc\`**

`tabla-sin-descripción`

**Estructura**

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

**Descripción de los campos**

### entry

ID de encantamiento de SpellItemEnchantment.dbc

### customChance

`campo-sin-descripción|2`

### PPMChance

El valor debe ser >=0. Si el valor no cumple la condición, el SQL fallará en `spell_enchant_proc_data_chk_1`.

### procEx

`campo-sin-descripción|4`
