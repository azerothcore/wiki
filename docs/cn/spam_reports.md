# spam\_reports

[<-返回至:Characters](database-characters)

**`spam_reports` 表**

此表存储玩家在游戏中提交的垃圾信息举报（例如举报聊天、邮件或日历中的垃圾信息）。可通过 `worldserver.conf` 中的 `LogSpamReports` 选项启用垃圾信息举报的记录功能。

**表结构**

| Field                                           | Type     | Attributes | Key | Null | Default | Extra          | Comment                              |
| ----------------------------------------------- | -------- | ---------- | --- | ---- | ------- | -------------- | ------------------------------------ |
| [ID](#id)                                       | INT      | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT | 唯一标识符                            |
| [SpamType](#spamtype)                           | TINYINT  | UNSIGNED   |     | NO   |         |                | 0 = 邮件，1 = 聊天，2 = 日历          |
| [SpammerGuid](#spammerguid)                     | INT      | UNSIGNED   |     | NO   | 0       |                | 被举报玩家的 GUID                     |
| [Unk1](#unk1)                                   | INT      | UNSIGNED   |     | YES  | 0       |                |                                       |
| [MailIdOrMessageType](#mailidormessagetype)     | INT      | UNSIGNED   |     | YES  | 0       |                | 邮件 ID 或消息类型                    |
| [ChannelId](#channelid)                         | INT      | UNSIGNED   |     | YES  | NULL    |                | 仅当 SpamType = 1（聊天）时使用       |
| [SecondsSinceMessage](#secondssincemessage)     | INT      | UNSIGNED   |     | YES  | NULL    |                | 仅当 SpamType = 1（聊天）时使用       |
| [Description](#description)                    | LONGTEXT |            |     | YES  | NULL    |                | 举报的描述或上下文                    |
| [Time](#time)                                   | INT      | SIGNED     |     | YES  | NULL    |                | 举报时间（Unix 时间戳）               |

**字段说明**

### ID

垃圾信息举报的唯一标识符。此数字会自动递增。

### SpamType

被举报的垃圾信息类型：

- 0 = 邮件
- 1 = 聊天
- 2 = 日历

### SpammerGuid

因发送垃圾信息而被举报的玩家的 GUID。参见 [characters.guid](characters#guid)。

### Unk1

未知字段。保留供将来使用。

### MailIdOrMessageType

对于邮件举报（SpamType = 0）：违规邮件的 ID。
对于聊天举报（SpamType = 1）：消息类型。

### ChannelId

发生垃圾信息的聊天频道的频道 ID。仅当 SpamType = 1（聊天）时使用。

### SecondsSinceMessage

自被举报的消息发出以来经过的秒数。仅当 SpamType = 1（聊天）时使用。

### Description

举报所提供的描述或附加上下文（例如日历举报的事件 ID）。

### Time

垃圾信息举报提交时的 Unix 时间戳。
