# character\_skills

[<-Back-to:Characters](database-characters)

**The \`character\_skills\` table**

This table holds a listing of all skill for each character.

**Table: character\_skills's Structure**

| Field           | Type     |          | Null | Key | Default | Extra | Comment                  |
| :-------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)   | INT      | UNSIGNED | NO   | PRI |         |       | Global Unique Identifier |
| [skill](#skill) | SMALLINT | UNSIGNED | NO   | PRI |         |       |                          |
| [value](#value) | SMALLINT | UNSIGNED | NO   |     |         |       |                          |
| [max](#max)     | SMALLINT | UNSIGNED | NO   |     |         |       |                          |

**Description of the table's fields**

### guid

The character guid. See [characters.guid](characters#guid).

### skill

The skill a character own's. A listing of those can be found in here.

### value

The current skillrank(value) the character owns.

### max

The highest possible value for the given skill within a given rank.
