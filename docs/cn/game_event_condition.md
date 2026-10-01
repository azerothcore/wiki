# game_event_condition

[<-返回:World](database-world)

**\`game_event_condition\` 表**

该表包含完成指定游戏事件所需满足的条件。还包含用于报告给定条件进度和/或最大所需值的世界状态字段。如果您没有将事件设置为世界事件，该表将完全不起作用。

**表结构**

| 字段                                            | 类型        | 属性     | 键 | 允许为空 | 默认值 | 额外 | 注释                 |
| ----------------------------------------------- | ----------- | -------- | --- | -------- | ------ | ---- | -------------------- |
| [eventEntry](#evententry)                       | TINYINT     | UNSIGNED | PRI | NO       |        |      | 游戏事件的条目       |
| [condition_id](#conditionid)                    | MEDIUMINT   | UNSIGNED | PRI | NO       |        |      |                      |
| [req_num](#reqnum)                              | FLOAT       | SIGNED   |     | YES      | 0      |      |                      |
| [max_world_state_field](#maxworldstatefield)    | SMALLINT    | UNSIGNED |     | NO       |        |      |                      |
| [done_world_state_field](#doneworldstatefield)  | SMALLINT    | UNSIGNED |     | NO       |        |      |                      |
| [description](#description)                     | VARCHAR(25) | SIGNED   |     | NO       |        |      |                      |

**字段说明**

### eventEntry

这是指向 [game_event](game_event#evententry) 表中事件条目的链接。

### condition_id

这是此特定世界事件条件的条件 ID。它是一个任意数字，每个世界事件可以有多个条件。它链接到 [game_event_quest_condition](#conditionid) 表的 condition_id 字段。

### req_num

这是一个决定何时满足此条件的任意值。例如，如果您将此值设置为 1000，并且 [game_event_quest_condition](#conditionid) 中只有一个任务会达成此条件，并且该任务将此条件增加 100（通过将 num 字段设置为 100），那么您就需要让玩家完成 10 次该任务才能满足此条件。

### max_world_state_field

这是发送给客户端的世界状态更新字段编号，用于报告满足此条件所需的最大点数。可以在以 $XXXXw 引用的对话文本中找到，其中 XXXX 是在显示该对话时发送的世界状态编号。如果您在做自定义事件，可以选择任何未被使用的编号，它只需要与您放入 [npc_text](npc_text) 表的自定义文本匹配即可。

### done_world_state_field

这是发送给客户端的世界状态更新字段编号，用于报告此条件迄今为止累积的点数。可以在以 $XXXXw 引用的对话文本中找到，其中 XXXX 是在显示该对话时发送的世界状态编号。如果您在做自定义事件，可以选择任何未被使用的编号，它只需要与您放入 [npc_text](npc_text) 表的自定义文本匹配即可。

### description

描述此条件的任意文本字段。
