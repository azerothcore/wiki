# auctionhouse

[<-返回:Characters](database-characters)

**\`auctionhouse\` 表**

包含拍卖行中当前正在进行的拍卖的所有信息。它控制哪些物品被拍卖、由谁上架、谁是最高出价者等。

**表结构**

| Field            | Type | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]          | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [houseid][2]     | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [itemguid][3]    | INT  | UNSIGNED   | UNI | NO   | 0       |       |         |
| [itemowner][4]   | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [buyoutprice][5] | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [time][6]        | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [buyguid][7]     | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [lastbid][8]     | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [startbid][9]    | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [deposit][10]    | INT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #id
[2]: #houseid
[3]: #itemguid
[4]: #itemowner
[5]: #buyoutprice
[6]: #time
[7]: #buyguid
[8]: #lastbid
[9]: #startbid
[10]: #deposit

**字段说明**

### id

每个拍卖的唯一标识符。

### houseid

添加拍卖物品的生物的 GUID。参见 [creature.guid](creature#guid)。

### itemguid

正在拍卖的物品的 GUID。参见 [item\_instance.guid](item_instance#guid)。

### itemowner

正在拍卖的物品的所有者的 GUID。参见 [characters.guid](characters#guid)。

### buyoutprice

物品的直接购买价格（以铜币计）。除以 100 得到银币，再除以 100 得到金币。

### time

拍卖结束的时间，以 [Unix 时间](http://en.wikipedia.org/wiki/Unix_time) 计量（自 1970 年 1 月 1 日 00:00 起的秒数）。

### buyguid

最高出价者的 GUID。参见 [characters.guid](characters#guid)。

### lastbid

对该物品的最后一次出价的金额（以铜币计）。

### startbid

起拍价的金额（以铜币计）。

### deposit

保证金所花费的金额（以铜币计）。
