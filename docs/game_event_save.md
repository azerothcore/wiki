# game\_event\_save

[<-Back-to:Characters](database-characters.md)

**The \`game\_event\_save\` table**

**Structure**

| Field           | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [eventEntry][1] | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [state][2]      | TINYINT | UNSIGNED   |     | NO   | 1       |       |         |
| [next_start][3] | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #evententry
[2]: #state
[3]: #next_start

**Description of the fields**

### eventEntry

`field-no-description|1`

### state

`field-no-description|2`

### next\_start

`field-no-description|3`