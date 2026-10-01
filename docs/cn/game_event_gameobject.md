# game_event_gameobject

[<-返回:世界](database-world)

**\`game_event_gameobject\` 表**

该表包含所有参与任何游戏事件的游戏对象（gameobject）实例。

**表结构**

| 字段 (Field)                | 类型 (Type) | 属性 (Attributes) | 键 (Key) | 空 (Null) | 默认 (Default) | 额外 (Extra) | 注释 (Comment)                                                        |
| --------------------------- | ----------- | ----------------- | -------- | --------- | -------------- | ------------ | --------------------------------------------------------------------- |
| [eventEntry](#evententry)   | SMALLINT    | SIGNED            |          | NO        |                |              | 游戏事件的条目。填负数可在事件期间移除。                              |
| [guid](#guid)               | INT         | UNSIGNED          | PRI      | NO        |                | Unique       |                                                                       |

**字段说明**

### eventEntry

参照：[game_event.entry](game_event#entry)。

使用**正数**会在事件运行期间**添加**该对象。

使用**负数**会在事件运行期间**移除**该对象。

### guid

参照：[gameobject.guid](gameobject#guid)。
