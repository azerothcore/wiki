# creature\_text\_options

[<-返回:世界](database-world)

**\`creature\_text\_options\` 表**

此表将可复用的选项规则集（定义于 [creature\_text\_option\_sets](creature_text_option_sets)）分配给来自 [creature\_text](creature_text) 的特定 (CreatureID, GroupID) 对。这使得无需每个脚本的样板代码，即可对 `SendChat()` 调用的冷却、触发概率和仅玩家过滤进行数据驱动的控制。

当为一个生物文本组调用 `SendChat()` 时，引擎会自动：
1. 检查该组是否处于冷却中（如果 `Cooldown > 0`）。
2. 根据 `TriggerChance` 进行判定，以决定文本是否触发。
3. 检查目标是否为玩家（如果 `PlayerOnly = 1`）。

如果任何检查失败，文本将被静默跳过。如果所有检查都通过，文本将触发并启动冷却计时器。

## 结构

| 字段                  | 类型    | 属性 | 键 | 空 | 默认值 | 额外 | 注释 |
|------------------------|------------|------------|-----|------|---------|-------|---------|
| [CreatureID][1]        | INT     | UNSIGNED   | PRI | NO   |         |       |         |
| [GroupID][2]           | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [OptionSetID][3]       | TINYINT | UNSIGNED   |     | NO   |         |       |         |

[1]: #creatureid
[2]: #groupid
[3]: #optionsetid

## 字段说明

### CreatureID

此选项分配所适用的 [creature\_template.entry](creature_template#entry) 中的生物条目。

### GroupID

此选项分配所适用的 [creature\_text.GroupID](creature_text#groupid) 中的文本组 ID。

### OptionSetID

来自 [creature\_text\_option\_sets.SetID](creature_text_option_sets#setid) 的规则集 ID，它定义了此 (CreatureID, GroupID) 对的冷却、触发概率和仅玩家行为。
