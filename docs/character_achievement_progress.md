# character\_achievement\_progress

[<-Back-to:Characters](database-characters)

**The \`character\_achievement\_progress\` table**

**Table Structure**

| Field         | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]     | INT         | UNSIGNED   | PRI | NO   |         |       |         |
| [criteria][2] | SMALLINT    | UNSIGNED   | PRI | NO   |         |       |         |
| [counter][3]  | INT         | UNSIGNED   |     | NO   |         |       |         |
| [date][4]     | INT         | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #criteria
[3]: #counter
[4]: #date

**Description of the fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### criteria

Criteria from [Achievement\_Criteria.dbc](achievement_criteria).

### counter

`field-no-description|3`

### date

The date when this achievement was earned. See [Unix timestamp Calculator](http://www.unixtimestamp.com/index.php).
