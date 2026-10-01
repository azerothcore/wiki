# exploration_basexp

[<-返回:World](database-world)

该表保存玩家探索新区域时所需的基础经验值信息。

| 字段         | 类型     | 属性     | 键 | 允许为空 | 默认值 |
| ------------ | -------- | -------- | --- | -------- | ------ |
| [level][1]   | TINYINT  | UNSIGNED | PRI | NO       | 0      |
| [basexp][2]  | MEDIUMINT| SIGNED   |     | NO       | 0      |

[1]: #level
[2]: #basexp

**字段说明**

### level
玩家的等级。

### basexp
玩家在 level 字段指定的等级下发现新区域时所获得的基础经验值。
