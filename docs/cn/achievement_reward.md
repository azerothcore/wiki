# achievement\_reward

[<-返回至:World](database-world)

**`achievement\_reward` 表**

此表描述了当你获得某个成就时将获得的奖励。

**表结构**

| Field               | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]             | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TitleA][2]         | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [TitleH][3]         | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [ItemID][4]         | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [Sender][5]         | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [Subject][6]        | VARCHAR(255) |            |     | YES  |         |       |         |
| [Body][7]           | text         |            |     | YES  |         |       |         |
| [MailTemplateID][8] | MEDIUMINT    | UNSIGNED   |     | YES  | 0       |       |         |

[1]: #id
[2]: #titlea
[3]: #titleh
[4]: #itemid
[5]: #sender
[6]: #subject
[7]: #body
[8]: #mailtemplateid

**字段说明**

### ID

这是取自 DBC `Achievement.dbc` 的成就 ID。

### TitleA

如果该成就奖励称号，这是 `CharTitles.dbc` 中联盟称号的 ID。

### TitleH

如果该成就奖励称号，这是 `CharTitles.dbc` 中部落称号的 ID。

### ItemID

如果该成就奖励物品，这是玩家将获得的物品。玩家会通过邮件获得这件物品。

### Sender

这是玩家将收到的邮件的发件人。

### Subject

这是玩家将收到的邮件的主题。

### Body

这是玩家将收到的邮件的正文（文本）。

### MailTemplateID

玩家将收到的邮件在 `MailTemplate.dbc` 中的 MailTemplate ID。要使用此列，`Subject` 和 `Body` 必须为空，因为它们是按 DBC 文件加载的。

### 示例

| ID  | TitleA | TitleH | ItemID | Sender | Subject             |
| --- | ------ | ------ | ------ | ------ | ------------------- |
| 13  | 0      | 0      | 41426  | 16128  | Level 80            |
| 45  | 0      | 0      | 43348  | 28070  | You've Been Around! |
