# spelldifficulty\_dbc

[<-Back-to:World](database-world)

**The \`spelldifficulty\_dbc\` table**

This table determines which spell ID should be used depending on the dungeon or raid difficulty.  

{% include note.html content="The EPIC difficulty value exists but is currently unused." %}

**Table: spelldifficulty\_dbc's Structure**

| Field                                      | Type |          | Null | Key | Default | Extra | Comment                                                    |
| :----------------------------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :--------------------------------------------------------- |
| [ID](#id)                                  | INT  |          | NO   | PRI | 0       |       |                                                            |
| [DifficultySpellID_1](#difficultyspellid1) | INT  |          | NO   |     | 0       |       | Spell ID for normal dungeon / 10-player normal raid        |
| [DifficultySpellID_2](#difficultyspellid2) | INT  |          | NO   |     | 0       |       | Spell ID for heroic dungeon / 25-player normal raid        |
| [DifficultySpellID_3](#difficultyspellid3) | INT  |          | NO   |     | 0       |       | Spell ID for epic dungeon (unused) / 10-player heroic raid |
| [DifficultySpellID_4](#difficultyspellid4) | INT  | UNSIGNED | NO   |     | 0       |       | Spell ID for 25-player heroic raid                         |

**Description of the table's fields**

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
