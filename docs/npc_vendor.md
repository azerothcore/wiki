# npc\_vendor

[<-Back-to:World](database-world.md)

## General information

This table holds the vendor data for all NPCs that sell items or currencies.

### Prices

The price (in gold) for each item or currency is defined in its item template related entry as [item_template.BuyPrice](item_template#buyprice).
Special costs (honor, tokens etc...) are defined in this table in the column [ExtendedCost](#extendedcost).

### GM mode

If you open the vendor's window in GM mode, you will see all the items sold by the vendor. If you disable GM mode, you will see the items sold like a normal player (ex: only for your own faction, only for your own class etc...).


## Table Structure

|      Field        |    Type      | Attributes | Key | Null | Default |
|-------------------|--------------|------------|-----|------|---------|
| [entry][1]        | mediumint(8) | unsigned   | PRI | NO   | 0       |
| [slot][2]         | smallint(6)  | signed     |     | NO   | 0       |
| [item][3]         | mediumint(8) | signed     | PRI | NO   | 0       |
| [maxcount][4]     | tinyint(3)   | unsigned   |     | NO   | 0       |
| [incrtime][5]     | int(10)      | unsigned   |     | NO   | 0       |
| [ExtendedCost][6] | mediumint(8) | unsigned   | PRI | NO   | 0       |

[1]: #entry
[2]: #slot
[3]: #item
[4]: #maxcount
[5]: #incrtime
[6]: #extendedcost


## Field Descriptions

### entry

The ID of the creature. See [creature\_template.entry](creature_template#entry).

### slot

Position of the item when the vendor window opens. The image below explains how the vendor-inventory slots are numbered. To continue on past the first page just use numbers 10, 11, 12, etc...

### item

The item ID. See  [item\_template.entry](item_template#entry).

### maxcount

The maximum number of items carried by the vendor at any time. If you want the vendor to carry an unlimited number of the item then set this to **0** else set it to any positive number. In the image below the maxcount value is circled.

### incrtime

Combined with [maxcount](#maxcount), this field tells how often (in seconds) the vendor list is refreshed and the limited item copies are restocked. For limited item copies, every refresh, the quantity is increased by [item\_template.BuyCount](item_template#buycount) .

### ExtendedCost

The value here corresponds to the ID in [ItemExtendedCost.dbc](NO_LINK_YET) and that ID controls the item's non monetary price, be it honor points, arena points, different types of badges or any combination of the above.
