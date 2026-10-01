# game_event_creature

[<-返回:World](database-world)

**\`game_event_creature\` 表**

包含所有在指定游戏事件期间必须生成/取消生成的生物实例。

**表结构**

| 字段                       | 类型     | 属性     | 键 | 允许为空 | 默认值 | 额外   | 注释                                                                 |
| -------------------------- | -------- | -------- | --- | -------- | ------ | ------ | -------------------------------------------------------------------- |
| [eventEntry](#evententry)  | SMALLINT | SIGNED   |     | NO       |        |        | 游戏事件的条目。填写负数条目可在事件期间移除。                        |
| [guid](#guid)              | INT      | UNSIGNED | PRI | NO       |        | Unique |                                                                      |

**字段说明**

### eventEntry

引用：[game_event.entry](game_event#entry)。

使用**正数**将在事件运行时**添加**该生物。

使用**负数**将在事件运行时**移除**该生物。

### guid

引用：[creature.guid](creature#guid)。
