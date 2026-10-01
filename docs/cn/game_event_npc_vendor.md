# game_event_npc_vendor

[<-返回:世界](database-world)

**\`game_event_npc_vendor\` 表**

该表允许你改变商人出售的物品，或者为一个原本不售卖物品的 NPC 创建[商人列表](npc_vendor)（该列表仅在某个事件激活时生效）。

**表结构**

| 字段 (Field)                | 类型 (Type) | 属性 (Attributes) | 键 (Key) | 空 (Null) | 默认 (Default) | 额外 (Extra) | 注释 (Comment) |
| --------------------------- | ----------- | ----------------- | -------- | --------- | -------------- | ------------ | -------------- |
| [eventEntry](#evententry)   | SMALLINT    | SIGNED            |          | NO        | 0              |              |                |
| [guid](#guid)               | MEDIUMINT   | UNSIGNED          | PRI      | NO        | 0              |              |                |
| [slot](#slot)               | SMALLINT    | SIGNED            |          | NO        | 0              |              |                |
| [item](#item)               | MEDIUMINT   | UNSIGNED          | PRI      | NO        | 0              |              |                |
| [maxcount](#maxcount)       | MEDIUMINT   | UNSIGNED          |          | NO        | 0              |              |                |
| [incrtime](#incrtime)       | MEDIUMINT   | UNSIGNED          |          | NO        | 0              |              |                |
| [ExtendedCost](#extendedcost)| MEDIUMINT  | UNSIGNED          |          | NO        | 0              |              |                |

**字段说明**

### eventEntry

参照：[game_event.entry](game_event#entry)。

只能使用**正数**值。

### guid

参照：[creature.guid](creature#guid)。

### slot

参照：[npc_vendor.slot](npc_vendor#slot)。

### item

参照：[item_template.entry](item_template#entry)。

### maxcount

参照：[npc_vendor.maxcount](npc_vendor#maxcount)。

### incrtime

参照：[npc_vendor.incrtime](npc_vendor#incrtime)。

### ExtendedCost

参照：[npc_vendor.extendedcost](npc_vendor#extendedcost)。
