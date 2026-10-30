# pet\_levelstats

[<-Back-to:World](database-world)

**The \`pet\_levelstats\` table**

This table holds information on individual pet base stats based on level.

**Table: pet\_levelstats's Structure**

| Field                             | Type    |          | Null | Key | Default | Extra | Comment |
| :-------------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [creature\_entry](#creatureentry) | INT     | UNSIGNED | NO   | PRI |         |       |         |
| [level](#level)                   | TINYINT | UNSIGNED | NO   | PRI |         |       |         |
| [hp](#hp)                         | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [mana](#mana)                     | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [armor](#armor)                   | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [str](#str)                       | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [agi](#agi)                       | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [sta](#sta)                       | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [inte](#inte)                     | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [spi](#spi)                       | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [min\_dmg](#mindmg)               | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [max\_dmg](#maxdmg)               | INT     | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

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

### min\_dmg

The minimum base melee damage of the pet at the currently selected [level](#level).

### max\_dmg

The maximum base melee damage of the pet at the currently selected [level](#level).
