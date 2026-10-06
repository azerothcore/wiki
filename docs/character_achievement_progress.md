# character\_achievement\_progress

[<-Back-to:Characters](database-characters)

**The \`character\_achievement\_progress\` table**

Holds each character's progress on achievement criteria.

**Table: character\_achievement\_progress's Structure**

| Field                 | Type     |          | Null | Key | Default | Extra | Comment |
| :-------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid)         | INT      | UNSIGNED | NO   | PRI |         |       |         |
| [criteria](#criteria) | SMALLINT | UNSIGNED | NO   | PRI |         |       |         |
| [counter](#counter)   | INT      | UNSIGNED | NO   |     |         |       |         |
| [date](#date)         | INT      | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### criteria

Criteria from [Achievement\_Criteria.dbc](achievement_criteria).

### counter

The current progress count towards completing the achievement criteria.

### date

The date when this achievement was earned. See [Unix timestamp Calculator](http://www.unixtimestamp.com/index.php).
