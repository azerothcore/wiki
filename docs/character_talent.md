# character\_talent

[<-Back-to:Characters](database-characters)

**The \`character\_talent\` table**

Contains all the individual talent data for each character. This is only used as a storage table, values get read from here and written to character\_spell, and vice-versa, when a player switches specs.

**Table Structure**

| Field         | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]     | INT       | UNSIGNED   | PRI | NO   |         |       |         |
| [spell][2]    | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [specMask][3] | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #guid
[2]: #spell
[3]: #specmask

**Description of the fields**

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
