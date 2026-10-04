# pet\_spell

[<-Back-to:Characters](database-characters)

**The \`pet\_spell\` table**

This table holds information on individual pet spells.

**Table: pet\_spell's Structure**

| Field             | Type    |          | Null | Key | Default | Extra | Comment                  |
| :---------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)     | INT     | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [spell](#spell)   | INT     | UNSIGNED | NO   | PRI | 0       |       | Spell Identifier         |
| [active](#active) | TINYINT | UNSIGNED | NO   |     | 0       |       |                          |

**Description of the table's fields**

### guid

The pet GUID. See [character\_pet.id](character_pet#id).

### spell

The spell ID. See [Spell.dbc](spell) column 1.

### active

Boolean 0 or 1 controlling if the spell is active or not.
