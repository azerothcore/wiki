# creature\_classlevelstats

**表结构**

此表包含生物生命值、法力值、护甲、攻击强度、远程攻击强度、伤害和经验值的基础数值。

| 字段                    | 类型     | 属性     | 空   | 默认值 | 额外 | 注释 |
| ----------------------- | -------- | -------- | ---- | ------ | ---- | ---- |
| [level][1]              | TINYINT  | UNSIGNED | NO   |        |      |      |
| [class][2]              | TINYINT  | UNSIGNED | NO   |        |      |      |
| [basehp0][3]            | SMALLINT | UNSIGNED | NO   |        |      |      |
| [basehp1][4]            | SMALLINT | UNSIGNED | NO   |        |      |      |
| [basehp2][5]            | SMALLINT | UNSIGNED | NO   |        |      |      |
| [basemana][6]           | SMALLINT | UNSIGNED | NO   |        |      |      |
| [basearmor][7]          | SMALLINT | UNSIGNED | NO   |        |      |      |
| [attackpower][8]        | SMALLINT | UNSIGNED | NO   |        |      |      |
| [rangedattackpower][9]  | SMALLINT | UNSIGNED | NO   |        |      |      |
| [damage_base][10]       | FLOAT    |           | NO   |        |      |      |
| [damage_exp1][11]       | FLOAT    |           | NO   |        |      |      |
| [damage_exp2][12]       | FLOAT    |           | NO   |        |      |      |
| [Strength][14]          | INT      |           | NO   | 0      |      |      |
| [Agility][15]           | INT      |           | NO   | 0      |      |      |
| [Stamina][16]           | INT      |           | NO   | 0      |      |      |
| [Intellect][17]         | INT      |           | NO   | 0      |      |      |
| [Spirit][18]            | INT      |           | NO   | 0      |      |      |
| [comment][13]           | text     |           | YES  | NULL   |      |      |

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

**字段说明**

### level

生物的等级。

### class

生物的职业。这是对 [creature\_template](creature_template) 表中 [unit\_class](creature_template#unitclass) 字段的引用。

### basehp0

当 creature\_template.exp 值设置为 0 时生物的基础生命值。此值乘以 [creature\_template.Health\_mod](creature_template#health_mod) 来确定生物的最终生命值。

### basehp1

当 creature\_template.exp 值设置为 1 时生物的基础生命值。此值乘以 [creature\_template.Health\_mod](creature_template#health_mod) 来确定生物的最终生命值。

### basehp2

当 creature\_template.exp 值设置为 2 时生物的基础生命值。此值乘以 [creature\_template.Health\_mod](creature_template#health_mod) 来确定生物的最终生命值。

### basemana

生物的基础法力值。此值乘以 [creature\_template.Mana\_mod](creature_template#mana_mod) 来确定生物的最终法力值。

### basearmor

生物的基础护甲值。此值乘以 creature\_template.Armor\_mod 来确定生物的最终护甲值。

### attackpower

生物的基础攻击强度。

### rangedattackpower

生物的基础远程攻击强度。

### damage\_base

用于计算生物伤害输出的修正值。当生物的 [exp](creature_template#exp) 设置为 0 时使用此字段。更多信息参见 [DamageModifier](creature_template#damagemodifier)。

### damage\_exp1

用于计算生物伤害输出的修正值。当生物的 [exp](creature_template#exp) 设置为 1 时使用此字段。更多信息参见 [DamageModifier](creature_template#damagemodifier)。

### damage\_exp2

用于计算生物伤害输出的修正值。当生物的 [exp](creature_template#exp) 设置为 2 时使用此字段。更多信息参见 [DamageModifier](creature_template#damagemodifier)。

### Strength

生物在该等级和职业下的基础力量。

### Agility

生物在该等级和职业下的基础敏捷。

### Stamina

生物在该等级和职业下的基础耐力。

### Intellect

生物在该等级和职业下的基础智力。

### Spirit

生物在该等级和职业下的基础精神。

### comment

描述该记录（entry）用途的注释。
