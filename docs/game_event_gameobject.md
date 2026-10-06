# game\_event\_gameobject

[<-Back-to:World](database-world)

**The \`game\_event\_gameobject\` table**

Contains all gameobjects instances that participate to any game event.

**Table: game\_event\_gameobject's Structure**

| Field                     | Type     |          | Null | Key | Default | Extra | Comment                                                             |
| :------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :------------------------------------------------------------------ |
| [eventEntry](#evententry) | SMALLINT |          | NO   | PRI |         |       | Entry of the game event. Put negative entry to remove during event. |
| [guid](#guid)             | INT      | UNSIGNED | NO   | PRI |         |       |                                                                     |

**Description of the table's fields**

### eventEntry

Refers to: [game_event.eventEntry](game_event#evententry).

Using a **positve** number will **add** the object to the event when is running.

Using a **negative** number will **remove** the object to the event when is running.

### guid

Refers to: [gameobject.guid](gameobject#guid).
