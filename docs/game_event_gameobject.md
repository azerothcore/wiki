# game\_event\_gameobject

[<-Back-to:World](database-world)

**The \`game\_event\_gameobject\` table**

Contains all gameobjects instances that participate to any game event.

**Table Structure**

| Field           | Type    | Attributes | Key | Null | Default | Extra  | Comment                                                             |
| --------------- | ------- | ---------- | --- | ---- | ------- | ------ | ------------------------------------------------------------------- |
| [eventEntry][1] | TINYINT | SIGNED     |     | NO   |         |        | Entry of the game event. Put negative entry to remove during event. |
| [guid][2]       | INT     | UNSIGNED   | PRI | NO   |         | Unique |                                                                     |

[1]: #evententry
[2]: #guid

**Description of the fields**

### eventEntry

Entry of the event (game\_event.eventEntry)

**Use**+\*eventEntry to have the gameobject added during the event
**Use**-\*eventEntry to have it removed during the event

### guid

Guid of the gameobject participating in the event (gameobject.guid)
