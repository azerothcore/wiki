# character\_spell

[<-Back-to:Characters](database-characters.md)

**The \`character\_spell\` table**

Holds information for each character's spells.

**Structure**

| Field         | Type      | Attributes | Key | Null | Default | Extra | Comment                  |
| ------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]     | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [spell][2]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Spell Identifier         |
| [specMask][3] | TINYINT   | UNSIGNED   |     | NO   | 1       |       |                          |

[1]: #guid
[2]: #spell
[3]: #specmask

**Description of the fields**

### guid

The character guid. See [characters.guid](characters#guid).

### spell

The spell ID. See [Spell.dbc](spell) column 1.

### specMask

Boolean 1 or 0 signifying whether the spell is active (appears in the spell book).