# game\_event\_model\_equip

[<-Back-to:World](database-world.md)

**The \`game\_event\_model\_equip\` table**

Contains all creature instances that need to change display id and/or equipment during defined game events.

**Structure**

| Field             | Type         | Attributes | Key | Null | Default | Extra  | Comment                  |
|-------------------|--------------|------------|-----|------|---------|--------|--------------------------|
| [eventEntry][1]   | tinyint(3)   | signed     |     | NO   | 0       |        | Entry of the game event. |
| [guid][2]         | int(10)      | unsigned   | PRI | NO   | 0       | Unique |                          |
| [modelid][3]      | mediumint(8) | unsigned   |     | NO   | 0       |        |                          |
| [equipment_id][4] | mediumint(8) | unsigned   |     | NO   | 0       |        |                          |

[1]: #evententry
[2]: #guid
[3]: #modelid
[4]: #equipment_id

**Description of the fields**

### eventEntry

Entry of the event (game\_event.eventEntry)

-   In this table, event entry can only be positive

### guid

Guid of the creature participating in the event (creature.guid)

### modelid

New model to be used while the event is active (Refers to creature\_model\_info.modelid)
Use 0 if only the [equipment](#game_event_model_equip-equipment_id) is to be changed during event.

### equipment\_id

New equipment to be used during the event (Refers to creature\_equip\_template.entry))
Use 0 if only the [model](#game_event_model_equip-modelid) is to be changed during event.
