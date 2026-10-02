# creature\_classlevelstats

[<-Back-to:World](database-world)

**Table: creature\_classlevelstats's Structure**

This table contains the base values for creature health, mana, armor, attack power, ranged attack power, damage, and experience.

| Field                  | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [level][1]             | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [class][2]             | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [basehp0][3]           | INT     | UNSIGNED   |     | NO   | 1       |       |         |
| [basehp1][4]           | INT     | UNSIGNED   |     | NO   | 1       |       |         |
| [basehp2][5]           | INT     | UNSIGNED   |     | NO   | 1       |       |         |
| [basemana][6]          | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [basearmor][7]         | INT     | UNSIGNED   |     | NO   | 1       |       |         |
| [attackpower][8]       | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [rangedattackpower][9] | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [damage_base][10]      | FLOAT   | SIGNED     |     | NO   | 0       |       |         |
| [damage_exp1][11]      | FLOAT   | SIGNED     |     | NO   | 0       |       |         |
| [damage_exp2][12]      | FLOAT   | SIGNED     |     | NO   | 0       |       |         |
| [Strength][14]         | INT     | SIGNED     |     | NO   | 0       |       |         |
| [Agility][15]          | INT     | SIGNED     |     | NO   | 0       |       |         |
| [Stamina][16]          | INT     | SIGNED     |     | NO   | 0       |       |         |
| [Intellect][17]        | INT     | SIGNED     |     | NO   | 0       |       |         |
| [Spirit][18]           | INT     | SIGNED     |     | NO   | 0       |       |         |
| [comment][13]          | TEXT    |            |     | YES  | NULL    |       |         |

[1]: #level
[2]: #class
[3]: #basehp0
[4]: #basehp1
[5]: #basehp2
[6]: #basemana
[7]: #basearmor
[8]: #attackpower
[9]: #rangedattackpower
[10]: #damagebase
[11]: #damageexp1
[12]: #damageexp2
[13]: #comment
[14]: #strength
[15]: #agility
[16]: #stamina
[17]: #intellect
[18]: #spirit

**Description of the table's fields**

### level

Level of the creature.

### class

Class of the creature. This is a reference to the [unit\_class](creature_template#unitclass) field in the [creature\_template](creature_template) table.

### basehp0

Base health for the creature if creature\_template.exp value is set to 0. This value is multiplied by [creature\_template.HealthModifier](creature_template#healthmodifier)  to determine the creature's final health.

### basehp1

Base health for the creature if creature\_template.exp value is set to 1. This value is multiplied by [creature\_template.HealthModifier](creature_template#healthmodifier)  to determine the creature's final health.

### basehp2

Base health for the creature if creature\_template.exp value is set to 2. This value is multiplied by [creature\_template.HealthModifier](creature_template#healthmodifier)  to determine the creature's final health.

### basemana

Base mana for the creature. This value is multiplied by  [creature\_template.ManaModifier](creature_template#manamodifier) to determine the creature's final mana.

### basearmor

Base armor for the creature. This value is multiplied by [creature\_template.ArmorModifier](creature_template#armormodifier) to determine the creature's final armor.

### attackpower

Base attack power for the creature.

### rangedattackpower

Base ranged attack power for the creature.

### damage\_base

Modifier used to calculate the damage output of a creature. This field is used if a creature's [exp](creature_template#exp) is set to 0. See [DamageModifier](creature_template#damagemodifier) for more information.

### damage\_exp1

Modifier used to calculate the damage output of a creature. This field is used if a creature's [exp](creature_template#exp) is set to 1. See [DamageModifier](creature_template#damagemodifier) for more information.

### damage\_exp2

Modifier used to calculate the damage output of a creature. This field is used if a creature's [exp](creature_template#exp) is set to 2. See [DamageModifier](creature_template#damagemodifier) for more information.

### Strength

Base Strength for the creature at this level and class.

### Agility

Base Agility for the creature at this level and class.

### Stamina

Base Stamina for the creature at this level and class.

### Intellect

Base Intellect for the creature at this level and class.

### Spirit

Base Spirit for the creature at this level and class.

### comment

A comment describing the purpose of the record (entry).
