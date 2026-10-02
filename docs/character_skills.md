# character\_skills

[<-Back-to:Characters](database-characters)

**The \`character\_skills\` table**

This table holds a listing of all skill for each character.

**Table: character\_skills's Structure**

| Field      | Type     | Attributes | Key | Null | Default | Extra | Comment                  |
| ---------- | -------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]  | INT      | UNSIGNED   | PRI | NO   |         |       | Global Unique Identifier |
| [skill][2] | SMALLINT | UNSIGNED   | PRI | NO   |         |       |                          |
| [value][3] | SMALLINT | UNSIGNED   |     | NO   |         |       |                          |
| [max][4]   | SMALLINT | UNSIGNED   |     | NO   |         |       |                          |

[1]: #guid
[2]: #skill
[3]: #value
[4]: #max

**Description of the table's fields**

### guid

The character guid. See [characters.guid](characters#guid).

### skill

The skill a character own's. A listing of those can be found in here.

### value

The current skillrank(value) the character owns.

### max

The highest possible value for the given skill within a given rank.
