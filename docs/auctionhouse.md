# auctionhouse

[<-Back-to:Characters](database-characters)

**The \`auctionhouse\` table**

Contains all information about the currently ongoing auctions in the auction houses. It controls what items are put up for auction and who put it up, who is the highest bidder, etc.

**Table: auctionhouse's Structure**

| Field                       | Type    |          | Null | Key | Default | Extra | Comment |
| :-------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [id](#id)                   | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [houseid](#houseid)         | TINYINT | UNSIGNED | NO   |     | 7       |       |         |
| [itemguid](#itemguid)       | INT     | UNSIGNED | NO   | UNI | 0       |       |         |
| [itemowner](#itemowner)     | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [buyoutprice](#buyoutprice) | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [time](#time)               | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [buyguid](#buyguid)         | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [lastbid](#lastbid)         | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [startbid](#startbid)       | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [deposit](#deposit)         | INT     | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

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
