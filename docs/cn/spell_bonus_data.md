# spell\_bonus\_data

[<-返回至:World](database-world)

**\`spell\_bonus\_data\` 表**

此表用于存储自定义的伤害/治疗加成系数。

**表结构**

| Field             | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]        | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [direct_bonus][2] | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [dot_bonus][3]    | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [ap_bonus][4]     | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [ap_dot_bonus][5] | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [comments][6]     | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |

[1]: #entry
[2]: #directbonus
[3]: #dotbonus
[4]: #apbonus
[5]: #apdotbonus
[6]: #comments

**字段说明**

### entry

法术 ID。参见 Spell.dbc。

如果法术存在于 Spell\_ranks 中，且每一层级的系数都相同，则只需为法术的第一层级填写数据。

### direct\_bonus

直接法术强度伤害。

若 < 0

计算默认的法术强度系数。

若 = 0

不应用任何法术强度系数。（伤害不随法术强度缩放）

若 > 0

将其用作新的法术强度系数。

### dot\_bonus

法术持续伤害。

若 < 0
计算默认的法术强度系数。
若 = 0
不应用任何法术强度系数。（伤害不随法术强度缩放）
若 > 0
将其用作新的法术强度系数。

### ap\_bonus

直接近战/远程伤害。

若 < 0

计算默认的攻击强度系数。

若 = 0

不应用任何攻击强度系数。（伤害不随攻击强度缩放）

若 > 0

将其用作新的攻击强度系数。

### ap\_dot\_bonus

近战/远程持续伤害。

若 < 0

计算默认的攻击强度系数。

若 = 0

不应用任何攻击强度系数。（伤害不随攻击强度缩放）

若 > 0

将其用作新的攻击强度系数。

### comments

注释，说明为何采用这些数值以及法术的名称。
