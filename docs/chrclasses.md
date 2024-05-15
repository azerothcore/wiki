# ChrClasses.dbc

[`Back-to:DBC`](dbc-index.md)

This DBC contains all possible player classes.

**Version is 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db.md)  

### Structure

| Column | Name                                         | Type    | Notes                                                                                        |
|--------|----------------------------------------------|---------|----------------------------------------------------------------------------------------------|
| 1      | ID                                           | Integer |                                                                                              |
| 2      | Unknown                                      | Integer | 1 for Hunter, Rogue, and Shaman, 9 for Death Knight, 0 for the others. Removed in Cataclysm. |
| 3      | PowerType                                    | Integer | 0 = Mana, 1 = Rage, 2 = Focus, 3 = Energy, 4 = Happiness, 6 = Runes. 2 and 4 unused.         |
| 4      | m_petNameToken                               | String  | Pet type. 101 for Warlock's demons, 1 for the other pets.                                    |
| 5-20   | Name                                         | Loc     | A name to display.                                                                           |
| 21     | NameLangMask                                 | Integer | String flags, unused.                                                                        |
| 22-37  | Name_female                                  | Loc     | If different from base case, otherwise unused.                                               |
| 38     | NameFemaleLangMask                           | Integer | String flags, unused.                                                                        |
| 39-54  | Name_male                                    | Loc     | If different from base case, otherwise unused.                                               |
| 55     | NameMaleLangMask                             | Integer | String flags, unused.                                                                        |
| 56     | fileName                                     | String  | Capitalized English name.                                                                    |
| 57     | [spellClassSet](#spellclassset)              | Integer |                                                                                              |
| 58     | [Flags](#flags)                              | Integer | Unused                                                                                       |
| 59     | Camera                                       | iRefID  | Used for the opening cinematic. 165 for Death Knight, 0 for the others.                      |
| 60     | required_expansion                           | Integer | 0 = Classic, 1 = Burning Crusade, 3 = Wrath.                                                 |

### Content

| ID | Value | Name               |
|----|-------|--------------------|
| 1  | 1     | Warrior            |
| 2  | 2     | Paladin            |
| 3  | 4     | Hunter             |
| 4  | 8     | Rogue              |
| 5  | 16    | Priest             |
| 6  | 32    | Death Knight       |
| 7  | 64    | Shaman             |
| 8  | 128   | Mage               |
| 9  | 256   | Warlock            |
| 11 | 1024  | Druid              |

### Flags

| Flag | Description                 |
|------|-----------------------------|
| 1    | Use loincloth               |
| 2    | Player class                |
| 4    | Display pet                 |
| 8    | Unused                      |
| 16   | Can wear mail               |
| 32   | Can wear scaling-stat plate |
| 64   | Bind starting area          |

### spellClassSet

| ID | Family       | Notes                       |
|----|--------------|-----------------------------|
| 0  | Generic      |                             |
| 1  | Unk1         | Events, holidays            |
| 2  | Unused       |                             |
| 3  | Mage         |                             |
| 4  | Warrior      |                             |
| 5  | Warlock      |                             |
| 6  | Priest       |                             |
| 7  | Druid        |                             |
| 8  | Rogue        |                             |
| 9  | Hunter       |                             |
| 10 | Paladin      |                             |
| 11 | Shaman       |                             |
| 12 | Unk2         | Spells (Silence resistance) |
| 13 | Potion       |                             |
| 14 | Unused       |                             |
| 15 | Death Knight |                             |
| 16 | Unused       |                             |
| 17 | Pet          |                             |

### Description of the fields

> Value

Value designates the bitmask used in various places of the core and database (quest_template.RequiresClasses etc).

The formula for it is: **Value = 1 << (ID - 1);**
