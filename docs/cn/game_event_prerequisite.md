# game\_event\_prerequisite

[<-返回:世界](database-world)

**\`game\_event\_prerequisite\` 表**

该表包含那些必须先完成才能开始给定事件的事件。你可以设置多个必须先完成的事件，之后下一个事件才会开始。

**表结构**

| 字段 (Field)                | 类型 (Type) | 属性 (Attributes) | 键 (Key) | 空 (Null) | 默认 (Default) | 额外 (Extra) | 注释 (Comment) |
| --------------------------- | ----------- | ----------------- | -------- | --------- | -------------- | ------------ | -------------- |
| [eventEntry][1]             | TINYINT     | UNSIGNED          | PRI      | NO        |                |              |                |
| [prerequisite_event][2]     | MEDIUMINT   | UNSIGNED          | PRI      | NO        |                |              |                |

[1]: #evententry
[2]: #prerequisiteevent

**字段说明**

### eventEntry

这是当所有前置事件都已完成时将要开始的事件。

### prerequisite\_event

这是在下一次 [事件](#evententry) 开始之前必须完成的事件。
