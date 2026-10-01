# quest\_request\_items

[<-返回至:World](database-world)

**`quest\_request\_items` 表**

该表主要处理 3 个任务细节：

1.  任务完成时 NPC 的表情
2.  任务未完成时 NPC 的表情
3.  需要任务物品的任务的完成文本

**表结构**

| Field                                   | Type      | Attributes | Key | NULL | Default | Comment |
| --------------------------------------- | --------- | ---------- | --- | ---- | ------- | ------- |
| [ID](#id)                               | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |         |
| [EmoteOnComplete](#emoteoncomplete)     | SMALLINT  | UNSIGNED   |     | NO   | 0       |         |
| [EmoteOnIncomplete](#emoteonincomplete) | SMALLINT  | UNSIGNED   |     | NO   | 0       |         |
| [CompletionText](#completiontext)       | text      |            |     | YES  | NULL    |         |
| [VerifiedBuild](#verifiedbuild)         | SMALLINT  |            |     | NO   | 0       |         |

**字段说明**

### ID

在交还物品交付任务时显示完成文本的任务的任务 ID。
本表的主键。每个任务 ID 必须是唯一的。

### EmoteOnComplete

当所有任务目标都完成时，由任务终结 NPC 播放的 [Emotes.dbc](emotes) 表情。

### EmoteOnIncomplete

如果任何任务目标未完成，则由任务终结 NPC 播放的 [Emotes.dbc](https://trinitycore.atlassian.net/wiki/display/tc/Emotes) 表情。

### CompletionText

在交还物品交付任务时，最终闲聊对话窗口中显示的任务闲聊文本。
任务所涉及的任务物品可以由任务给予者提供，也可以由玩家收集。

### VerifiedBuild

该字段由 TrinityCore 数据库团队使用，用于确定模板是否已根据 WDB 文件进行验证。

-   如果值为 0，则尚未解析。
-   如果值 &gt; 0，则表示已使用该特定[客户端构建](https://trinitycore.atlassian.net/wiki/display/tc/realmlist#realmlist-gamebuild)的 WDB 文件进行解析。
-   如果值为 -1，则在 WDB 中找到合适的数据之前，它只是一个占位符。
-   如果值为 -[客户端构建](https://trinitycore.atlassian.net/wiki/display/tc/realmlist#realmlist-gamebuild)，则表示已使用该特定[客户端构建](https://trinitycore.atlassian.net/wiki/display/tc/realmlist#realmlist-gamebuild)的 WDB 文件进行解析，随后因某些特定需求进行了手动编辑。
