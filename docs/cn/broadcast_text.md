# broadcast\_text

**\`broadcast\_text\` 表**

该表（参考 <https://github.com/TrinityCore/TrinityCore/commit/60e87db>）将包含你的脚本文本所需的**一切**内容，例如：[gossip](gossip_menu_option)、[生物文本](creature_text) 和 [npc\_text](npc_text)。

其用途是作为一个全局化的表，用于存放上述提及的文本，以及这些文本的声音、表情和应使用的语言等信息。

**此表中的值来自 sniff（正式服数据），除非你完全确定它们之前被错误修改过，否则不应更改。**

**大多数情况下，这里的值是正确的，需要修复的是你的脚本。在建议修改此表之前，请确保你的脚本能正常工作。**

**表结构**

| Field                                    | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                                | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [LanguageID](#broadcast_text-Language)   | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [MaleText](#maletext)                    | text     | SIGNED     |     | YES  | NULL    |       |         |
| [FemaleText](#femaletext)                | text     | SIGNED     |     | YES  | NULL    |       |         |
| EmoteID1                                 | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteID2                                 | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteID3                                 | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteDelay1                              | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteDelay2                              | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteDelay3                              | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| SoundEntriesId                           | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EmotesID                                 | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| Flags                                    | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| VerifiedBuild                            | SMALLINT |            |     | YES  | 0       |       |         |

**字段说明**

### ID

文本的唯一 ID 值。

### LanguageID

文本广播时使用的语言。

ID 来自 Languages.dbc

### MaleText

男性生物将广播的文本，或男性角色可以从 gossip 菜单中阅读的文本。

### FemaleText

女性生物将广播的文本，或女性角色可以从 gossip 菜单中阅读的文本。

### EmoteID\[1-3\]

文本广播时播放的表情。

ID 来自 Emotes.dbc

### EmoteDelay\[1-3\]

广播表情的延迟。

### SoundId

文本广播时播放的声音。

ID 来自 SoundEntries.dbc

### EmotesID

一个表情。

### Flags

#### VerifiedBuild

此字段用于确定一个模板是否已通过 WDB 文件（对于此表为 ADB 文件）验证。

如果值为 0，则表示尚未解析。

如果值大于 0，则表示已使用该特定客户端 build 的 WDB 文件进行了解析。

如果值为 -1，则只是一个占位符，直到在 WDB 中找到正确的数据。

如果值为 -Client Build，则表示已使用该特定[客户端 build](http://archive.trinitycore.info/DB:Auth:realmlist#gamebuild "DB:Auth:realmlist") 的 WDB 文件进行了解析，并出于某些特殊需要稍后手动编辑。
