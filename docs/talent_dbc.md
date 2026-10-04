# talent\_dbc

[<-Back-to:World](database-world)

**The \`talent\_dbc\` table**

This table has the same columns as the client file `Talent.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: talent\_dbc's Structure**

| Field                               | Type |     | Null | Key | Default | Extra | Comment |
| :---------------------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                           | INT  |     | NO   | PRI | 0       |       |         |
| [TabID](#tabid)                     | INT  |     | NO   |     | 0       |       |         |
| [TierID](#tierid)                   | INT  |     | NO   |     | 0       |       |         |
| [ColumnIndex](#columnindex)         | INT  |     | NO   |     | 0       |       |         |
| [SpellRank_1](#spellrank)           | INT  |     | NO   |     | 0       |       |         |
| [SpellRank_2](#spellrank)           | INT  |     | NO   |     | 0       |       |         |
| [SpellRank_3](#spellrank)           | INT  |     | NO   |     | 0       |       |         |
| [SpellRank_4](#spellrank)           | INT  |     | NO   |     | 0       |       |         |
| [SpellRank_5](#spellrank)           | INT  |     | NO   |     | 0       |       |         |
| [SpellRank_6](#spellrank)           | INT  |     | NO   |     | 0       |       |         |
| [SpellRank_7](#spellrank)           | INT  |     | NO   |     | 0       |       |         |
| [SpellRank_8](#spellrank)           | INT  |     | NO   |     | 0       |       |         |
| [SpellRank_9](#spellrank)           | INT  |     | NO   |     | 0       |       |         |
| [PrereqTalent_1](#prereqtalent)     | INT  |     | NO   |     | 0       |       |         |
| [PrereqTalent_2](#prereqtalent)     | INT  |     | NO   |     | 0       |       |         |
| [PrereqTalent_3](#prereqtalent)     | INT  |     | NO   |     | 0       |       |         |
| [PrereqRank_1](#prereqrank)         | INT  |     | NO   |     | 0       |       |         |
| [PrereqRank_2](#prereqrank)         | INT  |     | NO   |     | 0       |       |         |
| [PrereqRank_3](#prereqrank)         | INT  |     | NO   |     | 0       |       |         |
| [Flags](#flags)                     | INT  |     | NO   |     | 0       |       |         |
| [RequiredSpellID](#requiredspellid) | INT  |     | NO   |     | 0       |       |         |
| [CategoryMask_1](#categorymask)     | INT  |     | NO   |     | 0       |       |         |
| [CategoryMask_2](#categorymask)     | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `TalentEntry::TalentID`.

### TabID

The core reads this column into `TalentEntry::TalentTab`.

Comment in the core source: "index in TalentTab.dbc (TalentTabEntry)"

### TierID

The core reads this column into `TalentEntry::Row`.

### ColumnIndex

The core reads this column into `TalentEntry::Col`.

### SpellRank

The core reads `SpellRank_1` to `SpellRank_5`. `SpellRank_6` to `SpellRank_9` are not used by the core.

### PrereqTalent

The core reads `PrereqTalent_1` into `TalentEntry::DependsOn`. `PrereqTalent_2` and `PrereqTalent_3` are not used by the core.

Comment in the core source: "preReqTalent1 index in Talent.dbc (TalentEntry)"

### PrereqRank

The core reads `PrereqRank_1` into `TalentEntry::DependsOnRank`. `PrereqRank_2` and `PrereqRank_3` are not used by the core.

### Flags

The core reads this column into `TalentEntry::addToSpellBook`.

Comment in the core source: "also need disable higest ranks on reset talent tree"

### RequiredSpellID

Not used by the core.

### CategoryMask

Not used by the core.

Comment in the core source: "its a 64 bit mask for pet 1<<m_categoryEnumID in CreatureFamily.dbc"
