# pet\_levelstats

[<-Volver a:World](database-world)

**Tabla \`pet\_levelstats\`**

Esta tabla contiene información sobre las estadísticas base individuales de las mascotas según el nivel.

**Estructura**

| Field                             | Type      | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [creature\_entry](#creatureentry) | MEDIUMINT | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [level](#level)                   | TINYINT   | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [hp](#hp)                         | SMALLINT  | UNSIGNED   |     | NO   | NULL    |       |         |
| [mana](#mana)                     | SMALLINT  | UNSIGNED   |     | NO   | NULL    |       |         |
| [armor](#armor)                   | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [str](#str)                       | SMALLINT  | UNSIGNED   |     | NO   | NULL    |       |         |
| [agi](#agi)                       | SMALLINT  | UNSIGNED   |     | NO   | NULL    |       |         |
| [sta](#sta)                       | SMALLINT  | UNSIGNED   |     | NO   | NULL    |       |         |
| [inte](#inte)                     | SMALLINT  | UNSIGNED   |     | NO   | NULL    |       |         |
| [spi](#spi)                       | SMALLINT  | UNSIGNED   |     | NO   | NULL    |       |         |

**Descripción de los campos**

### creature\_entry

El ID de la creature template de la mascota. Ver creature\_template.entry

### level

El nivel de la mascota.

### hp

La vida base de la mascota en el [nivel](#level) seleccionado actualmente, calculada a través del core.

### mana

El maná base de la mascota en el [nivel](#level) seleccionado actualmente, calculado a través del core.

### armor

La armadura base de la mascota en el [nivel](#level) seleccionado actualmente, calculada a través del core.

### str

La fuerza base de la mascota en el [nivel](#level) seleccionado actualmente, calculada a través del core.

### agi

La agilidad base de la mascota en el [nivel](#level) seleccionado actualmente, calculada a través del core.

### sta

El aguante base de la mascota en el [nivel](#level) seleccionado actualmente, calculado a través del core.

### inte

El intelecto base de la mascota en el [nivel](#level) seleccionado actualmente, calculado a través del core.

### spi

El espíritu base de la mascota en el [nivel](#level) seleccionado actualmente, calculado a través del core.
