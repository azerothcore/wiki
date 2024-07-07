# pet\_levelstats

[<-Back-to:World](database-world)

**The \`pet\_levelstats\` table**

This table holds information on individual pet base stats based on level.

**Table Structure**

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

**Description of the fields**

### creature\_entry

The pet creature template ID. See creature\_template.entry

### level

The pet level.

### hp

The base health of the pet at currently selected [level](#level), calculated through core.

### mana

The base mana of the pet at currently selected [level](#level), calculated through core.

### armor

The base armor of the pet at currently selected [level](#level), calculated through core.

### str

The base strength of the pet at currently selected [level](#level), calculated through core.

### agi

The base agility of the pet at currently selected [level](#level), calculated through core.

### sta

The base stamina of the pet at currently selected [level](#level), calculated through core.

### inte

The base intellect of the pet at currently selected [level](#level), calculated through core.

### spi

The base spirit of the pet at currently selected [level](#level), calculated through core.
