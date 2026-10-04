# holidays\_dbc

[<-Back-to:World](database-world)

**The \`holidays\_dbc\` table**

This table has the same columns as the client file `Holidays.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: holidays\_dbc's Structure**

| Field                                         | Type         |     | Null | Key | Default | Extra | Comment |
| :-------------------------------------------- | :----------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                     | INT          |     | NO   | PRI | 0       |       |         |
| [Duration_1](#duration)                       | INT          |     | NO   |     | 0       |       |         |
| [Duration_2](#duration)                       | INT          |     | NO   |     | 0       |       |         |
| [Duration_3](#duration)                       | INT          |     | NO   |     | 0       |       |         |
| [Duration_4](#duration)                       | INT          |     | NO   |     | 0       |       |         |
| [Duration_5](#duration)                       | INT          |     | NO   |     | 0       |       |         |
| [Duration_6](#duration)                       | INT          |     | NO   |     | 0       |       |         |
| [Duration_7](#duration)                       | INT          |     | NO   |     | 0       |       |         |
| [Duration_8](#duration)                       | INT          |     | NO   |     | 0       |       |         |
| [Duration_9](#duration)                       | INT          |     | NO   |     | 0       |       |         |
| [Duration_10](#duration)                      | INT          |     | NO   |     | 0       |       |         |
| [Date_1](#date)                               | INT          |     | NO   |     | 0       |       |         |
| [Date_2](#date)                               | INT          |     | NO   |     | 0       |       |         |
| [Date_3](#date)                               | INT          |     | NO   |     | 0       |       |         |
| [Date_4](#date)                               | INT          |     | NO   |     | 0       |       |         |
| [Date_5](#date)                               | INT          |     | NO   |     | 0       |       |         |
| [Date_6](#date)                               | INT          |     | NO   |     | 0       |       |         |
| [Date_7](#date)                               | INT          |     | NO   |     | 0       |       |         |
| [Date_8](#date)                               | INT          |     | NO   |     | 0       |       |         |
| [Date_9](#date)                               | INT          |     | NO   |     | 0       |       |         |
| [Date_10](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_11](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_12](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_13](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_14](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_15](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_16](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_17](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_18](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_19](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_20](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_21](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_22](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_23](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_24](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_25](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Date_26](#date)                              | INT          |     | NO   |     | 0       |       |         |
| [Region](#region)                             | INT          |     | NO   |     | 0       |       |         |
| [Looping](#looping)                           | INT          |     | NO   |     | 0       |       |         |
| [CalendarFlags_1](#calendarflags)             | INT          |     | NO   |     | 0       |       |         |
| [CalendarFlags_2](#calendarflags)             | INT          |     | NO   |     | 0       |       |         |
| [CalendarFlags_3](#calendarflags)             | INT          |     | NO   |     | 0       |       |         |
| [CalendarFlags_4](#calendarflags)             | INT          |     | NO   |     | 0       |       |         |
| [CalendarFlags_5](#calendarflags)             | INT          |     | NO   |     | 0       |       |         |
| [CalendarFlags_6](#calendarflags)             | INT          |     | NO   |     | 0       |       |         |
| [CalendarFlags_7](#calendarflags)             | INT          |     | NO   |     | 0       |       |         |
| [CalendarFlags_8](#calendarflags)             | INT          |     | NO   |     | 0       |       |         |
| [CalendarFlags_9](#calendarflags)             | INT          |     | NO   |     | 0       |       |         |
| [CalendarFlags_10](#calendarflags)            | INT          |     | NO   |     | 0       |       |         |
| [HolidayNameID](#holidaynameid)               | INT          |     | NO   |     | 0       |       |         |
| [HolidayDescriptionID](#holidaydescriptionid) | INT          |     | NO   |     | 0       |       |         |
| [TextureFilename](#texturefilename)           | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Priority](#priority)                         | INT          |     | NO   |     | 0       |       |         |
| [CalendarFilterType](#calendarfiltertype)     | INT          |     | NO   |     | 0       |       |         |
| [Flags](#flags)                               | INT          |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `HolidaysEntry::Id`.

### Duration

The core reads these columns into `HolidaysEntry::Duration`.

### Date

The core reads these columns into `HolidaysEntry::Date`.

Comment in the core source: "(dates in unix time starting at January, 1, 2000)"

### Region

The core reads this column into `HolidaysEntry::Region`.

Comment in the core source: "(wow region)"

### Looping

The core reads this column into `HolidaysEntry::Looping`.

### CalendarFlags

The core reads these columns into `HolidaysEntry::CalendarFlags`.

### HolidayNameID

Not used by the core.

### HolidayDescriptionID

Not used by the core.

### TextureFilename

The core reads this column into `HolidaysEntry::TextureFilename`.

### Priority

The core reads this column into `HolidaysEntry::Priority`.

### CalendarFilterType

The core reads this column into `HolidaysEntry::CalendarFilterType`.

Comment in the core source: "(-1 = Fishing Contest, 0 = Unk, 1 = Darkmoon Festival, 2 = Yearly holiday)"

### Flags

Not used by the core.

Comment in the core source: "(0 = Darkmoon Faire, Fishing Contest and Wotlk Launch, rest is 1)"
