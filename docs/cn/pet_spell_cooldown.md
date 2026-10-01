# pet\_spell\_cooldown

[<-返回至:Characters](database-characters)

**`pet_spell_cooldown` 表**

该表保存宠物法术冷却时间的信息。

**表结构**

| Field      | Type      | Attributes | Key | Null | Default | Extra | Comment                            |
| ---------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [guid][1]  | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier, Low part |
| [spell][2] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Spell Identifier                   |
| [category][4] | INT    | UNSIGNED   |     | YES  | 0       |       | Spell category                     |
| [time][3]  | INT       | UNSIGNED   |     | NO   | 0       |       |                                    |

[1]: #guid
[2]: #spell
[3]: #time
[4]: #category

## 字段说明

### guid

宠物的 GUID。参见 [character\_pet.id](character_pet#id)。

### spell

该冷却时间所应用的法术 ID。参见 [Spell.dbc](spell) 第 1 列。

### category

该冷却时间所属的法术类别（类别冷却时间由所有同类别法术共享）。若法术没有类别，则为 `0`。

### time

冷却时间到期的时刻，以 Unix 时间表示。
