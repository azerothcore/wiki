# game\_event\_condition\_save

[<-Back-to:Characters](database-characters.md)

**The \`game\_event\_condition\_save\` table**

`table-no-description`

**Structure**

| Field             | Type       | Attributes | Key | Null | Default | Extra | Comment |
|-------------------|------------|------------|-----|------|---------|-------|---------|
| [eventEntry][1]   | tinyint(3) | unsigned   | PRI | NO   |         |       |         |
| [condition_id][2] | int(10)    | unsigned   | PRI | NO   | 0       |       |         |
| [done][3]         | float      | signed     |     | YES  | 0       |       |         |

[1]: #evententry
[2]: #condition_id
[3]: #done

**Description of the fields**

### eventEntry

This is a link to the event entry in the game\_event table.

### condition\_id

See game\_event\_condition.condition\_id

### done

Indicates how much has been done. See game\_event\_condition.req\_num
