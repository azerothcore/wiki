# mail

[<-Back-to:Characters](database-characters)

**The \`mail\` table**

This table contains main data about all mails in the game.

**Table: mail's Structure**

| Field                             | Type     |          | Null | Key | Default | Extra | Comment                            |
| :-------------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :--------------------------------- |
| [id](#id)                         | INT      | UNSIGNED | NO   | PRI | 0       |       | Identifier                         |
| [messageType](#messagetype)       | TINYINT  | UNSIGNED | NO   |     | 0       |       |                                    |
| [stationery](#stationery)         | TINYINT  |          | NO   |     | 41      |       |                                    |
| [mailTemplateId](#mailtemplateid) | SMALLINT | UNSIGNED | NO   |     | 0       |       |                                    |
| [sender](#sender)                 | INT      | UNSIGNED | NO   |     | 0       |       | Character Global Unique Identifier |
| [receiver](#receiver)             | INT      | UNSIGNED | NO   | MUL | 0       |       | Character Global Unique Identifier |
| [subject](#subject)               | LONGTEXT |          | YES  |     | NULL    |       |                                    |
| [body](#body)                     | LONGTEXT |          | YES  |     | NULL    |       |                                    |
| [has_items](#hasitems)            | TINYINT  | UNSIGNED | NO   |     | 0       |       |                                    |
| [expire_time](#expiretime)        | INT      | UNSIGNED | NO   |     | 0       |       |                                    |
| [deliver_time](#delivertime)      | INT      | UNSIGNED | NO   |     | 0       |       |                                    |
| [money](#money)                   | INT      | UNSIGNED | NO   |     | 0       |       |                                    |
| [cod](#cod)                       | INT      | UNSIGNED | NO   |     | 0       |       |                                    |
| [checked](#checked)               | TINYINT  | UNSIGNED | NO   |     | 0       |       |                                    |

**Description of the table's fields**

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

In this field is entered sender [characters.guid](characters#guid).

### receiver

Here is receiver's [characters.guid](characters#guid).

### subject

Here is stored mail subject.

If [stationery](#stationery) is 62, subject has formatted data:

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

If [stationery](#stationery) is 62, body has formatted data:

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

Here is timestamp which stores date for auto-return mail to sender or delete if [stationery](#stationery) is 62 (AuctionHouse).

### deliver\_time

Here is timestamp which stores date when mail must be delivered to receiver. Can be delayed mails from AuctionHouse.

### money

The ammout of money in mail, or money to pay when is COD.

### cod

Default: 0 - No COD,

when is set to 1, that field \`money\` stores gold for COD.

### checked

| Value | Hex    | Flag                        | Comment                                               |
| :---- | :----: | :-------------------------- | :---------------------------------------------------- |
| 0     | `0x00` | MAIL_CHECK_MASK_NONE        | No flag                                               |
| 1     | `0x01` | MAIL_CHECK_MASK_READ        | The mail was read                                     |
| 2     | `0x02` | MAIL_CHECK_MASK_RETURNED    | The mail was returned, it cannot be returned again    |
| 4     | `0x04` | MAIL_CHECK_MASK_COPIED      | The mail was copied, its items cannot be copied again |
| 8     | `0x08` | MAIL_CHECK_MASK_COD_PAYMENT | The mail is the payment of a cash on delivery mail    |
| 16    | `0x10` | MAIL_CHECK_MASK_HAS_BODY    | The mail has body text                                |
