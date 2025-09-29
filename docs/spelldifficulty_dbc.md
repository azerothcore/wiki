# spelldifficulty\_dbc

[<-Back-to:World](database-world)

**The \`spelldifficulty\_dbc\` table**

This table contains spell data regarding cpp scripts. The id is called in the script, and depending on what version of the dungeon/raid the characters are in, the proper spell ID will be casted by the creature.

**Table Structure**

| Field         | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]       | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [DifficultySpellID_1][2] | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [DifficultySpellID_2][3] | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [DifficultySpellID_3][4] | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [DifficultySpellID_4][5] | INT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #id
[2]: #difficultyspellid_1
[3]: #difficultyspellid_2
[4]: #difficultyspellid_3
[5]: #difficultyspellid_4

**Description of the fields**

### id

id referenced in the cpp script for the creature AI.

### DifficultySpellID_1

Spell ID to be used in normal dungeon (or normal 10men raid).

### DifficultySpellID_2

Spell ID to be used in heroic dungeon (or normal 25men raid).

### DifficultySpellID_3

Spell ID to be used in heroic 10men raid.

### DifficultySpellID_4

Spell ID to be used in heroic 25men raid.
