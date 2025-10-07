# game_event_npc_vendor

[<-Volver a:World](database-world)

**Tabla \`game_event_npc_vendor\`**

Esta tabla te permite cambiar los artículos que vende un vendedor o crear una [lista de vendedores](npc_vendor) para un NPC que no vende artículos a menos que un evento esté activo.

**Estructura**

| Campo                         | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ----------------------------- | --------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [eventEntry](#evententry)     | SMALLINT  | SIGNED    |       | NO   | 0           |       |            |
| [guid](#guid)                 | MEDIUMINT | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [slot](#slot)                 | SMALLINT  | SIGNED    |       | NO   | 0           |       |            |
| [item](#item)                 | MEDIUMINT | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [maxcount](#maxcount)         | MEDIUMINT | UNSIGNED  |       | NO   | 0           |       |            |
| [incrtime](#incrtime)         | MEDIUMINT | UNSIGNED  |       | NO   | 0           |       |            |
| [ExtendedCost](#extendedcost) | MEDIUMINT | UNSIGNED  |       | NO   | 0           |       |            |

**Description of the fields**

### eventEntry

Se refiere a: [game_event.entry](game_event#entry).

Only a **positve** value can be used.

### guid

Se refiere a: [creature.guid](creature#guid).

### slot

Refers to: [npc_vendor.slot](npc_vendor#slot).

### item

Se refiere a: [item_template.entry](item_template#entry).

### maxcount

Refers to: [npc_vendor.maxcount](npc_vendor#maxcount).

### incrtime

Refers to: [npc_vendor.incrtime](npc_vendor#incrtime).

### ExtendedCost

Refers to: [npc_vendor.extendedcost](npc_vendor#extendedcost).
