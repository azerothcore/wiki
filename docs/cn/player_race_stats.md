# player_race_stats

[<-返回至:World](database-world)

**`player_race_stats` 表**

该表保存应用于角色属性值的修正信息。此表中的所有值仅表示基于角色种族的属性值修正。

**表结构**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Race][1]      | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [Strength][2]  | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Agility][3]   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Stamina][4]   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Intellect][5] | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Spirit][6]    | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #Race
[2]: #Strength
[3]: #Agility
[4]: #Stamina
[5]: #Intellect
[6]: #Spirit

**字段说明**

### Race

角色种族。该字段决定将哪些值应用于角色的属性。此值取自 [`ChrRaces.dbc`](chrraces)。

### Strength

应用于角色基础属性的力量修正。

### Agility

应用于角色基础属性的敏捷修正。

### Stamina

应用于角色基础属性的耐力修正。

### Intellect

应用于角色基础属性的智力修正。

### Spirit

应用于角色基础属性的精神修正。

**与 [`player_class_stats`](player_class_stats) 的关系**

仅凭此表并不能定义角色的属性。此表中的值需与 `player_class_stats` 表中的值相结合，才能将最终属性应用于任何等级下的角色。

最终属性的计算方式如下：从 `player_class_stats` 中取基础属性值，再加上此表中该属性的修正值。

例如，一名四十级的德鲁伊基础力量为四十六。再加上暗夜精灵力量修正值负四，得到的最终值为四十二。
