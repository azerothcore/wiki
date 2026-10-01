# spell_jump_distance

[<-返回至:World](database-world)


**`spell_jump_distance` 表**

此表存储每个法术的链式跳跃距离覆盖值。当存在对应行时，服务器会加载 `JumpDistance` 并将其赋给 `SpellInfo::JumpDistance`；随后 `Spell::SearchChainTargets()` 会使用该值来限制链式目标的跳跃半径。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id) | INT | UNSIGNED | PRI | NO | 0 | | 法术 id（关联到 Spell.dbc） |
| [JumpDistance](#jumpdistance) | FLOAT | SIGNED | | NO | 0 | | 最大跳跃距离（以码为单位） |

**字段说明**

### ID

此行所应用的法术标识符。参见 [Spell.dbc](spell)。

### JumpDistance

该法术的最大链式跳跃距离（以码为单位）。当 > 0 时，服务器在搜索链式目标时将使用该值，而非默认的跳跃半径。
