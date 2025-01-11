# game_event

[<-Back-to:World](database-world)

**The \`game_event\` table**

**Table Structure**

This table holds definitions for all game events that are activated or deactivated automatically by the Game Event System in the core.

| Field                        | Type         | Attributes | Key | Null | Default | Extra  | Comment                                                                                                                              |
| ---------------------------- | ------------ | ---------- | --- | ---- | ------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| [eventEntry](#evententry)    | TINYINT      | UNSIGNED   | PRI | NO   |         | Unique | Entry of the game event                                                                                                              |
| [start_time](#starttime)     | TIMESTAMP    |            |     | YES  | NULL    |        | Absolute start date, the event will never start before                                                                               |
| [end_time](#endtime)         | TIMESTAMP    |            |     | YES  | NULL    |        | Absolute end date, the event will never start after; if NULL it will be implicitly set to 2 years in the future on each server start |
| [occurrence](#occurrence)    | BIGINT       | UNSIGNED   |     | NO   |         |        | Delay in minutes between occurrences of the event                                                                                    |
| [length](#length)            | BIGINT       | UNSIGNED   |     | NO   |         |        | Length in minutes of the event                                                                                                       |
| [holiday](#holiday)          | MEDIUMINT    | UNSIGNED   |     | NO   |         |        | Client side holiday id (from dbc)                                                                                                    |
| [holidayStage](holidaystage) | TINYINT      | UNSIGNED   |     | NO   |         |        |                                                                                                                                      |
| [description](#description)  | VARCHAR(255) | SIGNED     |     | YES  | NULL    |        | Description of the event displayed in console                                                                                        |
| [world_event](#worldevent)   | TINYINT      | UNSIGNED   |     | NO   |         |        | 0 if normal event, 1 if world event                                                                                                  |
| [announce](#announce)        | TINYINT      | UNSIGNED   |     | YES  | 2       |        | 0 dont announce, 1 announce, 2 value from config                                                                                     |

**Field Descriptions**

### eventEntry

Entry of the event. Keep it as low as possible and prevent making holes in the list. Higher the max id is, the more memory will be used to store the event data.

### start_time

Absolute start date of the event. The event will start occurring only if the local time at the server is after the one set here.

### end_time

Absolute end date of the event. The event will stop occurring if the local time at the server is after the one set here.

### occurrence

Number of minutes between 2 occurrences of the event. (2880 = 2 days, 1440 = 1 day, etc)

{% include warning.html content="Value can't be 0 or the server will crash." %}

### length

Number of minutes the event will last after the start of the occurrence. (2880 = 2 days, 1440 = 1 day, etc)
This value must be lower than occurrence one or the event will never stop.


### holiday

Holiday ID from  [Holidays DBC file](holidays). This is sent to the client to update the calender.

### description

String containing the name of the event displayed in console each time it starts or stops.

### world_event

This is a boolean field that determines if this game event is a world event or not. 0 = normal event, 1 = world event. For the world event to work, you need to at a minimum, populate [game_event_condition](game_event_condition) and [game_event_quest_condition](game_event_quest_condition).

### announce

| Value | Description                                        |
| ----- | -------------------------------------------------- |
| 0     | Don't announce the Event                           |
| 1     | Announce the description of the Event to the world |
| 2     | Use the `event.announce` settings from the config  |

