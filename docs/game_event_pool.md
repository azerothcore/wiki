# game_event_pool

[<-Back-to:World](database-world)

**The \`game_event_pool\` table**

This table determines if a given pool is active for a given game event.

**Table Structure**

| Field                     | Type      | Attributes | Key | Null | Default | Extra  | Comment                                                             |
| ------------------------- | --------- | ---------- | --- | ---- | ------- | ------ | ------------------------------------------------------------------- |
| [eventEntry](#evententry) | SMALLINT  | SIGNED     |     | NO   |         |        | Entry of the game event. Put negative entry to remove during event. |
| [pool_entry](#pool_entry) | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       | Unique | Id of the pool                                                      |

**Description of the fields**

### eventEntry

Refers to: [game_event.entry](game_event#entry).

Using a **positve** number will **add** the pool to the event when is running.

Using a **negative** number will **remove** the pool to the event when is running.

### pool_entry

Refers to: [pool_pool.pool_id](pool_pool#pool_id).
