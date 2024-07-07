# character\_skills

[<-Back-to:Characters](database-characters)

**The \`character\_skills\` table**

This table holds a listing of all skill for each character.

**Table Structure**

| Field      | Type     | Attributes | Key | Null | Default | Extra | Comment                  |
| ---------- | -------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]  | INT      | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [skill][2] | SMALLINT | UNSIGNED   | PRI | NO   | 0       |       |                          |
| [value][3] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [max][4]   | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #skill
[3]: #value
[4]: #max

**Description of the fields**

### guid

The character guid. See [characters.guid](characters#guid).

### skill

The skill a character own's. A listing of those can be found in here.

### value

The current skillrank(value) the character owns.

### max

The highest possible value for the given skill within a given rank.
