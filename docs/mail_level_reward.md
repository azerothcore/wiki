# mail\_level\_reward

[<-Back-to:World](database-world)

**The \`mail\_level\_reward\` table**

On certain levels, you receive a mail with some text.

**Table: mail\_level\_reward's Structure**

| Field                             | Type    |          | Null | Key | Default | Extra | Comment |
| :-------------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [level](#level)                   | TINYINT | UNSIGNED | NO   | PRI | 0       |       |         |
| [raceMask](#racemask)             | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [mailTemplateId](#mailtemplateid) | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [senderEntry](#senderentry)       | INT     | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### level

Level required for receiving specific mail

### raceMask

Mask required to receive mail.
`:ChrRaces.dbc`

### mailTemplateId

Mail ID to be send. See [MailTemplate.dbc](https://wowdev.wiki/DB/MailTemplate)

### senderEntry

The creature entry ID of the NPC that sends the reward mail. See [creature_template.entry](creature_template#entry).
