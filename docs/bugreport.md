# bugreport

[<-Back-to:Characters](database-characters)

**The \`bugreport\` table**

Stores the bug reports and suggestions that players submit in game, together with a state, an assignee and a comment for following them up.

**Table: bugreport's Structure**

| Field                 | Type         |          | Null | Key | Default | Extra          | Comment    |
| :-------------------- | :----------- | :------- | :--: | :-: | :-----: | :------------: | :--------- |
| [id](#id)             | INT          | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT | Identifier |
| [type](#type)         | LONGTEXT     |          | NO   |     |         |                |            |
| [content](#content)   | LONGTEXT     |          | NO   |     |         |                |            |
| [State](#state)       | TINYINT      |          | NO   |     | 1       |                |            |
| [Assignee](#assignee) | VARCHAR(255) |          | YES  |     | NULL    |                |            |
| [Comment](#comment)   | LONGTEXT     |          | YES  |     | NULL    |                |            |

**Description of the table's fields**

### id

The unique ID of the report.

### type

The type the player chose in the client, for example a bug or a suggestion.

### content

The text of the report.

### State

State of the report, for tracking it. Not used by the core, 1 for new reports.

### Assignee

Name of the person working on the report. Not used by the core.

### Comment

A comment on the report. Not used by the core.
