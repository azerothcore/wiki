# loot_template

[<-返回至:World](database-world)

**\*_loot_template 表**

**表结构**

| Field                           | Type         | Attributes | Key | Null | Default | Extra | Comment                       |
| ------------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ----------------------------- |
| [Entry](#entry)                 | INT          | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [Item](#item)                   | INT          | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [Reference](#reference)         | INT          |            |     | NO   | 0       |       |                               |
| [Chance](#chance)               | FLOAT        |            |     | NO   | 0       |       |                               |
| [QuestRequired](#questrequired) | TINYINT      |            |     | NO   | 0       |       |                               |
| [LootMode](#lootmode)           | SMALLINT     | UNSIGNED   |     | NO   | 1       |       |                               |
| [GroupId](#groupid)             | TINYINT      | UNSIGNED   |     | NO   | 0       |       | creature_loot_template 中的 PRI |
| [MinCount](#mincount)           | TINYINT      | UNSIGNED   |     | NO   | 1       |       |                               |
| [MaxCount](#maxcount)           | TINYINT      | UNSIGNED   |     | NO   | 1       |       |                               |
| [Comment](#comment)             | VARCHAR(255) |            |     | YES  | NULL    |       | player_loot_template 中为 TEXT |

## 字段说明

### Entry

| 表                        | Entry                                                                | Comment                                                                                   |
| ------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| creature_loot_template    | [creature_template.lootid](creature_template#lootid)                 | 通常与 [creature_template.entry](creature_template#entry) 相同                             |
| disenchant_loot_template  | [item_template.DisenchantID](item_template#disenchantid)             |                                                                                           |
| fishing_loot_template     | 区域 id                                                              |                                                                                           |
| gameobject_loot_template  | [gameobject_template.data1](gameobject_template#data023)             | 需要游戏对象类型为 GAMEOBJECT_TYPE_CHEST (3) 或 GAMEOBJECT_TYPE_FISHINGHOLE (25)          |
| item_loot_template        | [item_template.entry](item_template#entry)                           |                                                                                           |
| mail_loot_template        | 邮件模板 id                                                          |                                                                                           |
| milling_loot_template     | [item_template.entry](item_template#entry)                           |                                                                                           |
| pickpocket_loot_template  | [creature_template.pickpocketloot](creature_template#pickpocketloot) |                                                                                           |
| player_loot_template      | TeamID (0 部落/1 联盟)                                               | 仅在战场中以移除徽章的形式掉落。                                                            |
| prospecting_loot_template | [item_template.entry](item_template#entry)                           |                                                                                           |
| reference_loot_template   | [\*_loot_template.reference](loot_template#reference)                |                                                                                           |
| skinning_loot_template    | [creature_template.skinloot](creature_template#skinloot)             | 还包括从生物身上可挖掘/采集的掉落                                                          |
| spell_loot_template       | SpellID                                                              |                                                                                           |

### Item

[item_template.entry](item_template#entry)

### Reference

[reference_loot_template.entry](loot_template#entry)。

在当前模板中使用被引用模板中的条目。

**注意：绝不允许自我引用。这将导致崩溃。**

### Chance

物品掉落的几率。对于具有相同 [GroupID](#groupid) 的所有条目，几率总和不能超过 100。

如果该字段保持为 0，那么具有相同 [GroupID](#groupid) 的所有条目的掉落几率将平均分配，并且 chance = 0。

### QuestRequired

0 - 掉落始终可用。

1 - 只有当玩家拥有一个任务，且该任务在 [quest_template.RequiredItemId1-6](quest_template#requireditemid1) 中指定了此物品 id 时，掉落才会发生。

### LootMode

位掩码（Bitmask）。

用于区分条件性掉落，例如奥杜尔（Ulduar）中的困难模式掉落。核心可以在任何时候更改当前激活的 lootmode。

大多数情况下该字段保持为 1。

### GroupId

用于在同一掉落模板内对物品进行分组。

- 每个组只能掉落一个物品。
- 如果该组的总 [几率](#chance) 为 100，那么必定会掉落一个物品。
- 如果该组的总 [几率](#chance) 小于 100，则存在空掉落的可能。

被引用的掉落可以像物品一样成为组的一部分。当一个引用被分组时，它会与该组内的其他条目竞争，只有一个条目（物品或引用）会被选中。如果该引用在掷骰中胜出，则整个被引用的模板都会被处理。

**注意：客户端在拾取窗口中最多只能显示 16 个物品（包括金币）。因此不建议使用超过 16 个组。**

### MinCount

单次掉落中某物品的最小数量。不能为 0。

### MaxCount

| 表                      | Comment                                                                                                                                                                                                                                 |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \*_loot_template        | 单次掉落中某物品的最大数量。                                                                                                                                                                                                            |
| referenced_loot_template | 被引用的掉落模板应被处理的次数。**注意：核心每个掉落定义只掷一次几率。如果最初的引用掷骰失败了，无论 MaxCount 是多少，它都会完全跳过当前的掉落。** |

### Comment

评论
