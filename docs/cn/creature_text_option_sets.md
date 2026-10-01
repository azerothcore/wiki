# creature\_text\_option\_sets

[<-返回:世界](database-world)

**\`creature\_text\_option\_sets\` 表**

此表为生物文本组定义可复用的选项规则集。每个规则集控制 `SendChat()` 的冷却、触发概率和仅玩家过滤。规则集通过 [creature\_text\_options](creature_text_options) 表分配给特定的 (CreatureID, GroupID) 对。

## 结构

| 字段                  | 类型         | 属性 | 键 | 空 | 默认值 | 额外 | 注释                                  |
|------------------------|------------|------------|-----|------|---------|-------|------------------------------------------|
| [SetID][1]             | TINYINT      | UNSIGNED   | PRI | NO   |         |       |                                          |
| [Cooldown][2]          | INT          | UNSIGNED   |     | NO   | 0       |       | 组再次触发前需等待的冷却时间（毫秒） |
| [TriggerChance][3]     | TINYINT      | UNSIGNED   |     | NO   | 100     |       | 0-100 的百分比触发概率                |
| [PlayerOnly][4]        | TINYINT      | UNSIGNED   |     | NO   | 0       |       | 仅当目标是玩家时才触发               |
| [comment][5]           | VARCHAR(255) |            |     | YES  |         |       |                                          |

[1]: #setid
[2]: #cooldown
[3]: #triggerchance
[4]: #playeronly
[5]: #comment

## 字段说明

### SetID

此选项规则集的唯一标识符。由 [creature\_text\_options.OptionSetID](creature_text_options#optionsetid) 引用。

### Cooldown

同一个文本组在给定生物上再次触发之前必须经过的最短时间（毫秒）。设置为 `0` 可禁用冷却强制。

### TriggerChance

一个从 `0` 到 `100` 的百分比值，表示文本组被触发的整体概率。值为 `100` 表示文本在被调用时总是触发；值为 `30` 表示大约有 30% 的几率触发。

### PlayerOnly

设置为 `1` 时，仅当触发它的目标是玩家时，文本组才会触发。设置为 `0` 时，无论目标类型如何（玩家、宠物、守护者等），文本都会触发。

### comment

此规则集的可选人类可读标签。
