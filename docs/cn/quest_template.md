# quest\_template

[<-返回至:World](database-world)

**表：quest\_template**

包含所有可用任务的基本定义。

## **表结构**

| Field                           | Type      | Attribute | Key | Null | Default | Extra | Comment |
| ------------------------------- | --------- | --------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]                         | MEDIUMINT | UNSIGNED  | PRI | NO   | 0       |       |         |
| [QuestType][2]                  | TINYINT   | UNSIGNED  |     | NO   | 2       |       |         |
| [QuestLevel][3]                 | SMALLINT  |           |     | NO   | 1       |       |         |
| [MinLevel][4]                   | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [QuestSortID][5]                | SMALLINT  |           |     | NO   | 0       |       |         |
| [QuestInfoID][6]                | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [SuggestedGroupNum][7]          | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredFactionId1][8]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredFactionId2][9]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredFactionValue1][10]     | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredFactionValue2][11]     | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardNextQuest][12]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardXPDifficulty][13]        | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardMoney][14]               | INT       |           |     | NO   | 0       |       |         |
| [RewardMoneyDifficulty][15]     | INT       | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardDisplaySpell][16]        | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardSpell][17]               | INT       |           |     | NO   | 0       |       |         |
| [RewardHonor][18]               | INT       |           |     | NO   | 0       |       |         |
| [RewardKillHonor][19]           | FLOAT     |           |     | NO   | 0       |       |         |
| [StartItem][20]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [Flags][21]                     | INT       | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredPlayerKills][22]       | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardItem1][23]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardAmount1][24]             | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardItem2][25]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardAmount2][26]             | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardItem3][27]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardAmount3][28]             | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardItem4][29]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardAmount4][30]             | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDrop1][31]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDropQuantity1][32]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDrop2][33]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDropQuantity2][34]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDrop3][35]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDropQuantity3][36]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDrop4][37]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDropQuantity4][38]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID1][39]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity1][40] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID2][41]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity2][42] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID3][43]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity3][44] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID4][45]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity4][46] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID5][47]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity5][48] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID6][49]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity6][50] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [POIContinent][51]              | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [POIx][52]                      | FLOAT     |           |     | NO   | 0       |       |         |
| [POIy][53]                      | FLOAT     |           |     | NO   | 0       |       |         |
| [POIPriority][54]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardTitle][55]               | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardTalents][56]             | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardArenaPoints][57]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionID1][58]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue1][59]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride1][60]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionID2][61]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue2][62]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride2][63]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionID3][64]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue3][65]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride3][66]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionID4][67]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue4][68]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride4][69]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionID5][70]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue5][71]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride5][72]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [TimeAllowed][73]               | INT       | UNSIGNED  |     | NO   | 0       |       |         |
| [AllowableRaces][74]            | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [LogTitle][75]                  | TEXT      |           |     | YES  |         |       |         |
| [LogDescription][76]            | TEXT      |           |     | YES  |         |       |         |
| [QuestDescription][77]          | TEXT      |           |     | YES  |         |       |         |
| [AreaDescription][78]           | TEXT      |           |     | YES  |         |       |         |
| [QuestCompletionLog][79]        | TEXT      |           |     | YES  |         |       |         |
| [RequiredNpcOrGo1][80]          | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo2][81]          | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo3][82]          | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo4][83]          | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount1][84]     | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount2][85]     | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount3][86]     | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount4][87]     | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId1][88]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId2][89]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId3][90]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId4][91]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId5][92]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId6][93]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount1][94]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount2][95]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount3][96]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount4][97]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount5][98]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount6][99]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [Unknown0][100]                 | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [ObjectiveText1][101]           | TEXT      |           |     | YES  |         |       |         |
| [ObjectiveText2][102]           | TEXT      |           |     | YES  |         |       |         |
| [ObjectiveText3][103]           | TEXT      |           |     | YES  |         |       |         |
| [ObjectiveText4][104]           | TEXT      |           |     | YES  |         |       |         |
| [VerifiedBuild][105]            | SMALLINT  |           |     | YES  | 0       |       |         |

