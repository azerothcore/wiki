# game_event_model_equip

[<-返回:世界](database-world)

**\`game_event_model_equip\` 表**

该表包含所有需要在特定游戏事件期间改变显示 ID（display id）和/或装备（equipment）的生物实例。

**表结构**

| 字段 (Field)                | 类型 (Type) | 属性 (Attributes) | 键 (Key) | 空 (Null) | 默认 (Default) | 额外 (Extra) | 注释 (Comment)    |
| --------------------------- | ----------- | ----------------- | -------- | --------- | -------------- | ------------ | ----------------- |
| [eventEntry](#evententry)   | SMALLINT    | SIGNED            |          | NO        | 0              |              | 游戏事件的条目。  |
| [guid](#guid)               | INT         | UNSIGNED          | PRI      | NO        | 0              | Unique       |                   |
| [modelid](#modelid)         | MEDIUMINT   | UNSIGNED          |          | NO        | 0              |              |                   |
| [equipment_id](#equipmentid)| MEDIUMINT   | UNSIGNED          |          | NO        | 0              |              |                   |

**字段说明**

### eventEntry

参照：[game_event.entry](game_event#entry)。

只能使用**正数**值。

### guid

参照：[creature.guid](creature#guid)。

### modelid

参照 [creature_model_info.displayid](creature_model_info#displayid)，用于在事件运行期间改变 [creature](creature#guid) 的 [模型](creature_model_info#displayid)。

### equipment_id

参照 [creature_equip_template.creatureid](creature_equip_template#creatureid)，用于在事件运行期间更换装备。

如果你不想添加或改变当前正在使用的装备，请将该值设为 `0`。系统将使用 [creature_template](creature_template#entry) 中与 [creature.guid](creature#guid) 的 [creature.id1](creature#id1) 相匹配的 [creature_equip_template](creature_equip_template#CreatureID)。
