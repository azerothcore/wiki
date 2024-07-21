# game\_event\_gameobject\_quest

[<-Back-to:World](database-world)

**The \`game\_event\_gameobject\_quest\` table**

This table holds information on quests that should only be available when an event is currently taking place.

**Table Structure**

| Field           | Type      | Attributes | Key | Null | Default | Extra | Comment                 |
| --------------- | --------- | ---------- | --- | ---- | ------- | ----- | ----------------------- |
| [eventEntry][1] | TINYINT   | UNSIGNED   | PRI | NO   |         |       | Entry of the game event |
| [id][2]         | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                         |
| [quest][3]      | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                         |

[1]: #evententry
[2]: #id
[3]: #quest

**Description of the fields**

### id

The Gameobject ID. See gameobject\_template.entry

### quest

The quest ID. See quest\_template.entry

### eventEntry

The event ID. See game\_event.eventEntry
