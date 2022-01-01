# mail

[<-Back-to:Characters](database-characters.md)

**The \`mail\` table**

This table contains main data about all mails in the game.

**Structure**

| Field               | Type     | Attributes | Key | Null | Default | Extra | Comment                            |
| ------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [id][1]             | INT      | UNSIGNED   | PRI | NO   | 0       |       | Identifier                         |
| [messageType][2]    | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                    |
| [stationery][3]     | TINYINT  | UNSIGNED   |     | NO   | 41      |       |                                    |
| [mailTemplateId][4] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                    |
| [sender][5]         | INT      | UNSIGNED   |     | NO   | 0       |       | Character Global Unique Identifier |
| [receiver][6]       | INT      | UNSIGNED   |     | NO   | 0       |       | Character Global Unique Identifier |
| [subject][7]        | LONGTEXT | SIGNED     |     | YES  |         |       |                                    |
| [body][8]           | LONGTEXT | SIGNED     |     | YES  |         |       |                                    |
| [has_items][9]      | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                    |
| [expire_time][10]   | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [deliver_time][11]  | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [money][12]         | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [cod][13]           | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [checked][14]       | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                    |
| [auctionId][14]     | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |

[1]: #id
[2]: #messagetype
[3]: #stationery
[4]: #mailtemplateid
[5]: #sender
[6]: #receiver
[7]: #subject
[8]: #body
[9]: #hasitems
[10]: #expiretime
[11]: #delivertime
[12]: #money
[13]: #cod
[14]: #checked
[15]: #auctionid

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

In this field is entered sender [character.guid](character#guid).

### receiver

Here is receiver's [character.guid](character#guid).

### subject

Here is stored mail subject.

If [stationery][3] is 62, subject has formatted data:

`itemEntry:0:response:lotId:itemCount`

-    **itemEntry**: entry field from item_template table

-    0: allways 0

-    **response**: Flag from 0 to 6

| Flag | Comment                     |
| ---- | --------------------------- |
| 0    | AUCTION_OUTBIDDED           |
| 1    | AUCTION_WON                 |
| 2    | AUCTION_SUCCESSFUL          |
| 3    | AUCTION_EXPIRED             |
| 4    | AUCTION_CANCELLED_TO_BIDDER |
| 5    | AUCTION_CANCELED            |
| 6    | AUCTION_SALE_PENDING        |

-    **lotId**: id field from auctionhouse table

-    **itemCount**: amount of item at this Lot


### body

The text contained in the mail. Max length is 8000 characters.

If [stationery][3] is 62, body has formatted data:

`hexID:bid:buyout:deposit:cut:delay:eta`

-    **hexID**: hex value of itemowner's GUID (guid field from characters table)

-    **bid**: ending bid for this lot

-    **buyout**: buyout price of lot

-    **deposit**: amount of money which will be taken by auctionhouse and returned then auction ends

-    **cut**: Commission fee. Will be taken by auctionhouse then auction ends

-    **delay**: time in seconds to delay mail with money for successfully solded lot

-    **eta**: packed time to next mail whth money which appears in mail heder and body of notification mail

This formatted data seen only in mail with notification about successful auction or about pending mail with money.



### has_items

Default: 0,

When is set to 1, that mail can contain items.

For items look at [mail\_items](mail_items) table.

### expire\_time

Here is timestamp which stores date for auto-return mail to sender or delete if [stationery][3] is 62 (AuctionHouse).

### deliver\_time

Here is timestamp which stores date of send mail.

### money

The ammout of money in mail, or money to pay when is COD.

### cod

Default: 0 - No COD,

when is set to 1, that field \`money\` stores gold for COD.

### checked

| Flag | Comment                     |
| ---- | --------------------------- |
| 0    | MAIL_CHECK_MASK_NONE        |
| 1    | MAIL_CHECK_MASK_READ        |
| 2    | MAIL_CHECK_MASK_RETURNED    |
| 4    | MAIL_CHECK_MASK_COPIED      |
| 8    | MAIL_CHECK_MASK_COD_PAYMENT |
| 16   | MAIL_CHECK_MASK_HAS_BODY    |

### auctionId

`field-no-description|14`
