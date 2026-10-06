# game\_event\_gameobject\_quest

[<-Back-to:World](database-world)

**The \`game\_event\_gameobject\_quest\` table**

This table holds information on quests that should only be available when an event is currently taking place.

**Table: game\_event\_gameobject\_quest's Structure**

| Field                     | Type    |          | Null | Key | Default | Extra | Comment                 |
| :------------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :---------------------- |
| [eventEntry](#evententry) | TINYINT | UNSIGNED | NO   | PRI |         |       | Entry of the game event |
| [id](#id)                 | INT     | UNSIGNED | NO   | PRI | 0       |       |                         |
| [quest](#quest)           | INT     | UNSIGNED | NO   | PRI | 0       |       |                         |

**Description of the table's fields**

### eventEntry

The event ID. See game\_event.eventEntry

### id

The Gameobject ID. See gameobject\_template.entry

### quest

The quest ID. See [quest\_template.ID](quest_template#id)
