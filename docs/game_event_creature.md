# game\_event\_creature

[<-Back-to:World](database-world.md)

**The \`game\_event\_creature\` table**

Contains all creature instances that have to be spawned/unspawned during defined game events.

**Structure**

| Field           | Type       | Attributes | Key | Null | Default | Extra  | Comment                                                             |
|-----------------|------------|------------|-----|------|---------|--------|---------------------------------------------------------------------|
| [eventEntry][1] | TINYINT(3) | signed     |     | NO   |         |        | Entry of the game event. Put negative entry to remove during event. |
| [guid][2]       | INT(10)    | unsigned   | PRI | NO   |         | Unique |                                                                     |

[1]: #evententry
[2]: #guid

**Description of the fields**

### eventEntry

Entry of the event (game\_event.entry)

**Use**+\*entry to have the creature added during the event
**Use**-\*entry to have it removed during the event

### guid

Guid of the creature participating in the event (creature.guid)
