# game_event_pool

[<-返回:世界](database-world)

**\`game_event_pool\` 表**

该表决定某个给定的刷新组（pool）是否在某个给定的游戏事件中处于激活状态。

**表结构**

| 字段 (Field)               | 类型 (Type) | 属性 (Attributes) | 键 (Key) | 空 (Null) | 默认 (Default) | 额外 (Extra) | 注释 (Comment)                                                        |
| -------------------------- | ----------- | ----------------- | -------- | --------- | -------------- | ------------ | --------------------------------------------------------------------- |
| [eventEntry](#evententry)  | SMALLINT    | SIGNED            |          | NO        |                |              | 游戏事件的条目。填负数可在事件期间移除。                              |
| [pool_entry](#poolentry)   | MEDIUMINT   | UNSIGNED          | PRI      | NO        | 0              | Unique       | 刷新组（pool）的 ID                                                   |

**字段说明**

### eventEntry

参照：[game_event.entry](game_event#entry)。

使用**正数**会在事件运行期间**添加**该刷新组。

使用**负数**会在事件运行期间**移除**该刷新组。

### pool_entry

参照：[pool_pool.pool_id](pool_pool#poolid)。
