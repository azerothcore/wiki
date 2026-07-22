# holiday_dates

[<-Back-to:World](database-world)

**The `holiday_dates` table**

Stores calculated start dates and durations for in-game holidays referenced by the event system. Rows are keyed by holiday `id` and a `date_id` index into that holiday's list of occurrences.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id](#id) | INT | UNSIGNED | PRI | NO |  |  |  |
| [date_id](#date_id) | TINYINT | UNSIGNED | PRI | NO |  |  |  |
| [date_value](#date_value) | INT | UNSIGNED |  | NO |  |  |  |
| [holiday_duration](#holiday_duration) | INT | UNSIGNED |  | NO | 0 |  |  |

**Description of the fields**

### id

Holiday identifier (matches the holiday referenced by `game_event`).

### date_id

Index of this date within the holiday's set of occurrences.

### date_value

Packed date/time value for this occurrence.

### holiday_duration

Duration of the holiday, in the game's holiday time units.
