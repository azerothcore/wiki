# player_class_stats

[<-返回至:World](database-world)

**`player_class_stats` 表**

该表保存角色升级时应用于属性的值的信息。此表中的所有值仅表示某职业在特定等级下的基础属性。

**表结构**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Class][1]     | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [Level][2]     | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [BaseHP][3]    | INT     | UNSIGNED   |     | NO   | 1       |       |         |
| [BaseMana][4]  | INT     | UNSIGNED   |     | NO   | 1       |       |         |
| [Strength][5]  | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Agility][6]   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Stamina][7]   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Intellect][8] | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Spirit][9]    | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #Class
[2]: #Level
[3]: #BaseHP
[4]: #BaseMana
[5]: #Strength
[6]: #Agility
[7]: #Stamina
[8]: #Intellect
[9]: #Spirit

## 字段说明

### Class

角色职业。该字段决定将哪些值应用于角色的属性。此值取自 [`ChrClasses.dbc`](chrclasses)。

### Level

应应用这些属性的等级。

### BaseHP

应用于角色的基础生命值。在耐力加成之前应用。

### BaseMana

应用于角色的基础法力值。在智力加成之前应用。

### Strength

应用于角色的基础力量。

### Agility

应用于角色的基础敏捷。

### Stamina

应用于角色的基础耐力。

### Intellect

应用于角色的基础智力。

### Spirit

应用于角色的基础精神。

### 示例

| Class | Level | BaseHP | BaseMana | Strength | Agility | Stamina | Intellect | Spirit |
| ----- | ----- | ------ | -------- | -------- | ------- | ------- | --------- | ------ |
| 1     | 1     | 20     | 0        | 23       | 20      | 22      | 20        | 20     |
| 2     | 1     | 28     | 60       | 22       | 20      | 22      | 20        | 21     |
| 3     | 1     | 46     | 65       | 20       | 23      | 21      | 20        | 21     |
| 4     | 1     | 25     | 0        | 21       | 23      | 21      | 20        | 20     |
| 5     | 1     | 52     | 73       | 20       | 20      | 20      | 22        | 23     |
| 6     | 55    | 1359   | 0        | 108      | 73      | 99      | 29        | 42     |
| 7     | 1     | 40     | 85       | 21       | 20      | 21      | 21        | 22     |
| 8     | 1     | 32     | 100      | 20       | 20      | 20      | 23        | 22     |
| 9     | 1     | 23     | 90       | 20       | 20      | 21      | 22        | 22     |
| 11    | 1     | 44     | 60       | 21       | 20      | 20      | 22        | 22     |

**与 [\`player_race_stats\`](player_race_stats) 的关系**

仅凭此表并不能定义角色在任何等级下的属性。此表中的值需与 `player_race_stats` 表中的值相结合，才能将最终属性应用于任何等级下的角色。

最终属性的计算方式如下：取此表中的基础属性值，再加上 `player_race_stats` 中该属性的修正值。

例如，一名四十级的德鲁伊基础力量为四十六。再加上暗夜精灵力量修正值负四，得到的最终值为四十二。
