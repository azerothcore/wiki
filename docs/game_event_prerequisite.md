# game\_event\_prerequisite

[<-Back-to:World](database-world)

**The \`game\_event\_prerequisite\` table**

This table contains events that must have been completed to start the given event. You can have more than one event that must be completed before the next will start.

**Table Structure**

| Field                   | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [eventEntry][1]         | TINYINT   | UNSIGNED   | PRI | NO   |         |       |         |
| [prerequisite_event][2] | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |

[1]: #evententry
[2]: #prerequisite_event

**Description of the fields**

### eventEntry

This is the event that will start when all prerequisite events have been completed.

### prerequisite\_event

The is the event that must be completed before the next [event](#game_event_prerequisite-eventEntry) will start.
