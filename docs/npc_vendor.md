# npc\_vendor

[<-Back-to:World](database-world)

## General information

This table holds the vendor data for all NPCs that sell items or currencies. A vendor can only hold up to 150 items (15 pages), it is hardcoded in the emulator and if you change it, the client will crash.

### Prices

The price (in gold) for each item or currency is defined in its item template related entry as [item_template.BuyPrice](item_template#buyprice).
Special costs (honor, tokens etc...) are defined in this table in the column [ExtendedCost](#extendedcost).

### GM mode

If you open the vendor's window in GM mode, you will see all the items sold by the vendor. If you disable GM mode, you will see the items sold like a normal player (ex: if you can't use an item and cannot trade it, you won't see it listed).

**Table: npc\_vendor's Structure**

| Field                           | Type     |          | Null | Key | Default | Extra | Comment |
| :------------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [entry](#entry)                 | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [slot](#slot)                   | SMALLINT |          | NO   | MUL | 0       |       |         |
| [item](#item)                   | INT      |          | NO   | PRI | 0       |       |         |
| [maxcount](#maxcount)           | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [incrtime](#incrtime)           | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [ExtendedCost](#extendedcost)   | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [VerifiedBuild](#verifiedbuild) | INT      |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### entry

The ID of the creature. See [creature\_template.entry](creature_template#entry).

### slot

Position of the item when the vendor window opens. It starts from 0 to x, from top to bottom, and from left to right.
*Note: if you have a list of items at slot 0, and you edit one of them to be at slot 1 or any number, that item will always be at the end because all the other items are in slot 0.*

### item

The item ID. See  [item\_template.entry](item_template#entry).

### maxcount

The maximum number of items carried by the vendor at any time. If you want the vendor to carry an unlimited number of the item then set this to **0** else set it to any positive number. In the image below the maxcount value is circled.

### incrtime

Combined with [maxcount](#maxcount), this field tells how often (in seconds) the vendor list is refreshed and the limited item copies are restocked. For limited item copies, every refresh, the quantity is increased by [item\_template.BuyCount](item_template#buycount) .

### ExtendedCost

The value here corresponds to the ID in [ItemExtendedCost.dbc](itemextendedcost_dbc#id) and that ID controls the item's non monetary price, be it honor points, arena points, different types of badges or any combination of the above.

### VerifiedBuild

This field is used to determine if this vendor item originates from verified sniffs.

If value is 0 then it has not been parsed yet or it has been inherited from an older DB or another Core.

If value is above 0 then it has been parsed with sniffs from that specific client build.
