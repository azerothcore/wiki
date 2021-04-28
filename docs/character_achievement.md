# character\_achievement

[<-Back-to:Characters](database-characters.md)

**The \`character\_achievement\` table**

This table holds information on the achievements a character has earned / completed.

**Note:** if you delete a "realm first" achievement from the characters database, you have to reboot the server to take it into account.

**Structure**

| Field            | Type        | Attributes | Key | Null | Default | Extra | Comment |
|------------------|-------------|------------|-----|------|---------|-------|---------|
| [guid][1]        | INT(10)     | UNSIGNED   | PRI | NO   |         |       |         |
| [achievement][2] | SMALLINT(5) | UNSIGNED   | PRI | NO   |         |       |         |
| [date][3]        | INT(10)     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #achievement
[3]: #date

**Description of the fields**

### guid

The GUID of the character. See [characters.guid](characters_table_)

### achievement

The ID of the achievement from [Achievement.dbc](Achievement).

### date

The date/time when this achievement was earned, in Unix time. See [Unix TIMESTAMP Calculator](http://www.unixTIMESTAMP.com/index.php)
