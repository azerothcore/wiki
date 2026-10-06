---
redirect_from: "/Holidays"
---

# Holidays

## holidays.dbc

[`Back-to:DBC`](dbc-index)

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)  

This DBC defines the holidays shown in the in-game calendar and when they take place. A [game\_event](game_event) is linked to a holiday with its `holiday` column.

## Structure

| Column | Field                | Type   | holidays\_dbc column                                      | Comment                                                                                                                                 |
| :----: | :------------------- | :----- | :-------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| 0      | ID                   | uint32 | [ID](holidays_dbc#id)                                     | [ID](#id): Holiday ID                                                                                                                   |
| 1      | Duration_0           | uint32 | [Duration_1](holidays_dbc#duration)                       | [Duration1-10](#duration1-10): Length of each stage in hours                                                                            |
| 2      | Duration_1           | uint32 | [Duration_2](holidays_dbc#duration)                       |                                                                                                                                         |
| 3      | Duration_2           | uint32 | [Duration_3](holidays_dbc#duration)                       |                                                                                                                                         |
| 4      | Duration_3           | uint32 | [Duration_4](holidays_dbc#duration)                       |                                                                                                                                         |
| 5      | Duration_4           | uint32 | [Duration_5](holidays_dbc#duration)                       |                                                                                                                                         |
| 6      | Duration_5           | uint32 | [Duration_6](holidays_dbc#duration)                       |                                                                                                                                         |
| 7      | Duration_6           | uint32 | [Duration_7](holidays_dbc#duration)                       |                                                                                                                                         |
| 8      | Duration_7           | uint32 | [Duration_8](holidays_dbc#duration)                       |                                                                                                                                         |
| 9      | Duration_8           | uint32 | [Duration_9](holidays_dbc#duration)                       |                                                                                                                                         |
| 10     | Duration_9           | uint32 | [Duration_10](holidays_dbc#duration)                      |                                                                                                                                         |
| 11     | Date_0               | uint32 | [Date_1](holidays_dbc#date)                               | [Date1-26](#date1-26): Packed start dates                                                                                               |
| 12     | Date_1               | uint32 | [Date_2](holidays_dbc#date)                               |                                                                                                                                         |
| 13     | Date_2               | uint32 | [Date_3](holidays_dbc#date)                               |                                                                                                                                         |
| 14     | Date_3               | uint32 | [Date_4](holidays_dbc#date)                               |                                                                                                                                         |
| 15     | Date_4               | uint32 | [Date_5](holidays_dbc#date)                               |                                                                                                                                         |
| 16     | Date_5               | uint32 | [Date_6](holidays_dbc#date)                               |                                                                                                                                         |
| 17     | Date_6               | uint32 | [Date_7](holidays_dbc#date)                               |                                                                                                                                         |
| 18     | Date_7               | uint32 | [Date_8](holidays_dbc#date)                               |                                                                                                                                         |
| 19     | Date_8               | uint32 | [Date_9](holidays_dbc#date)                               |                                                                                                                                         |
| 20     | Date_9               | uint32 | [Date_10](holidays_dbc#date)                              |                                                                                                                                         |
| 21     | Date_10              | uint32 | [Date_11](holidays_dbc#date)                              |                                                                                                                                         |
| 22     | Date_11              | uint32 | [Date_12](holidays_dbc#date)                              |                                                                                                                                         |
| 23     | Date_12              | uint32 | [Date_13](holidays_dbc#date)                              |                                                                                                                                         |
| 24     | Date_13              | uint32 | [Date_14](holidays_dbc#date)                              |                                                                                                                                         |
| 25     | Date_14              | uint32 | [Date_15](holidays_dbc#date)                              |                                                                                                                                         |
| 26     | Date_15              | uint32 | [Date_16](holidays_dbc#date)                              |                                                                                                                                         |
| 27     | Date_16              | uint32 | [Date_17](holidays_dbc#date)                              |                                                                                                                                         |
| 28     | Date_17              | uint32 | [Date_18](holidays_dbc#date)                              |                                                                                                                                         |
| 29     | Date_18              | uint32 | [Date_19](holidays_dbc#date)                              |                                                                                                                                         |
| 30     | Date_19              | uint32 | [Date_20](holidays_dbc#date)                              |                                                                                                                                         |
| 31     | Date_20              | uint32 | [Date_21](holidays_dbc#date)                              |                                                                                                                                         |
| 32     | Date_21              | uint32 | [Date_22](holidays_dbc#date)                              |                                                                                                                                         |
| 33     | Date_22              | uint32 | [Date_23](holidays_dbc#date)                              |                                                                                                                                         |
| 34     | Date_23              | uint32 | [Date_24](holidays_dbc#date)                              |                                                                                                                                         |
| 35     | Date_24              | uint32 | [Date_25](holidays_dbc#date)                              |                                                                                                                                         |
| 36     | Date_25              | uint32 | [Date_26](holidays_dbc#date)                              |                                                                                                                                         |
| 37     | Region               | uint32 | [Region](holidays_dbc#region)                             | [Region](#region): Region                                                                                                               |
| 38     | Looping              | uint32 | [Looping](holidays_dbc#looping)                           | [Looping](#looping): 1 if the holiday repeats back to back                                                                              |
| 39     | CalendarFlags_0      | uint32 | [CalendarFlags_1](holidays_dbc#calendarflags)             | [CalendarFlags1-10](#calendarflags1-10): Calendar flags for each stage                                                                  |
| 40     | CalendarFlags_1      | uint32 | [CalendarFlags_2](holidays_dbc#calendarflags)             |                                                                                                                                         |
| 41     | CalendarFlags_2      | uint32 | [CalendarFlags_3](holidays_dbc#calendarflags)             |                                                                                                                                         |
| 42     | CalendarFlags_3      | uint32 | [CalendarFlags_4](holidays_dbc#calendarflags)             |                                                                                                                                         |
| 43     | CalendarFlags_4      | uint32 | [CalendarFlags_5](holidays_dbc#calendarflags)             |                                                                                                                                         |
| 44     | CalendarFlags_5      | uint32 | [CalendarFlags_6](holidays_dbc#calendarflags)             |                                                                                                                                         |
| 45     | CalendarFlags_6      | uint32 | [CalendarFlags_7](holidays_dbc#calendarflags)             |                                                                                                                                         |
| 46     | CalendarFlags_7      | uint32 | [CalendarFlags_8](holidays_dbc#calendarflags)             |                                                                                                                                         |
| 47     | CalendarFlags_8      | uint32 | [CalendarFlags_9](holidays_dbc#calendarflags)             |                                                                                                                                         |
| 48     | CalendarFlags_9      | uint32 | [CalendarFlags_10](holidays_dbc#calendarflags)            |                                                                                                                                         |
| 49     | HolidayNameID        | uint32 | [HolidayNameID](holidays_dbc#holidaynameid)               | [HolidayNameID](#holidaynameid): Ref to HolidayNames.dbc. ID in [HolidayNames.dbc](dbc-holidaynames)                                    |
| 50     | HolidayDescriptionID | uint32 | [HolidayDescriptionID](holidays_dbc#holidaydescriptionid) | [HolidayDescriptionID](#holidaydescriptionid): Ref to HolidayDescriptions.dbc. ID in [HolidayDescriptions.dbc](dbc-holidaydescriptions) |
| 51     | TextureFilename      | string | [TextureFilename](holidays_dbc#texturefilename)           | [TextureFilename](#texturefilename): Calendar texture                                                                                   |
| 52     | Priority             | uint32 | [Priority](holidays_dbc#priority)                         | [Priority](#priority): Calendar priority                                                                                                |
| 53     | CalendarFilterType   | int32  | [CalendarFilterType](holidays_dbc#calendarfiltertype)     | [CalendarFilterType](#calendarfiltertype): Kind of holiday, see below                                                                   |
| 54     | Flags                | uint32 | [Flags](holidays_dbc#flags)                               | [Flags](#flags): Flags                                                                                                                  |

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
