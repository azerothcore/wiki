# game\_event

**Table Structure**

This table holds definitions for all game events that are activated or deactivated automatically by the Game Event System in the core.

| Field             | Type         | Attributes | Key | Null | Default | Extra  | Comment                                                                                                                              |
|-------------------|--------------|------------|-----|------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------|
| [eventEntry][1]   | TINYINT(3)   | UNSIGNED   | PRI | NO   |         | Unique | Entry of the game event                                                                                                              |
| [start_time][2]   | TIMESTAMP    |            |     | YES  | NULL    |        | Absolute start date, the event will never start before                                                                               |
| [end_time][3]     | TIMESTAMP    |            |     | YES  | NULL    |        | Absolute end date, the event will never start after; if NULL it will be implicitly set to 2 years in the future on each server start |
| [occurrence][4]   | BIGINT(20)   | UNSIGNED   |     | NO   |         |        | Delay in minutes between occurrences of the event                                                                                    |
| [length][5]       | BIGINT(20)   | UNSIGNED   |     | NO   |         |        | Length in minutes of the event                                                                                                       |
| [holiday][6]      | MEDIUMINT(8) | UNSIGNED   |     | NO   |         |        | Client side holiday id (from dbc)                                                                                                    |
| [holidayStage][7] | TINYINT(3)   | UNSIGNED   |     | NO   |         |        |                                                                                                                                      |
| [description][8]  | VARCHAR(255) | SIGNED     |     | YES  | NULL    |        | Description of the event displayed in console                                                                                        |
| [world_event][9]  | TINYINT(3)   | UNSIGNED   |     | NO   |         |        | 0 if normal event, 1 if world event                                                                                                  |
| [announce][10]    | TINYINT(3)   | UNSIGNED   |     | YES  | 2       |        | 0 dont announce, 1 announce, 2 value from config                                                                                     |

[1]: #evententry
[2]: #start_time
[3]: #end_time
[4]: #occurrence
[5]: #length
[6]: #holiday
[7]: #holidaystage
[8]: #description
[9]: #world_event
[10]: #announce

**Field Descriptions**

### eventEntry

Entry of the event. Keep it as low as possible and prevent making holes in the list. Higher the max id is, the more memory will be used to store the event data.

### start\_time

Absolute start date of the event. The event will start occurring only if the local time at the server is after the one set here.

### end\_time

Absolute end date of the event. The event will stop occurring if the local time at the server is after the one set here.

### occurrence

Number of minutes between 2 occurrences of the event. (2880 = 2 days, 1440 = 1 day, etc)

### length

Number of minutes the event will last after the start of the occurrence. (2880 = 2 days, 1440 = 1 day, etc)
This value must be lower than occurrence one or the event will never stop.

### holiday

Holiday ID from  [Holidays DBC file](Holidays). This is sent to the client to update the calender.

### description

String containing the name of the event displayed in console each time it starts or stops.

### world\_event

This is a boolean field that determines if this game event is a world event or not. 0 = normal event, 1 = world event. For the world event to work, you need to at a minimum, populate game\_event\_condition and game\_event\_quest\_condition.

### announce
