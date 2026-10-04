# item\_refund\_instance

[<-Back-to:Characters](database-characters)

**The \`item\_refund\_instance\` table**

This table serves as a receipt of refundable purchases during a 2 hour ingame time window. It holds information on what currency was spent to purchase the item.

**Table: item\_refund\_instance's Structure**

| Field                                 | Type     |          | Null | Key | Default | Extra | Comment     |
| :------------------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :---------- |
| [item_guid](#itemguid)                | INT      | UNSIGNED | NO   | PRI |         |       | Item GUID   |
| [player_guid](#playerguid)            | INT      | UNSIGNED | NO   | PRI |         |       | Player GUID |
| [paidMoney](#paidmoney)               | INT      | UNSIGNED | NO   |     | 0       |       |             |
| [paidExtendedCost](#paidextendedcost) | SMALLINT | UNSIGNED | NO   |     | 0       |       |             |

**Description of the table's fields**

### item\_guid

The GUID of the item bought by the vendor. See [item\_instance.guid](item_instance#guid).

### player\_guid

The GUID of the player eligible for the refund. See [characters.guid](characters#guid).

### paidMoney

The amount of money (in copper) paid for the item.

### paidExtendedCost

The ItemExtendedCost.dbc ID that was paid for the item.
