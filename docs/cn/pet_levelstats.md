# pet\_levelstats

[<-返回至:World](database-world)

**`pet_levelstats` 表**

该表保存基于等级的各个宠物基础属性信息。

**表结构**

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
| [min\_dmg](#mindmg)               | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [max\_dmg](#maxdmg)               | INT       | UNSIGNED   |     | NO   | 0       |       |         |

## 字段说明

### creature\_entry

宠物生物模板 ID。参见 creature\_template.entry

### level

宠物等级。

### hp

宠物在当前所选[等级](#level)下的基础生命值，由核心计算得出。

### mana

宠物在当前所选[等级](#level)下的基础法力值，由核心计算得出。

### armor

宠物在当前所选[等级](#level)下的基础护甲，由核心计算得出。

### str

宠物在当前所选[等级](#level)下的基础力量，由核心计算得出。

### agi

宠物在当前所选[等级](#level)下的基础敏捷，由核心计算得出。

### sta

宠物在当前所选[等级](#level)下的基础耐力，由核心计算得出。

### inte

宠物在当前所选[等级](#level)下的基础智力，由核心计算得出。

### spi

宠物在当前所选[等级](#level)下的基础精神，由核心计算得出。

### min\_dmg

宠物在当前所选[等级](#level)下的基础近战伤害最小值。

### max\_dmg

宠物在当前所选[等级](#level)下的基础近战伤害最大值。
