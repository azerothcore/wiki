# game_event_creature

[<-Back-to:World](database-world)

**The \`game_event_creature\` table**

Contains all creature instances that have to be spawned/unspawned during defined game events.

**Table Structure**

| Field                     | Type     | Attributes | Key | Null | Default | Extra  | Comment                                                             |
| ------------------------- | -------- | ---------- | --- | ---- | ------- | ------ | ------------------------------------------------------------------- |
| [eventEntry](#evententry) | SMALLINT | SIGNED     |     | NO   |         |        | Entry of the game event. Put negative entry to remove during event. |
| [guid](#guid)             | INT      | UNSIGNED   | PRI | NO   |         | Unique |                                                                     |

**Description of the fields**

### eventEntry

Refers to: [game_event.entry](game_event#entry).

Using a **positve** number will **add** the creature to the event when is running.

Using a **negative** number will **remove** the creature to the event when is running.

### guid

Refers to: [creature.guid](creature#guid).
