# character\_spell

[<-Back-to:Characters](database-characters)

**The \`character\_spell\` table**

Holds information for each character's spells.

**Table: character\_spell's Structure**

| Field                 | Type    |          | Null | Key | Default | Extra | Comment                  |
| :-------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)         | INT     | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [spell](#spell)       | INT     | UNSIGNED | NO   | PRI | 0       |       | Spell Identifier         |
| [specMask](#specmask) | TINYINT | UNSIGNED | NO   |     | 1       |       |                          |

**Description of the table's fields**

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
