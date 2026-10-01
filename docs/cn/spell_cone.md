# spell_cone

[<-返回至:World](database-world)

**`spell_cone` 表**

此表存储锥形目标选择所使用的锥角覆盖值。
当存在对应行时，将使用 `spell_cone.ConeDegrees` 的值作为锥角（以度为单位）。
如果不存在覆盖值，核心将回退到旧版的硬编码法术处理方式。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id](#id) | INT | UNSIGNED | PRI | NO | 0 | | 法术标识符 |
| [ConeDegrees](#conedegrees) | SMALLINT | | | NO | 60 | | 锥角（以度为单位） |

**字段说明**

### id

此行所应用的法术标识符。

### ConeDegrees

锥形目标选择所使用的锥角（以度为单位）。模式（schema）默认值为 60。
