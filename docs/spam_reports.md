# spam\_reports

[<-Back-to:Characters](database-characters)

**The `spam_reports` table**

This table stores spam reports submitted by players in-game (e.g. reporting spam in chat, mail, or calendar). Logging of spam reports can be enabled via the `LogSpamReports` option in `worldserver.conf`.

**Table Structure**

| Field                                           | Type     | Attributes | Key | Null | Default | Extra          | Comment                              |
| ----------------------------------------------- | -------- | ---------- | --- | ---- | ------- | -------------- | ------------------------------------ |
| [ID](#id)                                       | INT      | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT | Unique identifier                    |
| [SpamType](#spamtype)                           | TINYINT  | UNSIGNED   |     | NO   |         |                | 0 = mail, 1 = chat, 2 = calendar     |
| [SpammerGuid](#spammerguid)                     | INT      | UNSIGNED   |     | NO   | 0       |                | GUID of the reported player          |
| [Unk1](#unk1)                                   | INT      | UNSIGNED   |     | YES  | 0       |                |                                      |
| [MailIdOrMessageType](#mailIdOrMessageType)     | INT      | UNSIGNED   |     | YES  | 0       |                | Mail ID or message type              |
| [ChannelId](#channelid)                         | INT      | UNSIGNED   |     | YES  | NULL    |                | Only used if SpamType = 1 (chat)     |
| [SecondsSinceMessage](#secondssinceMessage)     | INT      | UNSIGNED   |     | YES  | NULL    |                | Only used if SpamType = 1 (chat)     |
| [Description](#description)                    | LONGTEXT |            |     | YES  | NULL    |                | Description or context of the report |
| [Time](#time)                                   | INT      | SIGNED     |     | YES  | NULL    |                | Time of report as Unix timestamp     |

**Description of the fields**

### ID

The unique identifier for the spam report. This number is automatically incremented.

### SpamType

The type of spam being reported:

- 0 = Mail
- 1 = Chat
- 2 = Calendar

### SpammerGuid

The GUID of the player being reported for spam. See [characters.guid](characters#guid).

### Unk1

Unknown field. Reserved for future use.

### MailIdOrMessageType

For mail reports (SpamType = 0): the ID of the offending mail.
For chat reports (SpamType = 1): the message type.

### ChannelId

The channel ID of the chat channel in which the spam occurred. Only used when SpamType = 1 (chat).

### SecondsSinceMessage

The number of seconds elapsed since the reported message was sent. Only used when SpamType = 1 (chat).

### Description

A description or additional context provided by the report (e.g. event ID for calendar reports).

### Time

The Unix timestamp of when the spam report was submitted.
