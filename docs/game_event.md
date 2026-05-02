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

{% include note.html content="For events linked to holidays with dynamic date calculation (Easter, Lunar New Year, Thanksgiving, etc.), start_time is automatically computed on server startup and overrides any value set in the database. See the Dynamic Holiday System section below." %}

### end_time

Absolute end date of the event. The event will stop occurring if the local time at the server is after the one set here.

{% include note.html content="For events linked to holidays with dynamic date calculation, end_time is automatically computed based on the event length and start_time." %}

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

## Dynamic Holiday System

Some holidays occur on dates that vary from year to year. For these holidays, the server automatically calculates the correct dates on startup using astronomical algorithms and calendar rules.

### Dynamically Calculated Holidays

| Holiday ID | Holiday Name | Calculation Method |
| ---------- | ------------ | ------------------ |
| 141 | Feast of Winter Veil | 6 days before winter solstice (Dec 15-16) |
| 181 | Noblegarden | Day after Easter Sunday |
| 201 | Children's Week | First Monday on or after April 25 |
| 283 | Harvest Festival | 2 days before autumn equinox |
| 301 | Hallow's End | Fixed Oct 18 |
| 321 | Lunar Festival | Day before Chinese New Year (astronomical lunar calculation) |
| 324 | Midsummer Fire Festival | Fixed Jun 21 |
| 327 | Brewfest | First Saturday on or after Sept 15, minus 7 days |
| 335 | Love is in the Air | First Monday on or after Feb 3 |
| 341 | Day of the Dead | Fixed Nov 1 |
| 372 | Pilgrim's Bounty | 4th Thursday of November minus 4 days |
| 374 | Darkmoon Faire (Elwynn) | First Sunday of Mar/Jun/Sep/Dec minus 2 days |
| 375 | Darkmoon Faire (Mulgore) | First Sunday of Jan/Apr/Jul/Oct minus 2 days |
| 376 | Darkmoon Faire (Terokkar) | First Sunday of Feb/May/Aug/Nov minus 2 days |

### How It Works

1. On server startup, `GameEventMgr::LoadHolidayDates()` iterates through all holiday rules
2. For each holiday, dates are calculated for multiple years (current year ± several years)
3. The calculated dates are written to the `Holidays.dbc` Date[] array for calendar display
4. The corresponding game_event's `start_time` and `end_time` are updated to match the next occurrence
5. Events automatically re-schedule after each occurrence completes

### Notes

- The `holiday_dates` database table has been **removed** - all dates are now calculated dynamically
- Calendar dates are populated for ~4 years to ensure the in-game calendar displays correctly
- Darkmoon Faire has multiple occurrences per year, rotating monthly between Mulgore (Jan), Terokkar (Feb), Elwynn (Mar), and repeating

