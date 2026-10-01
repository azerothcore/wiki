# game\_event\_npcflag

[<-返回:世界](database-world)

**\`game\_event\_npcflag\` 表**

该表包含当指定事件激活时，需要添加到具有给定 guid 的生物身上的 npcflag。

**表结构**

| 字段 (Field)     | 类型 (Type) | 属性 (Attributes) | 键 (Key) | 空 (Null) | 默认 (Default) | 额外 (Extra) | 注释 (Comment)   |
| ---------------- | ----------- | ----------------- | -------- | --------- | -------------- | ------------ | ---------------- |
| [eventEntry][1]  | TINYINT     | UNSIGNED          | PRI      | NO        |                |              | 游戏事件的条目   |
| [guid][2]        | MEDIUMINT   | UNSIGNED          | PRI      | NO        | 0              |              |                  |
| [npcflag][3]     | INT         | UNSIGNED          |          | NO        | 0              |              |                  |

[1]: #evententry
[2]: #guid
[3]: #npcflag

**字段说明**

### eventEntry

与此 npcflag 变更相关联的事件条目。

### guid

你想要为其改变 npcflag 的生物的 guid。

### npcflag

你想要设置的 npcflag。这里指定的值会按位加到该 NPC 已设置的 npcflag 上。

因此，如果你想让该生物同时成为一个任务给予者，只需在本列填入 2。
