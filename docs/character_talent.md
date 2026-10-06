# character\_talent

[<-Back-to:Characters](database-characters)

**The \`character\_talent\` table**

Contains all the individual talent data for each character. This is only used as a storage table, values get read from here and written to character\_spell, and vice-versa, when a player switches specs.

**Table: character\_talent's Structure**

| Field                 | Type    |          | Null | Key | Default | Extra | Comment |
| :-------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid)         | INT     | UNSIGNED | NO   | PRI |         |       |         |
| [spell](#spell)       | INT     | UNSIGNED | NO   | PRI |         |       |         |
| [specMask](#specmask) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### guid

The character guid. See [characters.guid](characters#guid).

### spell

The spell ID. See [Spell.dbc](spell) column 1.

### specMask

Bitmask saving the specs using the talent.
| Value | Type                              |
| ----- | --------------------------------- |
| 1     | First Spec                        |
| 2     | Second Spec                       |
| 3     | Both Specs                        |
