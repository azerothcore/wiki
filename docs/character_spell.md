# character\_spell

[<-Back-to:Characters](database-characters)

**The \`character\_spell\` table**

Holds information for each character's spells.

**Table Structure**

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

Bitmask saving the specs using the spell.
| Value | Type                              |
| ----- | --------------------------------- |
| 1     | First Spec                        |
| 2     | Second Spec                       |
| 3     | Both Specs                        |
