---
redirect_from: "/Holidays"
---

# Holidays

## holidays.dbc

[`Back-to:DBC`](dbc-index)

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)  

This DBC defines the holidays shown in the in-game calendar and when they take place. A [game\_event](game_event) is linked to a holiday with its `holiday` column.

## Structure

| Column | Field                                                  | Type    | Notes                                                 |
| ------ | ------------------------------------------------------ | ------- | ----------------------------------------------------- |
| 0      | [ID](#id)                                              | Integer | Holiday ID                                            |
| 1-10   | [Duration1-10](#duration1-10)                          | Integer | Length of each stage in hours                         |
| 11-36  | [Date1-26](#date1-26)                                  | Integer | Packed start dates                                    |
| 37     | [Region](#region)                                      | Integer | Region                                                |
| 38     | [Looping](#looping)                                    | Integer | 1 if the holiday repeats back to back                 |
| 39-48  | [CalendarFlags1-10](#calendarflags1-10)                | Integer | Calendar flags for each stage                         |
| 49     | [HolidayNameID](#holidaynameid)                        | Integer | Ref to HolidayNames.dbc                               |
| 50     | [HolidayDescriptionID](#holidaydescriptionid)          | Integer | Ref to HolidayDescriptions.dbc                        |
| 51     | [TextureFilename](#texturefilename)                    | String  | Calendar texture                                      |
| 52     | [Priority](#priority)                                  | Integer | Calendar priority                                     |
| 53     | [CalendarFilterType](#calendarfiltertype)              | Integer | Kind of holiday, see below                            |
| 54     | [Flags](#flags)                                        | Integer | Flags                                                 |

### ID

The holiday ID. This is the value used in [game\_event.holiday](game_event#holiday) and [item\_template.HolidayId](item_template#holidayid).

### Duration1-10

The length in hours of each stage of the holiday. Most holidays only use the first stage. Holidays with more than one stage, like the Call to Arms battleground weekends, use one duration per stage.

A game event picks which stage it is with the `holidayStage` column of [game\_event](game_event). The stage starts after all the stages before it have ended.

### Date1-26

The start dates of the holiday, packed into one integer:

| Bits  | Value                                           |
| ----- | ----------------------------------------------- |
| 0-5   | Minute                                          |
| 6-10  | Hour                                            |
| 11-13 | Day of the week                                 |
| 14-19 | Day of the month, starting at 0                 |
| 20-23 | Month, starting at 0                            |
| 24-28 | Year, counted from 2000. 31 means every year    |

The dates in the DBC only cover the years around the release of the client. For the main holidays, the core calculates the dates of the current and upcoming years when the server starts. A `start_time` in the current year or later in [game\_event](game_event) overrides the calculated date. See [Dynamic Holiday System](game_event#dynamic-holiday-system).

### Region

The World of Warcraft region the holiday is for. It is sent to the client with the calendar data.

### Looping

1 if the holiday repeats back to back, with no pause between the end of the last stage and the start of the first one. Used by the Call to Arms battleground weekends:

| ID  | Holiday                                  |
| --- | ---------------------------------------- |
| 283 | Call to Arms: Alterac Valley             |
| 284 | Call to Arms: Warsong Gulch              |
| 285 | Call to Arms: Arathi Basin               |
| 353 | Call to Arms: Eye of the Storm           |
| 400 | Call to Arms: Strand of the Ancients     |
| 420 | Call to Arms: Isle of Conquest           |

The core repeats a looping holiday every time the sum of all its stage durations has passed, starting from the first date.

### CalendarFlags1-10

Flags for each stage of the holiday. They are sent to the client with the calendar data and are not used by the core.

### HolidayNameID

ID of the holiday's name in HolidayNames.dbc. Not loaded by the core.

### HolidayDescriptionID

ID of the holiday's description in HolidayDescriptions.dbc. Not loaded by the core.

### TextureFilename

Name of the texture the in-game calendar shows on the days of the holiday.

### Priority

Sent to the client with the calendar data.

### CalendarFilterType

The core uses it to set how often the linked game event repeats.

| Value | Effect                                                                                  |
| ----- | --------------------------------------------------------------------------------------- |
| -1    | The event repeats every year.                                                           |
| 0     | The event repeats every 7 days.                                                         |
| 1     | The event only takes place on the defined dates. Used by the Darkmoon Faire.            |
| 2     | No repeat interval is set from this value. Looping holidays use [Looping](#looping).    |

### Flags

0 for the Darkmoon Faire, the Fishing Contest and the Wrath of the Lich King launch event, 1 for all other holidays. Not loaded by the core.
