# game_event_npc_vendor

[<-Back-to:World](database-world)

**The \`game_event_npc_vendor\` table**

This table allows you to change the items a vendor sells, or to create a [vendor list](npc_vendor) for an NPC who does not sell items unless an event is active.

**Table Structure**

| Field                         | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [eventEntry](#evententry)     | SMALLINT  | SIGNED     |     | NO   | 0       |       |         |
| [guid](#guid)                 | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [slot](#slot)                 | SMALLINT  | SIGNED     |     | NO   | 0       |       |         |
| [item](#item)                 | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [maxcount](#maxcount)         | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [incrtime](#incrtime)         | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [ExtendedCost](#extendedcost) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |

**Description of the fields**

### eventEntry

Refers to: [game_event.entry](game_event#entry).

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
