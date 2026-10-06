# game\_event\_npc\_vendor

[<-Back-to:World](database-world)

**The \`game\_event\_npc\_vendor\` table**

This table allows you to change the items a vendor sells, or to create a [vendor list](npc_vendor) for an NPC who does not sell items unless an event is active.

**Table: game\_event\_npc\_vendor's Structure**

| Field                         | Type     |          | Null | Key | Default | Extra | Comment                  |
| :---------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [eventEntry](#evententry)     | SMALLINT |          | NO   | PRI |         |       | Entry of the game event. |
| [guid](#guid)                 | INT      | UNSIGNED | NO   | PRI | 0       |       |                          |
| [slot](#slot)                 | SMALLINT |          | NO   | MUL | 0       |       |                          |
| [item](#item)                 | INT      | UNSIGNED | NO   | PRI | 0       |       |                          |
| [maxcount](#maxcount)         | INT      | UNSIGNED | NO   |     | 0       |       |                          |
| [incrtime](#incrtime)         | INT      | UNSIGNED | NO   |     | 0       |       |                          |
| [ExtendedCost](#extendedcost) | INT      | UNSIGNED | NO   |     | 0       |       |                          |

**Description of the table's fields**

### eventEntry

Refers to: [game_event.eventEntry](game_event#evententry).

Only a **positve** value can be used.

### guid

Refers to: [creature.guid](creature#guid).

### slot

Refer to: [npc_vendor.slot](npc_vendor#slot).

### item

Refers to: [item_template.entry](item_template#entry).

### maxcount

Refer to: [npc_vendor.maxcount](npc_vendor#maxcount).

### incrtime

Refer to: [npc_vendor.incrtime](npc_vendor#incrtime).

### ExtendedCost

Refer to: [npc_vendor.extendedcost](npc_vendor#extendedcost).
