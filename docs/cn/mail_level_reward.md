# mail\_level\_reward

[<-返回至:World](database-world)

**\`mail\_level\_reward\` 表**

在特定等级，你会收到一封附带一些文字的邮件。

**表结构**

| Field               | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [level][1]          | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |         |
| [raceMask][2]       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [mailTemplateId][3] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [senderEntry][4]    | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #level
[2]: #racemask
[3]: #mailtemplateid
[4]: #senderentry

## 字段说明

### level

接收特定邮件所需的等级

### raceMask

接收邮件所需的种族掩码。
`:ChrRaces.dbc`

### mailTemplateId

要发送的邮件 ID。参见 [MailTemplate.dbc](https://wowdev.wiki/DB/MailTemplate)

### senderEntry

发送奖励邮件的 NPC 的生物 entry ID。参见 [creature_template.entry](creature_template#entry)。
