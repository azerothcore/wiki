# character\_achievement

[<-Back-to:Characters](database-characters)

**The \`character\_achievement\` table**

This table holds information on the achievements a character has earned/completed.

**Note:** if you delete a "realm first" achievement from the characters database, you have to reboot the server to take it into account.

**Table: character\_achievement's Structure**

| Field                       | Type     |          | Null | Key | Default | Extra | Comment |
| :-------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid)               | INT      | UNSIGNED | NO   | PRI |         |       |         |
| [achievement](#achievement) | SMALLINT | UNSIGNED | NO   | PRI |         |       |         |
| [date](#date)               | INT      | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### achievement

The ID of the achievement from [Achievement.dbc](achievement).

### date

The date/time when this achievement was earned, in Unix time. See [Unix timestamp Calculator](http://www.unixtimestamp.com/index.php)
