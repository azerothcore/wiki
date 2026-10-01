# mail

[<-返回至:Characters](database-characters)

**\`mail\` 表**

此表包含游戏中所有邮件的主要数据。

**表结构**

| Field               | Type     | Attributes | Key | Null | Default | Extra | Comment                            |
| ------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [id][1]             | INT      | UNSIGNED   | PRI | NO   | 0       |       | 标识符                             |
| [messageType][2]    | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                    |
| [stationery][3]     | TINYINT  | UNSIGNED   |     | NO   | 41      |       |                                    |
| [mailTemplateId][4] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                    |
| [sender][5]         | INT      | UNSIGNED   |     | NO   | 0       |       | 角色全局唯一标识符                 |
| [receiver][6]       | INT      | UNSIGNED   |     | NO   | 0       |       | 角色全局唯一标识符                 |
| [subject][7]        | LONGTEXT | SIGNED     |     | YES  |         |       |                                    |
| [body][8]           | LONGTEXT | SIGNED     |     | YES  |         |       |                                    |
| [has_items][9]      | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                    |
| [expire_time][10]   | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [deliver_time][11]  | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [money][12]         | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [cod][13]           | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [checked][14]       | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                    |

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

## 字段说明

### id

此字段包含任何邮件的唯一 ID。

没有自增（autoincrement）!!!

### messageType

-   0 = 普通
-   1 = 不存在
-   2 = 拍卖
-   3 = 生物
-   4 = 游戏对象
-   5 = 物品

### stationery

此字段可以包含以下值：

-   1 = 测试
-   41 = 普通邮件版式
-   61 = GM（暴雪）
-   62 = 拍卖
-   64 = VAL (???)
-   65 = CHR (???)

### mailTemplateId

来自 MailTemplate.dbc 的 ID

### sender

在此字段中输入发件人的 [characters.guid](characters#guid)。

### receiver

这里是收件人的 [characters.guid](characters#guid)。

### subject

这里存储邮件的主题。

如果 [stationery][3] 为 62，则主题包含格式化数据：

`itemEntry:0:response:lotId:itemCount`

-    **itemEntry**：来自 item_template 表的 entry 字段

-    0：始终为 0

-    **response**：从 0 到 6 的标志

| 标志 | Comment                     |
| ---- | --------------------------- |
| 0    | AUCTION_OUTBIDDED           |
| 1    | AUCTION_WON                 |
| 2    | AUCTION_SUCCESSFUL          |
| 3    | AUCTION_EXPIRED             |
| 4    | AUCTION_CANCELLED_TO_BIDDER |
| 5    | AUCTION_CANCELED            |
| 6    | AUCTION_SALE_PENDING        |

-    **lotId**：来自 auctionhouse 表的 id 字段

-    **itemCount**：该拍卖品（Lot）中的物品数量

### body

邮件中包含的文本。最大长度为 8000 个字符。

如果 [stationery][3] 为 62，则正文包含格式化数据：

`hexID:bid:buyout:deposit:cut:delay:eta`

-    **hexID**：物品所有者的 GUID 的十六进制值（来自 characters 表的 guid 字段）

-    **bid**：此拍卖品的最终出价

-    **buyout**：拍卖品的一口价

-    **deposit**：拍卖行将收取并在拍卖结束时返还的金额

-    **cut**：佣金费用。拍卖结束时将由拍卖行收取

-    **delay**：成功售出的拍卖品延迟寄送附有金币邮件的时间（以秒为单位）

-    **eta**：包裹好的时间，指下一封带金币邮件出现在邮件标题和通知邮件正文中的时间

这些格式化数据只出现在关于拍卖成功或待寄送带金币邮件的通知邮件中。

### has_items

默认值：0，

当设置为 1 时，该邮件可以包含物品。

关于物品请查看 [mail\_items](mail_items) 表。

### expire\_time

这里存储的是时间戳，用于确定邮件自动退回给发件人的日期，或者如果 [stationery][3] 为 62（拍卖行）时删除邮件的日期。

### deliver\_time

这里存储的是时间戳，表示邮件必须投递给收件人的日期。可以是来自拍卖行的延迟邮件。

### money

邮件中的金币金额，或者是货到付款（COD）时需要支付的金额。

### cod

默认值：0 - 无 COD，

当设置为 1 时，\`money\` 字段存储货到付款（COD）的金币。

### checked

| 标志 | Comment                     |
| ---- | --------------------------- |
| 0    | MAIL_CHECK_MASK_NONE        |
| 1    | MAIL_CHECK_MASK_READ        |
| 2    | MAIL_CHECK_MASK_RETURNED    |
| 4    | MAIL_CHECK_MASK_COPIED      |
| 8    | MAIL_CHECK_MASK_COD_PAYMENT |
| 16   | MAIL_CHECK_MASK_HAS_BODY    |
