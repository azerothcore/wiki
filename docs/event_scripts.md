[Database Structure](Database-Structure) > [World-Database](World-Database) > [event_scripts](event_scripts)

# event\_scripts

### Information

Holds scripts activated whenever an event is activated, be it by an object or as the spell effect SPELL\_EFFECT\_SEND\_EVENT (61).

### Structure

| Field                            | Type         | Attributes   | Key | Null | Default |
|----------------------------------|--------------|--------------|-----|------|---------|
| [id](scripts#id)                 | MEDIUMINT | UNSIGNED     |     | NO   | 0       |
| [delay](scripts#delay)           | INT      | UNSIGNED     |     | NO   | 0       |
| [command](scripts#command)       | MEDIUMINT | UNSIGNED     |     | NO   | 0       |
| [datalong](scripts#otherfields)  | MEDIUMINT | UNSIGNED     |     | NO   | 0       |
| [datalong2](scripts#otherfields) | INT      | UNSIGNED     |     | NO   | 0       |
| [dataint](scripts#otherfields)   | INT      |              |     | NO   | 0       |
| [x](scripts#otherfields)         | FLOAT        |              |     | NO   | 0       |
| [y](scripts#otherfields)         | FLOAT        |              |     | NO   | 0       |
| [z](scripts#otherfields)         | FLOAT        |              |     | NO   | 0       |
| [o](scripts#otherfields)         | FLOAT        |              |     | NO   | 0       |

