# game\_event\_model\_equip

[<-Back-to:World](database-world)

**The \`game\_event\_model\_equip\` table**

Contains all creature instances that need to change display id and/or equipment during defined game events.

**Table: game\_event\_model\_equip's Structure**

| Field                        | Type    |          | Null | Key | Default | Extra | Comment                  |
| :--------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [eventEntry](#evententry)    | TINYINT | UNSIGNED | NO   |     |         |       | Entry of the game event. |
| [guid](#guid)                | INT     | UNSIGNED | NO   | PRI | 0       |       |                          |
| [modelid](#modelid)          | INT     | UNSIGNED | NO   |     | 0       |       |                          |
| [equipment_id](#equipmentid) | TINYINT | UNSIGNED | NO   |     | 0       |       |                          |

**Description of the table's fields**

### eventEntry

Refers to: [game_event.eventEntry](game_event#evententry).

Only a **positve** value can be used.

### guid

Refers to: [creature.guid](creature#guid).

### modelid

Refers to [creature_model_info.displayid](creature_model_info#displayid) to change the [creature](creature#guid)'s [model](creature_model_info#displayid) when the event running.

### equipment_id

Refers to [creature_equip_template.creatureid](creature_equip_template#creatureid) to change when the event running.

If you don't want to add or change the current equipment being used, set the value to `0`, It will use [creature_equip_template](creature_equip_template#creatureid) for the [creature_template](creature_template#entry) where it matches with [creature.id](creature#id) from [creature.guid](creature#guid).
