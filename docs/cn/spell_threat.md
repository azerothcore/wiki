# spell\_threat

[<-返回:世界数据库](database-world)

**\`spell\_threat\` 表**

该表保存所有应增加或减少仇恨的法术的仇恨值。

**表结构**

| Field       | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]    | MEDIUMINT | UNSIGNED   | PRI | NO   | NULL    |       |                                           |
| [flatMod][2]  | INT       | SIGNED     |     | YES  | NULL    |       |                                           |
| [pctMod][3]   | FLOAT     |            |     | NO   | 1       |       | 伤害/治疗的仇恨倍率                        |
| [apPctMod][4] | FLOAT     |            |     | NO   | 0       |       | 由攻击强度产生的额外仇恨加成              |

[1]: #entry
[2]: #flatmod
[3]: #pctmod
[4]: #appctmod

**字段说明**

### entry

法术 ID。参见 [Spell.dbc](spell)。

### flatMod

该法术增加（若为负则减少）的仇恨固定值。如果没有适用的固定修正则为 `NULL`。

### pctMod

应用于该法术造成的伤害或治疗的仇恨倍率。默认 `1`。

### apPctMod

由施法者的攻击强度产生的额外仇恨加成。默认 `0`。
