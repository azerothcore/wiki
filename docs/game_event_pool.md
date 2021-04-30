# game\_event\_pool

[<-Back-to:World](database-world.md)

**The \`game\_event\_pool\` table**

This table determines if a given pool is active for a given game event.

**Structure**

| Field           | Type         | Attributes | Key | Null | Default | Extra  | Comment                                                             |
|-----------------|--------------|------------|-----|------|---------|--------|---------------------------------------------------------------------|
| [eventEntry][1] | TINYINT   | SIGNED     |     | NO   |         |        | Entry of the game event. Put negative entry to remove during event. |
| [pool_entry][2] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       | Unique | Id of the pool                                                      |

[1]: #evententry
[2]: #pool_entry

**Description of the fields**

### eventEntry

This is the ID of the event.

-   +event adds the pool
-   -event removed the pool

### pool\_entry

This is ID of the pool that you want either active or removed for the event.
