# character\_spell

[<-Back-to:Characters](database-characters.md)

**The \`character\_spell\` table**

Holds information for each character's spells.

**Structure**

| Field         | Type         | Attributes | Key | Null | Default | Extra | Comment                  |
|---------------|--------------|------------|-----|------|---------|-------|--------------------------|
| [guid][1]     | INT(10)      | unsigned   | PRI | NO   | 0       |       | Global Unique Identifier |
| [spell][2]    | MEDIUMINT(8) | unsigned   | PRI | NO   | 0       |       | Spell Identifier         |
| [active][3]   | TINYINT(3)   | unsigned   |     | NO   | 1       |       |                          |
| [disabled][4] | TINYINT(3)   | unsigned   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #spell
[3]: #active
[4]: #disabled

**Description of the fields**

### guid

The GUID of the character. See characters.guid

### spell

The spell ID. See Spell.dbc column 1

### active

Boolean 1 or 0 signifying whether the spell is active (appears in the spell book).

### disabled

Boolean flag 0 or 1 when spell is disabled because talent which teaches it has been unlearned. When talent is learned again the spell will be available again.