[1]: #id
[2]: #questtype
[3]: #questlevel
[4]: #minlevel
[5]: #questsortid
[6]: #questinfoid
[7]: #suggestedgroupnum
[8]: #requiredfactionid1
[9]: #requiredfactionid2
[10]: #requiredfactionvalue1
[11]: #requiredfactionvalue2
[12]: #rewardnextquest
[13]: #rewardxpdifficulty
[14]: #rewardmoney
[15]: #rewardmoneydifficulty
[16]: #rewarddisplayspell
[17]: #rewardspell
[18]: #rewardhonor
[19]: #rewardkillhonor
[20]: #startitem
[21]: #flags
[22]: #requiredplayerkills
[23]: #rewarditem1
[24]: #rewardamount1
[25]: #rewarditem2
[26]: #rewardamount2
[27]: #rewarditem3
[28]: #rewardamount3
[29]: #rewarditem4
[30]: #rewardamount4
[31]: #itemdrop1
[32]: #itemdropquantity1
[33]: #itemdrop2
[34]: #itemdropquantity2
[35]: #itemdrop3
[36]: #itemdropquantity3
[37]: #itemdrop4
[38]: #itemdropquantity4
[39]: #rewardchoiceitemid1
[40]: #rewardchoiceitemquantity1
[41]: #rewardchoiceitemid2
[42]: #rewardchoiceitemquantity2
[43]: #rewardchoiceitemid3
[44]: #rewardchoiceitemquantity3
[45]: #rewardchoiceitemid4
[46]: #rewardchoiceitemquantity4
[47]: #rewardchoiceitemid5
[48]: #rewardchoiceitemquantity5
[49]: #rewardchoiceitemid6
[50]: #rewardchoiceitemquantity6
[51]: #poicontinent
[52]: #poix
[53]: #poiy
[54]: #poipriority
[55]: #rewardtitle
[56]: #rewardtalents
[57]: #rewardarenapoints
[58]: #rewardfactionid1
[59]: #rewardfactionvalue1
[60]: #rewardfactionoverride1
[61]: #rewardfactionid2
[62]: #rewardfactionvalue2
[63]: #rewardfactionoverride2
[64]: #rewardfactionid3
[65]: #rewardfactionvalue3
[66]: #rewardfactionoverride3
[67]: #rewardfactionid4
[68]: #rewardfactionvalue4
[69]: #rewardfactionoverride4
[70]: #rewardfactionid5
[71]: #rewardfactionvalue5
[72]: #rewardfactionoverride5
[73]: #timeallowed
[74]: #allowableraces
[75]: #logtitle
[76]: #logdescription
[77]: #questdescription
[78]: #areadescription
[79]: #questcompletionlog
[80]: #requirednpcorgo1
[81]: #requirednpcorgo2
[82]: #requirednpcorgo3
[83]: #requirednpcorgo4
[84]: #requirednpcorgocount1
[85]: #requirednpcorgocount2
[86]: #requirednpcorgocount3
[87]: #requirednpcorgocount4
[88]: #requireditemid1
[89]: #requireditemid2
[90]: #requireditemid3
[91]: #requireditemid4
[92]: #requireditemid5
[93]: #requireditemid6
[94]: #requireditemcount1
[95]: #requireditemcount2
[96]: #requireditemcount3
[97]: #requireditemcount4
[98]: #requireditemcount5
[99]: #requireditemcount6
[100]: #unknown0
[101]: #objectivetext1
[102]: #objectivetext2
[103]: #objectivetext3
[104]: #objectivetext4
[105]: #verifiedbuild


**字段说明**

### ID

任务 ID。此列是表的主键。每个任务 ID 必须是唯一的！

