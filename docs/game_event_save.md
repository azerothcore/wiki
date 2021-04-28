# game\_event\_save

[<-Back-to:Characters](database-characters.md)

**The \`game\_event\_save\` table**

`table-no-description`

**Structure**

| Field           | Type         | Attributes | Key | Null | Default | Extra | Comment |
|-----------------|--------------|------------|-----|------|---------|-------|---------|
| [event_id][1]   | MEDIUMINT(8) | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [state][2]      | TINYINT(3)   | UNSIGNED   |     | NO   | 1       |       |         |
| [next_start][3] | BIGINT(11)   | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #event_id
[2]: #state
[3]: #next_start

**Description of the fields**

### event\_id

`field-no-description|1`

### state

`field-no-description|2`

### next\_start

`field-no-description|3`
