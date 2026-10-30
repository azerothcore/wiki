# mail\_server\_template

[<-Back-to:Characters](database-characters)

**The \`mail\_server\_template\` table**

This table contains information for server mail to be sent to players that meet the requirement. Mails are sent OnLogin.

Works alongside
- [mail_server_template_items](mail_server_template_items) to attach items to the mail.
- [mail_server_template_conditions](mail_server_template_conditions) to create conditions to receive the mail.

**Table: mail\_server\_template's Structure**

| Field                       | Type    |          | Null | Key | Default | Extra          | Comment                                                                |
| :-------------------------- | :------ | :------- | :--: | :-: | :-----: | :------------: | :--------------------------------------------------------------------- |
| [id](#id)                   | INT     | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT |                                                                        |
| [senderEntry](#senderentry) | INT     | UNSIGNED | NO   |     | 0       |                | Entry from creature_template. 0 for default "Customer Support" sender. |
| [moneyA](#moneya)           | INT     | UNSIGNED | NO   |     | 0       |                |                                                                        |
| [moneyH](#moneyh)           | INT     | UNSIGNED | NO   |     | 0       |                |                                                                        |
| [subject](#subject)         | TEXT    |          | NO   |     |         |                |                                                                        |
| [body](#body)               | TEXT    |          | NO   |     |         |                |                                                                        |
| [active](#active)           | TINYINT | UNSIGNED | NO   |     | 1       |                |                                                                        |

**Description of the table's fields**

### id

Unique ID.

### senderentry

[creature_template.entry](creature_template#entry) used as the mail sender.

Set to `0` to keep using the default **Customer Support** sender.

### moneyA

Money in copper that is sent to Alliance player.

### moneyH

Money in copper that is sent to Horde player.

### subject

The title/subject of the mail.

### body

The body of the mail.

### active

boolean

- 1 = Mail is active and will be sent to the players if they meet the requirement.
- 0 = Disabled.
