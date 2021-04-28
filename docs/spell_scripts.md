[Database Structure](Database-Structure) > [World-Database](World-Database) > [spell_scripts](spell_scripts)

# spell\_scripts

### Information

Holds scripts that can be activated by spells with effect SPELL\_EFFECT\_SCRIPT\_EFFECT (77) or SPELL\_EFFECT\_DUMMY(3).

### Structure

| Field                            | Type         | Attributes   | Key | Null | Default |
|----------------------------------|--------------|--------------|-----|------|---------|
| [id](scripts#id)                 | MEDIUMINT | UNSIGNED     |     | NO   | 0       |
| [effIndex](scripts#effindex)     | TINYINT   | UNSIGNED     |     | NO   | 0       |
| [delay](scripts#delay)           | INT      | UNSIGNED     |     | NO   | 0       |
| [command](scripts#command)       | MEDIUMINT | UNSIGNED     |     | NO   | 0       |
| [datalong](scripts#otherfields)  | MEDIUMINT | UNSIGNED     |     | NO   | 0       |
| [datalong2](scripts#otherfields) | INT      | UNSIGNED     |     | NO   | 0       |
| [dataint](scripts#otherfields)   | INT      |              |     | NO   | 0       |
| [x](scripts#otherfields)         | FLOAT        |              |     | NO   | 0       |
| [y](scripts#otherfields)         | FLOAT        |              |     | NO   | 0       |
| [z](scripts#otherfields)         | FLOAT        |              |     | NO   | 0       |
| [o](scripts#otherfields)         | FLOAT        |              |     | NO   | 0       |

