# game\_event\_pool

[<-Back-to:World](database-world)

**The \`game\_event\_pool\` table**

This table determines if a given pool is active for a given game event.

**Table: game\_event\_pool's Structure**

| Field                     | Type     | Attributes | Key | Null | Default | Extra | Comment                                                             |
| ------------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------------------------------------------------------------------- |
| [eventEntry](#evententry) | SMALLINT | SIGNED     |     | NO   |         |       | Entry of the game event. Put negative entry to remove during event. |
| [pool_entry](#poolentry)  | INT      | UNSIGNED   | PRI | NO   | 0       |       | Id of the pool                                                      |

**Description of the table's fields**

### eventEntry

Refers to: [game_event.eventEntry](game_event#evententry).

Using a **positve** number will **add** the pool to the event when is running.

Using a **negative** number will **remove** the pool to the event when is running.

### pool_entry

Refers to: [pool_pool.pool_id](pool_pool#poolid).
