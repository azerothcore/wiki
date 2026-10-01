# quest_template_addon

[<-返回至:World](database-world)

**表：quest_template_addon**

包含额外定义，例如任务关联、依赖关系以及 [quest_template](quest_template) 表中定义的任务对玩家变为可用所需满足的条件。

**结构：**

| Field                                           | Type      | Attributes | Key | Null | Default | Extra | Comment                               |
| ----------------------------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------------------------------- |
| [ID](#id)                                       | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       | 链接到 quest_template.ID 的唯一 ID    |
| [MaxLevel](#maxlevel)                           | TINYINT   | UNSIGNED   |     | NO   |         |       |                                       |
| [AllowableClasses](#allowableclasses)           | INT       | UNSIGNED   |     | NO   |         |       |                                       |
| [SourceSpellID](#sourcespellid)                 | MEDIUMINT | UNSIGNED   |     | NO   |         |       |                                       |
| [PrevQuestID](#prevquestid)                     | MEDIUMINT |            |     | NO   |         |       |                                       |
| [NextQuestID](#nextquestid)                     | MEDIUMINT |            |     | NO   |         |       |                                       |
| [ExclusiveGroup](#exclusivegroup)               | MEDIUMINT |            |     | NO   |         |       |                                       |
| [BreadcrumbForQuestId](#breadcrumbforquestid)   | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |                                       |
| [RewardMailTemplateID](#rewardmailtemplateid)   | MEDIUMINT | UNSIGNED   |     | NO   |         |       |                                       |
| [RewardMailDelay](#rewardmaildelay)             | INT       | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredSkillID](#requiredskillid)             | SMALLINT  | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredSkillPoints](#requiredskillpoints)     | SMALLINT  | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredMinRepFaction](#requiredminrepfaction) | SMALLINT  | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredMaxRepFaction](#requiredmaxrepfaction) | SMALLINT  | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredMinRepValue](#requiredminrepvalue)     | MEDIUMINT |            |     | NO   |         |       |                                       |
| [RequiredMaxRepValue](#requiredmaxrepvalue)     | MEDIUMINT |            |     | NO   |         |       |                                       |
| [ProvidedItemCount](#provideditemcount)         | TINYINT   | UNSIGNED   |     | NO   |         |       |                                       |
| [SpecialFlags](#specialflags)                   | TINYINT   | UNSIGNED   |     | NO   |         |       |                                       |

**字段说明：**

### ID

唯一任务 ID，与 [quest_template.ID](quest_template#id) 中的同一任务 ID 对应。

### MaxLevel

角色可以接到该任务的最高玩家等级。

### AllowableClasses

接到该任务所需的职业。0 表示该任务对所有职业可用。
此字段是位掩码，可以组合多个职业值。请参阅 [ChrClasses.dbc](chrclasses)

### SourceSpellID

开始任务时对玩家施放的法术 ID。

### PrevQuestID

- **如果值 > 0：** 包含前一个任务 ID，必须先完成该任务才能开始此任务。
- **如果值 < 0：** 包含父任务 ID，必须先激活该任务才能开始此任务。

### NextQuestID

包含下一个任务 ID，以防那个任务的 PrevQuestId 不足以满足要求。

### ExclusiveGroup

- **如果 ExclusiveGroup > 0**

用于定义一组任务，只能从中选择和完成一个任务。例如，如果任务 1200、1201 和 1202 中只应允许选择一个，则将 1200 插入这 3 个任务的 ExclusiveGroup 中。

- **如果 ExclusiveGroup < 0**

用于定义一组任务，必须全部完成并获得奖励后才能开始下一个任务。例如，如果任务 1000 依赖于任务 1200、1201 和 1202 中的其中一个，且所有这些任务都有相同的负 ExclusiveGroup，那么必须先完成并获得所有这些任务的奖励，才能开始任务 1000。

注意：所有使用 ExclusiveGroup 的任务还必须在 [pool_template](pool_template) 和 [pool_quest](quest_template#examples-dealing-with-quests) 中有条目，以获取示例。

### BreadcrumbForQuestId

如果设置，表示此任务是引导至指定 ID 任务的面包屑任务。这两个任务会变得互斥：

- 如果目标任务已被接受、完成或获得奖励，此任务（面包屑任务）将变得不可用。
- 如果此任务正在进行中或已完成（但未获得奖励），目标任务将变得不可用——完成面包屑任务会解锁目标任务。

此单一字段替代了多条条件记录的需求。`0` 表示不存在面包屑关系。

### RewardMailTemplateID

如果任务从一组可能的物品中给出物品作为奖励，此处的 ID 对应 [quest_mail_loot_template](loot_template) 中的适当掉落模板。根据该掉落模板中的规则，被"拾取"的物品将在任务完成时通过邮件发送。

### RewardMailDelay

从掉落模板奖励物品的任务交还后，等待多少秒才将邮件发送给角色。

### RequiredSkillID

接受任务所需掌握的专业技能。请参阅 [SkillLine.dbc](skillline)
0 表示不需要任何专业技能。

### RequiredSkillPoints

接受任务所需的专业技能点数。

### RequiredMinRepFaction

声望要求对应的阵营 ID。请参阅 [Faction.dbc](faction)。

### RequiredMaxRepFaction

控制玩家拥有多少声望后仍能接到任务的最大声望值的阵营 ID。请参阅 [Faction.dbc](faction)。

### RequiredMinRepValue

玩家必须拥有此声望或更高的声望才能接到任务。

### RequiredMaxRepValue

玩家可以与某阵营拥有的最大声望值，超过此值仍可接到任务。如果玩家的声望高于此字段中的值，则无法再接取该任务。

### ProvidedItemCount

接受任务时给予玩家（放入玩家背包）的物品数量。

### SpecialFlags

此字段是位掩码，用于控制服务器端的任务功能。暴雪将这些数据保存在服务器端，不会发送给客户端，因此我们必须手动填充此字段。

| Flag                                      | Value | Description                                                                                                                                                                                                                              |
| ----------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| QUEST_SPECIAL_FLAGS_NONE                  | 0     | 无额外要求。                                                                                                                                                                                                                             |
| QUEST_SPECIAL_FLAGS_REPEATABLE            | 1     | 使任务可重复。                                                                                                                                                                                                                           |
| QUEST_SPECIAL_FLAGS_EXPLORATION_OR_EVENT  | 2     | 使任务只能通过某些外部事件完成（例如 [areatrigger_involvedrelation](areatrigger_involvedrelation) 中的条目、法术效果任务完成，或 [spell_scripts](scripts) 中命令 7 的条目）。                                                             |
| QUEST_SPECIAL_FLAGS_AUTO_ACCEPT           | 4     | 使任务自动接受。在 3.3.5a 补丁中，只有起始区域的任务需要此标志。                                                                                                                                                                        |
| QUEST_SPECIAL_FLAGS_DF_QUEST              | 8     | 仅用于地下城查找器任务。                                                                                                                                                                                                                 |
| QUEST_SPECIAL_FLAGS_MONTHLY               | 16    | 使任务每月可完成一次。                                                                                                                                                                                                                   |
| QUEST_SPECIAL_FLAGS_CAST                  | 32    | 任务需要 RequiredOrNpcGo 击杀荣誉（法术施放），但不需要实际的 NPC 击杀。此操作通常涉及击杀一个不可见的"兔子"NPC。                                                                                                                        |
| QUEST_SPECIAL_FLAGS_NO_REP_SPILLOVER      | 64    | 使任务不与其他结盟阵营共享奖励的声望。                                                                                                                                                                                                   |
| QUEST_SPECIAL_FLAGS_CAN_FAIL_IN_ANY_STATE | 128   | 允许任务在 Player::FailQuest() 中独立于其当前状态失败，例如与一开始就处于'已完成'状态的限时任务相关。                                                                                                                                   |
| QUEST_SPECIAL_FLAGS_NO_LOREMASTER_COUNT   | 256   | 此任务不应计入博学者成就。                                                                                                                                                                                                               |
