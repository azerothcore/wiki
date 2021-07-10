# auctionhouse

[<-Back-to:Characters](database-characters.md)

**The \`auctionhouse\` table**

Contains all information about the currently ongoing auctions in the auction houses. It controls what items are put up for auction and who put it up, who is the highest bidder, etc.

This table is used by Trinity while running and not a table that you would usually edit.

**Structure**

| Field               | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]             | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [houseid][2]        | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [itemguid][3]       | INT  | UNSIGNED   | UNI | NO   | 0       |       |         |
| [itemowner][4]      | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [buyoutprice][5]    | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [time][6]           | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [buyguid][7]        | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [lastbid][8]        | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [startbid][9]       | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [deposit][10]       | INT  | UNSIGNED   |     | NO   | 0       |       |         |

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

**Description of the fields**

### id

Unique identifier for every auction.

### houseid

The GUID of the creature where the auction item was added. See [creature.guid](creature#guid).

### itemguid

The GUID of the item that is up for auction. See [item\_instance.guid](item_instance#guid).

### itemowner

The GUID of the owner of the item up for auction. See [characters.guid](characters#guid).

### buyoutprice

The buyout price of the item in copper. Divide by 100 to get silver and by 100 again to get gold.

### time

The time when the auction will end, measured in [Unix time](http://en.wikipedia.org/wiki/Unix_time) (number of seconds from 00:00 Jan 1, 1970).

### buyguid

The GUID of the highest bidder. See [characters.guid](characters#guid).

### lastbid

The amount of copper of the last bid put on the item.

### startbid

The amount of copper of the starting bid.

### deposit

The amount of copper spent on the deposit.
