# npc_text

[<-返回:World](database-world)

**表结构**

此表包含用于闲聊（gossip）的文本。关于此表还需要进行更多的研究。

| Field         | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| ID               | INT       | UNSIGNED | PRI | NO  | 0       |     |         |
| text0_0          | longtext  |          |     | YES |         |     |         |
| text0_1          | longtext  |          |     | YES |         |     |         |
| BroadcastTextID0 | INT       |          |     | NO  | 0       |     |         |
| lang0            | TINYINT   | UNSIGNED |     | NO  | 0       |     |         |
| Probability0     | FLOAT     |          |     | NO  | 0       |     |         |
| em0_0            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em0_1            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em0_2            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em0_3            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em0_4            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em0_5            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| text1_0          | longtext  |          |     | YES |         |     |         |
| text1_1          | longtext  |          |     | YES |         |     |         |
| BroadcastTextID1 | INT       |          |     | NO  | 0       |     |         |
| lang1            | TINYINT   | UNSIGNED |     | NO  | 0       |     |         |
| Probability1     | FLOAT     |          |     | NO  | 0       |     |         |
| em1_0            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em1_1            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em1_2            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em1_3            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em1_4            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em1_5            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| text2_0          | longtext  |          |     | YES |         |     |         |
| text2_1          | longtext  |          |     | YES |         |     |         |
| BroadcastTextID2 | INT       |          |     | NO  | 0       |     |         |
| lang2            | TINYINT   | UNSIGNED |     | NO  | 0       |     |         |
| Probability2     | FLOAT     |          |     | NO  | 0       |     |         |
| em2_0            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em2_1            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em2_2            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em2_3            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em2_4            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em2_5            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| text3_0          | longtext  |          |     | YES |         |     |         |
| text3_1          | longtext  |          |     | YES |         |     |         |
| BroadcastTextID3 | INT       |          |     | NO  | 0       |     |         |
| lang3            | TINYINT   | UNSIGNED |     | NO  | 0       |     |         |
| Probability3     | FLOAT     |          |     | NO  | 0       |     |         |
| em3_0            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em3_1            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em3_2            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em3_3            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em3_4            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em3_5            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| text4_0          | longtext  |          |     | YES |         |     |         |
| text4_1          | longtext  |          |     | YES |         |     |         |
| BroadcastTextID4 | INT       |          |     | NO  | 0       |     |         |
| lang4            | TINYINT   | UNSIGNED |     | NO  | 0       |     |         |
| Probability4     | FLOAT     |          |     | NO  | 0       |     |         |
| em4_0            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em4_1            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em4_2            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em4_3            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em4_4            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em4_5            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| text5_0          | longtext  |          |     | YES |         |     |         |
| text5_1          | longtext  |          |     | YES |         |     |         |
| BroadcastTextID5 | INT       |          |     | NO  | 0       |     |         |
| lang5            | TINYINT   | UNSIGNED |     | NO  | 0       |     |         |
| Probability5     | FLOAT     |          |     | NO  | 0       |     |         |
| em5_0            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em5_1            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em5_2            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em5_3            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em5_4            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em5_5            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| text6_0          | longtext  |          |     | YES |         |     |         |
| text6_1          | longtext  |          |     | YES |         |     |         |
| BroadcastTextID6 | INT       |          |     | NO  | 0       |     |         |
| lang6            | TINYINT   | UNSIGNED |     | NO  | 0       |     |         |
| Probability6     | FLOAT     |          |     | NO  | 0       |     |         |
| em6_0            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em6_1            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em6_2            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em6_3            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em6_4            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em6_5            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| text7_0          | longtext  |          |     | YES |         |     |         |
| text7_1          | longtext  |          |     | YES |         |     |         |
| BroadcastTextID7 | INT       |          |     | NO  | 0       |     |         |
| lang7            | TINYINT   | UNSIGNED |     | NO  | 0       |     |         |
| Probability7     | FLOAT     |          |     | NO  | 0       |     |         |
| em7_0            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em7_1            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em7_2            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em7_3            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em7_4            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| em7_5            | SMALLINT  | UNSIGNED |     | NO  | 0       |     |         |
| VerifiedBuild    | INT       |          |     | YES | NULL    |     |         |

**字段说明**

### ID

这是文本条目的 ID。

### text0_0 至 text7_0

当 NPC 为男性时显示的本地化文本。

### text0_1 至 text7_1

当 NPC 为女性时显示的本地化文本。

### BroadcastTextID0 至 BroadcastTextID7

\`broadcast\_text\` 表中 \`MaleText\` 对应的 \`broadcast\_text\`.\`ID\` 字段值。

### lang0 至 lang7

游戏中文本的语言。可用的语言 ID 请参考[此页面](languages)。
如果设置为 0，则表示不需要掌握任何特定语言。

### Probability0 至 Probability7

NPC 根据自身性别选择说出 text0\_0 或 text0\_1 的几率。

### em0_0-5 至 em7_0-5

NPC 在显示文本时应执行的表情（emote）的 ID。表情按顺序依次播放。要查看表情列表，请参阅 Emotes.DBC

### VerifiedBuild

此字段用于判断某个模板是否已根据 WDB 文件验证过。

如果值为 0，则表示尚未解析。

如果值大于 0，则表示已使用来自该特定客户端版本的 WDB 文件进行过解析。

如果值为 -1，则只是在 WDB 中找到正确数据之前的占位符。
