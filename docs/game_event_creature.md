# game\_event\_creature

[<-Back-to:World](database-world)

**The \`game\_event\_creature\` table**

Contains all creature instances that have to be spawned/unspawned during defined game events.

**Table: game\_event\_creature's Structure**

| Field                     | Type     |          | Null | Key | Default | Extra | Comment                                                             |
| :------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :------------------------------------------------------------------ |
| [eventEntry](#evententry) | SMALLINT |          | NO   | PRI |         |       | Entry of the game event. Put negative entry to remove during event. |
| [guid](#guid)             | INT      | UNSIGNED | NO   | PRI |         |       |                                                                     |

**Description of the table's fields**

### eventEntry

Refers to: [game_event.eventEntry](game_event#evententry).

Using a **positve** number will **add** the creature to the event when is running.

Using a **negative** number will **remove** the creature to the event when is running.

### guid

Refers to: [creature.guid](creature#guid).
