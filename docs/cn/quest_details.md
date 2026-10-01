# quest\_details

[<-返回至:World](database-world)

**\`quest_details\` 表**

此表处理带表情延迟的任务 NPC 表情。

**表结构**

| Field                           | Type      | Attributes | Key | NULL | Default | Comment                                             |
| ------------------------------- | --------- | ---------- | --- | ---- | ------- | --------------------------------------------------- |
| [ID](#id)                       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       | Unique ID ([quest\_template.ID](quest_template#id)) |
| [Emote1](#emote1)               | SMALLINT  | UNSIGNED   |     | NO   | 0       | Quest NPC [Emote](emotes)                           |
| [Emote2](#emote2)               | SMALLINT  | UNSIGNED   |     | NO   | 0       | Quest NPC [Emote](emotes)                           |
| [Emote3](#emote3)               | SMALLINT  | UNSIGNED   |     | NO   | 0       | Quest NPC [Emote](emotes)                           |
| [Emote4](#emote4)               | SMALLINT  | UNSIGNED   |     | NO   | 0       | Quest NPC [Emote](emotes)                           |
| [EmoteDelay1](#emotedelay1)     | INT       | UNSIGNED   |     | NO   | 0       | Emote delay in milliseconds                         |
| [EmoteDelay2](#emotedelay2)     | INT       | UNSIGNED   |     | NO   | 0       | Emote delay in milliseconds                         |
| [EmoteDelay3](#emotedelay3)     | INT       | UNSIGNED   |     | NO   | 0       | Emote delay in milliseconds                         |
| [EmoteDelay4](#emotedelay4)     | INT       | UNSIGNED   |     | NO   | 0       | Emote delay in milliseconds                         |
| [VerifiedBuild](#verifiedbuild) | SMALLINT  |            |     | NO   | 0       | Game client Build number or manually set value      |

**字段说明**

### ID

唯一 ID（[quest\_template.ID](quest_template#id)）

### Emote1

NPC 播放的表情（来自 [Emotes.dbc](emotes)）

### Emote2

NPC 播放的表情（来自 [Emotes.dbc](emotes)）

### Emote3

NPC 播放的表情（来自 [Emotes.dbc](emotes)）

### Emote4

NPC 播放的表情（来自 [Emotes.dbc](emotes)）

### EmoteDelay1

以毫秒为单位的表情延迟

### EmoteDelay2

以毫秒为单位的表情延迟

### EmoteDelay3

以毫秒为单位的表情延迟

### EmoteDelay4

以毫秒为单位的表情延迟

### VerifiedBuild

此字段由 TrinityCore 数据库团队用于确定一个模板是否已通过 WDB 文件验证。

-   如果值为 0，则表示尚未解析。
-   如果值大于 0，则表示已使用该特定[客户端 Build](realmlist#gamebuild) 的 WDB 文件进行了解析。
-   如果值为 -1，则只是一个占位符，直到在 WDB 中找到正确的数据。
-   如果值为 -[客户端 Build](realmlist#gamebuild)，则表示已使用该特定[客户端 build](realmlist#gamebuild) 的 WDB 文件进行了解析，并出于某些特定需要稍后进行了手动编辑。
