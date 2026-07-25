# spell\_pet\_auras

[<-Volver a: World](database-world)

**Tabla \`spell\_pet\_auras\`**

`tabla-sin-descripción`

**Estructura**

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

**Descripción de los campos**

### spell

`campo-sin-descripción|1`

### effectId

`campo-sin-descripción|2`

### pet

`campo-sin-descripción|3`

### aura

`campo-sin-descripción|4`
