# chat\_filter

[<-返回:角色库](database-characters)

**`chat_filter` 表**

该表存储核心聊天过滤器使用的保留词。当找到匹配的条目时，会通过不区分大小写的子串匹配来屏蔽该消息。

该过滤器由 `worldserver.conf` 中的 `ChatFilter.Whisper`、`ChatFilter.Say`、`ChatFilter.Yell` 和 `ChatFilter.Emote` 设置控制。可以在游戏内使用 `.chatfilter list`、`.chatfilter add`、`.chatfilter remove` 和 `.reload chat_filter` 命令管理条目。

**表结构**

| 字段 | 类型         | 属性 | 键 | 空 | 默认值 | 额外          | 备注 |
| --------- | ------------ | ---------- | --- | ---- | ------- | -------------- | ------- |
| [ID](#id) | INT          | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [Word](#word) | VARCHAR(255) | SIGNED     |     | NO   |         |                |         |

**字段说明**

### ID

唯一的行标识符。

### Word

聊天过滤器检查的保留词或短语。
