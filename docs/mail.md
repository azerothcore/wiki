# mail

[<-Back-to:Characters](database-characters.md)

**The \`mail\` table**

This table contains main data about all mails in the game.

**Structure**

| Field               | Type         | Attributes | Key | Null | Default | Extra | Comment                            |
|---------------------|--------------|------------|-----|------|---------|-------|------------------------------------|
| [id][1]             | int(10)      | unsigned   | PRI | NO   | 0       |       | Identifier                         |
| [messageType][2]    | tinyint(3)   | unsigned   |     | NO   | 0       |       |                                    |
| [stationery][3]     | tinyint(3)   | signed     |     | NO   | 41      |       |                                    |
| [mailTemplateId][4] | MEDIUMINT(5) | unsigned   |     | NO   | 0       |       |                                    |
| [sender][5]         | int(10)      | unsigned   |     | NO   | 0       |       | Character Global Unique Identifier |
| [receiver][6]       | int(10)      | unsigned   |     | NO   | 0       |       | Character Global Unique Identifier |
| [subject][7]        | longtext     | signed     |     | YES  | NULL    |       |                                    |
| [body][8]           | longtext     | signed     |     | YES  |         |       |                                    |
| [has_items][9]      | tinyint(3)   | unsigned   |     | NO   | 0       |       |                                    |
| [expire_time][10]   | int(10)      | unsigned   |     | NO   | 0       |       |                                    |
| [deliver_time][11]  | int(10)      | unsigned   |     | NO   | 0       |       |                                    |
| [money][12]         | int(10)      | unsigned   |     | NO   | 0       |       |                                    |
| [cod][13]           | int(10)      | unsigned   |     | NO   | 0       |       |                                    |
| [checked][14]       | tinyint(3)   | unsigned   |     | NO   | 0       |       |                                    |

[1]: #id
[2]: #messagetype
[3]: #stationery
[4]: #mailtemplateid
[5]: #sender
[6]: #receiver
[7]: #subject
[8]: #body
[9]: #has_items
[10]: #expire_time
[11]: #deliver_time
[12]: #money
[13]: #cod
[14]: #checked

**Description of the fields**

### id

This field contains unique ID of any messages.

Don't have autoincrement !!!

### messageType

-   0 = Normal
-   1 = doesn't exist
-   2 = Auction
-   3 = Creature
-   4 = Gameobject
-   5 = Item

### stationery

This field can contain these values:

-   1 = Test
-   41 = Normal mail layout
-   61 = GM (Blizzard)
-   62 = Auction
-   64 = VAL (???)
-   65 = CHR (???)

### mailTemplateId

Id from MailTemplate.dbc

### sender

In this field is entered sender [character.guid.](2129969.html#characters(table)-guid)

### receiver

Here is receiver's [character.guid.](2129969.html#characters(table)-guid)

### subject

Here is stored mail subject.

### body

The text contained in the mail. Max length is 8000 characters.

### has_items

Default: 0,

When is set to 1, that mail can contain items.

For items look at [mail_items](mail_items) table.

### expire\_time

Here is TIMESTAMP which stores date for auto-return mail to sender.

### deliver\_time

Here is TIMESTAMP which stores date of send mail.

### money

The ammout of money in mail, or money to pay when is COD.

### cod

Default: 0 - No COD,

when is set to 1, that field \`money\` stores gold for COD.

### checked

| Flag | Comment                     |
|------|-----------------------------|
| 0    | MAIL_CHECK_MASK_NONE        |
| 1    | MAIL_CHECK_MASK_READ        |
| 2    | MAIL_CHECK_MASK_RETURNED    |
| 4    | MAIL_CHECK_MASK_COPIED      |
| 8    | MAIL_CHECK_MASK_COD_PAYMENT |
| 16   | MAIL_CHECK_MASK_HAS_BODY    |
