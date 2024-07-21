# pet\_spell

[<-Back-to:Characters](database-characters)

**The \`pet\_spell\` table**

This table holds information on individual pet spells.

**Table Structure**

| Field       | Type      | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]   | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [spell][2]  | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Spell Identifier         |
| [active][3] | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #spell
[3]: #active

**Description of the fields**

### guid

The pet GUID. See [character\_pet.id](character_pet#id).

### spell

The spell ID. See [Spell.dbc](spell) column 1.

### active

Boolean 0 or 1 controlling if the spell is active or not.