### QuestType

可接受的值：0、1 或 2。其含义如下表所示。

| Value | Result                                                                                                   |
| ----- | -------------------------------------------------------------------------------------------------------- |
| 0     | 任务已启用，但在接受时自动完成；这会跳过任务目标和任务细节。                                             |
| 1     | 任务已禁用（尚未在核心中实现）。                                                                         |
| 2     | 任务已启用（不会自动完成）。                                                                             |

### QuestLevel

任务等级。只有当玩家的等级小于或等于 等级+5 时，玩家才会获得全部经验值。如果等级设为 -1，则使用玩家等级作为（任务）等级来计算经验值。

### MinLevel

玩家可以接到该任务的最低等级。

### QuestSortID

该字段定义任务在任务日志中归入哪个类别。

如果 **值 &gt; 0**，则该值是取自 AreaTable.dbc 的区域 ID。

如果 **值 &lt; 0**，则 (**-值**) 是任务排序 ID：（通常用于专业或职业任务。另请参阅 [RequiredSkillPoints](#quest_template-RequiredSkillPoints)）。该值是取自 QuestSort.dbc 的 ID。

### QuestInfoID

这些值是取自 [QuestInfo.dbc](https://wowdev.wiki/DB/QuestInfo) 的 ID。

| Value | Result       |
| ----- | ------------ |
| 0     | 无           |
| 1     | 组队         |
| 21    | 生活         |
| 41    | PvP          |
| 62    | 团队         |
| 81    | 地下城       |
| 82    | 事件         |
| 83    | 传说         |
| 84    | 护送         |
| 85    | 英雄         |
| 88    | 团队 (10)    |
| 89    | 团队 (25)    |

### SuggestedGroupNum

建议一起完成该任务的玩家人数。

### RewardFactionId1

任务为其增加声望值的阵营 ID（来自 Faction.dbc）。
任务完成时为阵营增加或减少的声望点数。这是一种特殊的声望奖励。任务奖励生物阵营的正常声望奖励会被自动计算并添加。

### RewardFactionId2

任务为其增加声望值的阵营 ID（来自 Faction.dbc）。
任务完成时为阵营增加或减少的声望点数。这是一种特殊的声望奖励。任务奖励生物阵营的正常声望奖励会被自动计算并添加。

### RewardFactionValueId1

如果 quest_template#RewardFactionValueId 为 0，则此字段用于在 QuestFactionReward.dbc 中进行声望查找。此字段中的值 X 表示 QuestFactionReward.dbc 的 RepX 列。如果 RewardRepValueId 为正，则使用 QuestFactionReward.dbc 第一行的声望值，为负则使用第二行。

### RewardFactionValueId2
如果 quest_template#RewardFactionValueId 为 0，则此字段用于在 QuestFactionReward.dbc 中进行声望查找。此字段中的值 X 表示 QuestFactionReward.dbc 的 RepX 列。如果 RewardRepValueId 为正，则使用 QuestFactionReward.dbc 第一行的声望值，为负则使用第二行。

### RewardNextQuest

**RewardNextQuest（旧字段名：NextQuestIdChain）**

来自**生物**或**游戏对象**的任务条目，用于结束一个任务并开始一个新任务。结果是，当你结束这个任务后，新任务会立即出现在任务给予者处。

示例请参阅[示例部分](#quest_template-Examples)。

### RewardXPDifficulty

根据[等级](#quest_template-Level)，从 QuestXP.dbc 中取出索引为 *RewardXPDifficulty* 的基础经验值。

此字段还通过以下公式根据该字段的值控制所给的经验值。如果任务可重复，经验值只会给予一次。角色获得的总经验值还会受到角色等级与任务等级之间等级差的影响。

根据该字段的值计算经验值的公式：
- **QuestLevel &gt;= 65:** XP = RewMoneyMaxLevel / 6.0
- **QuestLevel 64:** XP = RewMoneyMaxLevel / 4.8
- **QuestLevel 63:** XP = RewMoneyMaxLevel / 3.6
- **QuestLevel 62:** XP = RewMoneyMaxLevel / 2.4
- **QuestLevel 61:** XP = RewMoneyMaxLevel / 1.2
- **QuestLevel &lt;= 60:** XP = RewMoneyMaxLevel / 0.6

### RewardMoney

完成任务所获得的金钱（如果值 &gt; 0）或完成任务所需的金钱（如果值 &lt; 0）。

### RewardMoneyDifficulty

该 ID 指向 [MoneyFactor](quest_money_reward) 中按等级排列的其中一个金钱系数。

### RewardDisplaySpell

任务完成时显示在任务日志中要被施放的法术。请注意，如果 [RewardSpell](#rewardspell) 非零，此法术将不会被施放。此时会施放另一个字段中的法术，而此处的法术仅作为任务日志中的视觉展示。

### RewardSpell

任务完成时显示在任务日志中要被施放的法术。请注意，如果 [RewardSpell](quest_template#rewardspell) 非零，此法术将不会被施放。此时会施放另一个字段中的法术，而此处的法术仅作为任务日志中的视觉展示。

注意：此字段直接来自 WDB，不应更改。

### RewardHonor

完成此任务所奖励的荣誉击杀荣誉点数。

示例：任务 8388 的示例值为 15：在 80 级时，一次荣誉击杀价值 124 点荣誉。乘以 15 后得到 1860，相乘后取整。因此该任务在 80 级奖励的荣誉为 1860。

### RewardKillHonor


### StartItem

任务开始时由任务给予者给予的物品。任务被放弃时这些物品会被删除。

### Flags

此标志字段更具体地定义了任务的类型。除了日常标志和可共享标志外，此字段仅用于分组目的，不用于任何其他任务要求。任务要求是根据其他任务模板字段中的非零值计算得出的。此外，虽然其中一些标志是已知的，但另一些标志的用途尚不明确，下面的注释只是对它们的猜测。

| Flag       | Name                                 | Comments                                                                                                                                                               |
| ---------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0          | QUEST_FLAGS_NONE                     | 无标志，因此此任务没有分配任何分组。                                                                                                                                   |
| 1          | QUEST_FLAGS_STAY_ALIVE               | 如果玩家死亡，任务失败。                                                                                                                                               |
| 2          | QUEST_FLAGS_PARTY_ACCEPT             | 护送任务或任何其他事件驱动的任务。如果玩家在队伍中，所有可以接受此任务的玩家都会收到接受任务的确认框。                                                                 |
| 4          | QUEST_FLAGS_EXPLORATION              | 涉及区域触发器的激活。                                                                                                                                                 |
| 8          | QUEST_FLAGS_SHARABLE                 | 允许该任务与其他玩家共享。                                                                                                                                             |
| 16         | QUEST_FLAGS_HAS_CONDITION            | 目前未使用                                                                                                                                                             |
| 32         | QUEST_FLAGS_HIDE_REWARD_POI          | 目前未使用：内容不确定                                                                                                                                                 |
| 64         | QUEST_FLAGS_RAID                     | 可以在团队中完成                                                                                                                                                       |
| 128        | QUEST_FLAGS_TBC                      | 目前未使用：仅在启用 TBC 扩展时可用                                                                                                                                    |
| 256        | QUEST_FLAGS_NO_MONEY_FROM_XP         | 目前未使用：在最高等级时经验不会转换为金币                                                                                                                             |
| 512        | QUEST_FLAGS_HIDDEN_REWARDS           | 物品和金钱奖励在初始任务详情页和任务日志中隐藏，但在准备好获得奖励时会出现。                                                                                           |
| 1024       | QUEST_FLAGS_TRACKING                 | 这些任务在完成时自动获得奖励，并且永远不会出现在客户端任务日志中。                                                                                                     |
| 2048       | QUEST_FLAGS_DEPRECATE_REPUTATION     | 目前未使用                                                                                                                                                             |
| 4096       | QUEST_FLAGS_DAILY                    | 日常可重复任务（唯一一个核心对其应用特定行为的标志）                                                                                                                   |
| 8192       | QUEST_FLAGS_FLAGS_PVP                | 任务日志中包含此任务会强制启用 PvP 标志                                                                                                                               |
| 16384      | QUEST_FLAGS_UNAVAILABLE              | 用于并非普遍可用的任务                                                                                                                                                 |
| 32768      | QUEST_FLAGS_WEEKLY                   | 周常可重复任务（唯一一个核心对其应用特定行为的标志）                                                                                                                   |
| 65536      | QUEST_FLAGS_AUTOCOMPLETE             | 自动完成                                                                                                                                                               |
| 131072     | QUEST_FLAGS_DISPLAY_ITEM_IN_TRACKER  | 在任务追踪器中显示可用物品                                                                                                                                             |
| 262144     | QUEST_FLAGS_OBJ_TEXT                 | 使用目标文本作为完成文本                                                                                                                                               |
| 524288     | QUEST_FLAGS_AUTO_ACCEPT              | 客户端将此标志识别为自动接受。然而，当前（3.3.5a）的任务都没有此标志。也许暴雪以前使用过，或者将来会使用。                                                             |
| 1048576    | QUEST_FLAGS_PLAYER_CAST_ON_ACCEPT    | 带有此标志的任务由玩家通过玩家 GUI 中的特殊按钮自动提交                                                                                                                |
| 2097152    | QUEST_FLAGS_PLAYER_CAST_ON_COMPLETE  | 自动提示接受任务。不是来自 NPC。                                                                                                                                       |
| 4194304    | QUEST_FLAGS_UPDATE_PHASE_SHIFT       |                                                                                                                                                                        |
| 8388608    | QUEST_FLAGS_SOR_WHITELIST            |                                                                                                                                                                        |
| 16777216   | QUEST_FLAGS_LAUNCH_GOSSIP_COMPLETE   |                                                                                                                                                                        |
| 54432      | QUEST_FLAGS_REMOVE_EXTRA_GET_ITEMS   |                                                                                                                                                                        |
| 67108864   | QUEST_FLAGS_HIDE_UNTIL_DISCOVERED    |                                                                                                                                                                        |
| 134217728  | QUEST_FLAGS_PORTRAIT_IN_QUEST_LOG    |                                                                                                                                                                        |
| 268435456  | QUEST_FLAGS_SHOW_ITEM_WHEN_COMPLETED |                                                                                                                                                                        |
| 536870912  | QUEST_FLAGS_LAUNCH_GOSSIP_ACCEPT     |                                                                                                                                                                        |
| 1073741824 | QUEST_FLAGS_ITEMS_GLOW_WHEN_DONE     |                                                                                                                                                                        |
| 2147483648 | QUEST_FLAGS_FAIL_ON_LOGOUT           |                                                                                                                                                                        |

与所有基于标志的字段一样，**QuestFlags** 可以为不同类型的任务进行叠加。

请注意，某些标志可能不受核心支持。

### RequiredPlayerKills

显示完成该任务之前你需要击杀多少玩家。betd class=td class=a class=/td data-linked-resource-default-alias=fore

### RewardItem1

作为奖励给出的[物品 ID 1](item_template#entry)（不可选择）。

### RewardAmount1

从上述物品中获得的物品数量

### RewardItem2

作为奖励给出的[物品 ID 2](item_template#entry)（不可选择）。

### RewardAmount2

从上述物品中获得的物品数量

### RewardItem3

作为奖励给出的[物品 ID 3](item_template#entry)（不可选择）。

### RewardAmount3

从上述物品中获得的物品数量

### RewardItem4

作为奖励给出的[物品 ID 4](item_template#entry)（不可选择）。

### RewardAmount4

从上述物品中获得的物品数量

### ItemDrop1



### ItemDropQuantity1



### ItemDrop2



### ItemDropQuantity2



### ItemDrop3



### ItemDropQuantity3



### ItemDrop4



### ItemDropQuantity4



### RewardChoiceItemID1



### RewardChoiceItemQuantity1


### RewardChoiceItemID2


### RewardChoiceItemQuantity2


### RewardChoiceItemID3


### RewardChoiceItemQuantity3


### RewardChoiceItemID4


### RewardChoiceItemQuantity4


### RewardChoiceItemID5


### RewardChoiceItemQuantity5


### RewardChoiceItemID6


### RewardChoiceItemQuantity6


### POIContinent

任务兴趣点（POI）的 MapId。任务激活时，POI 会显示在地图上。

### POIx

任务 POI 的 X 坐标。

### POIy

任务 POI 的 Y 坐标。

### POIPriority

TODO

### RewardTitle


### RewardTalents


### RewardArenaPoints


### RewardFactionID1


### RewardFactionValue1


### RewardFactionOverride1


### RewardFactionID2


### RewardFactionValue2


### ItemDrop


### RewardFactionOverride2


### RewardFactionID3


### ItemDropQuantity

ItemDrop 中可以拾取（并由核心掉落）的物品的最大副本数量。

### RewardFactionValue3


### RewardFactionOverride3


### RewardFactionID4


### RewardFactionValue4


### RewardFactionOverride4


### RewardFactionID5


### RewardFactionValue5


### RewardFactionOverride5


### TimeAllowed


### AllowableRaces


### LogTitle

任务的标题。

### LogDescription

任务的目标。如果为空，则任务为自动完成任务，无需先接受即可立即完成。

### QuestDescription

任务文本。你可以使用某些在游戏中会填充的占位符：$B - 换行，$N - 名字，$R - 种族，$C - 职业，$G男性:女性;（男性和女性可以替换为你想要的任何同义词，但顺序必须保持不变。例如：boy:girl / man:woman / sir:madam / dude:chick）

### AreaDescription


### QuestCompletionLog

当玩家试图与任务已激活但尚未完成的 NPC 交谈时发送给玩家的文本。（Wowhead 中"Progress"标题下的文本。）你可以使用某些在游戏中会填充的占位符：$B - 换行，$N - 名字，$R - 种族，$C - 职业，$G男性:女性;（男性和女性可以替换为你想要的任何同义词，但顺序必须保持不变。例如：boy:girl / man:woman / sir:madam / dude:chick）

### RequiredNpcOrGo1
### RequiredNpcOrGo2
### RequiredNpcOrGo3
### RequiredNpcOrGo4

- 值 &gt; 0：玩家需要击杀/施放法术才能完成任务所需的 creature\_template ID。
- 值 &lt; 0：玩家需要施放法术才能完成任务所需的 gameobject\_template ID。
- 如果 \*RequiredSpellCast\* != 0，则目标是对目标施放法术，否则是击杀。

注意：如果 RequiredSpellCast != 0 且该法术具有发送事件或任务完成效果，则此字段可以留空。

### RequiredNpcOrGoCount1
### RequiredNpcOrGoCount2
### RequiredNpcOrGoCount3
### RequiredNpcOrGoCount4

生物或游戏对象必须被击杀或对其施放法术的次数。

### RequiredItemId1
### RequiredItemId2
### RequiredItemId3
### RequiredItemId4
### RequiredItemId5
### RequiredItemId6

完成任务所需物品的 [ID](item_template#entry)。

### RequiredItemCount1
### RequiredItemCount2
### RequiredItemCount3
### RequiredItemCount4
### RequiredItemCount5
### RequiredItemCount6

所需物品的数量

### Unknown0


### ObjectiveText1
### ObjectiveText2
### ObjectiveText3
### ObjectiveText4

用于定义非标准的目标文本，这些文本会显示在任务日志中。例如，"治疗倒下的战士"，数字由计数（Count）值添加。

### VerifiedBuild
