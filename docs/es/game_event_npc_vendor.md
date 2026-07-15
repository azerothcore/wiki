# game_event_npc_vendor

[<-Volver a:World](database-world)

**Tabla \`game_event_npc_vendor\`**

Esta tabla te permite cambiar los items que vende un vendedor, o crear una [lista de vendedor](npc_vendor) para un NPC que no vende items salvo que un evento esté activo.

**Estructura**

| Field                         | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [eventEntry](#evententry)     | SMALLINT  | SIGNED     |     | NO   | 0       |       |         |
| [guid](#guid)                 | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [slot](#slot)                 | SMALLINT  | SIGNED     |     | NO   | 0       |       |         |
| [item](#item)                 | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [maxcount](#maxcount)         | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [incrtime](#incrtime)         | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [ExtendedCost](#extendedcost) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |

**Descripción de los campos**

### eventEntry

Se refiere a: [game_event.entry](game_event#entry).

Solo se puede usar un valor **positivo**.

### guid

Se refiere a: [creature.guid](creature#guid).

### slot

Se refiere a: [npc_vendor.slot](npc_vendor#slot).

### item

Se refiere a: [item_template.entry](item_template#entry).

### maxcount

Se refiere a: [npc_vendor.maxcount](npc_vendor#maxcount).

### incrtime

Se refiere a: [npc_vendor.incrtime](npc_vendor#incrtime).

### ExtendedCost

Se refiere a: [npc_vendor.extendedcost](npc_vendor#extendedcost).
