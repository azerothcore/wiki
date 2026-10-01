# game\_event\_condition\_save

[<-返回:Characters](database-characters)

**\`game\_event\_condition\_save\` 表**

**表结构**

| 字段               | 类型    | 属性     | 键 | 允许为空 | 默认值 | 额外 | 注释 |
| ------------------ | ------- | -------- | --- | -------- | ------ | ---- | ---- |
| [eventEntry][1]    | TINYINT | UNSIGNED | PRI | NO       |        |      |      |
| [condition_id][2]  | INT     | UNSIGNED | PRI | NO       | 0      |      |      |
| [done][3]          | FLOAT   | SIGNED   |     | YES      | 0      |      |      |

[1]: #evententry
[2]: #conditionid
[3]: #done

**字段说明**

### eventEntry

这是指向 game\_event 表中事件条目的链接。

### condition\_id

参见 [game\_event\_condition.condition\_id](game_event_condition#conditionid)。

### done

表示已完成的数量。参见 [game\_event\_condition.req\_num](game_event_condition#reqnum)。
