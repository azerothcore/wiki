# creature\_classlevelstats

[<-Back-to:World](database-world)

**Table: creature\_classlevelstats's Structure**

This table contains the base values for creature health, mana, armor, attack power, ranged attack power, damage, and experience.

| Field                                   | Type    |          | Null | Key | Default | Extra | Comment |
| :-------------------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [level](#level)                         | TINYINT | UNSIGNED | NO   | PRI |         |       |         |
| [class](#class)                         | TINYINT | UNSIGNED | NO   | PRI |         |       |         |
| [basehp0](#basehp0)                     | INT     | UNSIGNED | NO   |     | 1       |       |         |
| [basehp1](#basehp1)                     | INT     | UNSIGNED | NO   |     | 1       |       |         |
| [basehp2](#basehp2)                     | INT     | UNSIGNED | NO   |     | 1       |       |         |
| [basemana](#basemana)                   | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [basearmor](#basearmor)                 | INT     | UNSIGNED | NO   |     | 1       |       |         |
| [attackpower](#attackpower)             | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [rangedattackpower](#rangedattackpower) | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [damage_base](#damagebase)              | FLOAT   |          | NO   |     | 0       |       |         |
| [damage_exp1](#damageexp1)              | FLOAT   |          | NO   |     | 0       |       |         |
| [damage_exp2](#damageexp2)              | FLOAT   |          | NO   |     | 0       |       |         |
| [Strength](#strength)                   | INT     |          | NO   |     | 0       |       |         |
| [Agility](#agility)                     | INT     |          | NO   |     | 0       |       |         |
| [Stamina](#stamina)                     | INT     |          | NO   |     | 0       |       |         |
| [Intellect](#intellect)                 | INT     |          | NO   |     | 0       |       |         |
| [Spirit](#spirit)                       | INT     |          | NO   |     | 0       |       |         |
| [comment](#comment)                     | TEXT    |          | YES  |     | NULL    |       |         |

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
