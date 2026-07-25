# spelldifficulty\_dbc

[<-Back-to:World](database-world)

**The \`spelldifficulty\_dbc\` table**

This table determines which spell ID should be used depending on the dungeon or raid difficulty.  

{% include note.html content="The EPIC difficulty value exists but is currently unused." %}

**Table Structure**

| Field         | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]       | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [DifficultySpellID_1][2] | INT  | UNSIGNED   |     | NO   | 0       |       | Spell ID for normal dungeon / 10-player normal raid |
| [DifficultySpellID_2][3] | INT  | UNSIGNED   |     | NO   | 0       |       | Spell ID for heroic dungeon / 25-player normal raid |
| [DifficultySpellID_3][4] | INT  | UNSIGNED   |     | NO   | 0       |       | Spell ID for epic dungeon (unused) / 10-player heroic raid |
| [DifficultySpellID_4][5] | INT  | UNSIGNED   |     | NO   | 0       |       | Spell ID for 25-player heroic raid |

[1]: #id
[2]: #difficultyspellid_1
[3]: #difficultyspellid_2
[4]: #difficultyspellid_3
[5]: #difficultyspellid_4

**Description of the fields**

### ID
Spell ID reference in scripts/SmartAI

### DifficultySpellID_1

Spell ID to be used in normal dungeon or 10-player normal raid.

### DifficultySpellID_2

Spell ID to be used in heroic dungeon or 25-player normal raid.

### DifficultySpellID_3

Spell ID to be used in epic dungeon (unused) or 10-player heroic raid.

### DifficultySpellID_4

Spell ID to be used in 25-player heroic raid.
