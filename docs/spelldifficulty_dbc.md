# spelldifficulty\_dbc

[<-Back-to:World](database-world.md)

**The \`spelldifficulty\_dbc\` table**

This table contains spell data regarding cpp scripts. The id is called in the script, and depending on what version of the dungeon/raid the characters are in, the proper spell ID will be casted by the creature.

**Structure**

| Field         | Type    | Attributes | Key | Null | Default | Extra | Comment |
|---------------|---------|------------|-----|------|---------|-------|---------|
| [id][1]       | INT(11) | unsigned   | PRI | NO   | 0       |       |         |
| [spellid0][2] | INT(11) | unsigned   |     | NO   | 0       |       |         |
| [spellid1][3] | INT(11) | unsigned   |     | NO   | 0       |       |         |
| [spellid2][4] | INT(11) | unsigned   |     | NO   | 0       |       |         |
| [spellid3][5] | INT(11) | unsigned   |     | NO   | 0       |       |         |

[1]: #id
[2]: #spellid0
[3]: #spellid1
[4]: #spellid2
[5]: #spellid3

**Description of the fields**

### id

id referenced in the cpp script for the creature AI.

### spellid0

Spell ID to be used in normal dungeon (or normal 10men raid).

### spellid1

Spell ID to be used in heroic dungeon (or normal 25men raid).

### spellid2

Spell ID to be used in heroic 10men raid.

### spellid3

Spell ID to be used in heroic 25men raid.
