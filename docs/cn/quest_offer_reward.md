# quest\_offer\_reward

[<-返回至:World](database-world)

**`quest\_offer\_reward` 表**

该表用于提供奖励但不需要任何任务物品（不涉及物品交付）的任务。

**表结构**

| Field                           | Type      | Attributes | Key | NULL | Default | Comment                                             |
| ------------------------------- | --------- | ---------- | --- | ---- | ------- | --------------------------------------------------- |
| [ID](#id)                       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       | 唯一 ID ([quest\_template.ID](quest_template#id))   |
| [Emote1](#emote1)               | SMALLINT  | UNSIGNED   |     | NO   | 0       | 任务 NPC [表情](emotes)                             |
| [Emote2](#emote2)               | SMALLINT  | UNSIGNED   |     | NO   | 0       | 任务 NPC [表情](emotes)                             |
| [Emote3](#emote3)               | SMALLINT  | UNSIGNED   |     | NO   | 0       | 任务 NPC [表情](emotes)                             |
| [Emote4](#emote4)               | SMALLINT  | UNSIGNED   |     | NO   | 0       | 任务 NPC [表情](emotes)                             |
| [EmoteDelay1](#emotedelay1)     | INT       | UNSIGNED   |     | NO   | 0       | 表情延迟（毫秒）                                    |
| [EmoteDelay2](#emotedelay2)     | INT       | UNSIGNED   |     | NO   | 0       | 表情延迟（毫秒）                                    |
| [EmoteDelay3](#emotedelay3)     | INT       | UNSIGNED   |     | NO   | 0       | 表情延迟（毫秒）                                    |
| [EmoteDelay4](#emotedelay4)     | INT       | UNSIGNED   |     | NO   | 0       | 表情延迟（毫秒）                                    |
| [RewardText](#rewardtext)       | TEXT      |            |     | YES  | NULL    | 任务闲聊文本，单一任务对话                          |
| [VerifiedBuild](#verifiedbuild) | SMALLINT  |            |     | NO   | 0       | 游戏客户端构建号或手动设置的值                      |

**字段说明：**

### ID

唯一 ID ([quest\_template.ID](quest_template#id))

### Emote1

由 NPC 播放的 [Emotes.dbc](emotes) 表情

### Emote2

由 NPC 播放的 [Emotes.dbc](emotes) 表情

### Emote3

由 NPC 播放的 [Emotes.dbc](emotes) 表情

### Emote4

由 NPC 播放的 [Emotes.dbc](emotes) 表情

### EmoteDelay1

表情延迟（毫秒）

### EmoteDelay2

表情延迟（毫秒）

### EmoteDelay3

表情延迟（毫秒）

### EmoteDelay4

表情延迟（毫秒）

### RewardText

在交还不涉及物品交付的任务时显示的任务闲聊文本。

某些任务只是领取奖励，而无需接受一个新的初始任务。

此类任务可以是职业专属、可重复的，或者在物品丢失时用于取回任务物品。

### VerifiedBuild

该字段由 TrinityCore 数据库团队使用，用于确定模板是否已根据 WDB 文件进行验证。

-   如果值为 0，则尚未解析。
-   如果值 &gt; 0，则表示已使用该特定[客户端构建](realmlist#gamebuild)的 WDB 文件进行解析。
-   如果值为 -1，则在 WDB 中找到合适的数据之前，它只是一个占位符。
-   如果值为 -[客户端构建](realmlist#gamebuild)，则表示已使用该特定[客户端构建](realmlist#gamebuild)的 WDB 文件进行解析，随后因某些特定需求进行了手动编辑。
