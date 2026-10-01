# game\_event\_save

[<-返回:角色](database-characters)

**\`game\_event\_save\` 表**

**表结构**

| 字段 (Field)     | 类型 (Type) | 属性 (Attributes) | 键 (Key) | 空 (Null) | 默认 (Default) | 额外 (Extra) | 注释 (Comment) |
| ---------------- | ----------- | ----------------- | -------- | --------- | -------------- | ------------ | -------------- |
| [eventEntry][1]  | TINYINT     | UNSIGNED          | PRI      | NO        |                |              |                |
| [state][2]       | TINYINT     | UNSIGNED          |          | NO        | 1              |              |                |
| [next_start][3]  | INT         | UNSIGNED          |          | NO        | 0              |              |                |

[1]: #evententry
[2]: #state
[3]: #nextstart

**字段说明**

### eventEntry

`field-no-description|1`

### state

`field-no-description|2`

### next\_start

`field-no-description|3`
