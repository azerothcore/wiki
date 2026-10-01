# game_event_quest_condition

[<-返回:世界](database-world)

**\`game_event_quest_condition\` 表**

该表包含世界事件中某个任务与其所要完成的条件（condition）之间的映射关系。它还包含一旦某个玩家完成了给定任务后，该任务会为某个条件增加多少数值。

**表结构**

| 字段 (Field)                 | 类型 (Type) | 属性 (Attributes) | 键 (Key) | 空 (Null) | 默认 (Default) | 额外 (Extra) | 注释 (Comment) |
| ---------------------------- | ----------- | ----------------- | -------- | --------- | -------------- | ------------ | -------------- |
| [eventEntry](#evententry)    | TINYINT     | UNSIGNED          |          | NO        |                |              |                |
| [quest](#quest)              | MEDIUMINT   | UNSIGNED          | PRI      | NO        | 0              |              |                |
| [condition_id](#conditionid) | MEDIUMINT   | UNSIGNED          |          | NO        | 0              |              |                |
| [num](#num)                  | FLOAT       | SIGNED            |          | YES       | 0              |              |                |

**字段说明**

### eventEntry

与该任务和条件相关联的事件。

### quest

将触发该条件的任务。

### condition_id

在任务完成时将被触发的条件。

### num

将被添加到条件中的"单位"数量（暂且这样称呼），用于满足该条件所需的数量。
