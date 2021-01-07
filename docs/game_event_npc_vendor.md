# game\_event\_npc\_vendor

[<-Back-to:World](database-world.md)

**The \`game\_event\_npc\_vendor\` table**

This table allows you to change the items a vendor sells, or to create a [vendor list](npc_vendor) for an NPC who does not sell items unless an event is active.

**Structure**

| Field             | Type         | Attributes | Key | Null | Default | Extra | Comment |
|-------------------|--------------|------------|-----|------|---------|-------|---------|
| [eventEntry][1]   | tinyint(3)   | signed     |     | NO   | 0       |       |         |
| [guid][2]         | mediumint(8) | unsigned   | PRI | NO   | 0       |       |         |
| [slot][3]         | smallint(6)  | signed     |     | NO   | 0       |       |         |
| [item][4]         | mediumint(8) | unsigned   | PRI | NO   | 0       |       |         |
| [maxcount][5]     | mediumint(8) | unsigned   |     | NO   | 0       |       |         |
| [incrtime][6]     | mediumint(8) | unsigned   |     | NO   | 0       |       |         |
| [ExtendedCost][7] | mediumint(8) | unsigned   |     | NO   | 0       |       |         |

[1]: #evententry
[2]: #guid
[3]: #slot
[4]: #item
[5]: #maxcount
[6]: #incrtime
[7]: #extendedcost

**Description of the fields**

### eventEntry

This is the eventEntry from the game\_event table that you wish to setup a vendor list for while the event is running.

### guid

This is the guid of the NPC that you wish to create a vendor list for.

### slot

Position of the item when the vendor window opens (order from top-left to bottom.right of the window with values 0 and then 1,2,3,etc).

### item

This is an item from the item\_template table.

### maxcount

The maximum number of copies of the item the vendor has available to be sold before [incrtime](#game_event_npc_vendor-incrtime) is up. If 0, then it is an unlimited number of copies.

### incrtime

Combined with [maxcount](#game_event_npc_vendor-maxcount), this field tells how often (in seconds) the vendor list is refreshed and the limited item copies are restocked. For limited item copies, every refresh, the quantity is increased by item\_template.BuyCount

### ExtendedCost

The value here corresponds to the ID in ItemExtendedCost.dbc and that ID controls the item's non monetary price, be it honor points, arena points, different types of badges or any combination of the above.
