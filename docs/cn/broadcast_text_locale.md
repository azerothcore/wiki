# broadcast\_text\_locale

**\`broadcast\_text\_locale\` 表**

该表将包含 \`broadcast\_text\` 表的**本地化文本**。用于 [gossip](gossip_menu_option)、[生物文本](creature_text) 和 [npc\_text](npc_text) 中。

其用途是作为一个全局化的表，用于存放上述提及的本地化文本。

**表结构**

| Field                     | Type       | Key | Null | Default | Extra | Comment |
| ------------------------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#ID)                 | MEDIUMINT  | PRI | NO   | 0       |       |         |
| [locale](#locale)         | VARCHAR(4) | PRI | NO   | NULL    |       |         |
| [MaleText](#MaleText)     | text       |     | YES  | NULL    |       |         |
| [FemaleText](#FemaleText) | text       |     | YES  | NULL    |       |         |
| VerifiedBuild             | SMALLINT   |     | YES  | 0       |       |         |

**字段说明**

### ID

文本的唯一 ID 值，指向 broadcast_text 表中文本的 ID。

### locale

文本广播时使用的语言。
可以有 8 个值：deDE、esES、esMX、frFR、koKR、ruRU、zhCN、zhTW

### MaleText

男性生物将广播的本地化文本，或男性玩家可以从 gossip 菜单中阅读的文本。

### FemaleText

女性生物将广播的本地化文本，或女性玩家可以从 gossip 菜单中阅读的文本。

#### WDBVerified

此字段由 AzerothCore 团队使用，用于确定一个模板是否已通过 WDB 文件（对于此表为 ADB 文件）验证。

如果值为 0，则表示尚未解析。

如果值大于 0，则表示已使用该特定客户端 build 的 WDB 文件进行了解析。

如果值为 -1，则只是一个占位符，直到在 WDB 中找到正确的数据。

如果值为 -Client Build，则表示已使用该特定[客户端 build](realmlist#gamebuild "DB:Auth:realmlist") 的 WDB 文件进行了解析，并出于某些特殊需要稍后手动编辑。
