# calendar\_events

[<-Back-to:Characters](database-characters)

**The \`calendar\_events\` table**

**Table: calendar\_events's Structure**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment  |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | -------- |
| [id][1]          | BIGINT       | UNSIGNED   | PRI | NO   | 0       |       |          |
| [creator][2]     | INT          | UNSIGNED   |     | NO   | 0       |       |          |
| [title][3]       | VARCHAR(255) | SIGNED     |     | NO   | ''      |       |          |
| [description][4] | VARCHAR(255) | SIGNED     |     | NO   | ''      |       |          |
| [type][5]        | TINYINT      | UNSIGNED   |     | NO   | 4       |       |          |
| [dungeon][6]     | INT          | SIGNED     |     | NO   | -1      |       |          |
| [eventtime][7]   | INT          | UNSIGNED   |     | NO   | 0       |       |          |
| [flags][8]       | INT          | UNSIGNED   |     | NO   | 0       |       |          |
| [time2][9]       | INT          | UNSIGNED   |     | NO   | 0       |       |          |

[1]: #id
[3]: #creator
[4]: #title
[5]: #description
[6]: #type
[7]: #dungeon
[8]: #eventtime
[9]: #flags
[10]: #time2

**Description of the table's fields**

### id

The unique ID of the event.

### creator

GUID of the character that created the event. See [characters.guid](characters#guid).

### title

The title of the event.

### description

The description of the event.

### type

| Value | Type    |
| ----- | ------- |
| 0     | Raid    |
| 1     | Dungeon |
| 2     | PvP     |
| 3     | Meeting |
| 4     | Other   |

### dungeon

ID from LFGDungeons.dbc of the dungeon or raid the event is for. -1 if none.

### eventtime

The time the event starts, in Unix time.

### flags

| Flag  | Name                          | Description                                           |
| ----- | ----------------------------- | ----------------------------------------------------- |
| 1     | CALENDAR_FLAG_ALL_ALLOWED     |                                                       |
| 16    | CALENDAR_FLAG_INVITES_LOCKED  | Invites can not be changed.                           |
| 64    | CALENDAR_FLAG_WITHOUT_INVITES | Guild announcement without invites.                   |
| 1024  | CALENDAR_FLAG_GUILD_EVENT     | Guild event, all members of the guild can sign up.    |

### time2

The start time in the time zone of the creator, in Unix time.
