# character\_achievement\_progress

[<-Back-to:Characters](database-characters.md)

**The \`character\_achievement\_progress\` table**

`table-no-description`

**Structure**

| Field         | Type        | Attributes | Key | Null | Default | Extra | Comment |
|---------------|-------------|------------|-----|------|---------|-------|---------|
| [guid][1]     | int(10)     | unsigned   | PRI | NO   |         |       |         |
| [criteria][2] | smallint(5) | unsigned   | PRI | NO   |         |       |         |
| [counter][3]  | int(10)     | unsigned   |     | NO   |         |       |         |
| [date][4]     | int(10)     | unsigned   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #criteria
[3]: #counter
[4]: #date

**Description of the fields**

### guid

The GUID of the character. See characters.guid

### criteria

Criteria from [Achievement\_Criteria.dbc](Achievement_Criteria)

### counter

`field-no-description|3`

### date

The date when this achievement was earned. See [Unix TIMESTAMP Calculator](http://www.unixTIMESTAMP.com/index.php)
