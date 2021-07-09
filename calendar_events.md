# calendar\_events

[<-Back-to:Characters](database-characters.md)

**The \`calendar\_events\` table**

**Structure**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment  |
|----------------- |------------- |------------|-----|------|---------|-------|--------- |
| [id][1]          | BIGINT       | UNSIGNED   | PRI | NO   | 0       |       |          |
| [creator][2]     | INT          | UNSIGNED   |     | NO   | 0       |       |          |
| [title][4]       | VARCHAR(255) |            |     | NO   | ''      |       |          |
| [description][5] | VARCHAR(255) |            |     | NO   | ''      |       |          |
| [type][6]        | TINYINT      | UNSIGNED   |     | NO   | 4       |       |          |
| [dungeon][7]     | INT          |            |     | NO   | -1      |       |          |
| [eventtime][8]   | INT          | UNSIGNED   |     | NO   | 0       |       |          |
| [flags][9]       | INT          | UNSIGNED   |     | NO   | 0       |       |          |
| [time2][10]      | INT          | UNSIGNED   |     | NO   | 0       |       |          |

[1]: #id
[2]: #type
[3]: #creator
[4]: #title
[5]: #description
[6]: #type
[7]: #dungeon
[8]: #eventtime
[9]: #flags
[10]: #time2

**Description of the fields**

### id

`field-no-description|1`

### type

`field-no-description|2`

### creator

`field-no-description|3`

### title

`field-no-description|4`

### description

`field-no-description|5`

### type

`field-no-description|6`

### dungeon

`field-no-description|7`

### eventtime

`field-no-description|8`

### flags

`field-no-description|9`

### time2

`field-no-description|10`

