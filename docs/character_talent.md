# character\_talent

[<-Back-to:Characters](database-characters.md)

**The \`character\_talent\` table**

Contains all the individual talent data for each character. This is only used as a storage table, values get read from here and written to character\_spell, and vice-versa, when a player switches specs.

**Structure**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment |
|------------------|--------------|------------|-----|------|---------|-------|---------|
| [guid][1]        | INT      | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [spell][2]       | MEDIUMINT | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [talentGroup][3] | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #guid
[2]: #spell
[3]: #talentgroup

**Description of the fields**

### guid

The GUID of the character. See characters.guid

### spell

The spell ID. See Spell.dbc column 1

### talentGroup

talentGroup = 0 is the first spec, talentGroup = 1 is the second spec.
