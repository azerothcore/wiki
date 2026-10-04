# pet\_spell\_cooldown

[<-Back-to:Characters](database-characters)

**The \`pet\_spell\_cooldown\` table**

This table holds information on pet spell cooldowns.

**Table: pet\_spell\_cooldown's Structure**

| Field                 | Type |          | Null | Key | Default | Extra | Comment                            |
| :-------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :--------------------------------- |
| [guid](#guid)         | INT  | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier, Low part |
| [spell](#spell)       | INT  | UNSIGNED | NO   | PRI | 0       |       | Spell Identifier                   |
| [category](#category) | INT  | UNSIGNED | YES  |     | 0       |       | Spell category                     |
| [time](#time)         | INT  | UNSIGNED | NO   |     | 0       |       |                                    |

**Description of the table's fields**

### guid

The GUID of the pet. See [character\_pet.id](character_pet#id).

### spell

The spell ID to which the cooldown applies. See [Spell.dbc](spell) column 1.

### category

Spell category the cooldown belongs to (category cooldowns are shared by all spells of the same category). `0` if the spell has no category.

### time

The time when the cooldown expires, in Unix time.
