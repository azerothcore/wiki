# ChrClasses.dbc

[`Back-to:DBC`](dbc-index)

This DBC contains all possible player classes.

**Version is 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)  

**Table Structure**

| Column | Name                            | Type    | Notes                                                                                        |
| ------ | ------------------------------- | ------- | -------------------------------------------------------------------------------------------- |
| 1      | ID                              | Integer |                                                                                              |
| 2      | Unknown                         | Integer | 1 for Hunter, Rogue, and Shaman, 9 for Death Knight, 0 for the others. Removed in Cataclysm. |
| 3      | PowerType                       | Integer | 0 = Mana, 1 = Rage, 2 = Focus, 3 = Energy, 4 = Happiness, 6 = Runes. 2 and 4 unused.         |
| 4      | m_petNameToken                  | String  | Pet type. 101 for Warlock's demons, 1 for the other pets.                                    |
| 5-20   | Name                            | Loc     | A name to display.                                                                           |
| 21     | NameLangMask                    | Integer | String flags, unused.                                                                        |
| 22-37  | Name_female                     | Loc     | If different from base case, otherwise unused.                                               |
| 38     | NameFemaleLangMask              | Integer | String flags, unused.                                                                        |
| 39-54  | Name_male                       | Loc     | If different from base case, otherwise unused.                                               |
| 55     | NameMaleLangMask                | Integer | String flags, unused.                                                                        |
| 56     | fileName                        | String  | Capitalized English name.                                                                    |
| 57     | [spellClassSet](#spellclassset) | Integer |                                                                                              |
| 58     | [Flags](#flags)                 | Integer | Unused                                                                                       |
| 59     | Camera                          | iRefID  | Used for the opening cinematic. 165 for Death Knight, 0 for the others.                      |
| 60     | required_expansion              | Integer | 0 = Classic, 1 = Burning Crusade, 3 = Wrath.                                                 |

### Content

| Value | Hex    | Flag         | Class ID |
| :---- | :----: | :----------- | :------- |
| 1     | 0x0001 | Warrior      | 1        |
| 2     | 0x0002 | Paladin      | 2        |
| 4     | 0x0004 | Hunter       | 3        |
| 8     | 0x0008 | Rogue        | 4        |
| 16    | 0x0010 | Priest       | 5        |
| 32    | 0x0020 | Death Knight | 6        |
| 64    | 0x0040 | Shaman       | 7        |
| 128   | 0x0080 | Mage         | 8        |
| 256   | 0x0100 | Warlock      | 9        |
| 1024  | 0x0400 | Druid        | 11       |

### Flags

| Value | Hex  | Flag                        | Comment |
| :---- | :--: | :-------------------------- | :------ |
| 1     | 0x01 | Use loincloth               |         |
| 2     | 0x02 | Player class                |         |
| 4     | 0x04 | Display pet                 |         |
| 8     | 0x08 | Unused                      |         |
| 16    | 0x10 | Can wear mail               |         |
| 32    | 0x20 | Can wear scaling-stat plate |         |
| 64    | 0x40 | Bind starting area          |         |

### spellClassSet

| ID  | Family       | Notes                       |
| --- | ------------ | --------------------------- |
| 0   | Generic      |                             |
| 1   | Unk1         | Events, holidays            |
| 2   | Unused       |                             |
| 3   | Mage         |                             |
| 4   | Warrior      |                             |
| 5   | Warlock      |                             |
| 6   | Priest       |                             |
| 7   | Druid        |                             |
| 8   | Rogue        |                             |
| 9   | Hunter       |                             |
| 10  | Paladin      |                             |
| 11  | Shaman       |                             |
| 12  | Unk2         | Spells (Silence resistance) |
| 13  | Potion       |                             |
| 14  | Unused       |                             |
| 15  | Death Knight |                             |
| 16  | Unused       |                             |
| 17  | Pet          |                             |

### Description of the fields

> Value

Value designates the bitmask used in various places of the core and database (quest_template_addon.AllowableClasses etc).

The formula for it is: **Value = 1 << (ID - 1);**
