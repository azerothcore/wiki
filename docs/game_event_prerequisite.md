# game\_event\_prerequisite

[<-Back-to:World](database-world)

**The \`game\_event\_prerequisite\` table**

This table contains events that must have been completed to start the given event. You can have more than one event that must be completed before the next will start.

**Table: game\_event\_prerequisite's Structure**

| Field                                    | Type    |          | Null | Key | Default | Extra | Comment                 |
| :--------------------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :---------------------- |
| [eventEntry](#evententry)                | TINYINT | UNSIGNED | NO   | PRI |         |       | Entry of the game event |
| [prerequisite_event](#prerequisiteevent) | INT     | UNSIGNED | NO   | PRI |         |       |                         |

**Description of the table's fields**

### eventEntry

This is the event that will start when all prerequisite events have been completed.

### prerequisite\_event

The is the event that must be completed before the next [event](#evententry) will start.
