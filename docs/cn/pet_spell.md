# pet\_spell

[<-返回至:Characters](database-characters)

**`pet_spell` 表**

该表保存各个宠物法术的信息。

**表结构**

| Field       | Type      | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]   | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [spell][2]  | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Spell Identifier         |
| [active][3] | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #spell
[3]: #active

## 字段说明

### guid

宠物 GUID。参见 [character\_pet.id](character_pet#id)。

### spell

法术 ID。参见 [Spell.dbc](spell) 第 1 列。

### active

布尔值 0 或 1，控制法术是否激活。
