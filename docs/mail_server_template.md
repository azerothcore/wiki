# mail_server_template

[<-Back-to:Character](database-character)

**The \`mail_server_template\` table**

This table contains information for server mail to be sent to players that meet the requirement. Mails are sent OnLogin.

**Table Structure**

| Field            | Type    | Attributes | Key | Null | Default | Extra          | Comment |
| ---------------- | ------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [id][1]          | INT     | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [reqLevel][2]    | TINYINT | UNSIGNED   |     | NO   | 0       |                |         |
| [reqPlayTime][3] | INT     | UNSIGNED   |     | NO   | 0       |                |         |
| [moneyA][4]      | INT     | UNSIGNED   |     | NO   | 0       |                |         |
| [moneyH][5]      | INT     | UNSIGNED   |     | NO   | 0       |                |         |
| [itemA][6]       | INT     | UNSIGNED   |     | NO   | 0       |                |         |
| [itemCountA][7]  | INT     | UNSIGNED   |     | NO   | 0       |                |         |
| [itemH][8]       | INT     | UNSIGNED   |     | NO   | 0       |                |         |
| [itemCountH][9]  | INT     | UNSIGNED   |     | NO   | 0       |                |         |
| [subject][10]    | TEXT    |            |     | NO   |         |                |         |
| [body][11]       | TEXT    |            |     | NO   |         |                |         |
| [active][12]     | TINYINT | UNSIGNED   |     | NO   | 1       |                |         |

[1]: #id
[2]: #reqlevel
[3]: #reqplaytime
[4]: #moneya
[5]: #moneyh
[6]: #itema
[7]: #itemcounta
[8]: #itemh
[9]: #itemcounth
[10]: #subject
[11]: #body
[12]: #active

## Description of the fields

### id

Unique ID.

### reqLevel

Players required level to be able to recieve the mail.

### reqPlayTime

Players required play time in milliseconds to recieve the mail.

### moneyA

Money in copper that is sent to Alliance player.

### moneyH

Money in copper that is sent to Horde player.

### itemA

[item_template.entry](item_template#entry) that is sent to Alliance player.

### itemCountA

How many of the specified [itemA](#itema) is sent.

### itemH

[item_template.entry](item_template#entry).

### itemCountH

How many of the specified [itemH](#itemh) is sent that is sent to Horde player.

### subject

The title/subject of the mail.

### body

The body of the mail.

### active

boolean

- 1 = Mail is active and will be sent to the players if they meet the requirement.
- 0 = Disabled.
