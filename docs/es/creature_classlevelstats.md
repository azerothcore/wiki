# creature\_classlevelstats

**Estructura**

This table contains the base values for creature health, mana, armor, attack power, ranged attack power, damage, and experience.

| Campo                  | Tipo     | Atributos | Nulo | Por defecto | Extra | Comentario |
| ---------------------- | -------- | --------- | ---- | ----------- | ----- | ---------- |
| [level][1]             | TINYINT  | UNSIGNED  | NO   |             |       |            |
| [class][2]             | TINYINT  | UNSIGNED  | NO   |             |       |            |
| [basehp0][3]           | SMALLINT | UNSIGNED  | NO   |             |       |            |
| [basehp1][4]           | SMALLINT | UNSIGNED  | NO   |             |       |            |
| [basehp2][5]           | SMALLINT | UNSIGNED  | NO   |             |       |            |
| [basemana][6]          | SMALLINT | UNSIGNED  | NO   |             |       |            |
| [basearmor][7]         | SMALLINT | UNSIGNED  | NO   |             |       |            |
| [attackpower][8]       | SMALLINT | UNSIGNED  | NO   |             |       |            |
| [rangedattackpower][9] | SMALLINT | UNSIGNED  | NO   |             |       |            |
| [damage_base][10]      | FLOAT    |           | NO   |             |       |            |
| [damage_exp1][11]      | FLOAT    |           | NO   |             |       |            |
| [damage_exp2][12]      | FLOAT    |           | NO   |             |       |            |
| [comment][13]          | text     |           | Si   | NULL        |       |            |

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

Nivel de la criatura.

### class

Clase de la criatura. Esta es una referencia al campo [unit\_class](creature_template#creature_template-unit_class) de la tabla [creature\_template](creature_template).

### basehp0

Salud base de la criatura si el valor de creature\_template.exp se establece en 0. Este valor se multiplica por [creature\_template.Health\_mod](creature_template#health_mod) para determinar la salud final de la criatura.

### basehp1

Salud base de la criatura si el valor de creature\_template.exp está establecido en 1. Este valor se multiplica por [creature\_template.Health\_mod](creature_template#health_mod) para determinar la salud final de la criatura.

### basehp2

Salud base de la criatura si el valor de creature\_template.exp se establece en 2. Este valor se multiplica por [creature\_template.Health\_mod](creature_template#health_mod) para determinar la salud final de la criatura.

### basemana

Maná base de la criatura. Este valor se multiplica por [creature\_template.Mana\_mod](creature_template#mana_mod) para determinar el maná final de la criatura.

### basearmor

Armadura base de la criatura. Este valor se multiplica por la plantilla de creature.Armor\_mod para determinar la armadura final de la criatura.

### attackpower

Poder de ataque base de la criatura.

### rangedattackpower

Poder de ataque a distancia base de la criatura.

### damage\_base

Modificador utilizado para calcular el daño de una criatura. Este campo se usa si la [exp](creature_template#exp) de una criatura es 0. Consulta [DamageModifier](creature_template#damagemodifier) ​​para más información.

### damage\_exp1

Modificador utilizado para calcular el daño de una criatura. Este campo se usa si la [exp](creature_template#exp) de una criatura es 1. Consulta [DamageModifier](creature_template#damagemodifier) ​​para más información.

### damage\_exp2

Modificador utilizado para calcular el daño de una criatura. Este campo se usa si la [exp](creature_template#exp) de una criatura es 2. Consulta [DamageModifier](creature_template#damagemodifier) ​​para más información.

### comment

Un comentario que describe el propósito del registro (entrada).
