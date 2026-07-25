# creature\_classlevelstats

**Estructura**

Esta tabla contiene los valores base de vida, maná, armadura, poder de ataque, poder de ataque a distancia, daño y experiencia de las criaturas.

| Field                  | Type     | Attributes | Null | Default | Extra | Comment |
| ---------------------- | -------- | ---------- | ---- | ------- | ----- | ------- |
| [level][1]             | TINYINT  | UNSIGNED   | NO   |         |       |         |
| [class][2]             | TINYINT  | UNSIGNED   | NO   |         |       |         |
| [basehp0][3]           | SMALLINT | UNSIGNED   | NO   |         |       |         |
| [basehp1][4]           | SMALLINT | UNSIGNED   | NO   |         |       |         |
| [basehp2][5]           | SMALLINT | UNSIGNED   | NO   |         |       |         |
| [basemana][6]          | SMALLINT | UNSIGNED   | NO   |         |       |         |
| [basearmor][7]         | SMALLINT | UNSIGNED   | NO   |         |       |         |
| [attackpower][8]       | SMALLINT | UNSIGNED   | NO   |         |       |         |
| [rangedattackpower][9] | SMALLINT | UNSIGNED   | NO   |         |       |         |
| [damage_base][10]      | FLOAT    |            | NO   |         |       |         |
| [damage_exp1][11]      | FLOAT    |            | NO   |         |       |         |
| [damage_exp2][12]      | FLOAT    |            | NO   |         |       |         |
| [comment][13]          | text     |            | YES  | NULL    |       |         |

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

**Descripción de los campos**

### level

Nivel de la criatura.

### class

Clase de la criatura. Es una referencia al campo [unit\_class](creature_template#unitclass) en la tabla [creature\_template](creature_template).

### basehp0

Vida base de la criatura si el valor creature\_template.exp está en 0. Este valor se multiplica por [creature\_template.Health\_mod](creature_template#healthmodifier) para determinar la vida final de la criatura.

### basehp1

Vida base de la criatura si el valor creature\_template.exp está en 1. Este valor se multiplica por [creature\_template.Health\_mod](creature_template#healthmodifier) para determinar la vida final de la criatura.

### basehp2

Vida base de la criatura si el valor creature\_template.exp está en 2. Este valor se multiplica por [creature\_template.Health\_mod](creature_template#healthmodifier) para determinar la vida final de la criatura.

### basemana

Maná base de la criatura. Este valor se multiplica por [creature\_template.Mana\_mod](creature_template#manamodifier) para determinar el maná final de la criatura.

### basearmor

Armadura base de la criatura. Este valor se multiplica por creature\_template.Armor\_mod para determinar la armadura final de la criatura.

### attackpower

Poder de ataque base de la criatura.

### rangedattackpower

Poder de ataque a distancia base de la criatura.

### damage\_base

Modificador usado para calcular el daño que produce una criatura. Este campo se usa si el [exp](creature_template#exp) de una criatura está en 0. Véase [DamageModifier](creature_template#damagemodifier) para más información.

### damage\_exp1

Modificador usado para calcular el daño que produce una criatura. Este campo se usa si el [exp](creature_template#exp) de una criatura está en 1. Véase [DamageModifier](creature_template#damagemodifier) para más información.

### damage\_exp2

Modificador usado para calcular el daño que produce una criatura. Este campo se usa si el [exp](creature_template#exp) de una criatura está en 2. Véase [DamageModifier](creature_template#damagemodifier) para más información.

### comment

Un comentario que describe el propósito del registro (entry).
