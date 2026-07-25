# pet\_spell\_cooldown

[<-Back-to:Characters](database-characters)

**The \`pet\_spell\_cooldown\` table**

This table holds information on pet spell cooldowns.

**Table Structure**

| Field      | Type      | Attributes | Key | Null | Default | Extra | Comment                            |
| ---------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [guid][1]  | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier, Low part |
| [spell][2] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Spell Identifier                   |
| [category][4] | INT    | UNSIGNED   |     | YES  | 0       |       | Spell category                     |
| [time][3]  | INT       | UNSIGNED   |     | NO   | 0       |       |                                    |

[1]: #guid
[2]: #spell
[3]: #time
[4]: #category

**Description of the fields**

### guid

The GUID of the pet. See [character\_pet.id](character_pet#id).

### spell

The spell ID to which the cooldown applies. See [Spell.dbc](spell) column 1.

### category

Spell category the cooldown belongs to (category cooldowns are shared by all spells of the same category). `0` if the spell has no category.

### time

The time when the cooldown expires, in Unix time.
