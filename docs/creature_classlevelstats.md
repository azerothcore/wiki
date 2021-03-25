# creature\_classlevelstats

**Table Structure**

This table contains the base values for creature health, mana, armor, attack power, ranged attack power, damage, and experience.

| Field                  | Type        | Attributes | Null | Default | Extra | Comment |
|------------------------|-------------|------------|------|---------|-------|---------|
| [level][1]             | tinyint(3)  | unsigned   | NO   |         |       |         |
| [class][2]             | tinyint(3)  | unsigned   | NO   |         |       |         |
| [basehp0][3]           | smallint(5) | unsigned   | NO   |         |       |         |
| [basehp1][4]           | smallint(5) | unsigned   | NO   |         |       |         |
| [basehp2][5]           | smallint(5) | unsigned   | NO   |         |       |         |
| [basemana][6]          | smallint(5) | unsigned   | NO   |         |       |         |
| [basearmor][7]         | smallint(5) | unsigned   | NO   |         |       |         |
| [attackpower][8]       | smallint(5) | unsigned   | NO   |         |       |         |
| [rangedattackpower][9] | smallint(5) | unsigned   | NO   |         |       |         |
| [damage_base][10]      | float       |            | NO   |         |       |         |
| [damage_exp1][11]      | float       |            | NO   |         |       |         |
| [damage_exp2][12]      | float       |            | NO   |         |       |         |
| [comment][13]          | text        |            | YES  | NULL    |       |         |

[1]: #level
[2]: #class
[3]: #basehp0
[4]: #basehp1
[5]: #basehp2
[6]: #basemana
[7]: #basearmor
[8]: #attackpower
[9]: #rangedattackpower
[10]: #damage_base
[11]: #damage_exp1
[12]: #damage_exp2
[13]: #comment

**Field Descriptions**

### level

Level of the creature.

### class

Class of the creature. This is a reference to the [unit\_class](creature_template#creature_template-unit_class) field in the [creature\_template](creature_template) table.

### basehp0

Base health for the creature if creature\_template.exp value is set to 0. This value is multiplied by [creature\_template.Health\_mod](creature_template#creature_template-Health_mod)  to determine the creature's final health.

### basehp1

Base health for the creature if creature\_template.exp value is set to 1. This value is multiplied by [creature\_template.Health\_mod](creature_template#creature_template-Health_mod)  to determine the creature's final health.

### basehp2

Base health for the creature if creature\_template.exp value is set to 2. This value is multiplied by [creature\_template.Health\_mod](creature_template#creature_template-Health_mod)  to determine the creature's final health.

### basemana

Base mana for the creature. This value is multiplied by  [creature\_template.Mana\_mod](creature_template#creature_template-Mana_mod) to determine the creature's final mana.

### basearmor

Base armor for the creature. This value is multiplied by creature\_template.Armor\_mod to determine the creature's final armor.

### attackpower

Base attack power for the creature.

### rangedattackpower

Base ranged attack power for the creature.

### damage\_base

Modifier used to calculate the damage output of a creature. This field is used if a creature's [exp](http://www.azerothcore.org/wiki/creature_template#exp) is set to 0. See [DamageModifier](http://www.azerothcore.org/wiki/creature_template#DamageModifier) for more information.

### damage\_exp1

Modifier used to calculate the damage output of a creature. This field is used if a creature's [exp](http://www.azerothcore.org/wiki/creature_template#exp) is set to 1. See [DamageModifier](http://www.azerothcore.org/wiki/creature_template#DamageModifier) for more information.

### damage\_exp2

Modifier used to calculate the damage output of a creature. This field is used if a creature's [exp](http://www.azerothcore.org/wiki/creature_template#exp) is set to 2. See [DamageModifier](http://www.azerothcore.org/wiki/creature_template#DamageModifier) for more information.

### comment

A comment describing the purpose of the record (entry).
