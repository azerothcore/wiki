# conditions

[<-返回:世界库](database-world)

**\`conditions\` 表**

这张表允许你为各种系统定义条件——Gossip、掉落（loot）等。

**表结构**

| 字段                                                 | 类型               | 空 | 键 | 默认值 | 额外 | 备注                                                                          |
| ----------------------------------------------------- | ------------------ | ---- | --- | ------- | ----- | -------------------------------------------------------------------------------- |
| [SourceTypeOrReferenceId](#sourcetypeorreferenceid)   | MEDIUMINT SIGNED   | NO   | PRI | 0       |       |                                                                                  |
| [SourceGroup](#sourcegroup)                           | MEDIUMINT UNSIGNED | NO   | PRI | 0       |       |                                                                                  |
| [SourceEntry](#sourceentry)                           | MEDIUMINT SIGNED   | NO   | PRI | 0       |       |                                                                                  |
| [SourceId](#condition_source_type_smart_event=22)     | INT SIGNED         | NO   | PRI | 0       |       | [smart_scripts.source_type](smart_scripts#sourcetype) \|\| 其他情况为 0 |
| [ElseGroup](#elsegroup)                               | MEDIUMINT UNSIGNED | NO   | PRI | 0       |       |                                                                                  |
| [ConditionTypeOrReference](#conditiontypeorreference) | MEDIUMINT SIGNED   | NO   | PRI | 0       |       |                                                                                  |
| [ConditionTarget](#conditiontarget)                   | TINYINT UNSIGNED   | NO   | PRI | 0       |       |                                                                                  |
| [ConditionValue1](#conditionvalue1)                   | INT UNSIGNED       | NO   | PRI | 0       |       |                                                                                  |
| [ConditionValue2](#conditionvalue2)                   | INT UNSIGNED       | NO   | PRI | 0       |       |                                                                                  |
| [ConditionValue3](#conditionvalue3)                   | INT UNSIGNED       | NO   | PRI | 0       |       |                                                                                  |
| [NegativeCondition](#negativecondition)               | TINYINT UNSIGNED   | NO   |     | 0       |       | 布尔值 0 或 1（如果设置了 [NegativeCondition](#negativecondition)）                      |
| [ErrorType](#errortype)                               | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                                                                  |
| [ErrorTextId](#errortextid)                           | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                                                                  |
| [ScriptName](#scriptname)                             | char(64) SIGNED    | NO   |     | ' '     |       |                                                                                  |
| [Comment](#comment)                                   | VARCHAR(255)       | YES  |     | NULL    |       |                                                                                  |

**字段说明**

### SourceTypeOrReferenceId

如果为负数，则表示它是一个引用模板（reference template）。

| SourceTypeOrReferenceId                           | ID  | SourceGroup                                                                               | SourceEntry                                                                         | [SourceId](conditions#condition_source_type_smart_event=22)        | ConditionTarget                                                                                                              | 备注                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------- | --- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CONDITION_SOURCE_TYPE_NONE                        | 0   | **[参见引用模板](#referencetemplates)**                                        | (引用模板)                                                               | 始终为 0                                                           | （见下文）                                                                                                                  | **仅在[引用模板中使用！参见下文。](#referencetemplates)**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| CONDITION_SOURCE_TYPE_CREATURE_LOOT_TEMPLATE      | 1   | [creature_loot_template.Entry 或 reference_loot_template.Entry](loot_template#entry)      | 物品 id [_loot_template.Item 或 reference_loot_template.Item)](loot_template#item)  | 始终为 0                                                           | 始终为 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_DISENCHANT_LOOT_TEMPLATE    | 2   | [disenchant_loot_template.Entry 或 reference_loot_template.Entry](loot_template#entry)    | 物品 id [_loot_template.Item 或 reference_loot_template.Item)](loot_template#item)  | 始终为 0                                                           | 始终为 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_FISHING_LOOT_TEMPLATE       | 3   | [fishing_loot_template.Entry 或 reference_loot_template.Entry](loot_template#entry)       | 物品 id [_loot_template.Item 或 reference_loot_template.Item)](loot_template#item)  | 始终为 0                                                           | 始终为 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_GAMEOBJECT_LOOT_TEMPLATE    | 4   | [gameobject_loot_template.Entry 或 reference_loot_template.Entry](loot_template#entry)    | 物品 id [_loot_template.Item 或 reference_loot_template.Item)](loot_template#item)  | 始终为 0                                                           | 始终为 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_ITEM_LOOT_TEMPLATE          | 5   | [item_loot_template.Entry 或 reference_loot_template.Entry](loot_template#entry)          | 物品 id [_loot_template.Item 或 reference_loot_template.Item)](loot_template#item)  | 始终为 0                                                           | 始终为 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_MAIL_LOOT_TEMPLATE          | 6   | [mail_loot_template.Entry 或 reference_loot_template.Entry](loot_template#entry)          | 物品 id [_loot_template.Item 或 reference_loot_template.Item)](loot_template#item)  | 始终为 0                                                           | 始终为 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_MILLING_LOOT_TEMPLATE       | 7   | [milling_loot_template.Entry 或 reference_loot_template.Entry](loot_template#entry)       | 物品 id [_loot_template.Item 或 reference_loot_template.Item)](loot_template#item)  | 始终为 0                                                           | 始终为 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_PICKPOCKETING_LOOT_TEMPLATE | 8   | [pickpocketing_loot_template.Entry 或 reference_loot_template.Entry](loot_template#entry) | 物品 id [_loot_template.Item 或 reference_loot_template.Item)](loot_template#item)  | 始终为 0                                                           | 始终为 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_PROSPECTING_LOOT_TEMPLATE   | 9   | [prospecting_loot_template.Entry 或 reference_loot_template.Entry](loot_template#entry)   | 物品 id [_loot_template.Item 或 reference_loot_template.Item)](loot_template#item)  | 始终为 0                                                           | 始终为 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_REFERENCE_LOOT_TEMPLATE     | 10  | [reference_loot_template.Entry](loot_template#entry)                                      | 物品 id [_loot_template.Item 或 reference_loot_template.Item)](loot_template#item)  | 始终为 0                                                           | 始终为 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_SKINNING_LOOT_TEMPLATE      | 11  | [skinning_loot_template.Entry 或 reference_loot_template.Entry](loot_template#entry)      | 物品 id ([_loot_template.Item 或 reference_loot_template.Item)](loot_template#item) | 始终为 0                                                           | 始终为 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_SPELL_LOOT_TEMPLATE         | 12  | [spell_loot_template.Entry 或 reference_loot_template.Entry](loot_template#entry)         | 物品 id ([_loot_template.Item 或 reference_loot_template.Item)](loot_template#item) | 始终为 0                                                           | 始终为 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_SPELL_IMPLICIT_TARGET       | 13  | 受条件影响的法术效果掩码：<br>1 = EFFECT_0，2 = EFFECT_1，4 = EFFECT_2  | [Spell.dbc](spell) 中的法术 ID                                                    | 始终为 0                                                           | 0：潜在法术目标<br>1：法术施法者                                                                               | 不要使用 wowhead 获取效果数量，wowhead 的数据有时与真实效果编号不符。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| CONDITION_SOURCE_TYPE_GOSSIP_MENU                 | 14  | [gossip_menu.MenuID](gossip_menu#menuid)                                                  | [gossip_menu.TextID](gossip_menu#textid)（指向 npc_text.ID）                    | 始终为 0                                                           | 0 = 玩家<br>1 = WorldObject                                                                                                | 核心会按从最小到最大的顺序遍历该菜单的所有 TextID，并在条件通过时不断覆盖 TextID，因此最后一个匹配的行生效。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| CONDITION_SOURCE_TYPE_GOSSIP_MENU_OPTION          | 15  | [gossip_menu_option.MenuID](gossip_menu_option#menuid)                                    | [gossip_menu_option.OptionID](gossip_menu_option#optionid)                          | 始终为 0                                                           | 0 = 玩家<br>1 = WorldObject                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_CREATURE_TEMPLATE_VEHICLE   | 16  | 始终为 0                                                                                  | 生物 entry（[creature_template.entry](creature_template#entry)）                 | 始终为 0                                                           | 0 = 骑乘载具的玩家<br>1 = 载具生物                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_SPELL                       | 17  | 始终为 0                                                                                  | [Spell.dbc](spell) 中的法术 ID                                                    | 始终为 0                                                           | 0 = 法术施法者<br>1 = 法术的明确目标（仅适用于会考虑施法者所选对象的法术） | 此源类型允许你为要施放的法术定义施法者/明确目标的要求。<br>法术的明确目标是指玩家施法时选择的目标，并非所有法术都会考虑该目标。法术的非明确目标（例如由法术按区域或附近目标等方式选中的目标）不受此条件源类型影响，如果你想影响这些目标，请改用 CONDITION_SOURCE_TYPE_SPELL_IMPLICIT_TARGET。<br>如果你在寻找旧的 CONDITION_SOURCE_TYPE_ITEM_REQUIRED_TARGET，请改用此条件源类型（ConditionTarget = 1 允许你为给定法术设置要求，因此要使用此条件类型，你需要获得物品使用时所施法术的法术 ID）。<br>请记住，具有相同 ElseGroup 值的条件将用于进行逻辑 AND 检查，因此要为同一法术效果允许不同目标，你必须相应地设置 ElseGroup。 |
| CONDITION_SOURCE_TYPE_SPELL_CLICK_EVENT           | 18  | 生物 entry（[npc_spellclick_spells.npc_entry](npc_spellclick_spells#npcentry)）        | 法术（[npc_spellclick_spells.spell_id](npc_spellclick_spells#spellid)）             | 始终为 0                                                           | 0 = 点击者<br>1 = 法术点击目标（被点击者）                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_QUEST_AVAILABLE             | 19  | 始终为 0                                                                                  | [任务 ID](quest_template#id)                                                       | 始终为 0                                                           | 始终为 0                                                                                                                     | 必须满足该条件，任务才能对玩家可用。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| CONDITION_SOURCE_TYPE_GOSSIP_HELLO                | 20  | 始终为 0                                                                                  | 生物 entry（[creature_template.entry](creature_template#entry)）                 | 始终为 0                                                           | 0 = 玩家<br>1 = WorldObject                                                                                                | 如果条件不满足，则阻止从 NPC 打开 gossip 菜单。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| CONDITION_SOURCE_TYPE_VEHICLE_SPELL               | 21  | 生物 entry（[creature_template.entry](creature_template#entry)）                       | [Spell.dbc](spell) 中的法术 ID                                                    | 始终为 0                                                           | 0 = 显示法术栏的玩家<br>1 = 载具生物                                                               | 这将显示或隐藏载具法术栏中的法术。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| CONDITION_SOURCE_TYPE_SMART_EVENT                 | 22  | ID（[smart_scripts.id](smart_scripts#id)）+ 1                                             | EntryOrGuid（[smart_scripts.entryorguid](smart_scripts#entryorguid)）                | SourceType（[smart_scripts.source_type](smart_scripts#sourcetype)） | 0 = 调用者<br>1 = 对象                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_NPC_VENDOR                  | 23  | 商人 entry（[npc_vendor.entry](npc_vendor#entry)）                                       | 物品 entry（[npc_vendor.item](npc_vendor#item)）                                     | 始终为 0                                                           | 始终为 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_SPELL_PROC                  | 24  | 始终为 0                                                                                  | 触发 proс的 aura 的法术 ID                                            | 始终为 0                                                           | 0 = 行为者（Actor）<br>1 = 行为目标（ActionTarget）                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_PLAYER_LOOT_TEMPLATE        | 28  | player_loot_template.entry                                                                | 始终为 0                                                                            | 始终为 0                                                           | 始终为 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_CREATURE_RESPAWN            | 29  | enum-no-details\|29                                                                       | enum-no-details\|29                                                                 | enum-no-details\|29                                                | enum-no-details\|29                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_OBJECT_VISIBILITY           | 30  | 0 = 生物，1 = 游戏对象                                                              | 生物 entry（[creature_template.entry](creature_template#entry)）或游戏对象 entry（[gameobject_template.entry](gameobject_template#entry)） | 0 = 任意 guid（entry 级别），或特定的生物/游戏对象 guid   | 0 = 玩家<br>1 = WorldObject（生物/游戏对象）                                                                          | 控制生物和游戏对象的可见性。如果按 guid（SourceId）设置，条件优先于 entry。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| CONDITION_SOURCE_TYPE_MAX                         | 31  |                                                                                           |                                                                                     |                                                                    |                                                                                                                              | （占位符）                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### SourceGroup

参见上文。

### SourceEntry

参见上文。

### ElseGroup

允许构建分组条件——属于同一条件（相同 [SourceType](#sourcetypeorreferenceid)、[SourceGroup](#sourcegroup) 和 [SourceEntry](#sourceentry)）且 ElseGroup 中数字相同的所有条目构成一个组。当**其中任何一个组**满足时，**整个条件**即被满足（逻辑 OR）。当**该组的所有条目**都满足时，**该组**即被满足（逻辑 AND）。

示例：

两个条件具有相同的 SourceType、SourceGroup 和 SourceEntry，但条件不同，第一个的 ElseGroup = 1，第二个的 ElseGroup = 2，这将构成逻辑 OR。

两个条件具有相同的 SourceType、SourceGroup 和 SourceEntry，但条件不同，且两者的 ElseGroup 都为 1，这将构成逻辑 AND。

### ConditionTypeOrReference

| ConditionTypeOrReference (名称)    | 值 | ConditionValue1                                                                                                                                                                                                                                                                                                                             | ConditionValue2                                                                                                                                                                                                                                                                                                                                                                                                     | ConditionValue3                                                                                                                                                                                                                                                                                         |
| ---------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CONDITION_NONE                     | 0     | （从未使用）                                                                                                                                                                                                                                                                                                                                | （从未使用）                                                                                                                                                                                                                                                                                                                                                                                                        | （从未使用）                                                                                                                                                                                                                                                                                            |
| CONDITION_AURA                     | 1     | [Spell.dbc](spell) 中的法术 ID                                                                                                                                                                                                                                                                                                            | 效果索引（0-2）                                                                                                                                                                                                                                                                                                                                                                                                  | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_ITEM                     | 2     | 物品 entry（[item_template.entry](item_template#entry)）                                                                                                                                                                                                                                                                                     | 物品数量                                                                                                                                                                                                                                                                                                                                                                                                          | 0 = 不在银行中，1 = 在银行中                                                                                                                                                                                                                                                                            |
| CONDITION_ITEM_EQUIPPED            | 3     | 物品 entry（[item_template.entry](item_template#entry)）                                                                                                                                                                                                                                                                                     | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_ZONEID                   | 4     | 此条件为真时的区域 ID。                                                                                                                                                                                                                                                                                                  | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_REPUTATION_RANK          | 5     | [Faction.dbc](faction) 中的阵营模板 ID                                                                                                                                                                                                                                                                                             | 声望等级：<br>1 = 仇恨<br>2 = 敌对<br>4 = 不友善<br>8 = 中立<br>16 = 友善<br>32 = 尊敬<br>64 = 崇敬<br>128 = 崇拜<br><br>将目标等级相加，即可让条件在所有这些等级下均为真。                                                                                                                                                                                         | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_TEAM                     | 6     | 阵营 ID：联盟 = 469 / 部落 = 67                                                                                                                                                                                                                                                                                                        | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_SKILL                    | 7     | 所需技能。参见 [SkillLine.dbc](skillline)。                                                                                                                                                                                                                                                                                            | 技能等级值（例如 3.3.5 分支为 1 到 450）                                                                                                                                                                                                                                                                                                                                                          | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_QUESTREWARDED            | 8     | 任务 ID - 参见 [quest_template.id](quest_template#id)                                                                                                                                                                                                                                                                                       | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_QUESTTAKEN               | 9     | 任务 ID - 参见 [quest_template.id](quest_template#id)                                                                                                                                                                                                                                                                                       | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_DRUNKENSTATE             | 10    | 清醒=0；微醺=1，醉酒=2，烂醉=3                                                                                                                                                                                                                                                                                                        | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_WORLD_STATE              | 11    | 世界状态索引                                                                                                                                                                                                                                                                                                                           | 世界状态值                                                                                                                                                                                                                                                                                                                                                                                                   | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_ACTIVE_EVENT             | 12    | 事件 entry（[game_event.eventEntry](game_event#evententry)）                                                                                                                                                                                                                                                                                | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_INSTANCE_INFO            | 13    | **entry**（参见相应的脚本源文件以获取信息）                                                                                                                                                                                                                                                                                  | **data**（参见相应的脚本源文件以获取更多信息）                                                                                                                                                                                                                                                                                                                                                      | 0=INSTANCE_INFO_DATA<br>1=INSTANCE_INFO_GUID_DATA<br>2=INSTANCE_INFO_BOSS_STATE<br>3=INSTANCE_INFO_DATA64                                                                                                                                                                                               |
| CONDITION_QUEST_NONE               | 14    | 任务 ID - 参见 [quest_template.id](quest_template#id)                                                                                                                                                                                                                                                                                       | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_CLASS                    | 15    | [ChrClasses.dbc](chrclasses) 中的职业掩码<br>将所有条件为真的职业的标志相加。                                                                                                                                                                                                                                 | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_RACE                     | 16    | [ChrRaces.dbc](chrraces) 中的种族掩码。<br>将所有条件为真的种族的标志相加。                                                                                                                                                                                                                                      | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_ACHIEVEMENT              | 17    | [Achievement.dbc](achievement) 中的成就 ID                                                                                                                                                                                                                                                                                          | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_TITLE                    | 18    | [CharTitles.dbc](https://wowdev.wiki/DB/CharTitles) 中的头衔 ID                                                                                                                                                                                                                                                                                                  | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_SPAWNMASK                | 19    | 来自<br>[Creature.spawnMask](creature#spawnmask) / [Gameobject.spawnMask](gameobject#spawnmask) 的 spawnMask                                                                                                                                                                                                                                   | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_GENDER                   | 20    | 0 = 男，1 = 女，2 = 无                                                                                                                                                                                                                                                                                                              | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_UNIT_STATE               | 21    | UnitState（[来自 Unit.h 的枚举](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Entities/Unit/Unit.h#L498)）                                                                                                                                                                                                      | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_MAPID                    | 22    | 来自 Map.dbc 的地图 entry<br>（0=东部王国，1=卡利姆多，以此类推。）                                                                                                                                                                                                                                                                    | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_AREAID                   | 23    | 来自 AreaTable.dbc 的区域 ID                                                                                                                                                                                                                                                                                                                  | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_CREATURE_TYPE            | 24    | [creature_template.type](creature_template#type) 中的生物类型<br>如果 creature_template.type == ConditionValue1，则为真                                                                                                                                                                                                                    | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_SPELL                    | 25    | [Spell.dbc](spell) 中的法术 ID                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_PHASEMASK                | 26    | phasemask 值                                                                                                                                                                                                                                                                                                                             | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_LEVEL                    | 27    | 玩家等级（3.3.5 中为 1-80）                                                                                                                                                                                                                                                                                                                | 可选：0 = 等级必须相等，1 = 等级必须更高，2 = 等级必须更低，<br>3 = 等级必须更高或相等，4 = 等级必须更低或相等。                                                                                                                                                                                                                                                       | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_QUEST_COMPLETE           | 28    | 任务 ID - 参见 [quest_template.id](quest_template#id)                                                                                                                                                                                                                                                                                       | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_NEAR_CREATURE            | 29    | [creature_template.entry](creature_template#entry) 中的生物 entry                                                                                                                                                                                                                                                                      | 以码为单位的距离                                                                                                                                                                                                                                                                                                                                                                                                   | 存活=0 / 死亡=1                                                                                                                                                                                                                                                                                        |
| CONDITION_NEAR_GAMEOBJECT          | 30    | [gameobject_template.entry](gameobject_template#entry) 中的游戏对象 entry                                                                                                                                                                                                                                                                | 以码为单位的距离                                                                                                                                                                                                                                                                                                                                                                                                   | GoState<br><br>0 = 忽略，1 = 就绪，2 = 未就绪                                                                                                                                                                                                                                                     |
| CONDITION_OBJECT_ENTRY_GUID        | 31    | TypeID。可用的对象类型：<br>3：TYPEID_UNIT<br>4：TYPEID_PLAYER<br>5：TYPEID_GAMEOBJECT<br>7：TYPEID_CORPSE（玩家尸体，灵魂释放后）                                                                                                                                                                                 | 0 = 给定 TypeID 的任意对象<br>如果 TypeID = TYPEID_UNIT => [creature_template.entry](creature_template#entry) 中的生物 entry<br>如果 TypeID = TYPEID_GAMEOBJECT => [gameobject_template.entry](gameobject_template#entry) 中的游戏对象 entry                                                                                                                                                                | 0 = 给定类型的任意对象<br>1 - 500k：生物 / 游戏对象 GUID                                                                                                                                                                                                                                   |
| CONDITION_TYPE_MASK                | 32    | TypeMask - 以下对象类型的位掩码：<br>0x0008 - TYPEMASK_UNIT (8)<br>0x0010 - TYPEMASK_PLAYER (16)<br>0x0020 - TYPEMASK_GAMEOBJECT (32)<br>0x0080 - TYPEMASK_CORPSE（灵魂释放后的玩家尸体）(128)                                                                                                                  | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_RELATION_TO              | 33    | 检查关系的目标。<br>- 当前 [SourceType](#sourcetypeorreferenceid) 中可用的 ConditionTarget 之一                                                                                                                                                                                                           | RelationType - 定义当前 ConditionTarget 与 ConditionValue1 中指定目标的关系。<br>0 - RELATION_SELF<br>1 - RELATION_IN_PARTY<br>2 - RELATION_IN_RAID_OR_PARTY<br>3 - RELATION_OWNED_BY（ConditionTarget 归 ConditionValue1 所有）<br>4 - RELATION_PASSENGER_OF（ConditionTarget 是 ConditionValue1 的乘客）<br>5 - RELATION_CREATED_BY（ConditionTarget 由 ConditionValue1 召唤） | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_REACTION_TO              | 34    | 检查反应的目标。<br>- 当前 [SourceType](#sourcetypeorreferenceid) 中可用的 ConditionTarget 之一                                                                                                                                                                                                           | rankMask：此位掩码定义了当前 ConditionTarget 对 ConditionValue1 中指定目标（被允许的）反应。<br>反应的标志为：<br>1 = 仇恨<br>2 = 敌对<br>4 = 不友善<br>8 = 中立<br>16 = 友善<br>32 = 尊敬<br>64 = 崇敬<br>128 = 崇拜                                                                                                        | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_DISTANCE_TO              | 35    | 检查距离的目标<br>- 当前 [SourceType](#sourcetypeorreferenceid) 中可用的 ConditionTarget 之一                                                                                                                                                                                                                                                | 距离。<br>定义当前 ConditionTarget 与 ConditionValue1 中指定目标之间的距离                                                                                                                                                                                                                                                                                                               | 比较类型：<br>0 = 距离必须等于 ConditionValue2<br>1 = 距离必须高于 ConditionValue2<br>2 = 距离必须低于 ConditionValue2<br>3 = 距离必须等于或高于 ConditionValue2<br>4 = 距离必须等于或低于 ConditionValue2 |
| CONDITION_ALIVE                    | 36    | 始终为 0 - 使用 NegativeCondition 和以下设置：<br>如果目标需要**存活**，则 NegativeCondition = 0。<br>如果目标需要**死亡**，则 NegativeCondition = 1。<br>注意：生物的尸体和看起来已死亡的生物<br>是两回事。一个是真正死了，<br>另一个只是使用表情装作死了。 | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_HP_VAL                   | 37    | HP 值                                                                                                                                                                                                                                                                                                                                    | 比较类型：<br>0 = HP 必须相等<br>1 = HP 必须更高<br>2 = HP 必须更低<br>3 = HP 必须等于或更高<br>4 = HP 必须等于或更低                                                                                                                                                                                                                                                       | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_HP_PCT                   | 38    | 最大 HP 的百分比                                                                                                                                                                                                                                                                                                                        | 比较类型：<br>0 = 最大 HP 的百分比必须相等<br>1 = 最大 HP 的百分比必须更高<br>2 = 最大 HP 的百分比必须更低<br>3 = 最大 HP 的百分比必须等于或更高<br>4 = 最大 HP 的百分比必须等于或更低                                                                                                                                                              | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_REALM_ACHIEVEMENT        | 39    | [Achievement.dbc](achievement) 中的成就 ID                                                                                                                                                                                                                                                                                          | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_IN_WATER                 | 40    | 始终为 0 - 使用 NegativeCondition 和以下设置：如果目标需要在陆地上，则 NegativeCondition = 0；如果目标需要在水中，则 NegativeCondition = 1                                                                                                                                                                       | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_STAND_STATE              | 42    | stateType（精确或任意）：0 = ConditionValue2 中使用的**精确**状态 1 = ConditionValue2 中的**任意**类型状态                                                                                                                                                                                                                          | 精确的站立状态，或通用状态（站立 / 坐下），取决于值 10 = 站立 1 = 坐下                                                                                                                                                                                                                                                                                                                     | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_DAILY_QUEST_DONE         | 43    | 任务 ID - 参见 [quest_template.id](quest_template#id)                                                                                                                                                                                                                                                                                       | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_CHARMED                  | 44    | 始终为 0                                                                                                                                                                                                                                                                                                                                    | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_PET_TYPE                 | 45    | mask                                                                                                                                                                                                                                                                                                                                        | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_TAXI                     | 46    | 始终为 0                                                                                                                                                                                                                                                                                                                                    | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_QUESTSTATE               | 47    | 任务 ID - 参见 [quest_template.id](quest_template#id)                                                                                                                                                                                                                                                                                       | state_mask：<br>1 = 未接取<br>2 = 已完成<br>8 = 进行中<br>32 = 失败<br>64 = 已交还                                                                                                                                                                                                                                                                                                                    | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_QUEST_OBJECTIVE_PROGRESS | 48    | 任务 ID - 参见 [quest_template.id](quest_template#id)                                                                                                                                                                                                                                                                                       | 任务目标 ID - 参见 [quest_template.RequiredNpcOrGo](quest_template#requirednpcorgo)                                                                                                                                                                                                                                                                                                                           | 任务目标数量                                                                                                                                                                                                                                                                                   |
| CONDITION_DIFFICULTY_ID            | 49    | 难度                                                                                                                                                                                                                                                                                                                                  | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_QUEST_SATISFY_EXCLUSIVE  | 101   | quest_id                                                                                                                                                                                                                                                                                                                                    | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_HAS_AURA_TYPE            | 102   | aura_type                                                                                                                                                                                                                                                                                                                                   | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_WORLD_SCRIPT             | 103   | conditionId                                                                                                                                                                                                                                                                                                                                 | state                                                                                                                                                                                                                                                                                                                                                                                                               | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_AI_DATA                  | 104   | dataId（如果 AI::GetData(uint32 dataId) 返回值则为真）                                                                                                                                                                                                                                                                                   | value                                                                                                                                                                                                                                                                                                                                                                                                               | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_RANDOM_DUNGEON           | 105   | checkDifficulty                                                                                                                                                                                                                                                                                                                             | difficulty                                                                                                                                                                                                                                                                                                                                                                                                          | 始终为 0                                                                                                                                                                                                                                                                                                |
| CONDITION_UNIT_IN_COMBAT           | 106   | 始终为 0                                                                                                                                                                                                                                                                                                                                    | 始终为 0                                                                                                                                                                                                                                                                                                                                                                                                            | 始终为 0                                                                                                                                                                                                                                                                                                |

### ConditionTarget

允许选择要为其检查条件的对象。可用对象取决于 SourceTypeOrReferenceId，详情参见相应的源类型参考。

### ConditionValue1

参见下文

### ConditionValue2

参见下文

### ConditionValue3

参见下文

### NegativeCondition

如果设置为 1，条件将被"反转"。

示例：带 NegativeCondition 的 CONDITION\_AURA 在玩家**没有**该 aura 时为真。

### ErrorType

来自 [/src/server/game/Miscellaneous/SharedDefines.h#L830](https://github.com/azerothcore/azerothcore-wotlk/blob/97e65bd4479272106bba87364d35233d2e4bd2ef/src/server/game/Miscellaneous/SharedDefines.h#L830) 的 ID。仅对以下条件[源类型](#sourcetypeorreferenceid)显示：

CONDITION\_SOURCE\_TYPE\_SPELL = 17

### ErrorTextId

来自 [/src/server/game/Miscellaneous/SharedDefines.h#L1024](https://github.com/azerothcore/azerothcore-wotlk/blob/97e65bd4479272106bba87364d35233d2e4bd2ef/src/server/game/Miscellaneous/SharedDefines.h#L1024) 的 ID。仅对以下条件[源类型](#sourcetypeorreferenceid)显示：

CONDITION\_SOURCE\_TYPE\_SPELL = 17

（ErrorType 必须为 SPELL\_FAILED\_CUSTOM\_ERROR (209)，否则为 0）

### ScriptName

此条件使用的 ScriptName（如果有）。

### Comment

此条件或引用的说明。

### 条件类型说明

[SourceGroup](#sourcegroup) 和 [SourceEntry](#sourceentry) 字段的内容取决于 [SourceTypeOrReferenceId](#sourcetypeorreferenceid)

**CONDITION\_SOURCE\_TYPE\_NONE = 0**

**仅在引用模板中使用！参见下文。**

**CONDITION\_SOURCE\_TYPE\_ \* \_LOOT\_TEMPLATE = 1 - 12**
\***SourceGroup：loot entry（**\_loot\_template.Entry 或 Reference\_loot\_template.Entry）
\***SourceEntry：物品 id（**\_loot\_template.Item 或 Reference\_loot\_template.Item）

-   -   ConditionTarget：始终为 0

*示例：如果你使用类型 1（creature\_loot\_template），则使用该表的 entry 和 item 字段*

**CONDITION\_SOURCE\_TYPE\_SPELL\_IMPLICIT\_TARGET = 13**

-   -   SourceGroup：受条件影响的法术效果掩码（1 - EFFECT\_0，2 - EFFECT\_1，4 - EFFECT\_2 - 不要使用 wowhead 获取效果数量，wowhead 的数据有时与真实效果编号不符）
    -   SourceEntry：法术（来自 [Spell.dbc](spell) 的法术 ID。）
    -   ConditionTarget：
        -   0 - 法术的潜在目标
        -   1 - 法术的施法者

备注：

-   此条件源类型允许为可能的法术效果目标定义过滤器，因此只有匹配条件的对象才会被选为法术的隐式目标。只允许过滤 *AREA*、*NEARBY* 和 *CONE* 目标类型。此源类型只影响由法术选择的目标，不影响玩家施法时选择的法术目标，要影响该目标请使用 CONDITION\_SOURCE\_TYPE\_SPELL。
-   要将目标限制为仅玩家，请使用带 TYPEMASK\_PLAYER + TYPEMASK\_CORPSE 的 CONDITION\_TYPEMASK，以允许对死亡玩家施放。
-   请记住，具有相同 ElseGroup 值的条件将用于进行逻辑 AND 检查，因此要为同一法术效果允许不同目标，你必须相应地设置 ElseGroup。
-   如果你在寻找旧的 CONDITION\_SOURCE\_TYPE\_SPELL\_SCRIPT\_TARGET - 请改用此条件源类型

**CONDITION\_SOURCE\_TYPE\_GOSSIP\_MENU = 14**

-   -   SourceGroup：gossip 菜单 entry（[gossip\_menu.MenuID](gossip_menu#menuid)）
    -   SourceEntry：gossip 菜单文本 id（[gossip\_menu.TextID](gossip_menu#textid)）
    -   ConditionTarget：
        -   0 - 显示 gossip 文本的玩家
        -   1 - 提供 gossip 的 WorldObject

**CONDITION\_SOURCE\_TYPE\_GOSSIP\_MENU\_OPTION = 15**

-   -   SourceGroup：gossip 菜单 entry（[gossip\_menu\_option.MenuID](gossip_menu_option#menuid)）
    -   SourceEntry：gossip 菜单选项 id（[gossip\_menu\_option.OptionID](gossip_menu_option#optionid)）
    -   ConditionTarget：
        -   0 - 显示 gossip 文本的玩家
        -   1 - 提供 gossip 的 WorldObject

**CONDITION\_SOURCE\_TYPE\_CREATURE\_TEMPLATE\_VEHICLE = 16**

-   -   SourceGroup：始终为 0
    -   SourceEntry：生物 entry（[creature\_template.entry](creature_template#entry)）
    -   ConditionTarget：
        -   0 - 骑乘载具的玩家
        -   1 - 载具生物

注意：生物 entry 必须是载具。示例：如果与 CONDITION\_AREA 一起使用，当骑乘的玩家离开该区域时，玩家将从载具上被卸下。

**CONDITION\_SOURCE\_TYPE\_SPELL = 17**

-   -   SourceGroup：始终为 0
    -   SourceEntry：法术（来自 [Spell.dbc](spell) 的法术 ID）
    -   ConditionTarget：
        -   0 - 法术的施法者
        -   1 - 法术的明确目标（仅适用于会考虑施法者所选对象的法术）

备注：

-   此源类型允许你为要施放的法术定义施法者/明确目标的要求。
-   法术的明确目标是指玩家施法时选择的目标，并非所有法术都会考虑该目标。法术的非明确目标（例如由法术按区域或附近目标等方式选中的目标）不受此条件源类型影响，如果你想影响这些目标，请改用 CONDITION\_SOURCE\_TYPE\_SPELL\_IMPLICIT\_TARGET。
-   如果你在寻找旧的 CONDITION\_SOURCE\_TYPE\_ITEM\_REQUIRED\_TARGET - 请改用此条件源类型（ConditionTarget = 1 允许你为给定法术设置要求，因此要使用此条件类型，你需要获得物品使用时所施法术的法术 ID）
-   请记住，具有相同 ElseGroup 值的条件将用于进行逻辑 AND 检查，因此要为同一法术效果允许不同目标，你必须相应地设置 ElseGroup。

**CONDITION\_SOURCE\_TYPE\_SPELL\_CLICK\_EVENT = 18**

-   -   SourceGroup：生物 entry（[npc\_spellclick\_spells.npc\_entry](npc_spellclick_spells#npcentry)）
    -   SourceEntry：法术（[npc\_spellclick\_spells.spell\_id](npc_spellclick_spells#spellid)）
    -   ConditionTarget：
        -   0 - 点击者
        -   1 - 法术点击目标（被点击者）

**CONDITION\_SOURCE\_TYPE\_QUEST\_ACCEPT = 19**

-   -   SourceGroup：?
    -   SourceEntry：任务 [id](quest_template#id)）
    -   ConditionTarget：始终为 0

**CONDITION\_SOURCE\_TYPE\_GOSSIP\_HELLO = 20**

-   -   SourceGroup：始终为 0
    -   SourceEntry：生物 entry（[creature\_template.entry](creature_template#entry)）
    -   ConditionTarget：
        -   0 - 玩家
        -   1 - WorldObject（生物）

注意：如果条件不满足，此条件会阻止从 NPC 打开 gossip 菜单。

**CONDITION\_SOURCE\_TYPE\_VEHICLE\_SPELL = 21**

-   -   SourceGroup：生物 entry（[creature\_template.entry](creature_template#entry)）
    -   SourceEntry：法术（来自 [Spell.dbc](spell) 的法术 ID）
    -   ConditionTarget：
        -   0 - 显示法术栏的玩家
        -   1 - 载具生物

注意：它将显示或隐藏载具法术栏中的法术。

**CONDITION\_SOURCE\_TYPE\_SMART\_EVENT = 22**

-   -   SourceGroup：Id（[smart\_scripts.id](smart_scripts#id)）+ 1
    -   SourceEntry：EntryOrGuid（[smart\_scripts.entryorguid](smart_scripts#entryorguid)）
    -   SourceId：SourceType（[smart\_scripts.source\_type](smart_scripts#sourcetype)）
    -   ConditionTarget：
        -   0 - 调用者
        -   1 - 对象

**CONDITION\_SOURCE\_TYPE\_NPC\_VENDOR = 23**

-   -   SourceGroup：商人 entry（[npc\_vendor.entry](npc_vendor#entry)）
    -   SourceEntry：物品 entry（[npc\_vendor.item](npc_vendor#item)）
    -   SourceId：始终为 0

**CONDITION\_SOURCE\_TYPE\_SPELL\_PROC = 24**

-   -   SourceGroup：始终为 0
    -   SourceEntry：触发 proс 的 aura 的法术 id
    -   ConditionTarget：
        -   0 - 行为者（Actor）
        -   1 - 行为目标（ActionTarget）

**CONDITION\_SOURCE\_TYPE\_OBJECT\_VISIBILITY = 30**

-   -   SourceGroup：生物为 0，游戏对象为 1
    -   SourceEntry：生物 entry（[creature\_template.entry](creature_template#entry)）或游戏对象 entry（[gameobject\_template.entry](gameobject_template#entry)）
    -   SourceId：0 表示任意 guid（entry 级别），或特定的生物/游戏对象 guid
    -   ConditionTarget：
        -   0 - 玩家
        -   1 - WorldObject（生物/游戏对象）

注意：此条件根据针对玩家评估的条件来控制生物和游戏对象的可见性。如果按 guid（SourceId）设置条件，则它们优先于 entry 级别的条件。

### ConditionValueX 字段说明

**CONDITION\_NONE = 0**

**从未使用**

**CONDITION\_AURA = 1**

-   -   ConditionValue1：法术（来自 [Spell.dbc](spell) 的法术 ID）
    -   ConditionValue2：效果索引（0-2）
    -   ConditionValue3：始终为 0

**CONDITION\_ITEM = 2**

-   -   ConditionValue1：物品 entry（[item\_template.entry](item_template#entry)）
    -   ConditionValue2：物品数量
    -   ConditionValue3：在银行中？（true=1）

**CONDITION\_ITEM\_EQUIPPED = 3**

-   -   ConditionValue1：物品 entry（[item\_template.entry](item_template#entry)）
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_ZONEID = 4**

-   -   ConditionValue1：此条件为真时的区域 ID
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_REPUTATION\_RANK = 5**

-   -   ConditionValue1：阵营模板 ID（来自 [Faction.dbc](faction)）
    -   ConditionValue2：声望等级（仇恨 - 1，敌对 - 2，不友善 - 4，中立 - 8，友善 - 16，尊敬 - 32，崇敬 - 64，崇拜 - 128）可以将标志相加，用于条件应为真的所有等级。
    -   ConditionValue3：始终为 0

**CONDITION\_TEAM = 6**

-   -   ConditionValue1：阵营 id（469 - 联盟，67 - 部落）
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_SKILL = 7**

-   -   ConditionValue1：所需技能，参见 [SkillLine.dbc](skillline)
    -   ConditionValue2：技能等级值
    -   ConditionValue3：始终为 0

**CONDITION\_QUESTREWARDED = 8**

-   -   ConditionValue1：（[quest\_template.id](quest_template#id)）
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_QUESTTAKEN = 9**

-   -   ConditionValue1：（[quest\_template.id](quest_template#id)）
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_DRUNKENSTATE = 10**

-   -   ConditionValue1：醉酒状态：0 - 清醒；1 - 微醺，2 - 醉酒，3 - 烂醉
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0
    -   （以前是 AD\_COMMISSION\_AURA）

**CONDITION\_WORLD\_STATE = 11**

-   -   ConditionValue1：世界状态索引
    -   ConditionValue2：世界状态值
    -   ConditionValue3：始终为 0

**CONDITION\_ACTIVE\_EVENT= 12**

-   -   ConditionValue1：事件 entry（[game\_event.eventEntry](game_event#evententry)）
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_INSTANCE\_INFO = 13**

-   -   ConditionValue1：entry //参见相应的脚本源文件以获取更多信息
    -   ConditionValue2：data //参见相应的脚本源文件以获取更多信息
    -   ConditionValue3：type：
        -   0 - INSTANCE\_INFO\_DATA
        -   1 - INSTANCE\_INFO\_GUID\_DATA
        -   2 - INSTANCE\_INFO\_BOSS\_STATE
        -   3 - INSTANCE\_INFO\_DATA64

**CONDITION\_QUEST\_NONE = 14**

-   -   ConditionValue1：（[quest\_template.id](quest_template#id)）
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_CLASS = 15**

-   -   ConditionValue1：职业掩码。将所有条件应为真的职业的标志相加。参见 [ChrClasses.dbc](chrclasses)
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_RACE = 16**

-   -   ConditionValue1：种族掩码。将所有条件应为真的种族的标志相加。参见 [ChrRaces.dbc](chrraces)
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_ACHIEVEMENT = 17**

-   -   ConditionValue1：来自 [Achievement.dbc](achievement) 的成就 ID
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_TITLE = 18**

-   -   ConditionValue1：来自 [CharTitles.dbc](https://wowdev.wiki/DB/CharTitles) 的头衔 ID
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_SPAWNMASK = 19**

-   -   ConditionValue1：spawnMask（参见 [Gameobject.spawnMask](gameobject#spawnmask)/[Creature.spawnMask](creature#spawnmask)）
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_GENDER = 20**

-   -   ConditionValue1：0 = 男，1 = 女，2 = 无
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_UNIT\_STATE = 21**

-   -   ConditionValue1：UnitState（[枚举](https://github.com/azerothcore/azerothcore-wotlk/blob/97e65bd4479272106bba87364d35233d2e4bd2ef/src/server/game/Entities/Unit/Unit.h#L451)）
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_MAPID = 22**

-   -   ConditionValue1：地图 entry
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_AREAID = 23**

-   -   ConditionValue1：区域 ID
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_CREATURE\_TYPE = 24**

-   -   ConditionValue1：生物类型（[creature\_template.type](creature_template#entry)）。如果 creature\_template.type == ConditionValue1，则条件为真
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_SPELL = 25**

-   -   ConditionValue1：法术（来自 [Spell.dbc](spell) 的法术 ID）
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_PHASEMASK = 26**

-   -   ConditionValue1：phasemask 值
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_LEVEL = 27**

-   -   ConditionValue1：玩家等级
    -   ConditionValue2：可选
        -   0 = 等级必须相等
        -   1 = 等级必须更高
        -   2 = 等级必须更低
        -   3 = 等级必须相等或更高
        -   4 = 等级必须相等或更低
    -   ConditionValue3：始终为 0

**CONDITION\_QUEST\_COMPLETE = 28**

-   -   ConditionValue1：任务 [id](quest_template#id)
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

*仅当玩家已满足任务的所有目标，但尚未交还任务时。*

**CONDITION\_NEAR\_CREATURE = 29**

-   -   ConditionValue1：生物 [entry](creature_template#entry)
    -   ConditionValue2：距离（码）
    -   ConditionValue3：0 = 存活，1 = 死亡

**CONDITION\_NEAR\_GAMEOBJECT = 30**

-   -   ConditionValue1：游戏对象 [entry](gameobject_template#entry)
    -   ConditionValue2：距离（码）
    -   ConditionValue3：GoState，0 = 忽略，1 = 就绪，2 = 未就绪

**CONDITION\_OBJECT\_ENTRY\_GUID= 31**

-   -   ConditionValue1：TypeID - 可用的对象类型：
        -   3 - TYPEID\_UNIT
        -   4 - TYPEID\_PLAYER
        -   5 - TYPEID\_GAMEOBJECT
        -   7 - TYPEID\_CORPSE（玩家尸体，灵魂释放后）
    -   ConditionValue2：Entry
        -   0 表示给定类型的任意对象
        -   TypeID = TYPEID\_GAMEOBJECT 时为 [游戏对象 entry](gameobject_template#entry)
        -   TypeID = TYPEID\_UNIT 时为 [生物 entry](creature_template#entry)
    -   ConditionValue3：0 表示给定类型的任意对象，任何其他值表示匹配该 guid

**CONDITION\_TYPE\_MASK= 32**

-   -   ConditionValue1：TypeMask - 以下对象类型的位掩码：
        -   0x0008 - TYPEMASK\_UNIT
        -   0x0010 - TYPEMASK\_PLAYER
        -   0x0020 - TYPEMASK\_GAMEOBJECT
        -   0x0080 - TYPEMASK\_CORPSE（玩家尸体，灵魂释放后）
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_RELATION\_TO= 33**

-   -   ConditionValue1：检查关系的目标 - 当前 SourceType 中可用的 ConditionTarget 之一。
    -   ConditionValue2：RelationType - 定义当前 ConditionTarget 与 ConditionValue1 中指定目标的关系。
        -   0 - RELATION\_SELF
        -   1 - RELATION\_IN\_PARTY
        -   2 - RELATION\_IN\_RAID\_OR\_PARTY
        -   3 - RELATION\_OWNED\_BY（ConditionTarget 归 ConditionValue1 所有）
        -   4 - RELATION\_PASSENGER\_OF（ConditionTarget 是 ConditionValue1 的乘客）
        -   5 - RELATION\_CREATED\_BY（ConditionTarget 由 ConditionValue1 召唤）
    -   ConditionValue3：始终为 0

**CONDITION\_REACTION\_TO= 34**

-   -   ConditionValue1：检查反应的目标 - 当前 SourceType 中可用的 ConditionTarget 之一。
    -   ConditionValue2：rankMask - 定义当前 ConditionTarget 对 ConditionValue1 中指定目标被允许的反应。这是一个位掩码，反应的标志为：
        -   1 - 仇恨
        -   2 - 敌对
        -   4 - 不友善
        -   8 - 中立
        -   16 - 友善
        -   32 - 尊敬
        -   64 - 崇敬
        -   128 - 崇拜
    -   ConditionValue3：始终为 0

**CONDITION\_DISTANCE\_TO= 35**

-   -   ConditionValue1：检查距离的目标 - 当前 SourceType 中可用的 ConditionTarget 之一。
    -   ConditionValue2：距离 - 定义当前 ConditionTarget 与 ConditionValue1 中指定目标之间的距离。
    -   ConditionValue3：比较类型：
        -   0 = 距离必须等于 ConditionValue2
        -   1 = 距离必须高于 ConditionValue2
        -   2 = 距离必须低于 ConditionValue2
        -   3 = 距离必须等于或高于 ConditionValue2
        -   4 = 距离必须等于或低于 ConditionValue2

**CONDITION\_ALIVE= 36**

-   -   ConditionValue1：始终为 0
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0
    -   NegativeCondition：
        -   0（如果目标需要**存活**）
        -   1（如果目标需要**死亡**）
            *注意：生物的尸体和看起来已死亡的生物（creature that\_looks\_dead）是两回事。一个是真正死了，另一个只是使用表情装作死了。*

**CONDITION\_HP\_VAL = 37**

-   -   ConditionValue1：HP
    -   ConditionValue2：比较类型：
        -   0 = HP 必须相等
        -   1 = HP 必须更高
        -   2 = HP 必须更低
        -   3 = HP 必须相等或更高
        -   4 = HP 必须相等或更低
    -   ConditionValue3：始终为 0

**CONDITION\_HP\_PCT = 38**

-
    -   ConditionValue1：最大 HP 的百分比
    -   ConditionValue2：比较类型：
        -   0 = 最大 HP 的百分比必须相等
        -   1 = 最大 HP 的百分比必须更高
        -   2 = 最大 HP 的百分比必须更低
        -   3 = 最大 HP 的百分比必须相等或更高
        -   4 = 最大 HP 的百分比必须相等或更低
    -   ConditionValue3：始终为 0

**CONDITION\_REALM\_ACHIEVEMENT = 39**

-   -   ConditionValue1：来自 [Achievement.dbc](achievement) 的成就 ID
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0

**CONDITION\_IN\_WATER = 40**

-   -   ConditionValue1：始终为 0
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0
    -   NegativeCondition：
        -   0（如果目标需要在陆地上）
        -   1（如果目标需要在水中）

**CONDITION\_STAND\_STATE = 42**

-   -   ConditionValue1：stateType（精确或任意）
        -   0 = ConditionValue2 中使用的精确状态
        -   1 = ConditionValue2 中的任意类型状态
    -   ConditionValue2：精确的站立状态，或通用状态（站立 / 坐下），取决于值 1
        -   0 = 站立
        -   1 = 坐下
    -   ConditionValue3：始终为 0

**CONDITION\_WORLD\_SCRIPT = 103**

-   -   ConditionValue1：在 WorldState.h 中定义的 WorldStateCondition
    -   ConditionValue2：state 或 0（WORLD_STATE_CONDITION_STATE_NONE）
    -   ConditionValue3：始终为 0
        *注意：如果 WorldState::IsConditionFulfilled 返回 true，则条件为真*

**CONDITION\_AI\_DATA = 104**

当 `AI::GetData(ConditionValue1)` 返回 `ConditionValue2` 中指定的值时，返回 true。适用于使用 SmartAI 的生物和游戏对象。数据通过 `SMART_ACTION_SET_DATA` 存储。

-   -   ConditionValue1：dataId — 传递给 `AI::GetData()` 的键
    -   ConditionValue2：预期值 — 要与结果进行比较的值
    -   ConditionValue3：始终为 0

**CONDITION\_RANDOM\_DUNGEON = 105**

当玩家通过 LFG/RDF 系统排队随机副本时，返回 true。

- - `ConditionValue1`：0 = 不检查难度；1 = 检查难度（`ConditionValue2`）。
  - `ConditionValue2`：如果 `ConditionValue1 = 1`，与玩家当前地图难度进行比较。值必须小于 `MAX_DIFFICULTY`
  - `ConditionValue3`：始终为 0

**CONDITION\_UNIT\_IN\_COMBAT = 106**

当目标单位当前处于战斗中时，返回 true。

-   -   ConditionValue1：始终为 0
    -   ConditionValue2：始终为 0
    -   ConditionValue3：始终为 0
    -   NegativeCondition：
        -   0（如果目标**处于**战斗中则为 true）
        -   1（如果目标**未**处于战斗中则为 true）

*可与 `CONDITION_SOURCE_TYPE_GOSSIP_HELLO`（类型 20）和 `NegativeCondition = 1`（ConditionTarget = 1 以针对生物）一起使用，防止玩家在战斗时打开特定生物的 gossip 菜单。*

### \***引用模板（REFERENCE TEMPLATES）**

-   -   SourceTypeOrReferenceId：用作负数，作为引用 ID
    -   SourceGroup：始终为 0
    -   SourceEntry：始终为 0
    -   ElseGroup：OR 修饰符
    -   ConditionTypeOrReference：[ConditionTypeOrReference](#conditiontypeorreference)
    -   ConditionValue1：参见上文
    -   ConditionValue2：参见上文
    -   ConditionValue3：参见上文
    -   ErrorType：参见上文
    -   ErrorTextId：参见上文
    -   Comment：参见上文
