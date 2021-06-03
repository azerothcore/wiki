# item\_refund\_instance

[<-Back-to:Characters](database-characters.md)

**The \`item\_refund\_instance\` table**

This table serves as a receipt of refundable purchases during a 2 hour ingame time window. It holds information on what currency was spent to purchase the item.

**Structure**

| Field                 | Type        | Attributes | Key | Null | Default | Extra  | Comment     |
|-----------------------|-------------|------------|-----|------|---------|--------|-------------|
| [item_guid][1]        | INT     | UNSIGNED   | PRI | NO   |         | Unique | Item GUID   |
| [player_guid][2]      | INT     | UNSIGNED   | PRI | NO   |         |        | Player GUID |
| [paidMoney][3]        | INT     | UNSIGNED   |     | NO   | 0       |        |             |
| [paidExtendedCost][4] | SMALLINT | UNSIGNED   |     | NO   | 0       |        |             |

[1]: #item_guid
[2]: #player_guid
[3]: #paidmoney
[4]: #paidextendedcost

**Description of the fields**

### item\_guid

The GUID of the item bought by the vendor. See item\_instance.guid.

### player\_guid

The GUID of the player eligible for the refund. See characters.guid.

### paidMoney

The amount of money (in copper) paid for the item.

### paidExtendedCost

The ItemExtendedCost.dbc ID that was paid for the item.
