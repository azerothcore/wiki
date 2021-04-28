# pet\_spell\_cooldown

[<-Back-to:Characters](database-characters.md)

**The \`pet\_spell\_cooldown\` table**

This table holds information on pet spell cooldowns.

**Structure**

| Field      | Type         | Attributes | Key | Null | Default | Extra | Comment                            |
|------------|--------------|------------|-----|------|---------|-------|------------------------------------|
| [guid][1]  | int(10)      | unsigned   | PRI | NO   | 0       |       | Global Unique Identifier, Low part |
| [spell][2] | MEDIUMINT(8) | unsigned   | PRI | NO   | 0       |       | Spell Identifier                   |
| [time][3]  | int(10)      | unsigned   |     | NO   | 0       |       |                                    |

[1]: #guid
[2]: #spell
[3]: #time

**Description of the fields**

### guid

The GUID of the pet. See character\_pet.id

### spell

The spell ID to which the cooldown applies. See Spell.dbc column 1

### time

The time when the cooldown expires, in Unix time.
