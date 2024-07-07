# log\_arena\_fights

[<-Back-to:Characters](database-characters)

**The \`log\_arena\_fights\` table**

**Table Structure**

| Field                 | Type     | Attributes | Key | Null | Default | Extra | Comment |
| --------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [fight_id][1]         | INT      | UNSIGNED   | PRI | NO   |         |       |         |
| [time][2]             | DATETIME | SIGNED     |     | NO   |         |       |         |
| [type][3]             | TINYINT  | UNSIGNED   |     | NO   |         |       |         |
| [duration][4]         | INT      | UNSIGNED   |     | NO   |         |       |         |
| [winner][5]           | INT      | UNSIGNED   |     | NO   |         |       |         |
| [loser][6]            | INT      | UNSIGNED   |     | NO   |         |       |         |
| [winner_tr][7]        | SMALLINT | UNSIGNED   |     | NO   |         |       |         |
| [winner_mmr][8]       | SMALLINT | UNSIGNED   |     | NO   |         |       |         |
| [winner_tr_change][9] | SMALLINT | SIGNED     |     | NO   |         |       |         |
| [loser_tr][10]        | SMALLINT | UNSIGNED   |     | NO   |         |       |         |
| [loser_mmr][11]       | SMALLINT | UNSIGNED   |     | NO   |         |       |         |
| [loser_tr_change][12] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [currOnline][13]      | INT      | SIGNED     |     | NO   | 0       |       |         |

[1]: #fightid
[2]: #time
[3]: #type
[4]: #duration
[5]: #winner
[6]: #loser
[7]: #winnertr
[8]: #winnermmr
[9]: #winnertrchange
[10]: #losertr
[11]: #losermmr
[12]: #losertrchange
[13]: #curronline

**Description of the fields**

### fight\_id

`field-no-description|1`

### time

`field-no-description|2`

### type

`field-no-description|3`

### duration

`field-no-description|4`

### winner

`field-no-description|5`

### loser

`field-no-description|6`

### winner\_tr

`field-no-description|7`

### winner\_mmr

`field-no-description|8`

### winner\_tr\_change

`field-no-description|9`

### loser\_tr

`field-no-description|10`

### loser\_mmr

`field-no-description|11`

### loser\_tr\_change

`field-no-description|12`

### curronline

`field-no-description|13`
