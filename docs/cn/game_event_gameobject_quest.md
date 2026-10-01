# game\_event\_gameobject\_quest

[<-返回:世界](database-world)

**\`game\_event\_gameobject\_quest\` 表**

该表保存着关于某些任务的信息，这些任务只有在某个事件正在进行时才能接取。

**表结构**

| 字段 (Field)     | 类型 (Type) | 属性 (Attributes) | 键 (Key) | 空 (Null) | 默认 (Default) | 额外 (Extra) | 注释 (Comment)       |
| ---------------- | ----------- | ----------------- | -------- | --------- | -------------- | ------------ | -------------------- |
| [eventEntry][1]  | TINYINT     | UNSIGNED          | PRI      | NO        |                |              | 游戏事件的条目       |
| [id][2]          | MEDIUMINT   | UNSIGNED          | PRI      | NO        | 0              |              |                      |
| [quest][3]       | MEDIUMINT   | UNSIGNED          | PRI      | NO        | 0              |              |                      |

[1]: #evententry
[2]: #id
[3]: #quest

**字段说明**

### id

游戏对象（Gameobject）的 ID。参见 gameobject\_template.entry

### quest

任务 ID。参见 quest\_template.entry

### eventEntry

事件 ID。参见 game\_event.eventEntry
