# skilllineability\_dbc

[<-Back-to:World](database-world)

**The \`skilllineability\_dbc\` table**

This table has the same columns as the client file `SkillLineAbility.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: skilllineability\_dbc's Structure**

| Field                                                 | Type |     | Null | Key | Default | Extra | Comment |
| :---------------------------------------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                             | INT  |     | NO   | PRI | 0       |       |         |
| [SkillLine](#skillline)                               | INT  |     | NO   |     | 0       |       |         |
| [Spell](#spell)                                       | INT  |     | NO   |     | 0       |       |         |
| [RaceMask](#racemask)                                 | INT  |     | NO   |     | 0       |       |         |
| [ClassMask](#classmask)                               | INT  |     | NO   |     | 0       |       |         |
| [ExcludeRace](#excluderace)                           | INT  |     | NO   |     | 0       |       |         |
| [ExcludeClass](#excludeclass)                         | INT  |     | NO   |     | 0       |       |         |
| [MinSkillLineRank](#minskilllinerank)                 | INT  |     | NO   |     | 0       |       |         |
| [SupercededBySpell](#supercededbyspell)               | INT  |     | NO   |     | 0       |       |         |
| [AcquireMethod](#acquiremethod)                       | INT  |     | NO   |     | 0       |       |         |
| [TrivialSkillLineRankHigh](#trivialskilllinerankhigh) | INT  |     | NO   |     | 0       |       |         |
| [TrivialSkillLineRankLow](#trivialskilllineranklow)   | INT  |     | NO   |     | 0       |       |         |
| [CharacterPoints_1](#characterpoints)                 | INT  |     | NO   |     | 0       |       |         |
| [CharacterPoints_2](#characterpoints)                 | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `SkillLineAbilityEntry::ID`.

### SkillLine

The core reads this column into `SkillLineAbilityEntry::SkillLine`.

### Spell

The core reads this column into `SkillLineAbilityEntry::Spell`.

### RaceMask

The core reads this column into `SkillLineAbilityEntry::RaceMask`.

### ClassMask

The core reads this column into `SkillLineAbilityEntry::ClassMask`.

### ExcludeRace

Not used by the core.

### ExcludeClass

Not used by the core.

### MinSkillLineRank

The core reads this column into `SkillLineAbilityEntry::MinSkillLineRank`.

### SupercededBySpell

The core reads this column into `SkillLineAbilityEntry::SupercededBySpell`.

### AcquireMethod

The core reads this column into `SkillLineAbilityEntry::AcquireMethod`.

### TrivialSkillLineRankHigh

The core reads this column into `SkillLineAbilityEntry::TrivialSkillLineRankHigh`.

### TrivialSkillLineRankLow

The core reads this column into `SkillLineAbilityEntry::TrivialSkillLineRankLow`.

### CharacterPoints

Not used by the core.
