# achievement\_reward

[<-Back-to:World](database-world)

**The \`achievement\_reward\` table**

This table describes the reward that you will receive when you obtain a given achievement.

**Table Structure**

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

**Description of the fields**

### ID

This is the ID of the achievement taken from the DBC `Achievement.dbc`.

### TitleA

This is the ID of the title for Alliance from `CharTitles.dbc` if the achievement rewards a title.

### TitleH

This is the ID of the title for Horde from `CharTitles.dbc` if the achievement rewards a title.

### ItemID

This is the item that that the player will receive if the achievement rewards an item. The player will get this item in a mail.

### Sender

This is the sender of the mail that the player will receive.

### Subject

This is the subject of the mail that the player will receive.

### Body

This is the body (text) of the mail that the player will receive.

### MailTemplateID

Id of the MailTemplate from `MailTemplate.dbc` of that mail that the player will receive. To use this column, `Subject` and `Body` must be empty as they are loaded from the DBC file.

### Example

| ID  | TitleA | TitleH | ItemID | Sender | Subject             |
| --- | ------ | ------ | ------ | ------ | ------------------- |
| 13  | 0      | 0      | 41426  | 16128  | Level 80            |
| 45  | 0      | 0      | 43348  | 28070  | You've Been Around! |
