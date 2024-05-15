---
redirect_from: "/Holidays"
---

# Holidays

## holidays.dbc

[`Back-to:DBC`](dbc-index.md)

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db.md)  

## Structure

| Column | Field                         | Type    | Notes                                                                              | Extra info                                                                 |
|--------|-------------------------------|---------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| 0      | [eventID][1]                  | Integer | Holiday event ID                                                                   |                                                                            |
| 1      | [eventStage1Duration][2]      | Integer | Stage1 event length (for stage1                                                    | either as preparation or main event. See eventSchedulerType for more info) |
| 2      | [eventStage2Duration][3]      | Integer | Stage2 event length (for stage2                                                    | either as main event or cooldown. See eventSchedulerType for more info)    |
| 11     | [eventDate][4]                | Integer | Packed blizzdate - Epochdate=01.01.2000-00:00 - Year is discarded if column12 is 0 |                                                                            |
| 37     | [Region][5]                   | integer | ??? (needs more research)                                                          |                                                                            |
| 38     | [Looping][6]                  | integer | ??? (needs more research - used only on Call To Arms events)                       | 283 - Call to Arms: Alterac Valley                                         |
|        |                               |         |                                                                                    | 284 - Call to Arms: Warsong Gulch                                          |
|        |                               |         |                                                                                    | 285 - Call to Arms: Arathi Basin                                           |
|        |                               |         |                                                                                    | 353 - Call to Arms: Eye of the Storm                                       |
|        |                               |         |                                                                                    | 400 - Call to Arms: Strand of the Ancient                                  |
|        |                               |         |                                                                                    | 420 - Call to Arms: Isle of Conquest                                       |
| 39     | [calendarFlags][7]            | integer | ??? (needs more research)                                                          |                                                                            |
| 49     | [eventCalendarName][8]        | iRefID  | Ref to Loc in HolidayNames.dbc                                                     |                                                                            |
| 50     | [eventCalendarDescription][9] | iRefID  | Ref to Loc in HolidayDescriptions.dbc                                              |                                                                            |
| 51     | [eventCalendarOverlay][10]    | String  | Overlay texture used for ingame calendar event-decorations                         |                                                                            |
| 52     | [priority][11]                | Integer | ??? (needs more research)                                                          |                                                                            |
| 53     | [eventSchedulerType][12]      | Integer | Definition of which timer is used, see eventSchedulerType below                    | -1: repeat, yearly                                                         |
|        |                               |         |                                                                                    | 0: repeat, weekly                                                          |
|        |                               |         |                                                                                    | 1: repeat, use defined dates                                               |
|        |                               |         |                                                                                    | 2: repeat, hourly                                                          |
| 54     | [eventFlags][13]              | Integer | ??? (needs more research)                                                          |                                                                            |

[1]: #eventid
[2]: #eventstage1duration
[3]: #eventstage2duration
[4]: #eventdate
[5]: #region
[6]: #looping
[7]: #calendarflags
[8]: #eventcalendarname
[9]: #eventcalendardescription
[10]: #eventcalendaroverlay
[11]: #priority
[12]: #eventschedulertype
[13]: #eventflags

### eventID

### eventStage1Duration

### eventStage2Duration

### eventDate

### Region

### Looping

### calendarFlags

### eventCalendarName

### eventCalendarDescription

### eventCalendarOverlay

### priority

## eventSchedulerType
```
eventSchedulerType defines what kind of timer is used for when the event is to stop, start etc. - and if it uses different stages during it's "buildup"-phase (2 stages available)
-1: event repeats every year based on column11, column12 etc dates - length and possible event stages is taken from the information given in column1 and column2 (adjusted in DBC to keep it in line with **yearly** changes) - if column12=0, use DATE only from field11
0: event repeats every 7 days, with a duration of <eventStage1Duration> hours (hardcoded startdate serverside depending on eventID)
1: event repeats based on column11, column12 etc values (see -1) - if <eventStage2Duration> exists, use <eventStage1Duration> as event prestage length
2: event repeats every X hours (with <eventStage2Duration> being the eventPause/eventWait timer)
```

### eventFlags
