# ChrClasses.dbc

[`Back-to:DBC`](dbc-index)

This DBC contains all possible player classes.

**Version is 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)  

**Table Structure**

| Column | Field                | Type   | chrclasses\_dbc column                                    | Comment                                                                                                                        |
| :----: | :------------------- | :----- | :-------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| 0      | ID                   | uint32 | [ID](chrclasses_dbc#id)                                   |                                                                                                                                |
| 1      | DamageBonusStat      | uint32 | [Field01](chrclasses_dbc#field01)                         | 1 for Hunter, Rogue, and Shaman, 9 for Death Knight, 0 for the others. Removed in Cataclysm.                                   |
| 2      | DisplayPower         | uint32 | [DisplayPower](chrclasses_dbc#displaypower)               | 0 = Mana, 1 = Rage, 2 = Focus, 3 = Energy, 4 = Happiness, 6 = Runes. 2 and 4 unused.                                           |
| 3      | PetNameToken         | string | [PetNameToken](chrclasses_dbc#petnametoken)               | Pet type. 101 for Warlock's demons, 1 for the other pets.                                                                      |
| 4      | Name_0               | string | [Name_Lang_enUS](chrclasses_dbc#namelang)                 | A name to display. Assumed enUS                                                                                                |
| 5      | Name_1               | string | [Name_Lang_enGB](chrclasses_dbc#namelang)                 | Assumed enGB, not used in 3.3.5a                                                                                               |
| 6      | Name_2               | string | [Name_Lang_koKR](chrclasses_dbc#namelang)                 | Assumed koKR                                                                                                                   |
| 7      | Name_3               | string | [Name_Lang_frFR](chrclasses_dbc#namelang)                 | Assumed frFR                                                                                                                   |
| 8      | Name_4               | string | [Name_Lang_deDE](chrclasses_dbc#namelang)                 | Assumed deDE                                                                                                                   |
| 9      | Name_5               | string | [Name_Lang_enCN](chrclasses_dbc#namelang)                 | Assumed enCN, not used in 3.3.5a                                                                                               |
| 10     | Name_6               | string | [Name_Lang_zhCN](chrclasses_dbc#namelang)                 | Assumed zhCN                                                                                                                   |
| 11     | Name_7               | string | [Name_Lang_enTW](chrclasses_dbc#namelang)                 | Assumed enTW, not used in 3.3.5a                                                                                               |
| 12     | Name_8               | string | [Name_Lang_zhTW](chrclasses_dbc#namelang)                 | Assumed zhTW                                                                                                                   |
| 13     | Name_9               | string | [Name_Lang_esES](chrclasses_dbc#namelang)                 | Assumed esES                                                                                                                   |
| 14     | Name_10              | string | [Name_Lang_esMX](chrclasses_dbc#namelang)                 | Assumed esMX                                                                                                                   |
| 15     | Name_11              | string | [Name_Lang_ruRU](chrclasses_dbc#namelang)                 | Assumed ruRU                                                                                                                   |
| 16     | Name_12              | string | [Name_Lang_ptPT](chrclasses_dbc#namelang)                 | Assumed ptPT, not used in 3.3.5a                                                                                               |
| 17     | Name_13              | string | [Name_Lang_ptBR](chrclasses_dbc#namelang)                 | Assumed ptBR, not used in 3.3.5a                                                                                               |
| 18     | Name_14              | string | [Name_Lang_itIT](chrclasses_dbc#namelang)                 | Assumed itIT, not used in 3.3.5a                                                                                               |
| 19     | Name_15              | string | [Name_Lang_Unk](chrclasses_dbc#namelang)                  | Unknown language, unsure of the usage in 3.3.5a                                                                                |
| 20     | Name_lang_mask       | uint32 | [Name_Lang_Mask](chrclasses_dbc#namelang)                 | String flags, unused. Assumed flags of the localized text                                                                      |
| 21     | NameFemale_0         | string | [Name_Female_Lang_enUS](chrclasses_dbc#namefemalelang)    | If different from base case, otherwise unused. Assumed enUS                                                                    |
| 22     | NameFemale_1         | string | [Name_Female_Lang_enGB](chrclasses_dbc#namefemalelang)    | Assumed enGB, not used in 3.3.5a                                                                                               |
| 23     | NameFemale_2         | string | [Name_Female_Lang_koKR](chrclasses_dbc#namefemalelang)    | Assumed koKR                                                                                                                   |
| 24     | NameFemale_3         | string | [Name_Female_Lang_frFR](chrclasses_dbc#namefemalelang)    | Assumed frFR                                                                                                                   |
| 25     | NameFemale_4         | string | [Name_Female_Lang_deDE](chrclasses_dbc#namefemalelang)    | Assumed deDE                                                                                                                   |
| 26     | NameFemale_5         | string | [Name_Female_Lang_enCN](chrclasses_dbc#namefemalelang)    | Assumed enCN, not used in 3.3.5a                                                                                               |
| 27     | NameFemale_6         | string | [Name_Female_Lang_zhCN](chrclasses_dbc#namefemalelang)    | Assumed zhCN                                                                                                                   |
| 28     | NameFemale_7         | string | [Name_Female_Lang_enTW](chrclasses_dbc#namefemalelang)    | Assumed enTW, not used in 3.3.5a                                                                                               |
| 29     | NameFemale_8         | string | [Name_Female_Lang_zhTW](chrclasses_dbc#namefemalelang)    | Assumed zhTW                                                                                                                   |
| 30     | NameFemale_9         | string | [Name_Female_Lang_esES](chrclasses_dbc#namefemalelang)    | Assumed esES                                                                                                                   |
| 31     | NameFemale_10        | string | [Name_Female_Lang_esMX](chrclasses_dbc#namefemalelang)    | Assumed esMX                                                                                                                   |
| 32     | NameFemale_11        | string | [Name_Female_Lang_ruRU](chrclasses_dbc#namefemalelang)    | Assumed ruRU                                                                                                                   |
| 33     | NameFemale_12        | string | [Name_Female_Lang_ptPT](chrclasses_dbc#namefemalelang)    | Assumed ptPT, not used in 3.3.5a                                                                                               |
| 34     | NameFemale_13        | string | [Name_Female_Lang_ptBR](chrclasses_dbc#namefemalelang)    | Assumed ptBR, not used in 3.3.5a                                                                                               |
| 35     | NameFemale_14        | string | [Name_Female_Lang_itIT](chrclasses_dbc#namefemalelang)    | Assumed itIT, not used in 3.3.5a                                                                                               |
| 36     | NameFemale_15        | string | [Name_Female_Lang_Unk](chrclasses_dbc#namefemalelang)     | Unknown language, unsure of the usage in 3.3.5a                                                                                |
| 37     | NameFemale_lang_mask | uint32 | [Name_Female_Lang_Mask](chrclasses_dbc#namefemalelang)    | String flags, unused. Assumed flags of the localized text                                                                      |
| 38     | NameMale_0           | string | [Name_Male_Lang_enUS](chrclasses_dbc#namemalelang)        | If different from base case, otherwise unused. Assumed enUS                                                                    |
| 39     | NameMale_1           | string | [Name_Male_Lang_enGB](chrclasses_dbc#namemalelang)        | Assumed enGB, not used in 3.3.5a                                                                                               |
| 40     | NameMale_2           | string | [Name_Male_Lang_koKR](chrclasses_dbc#namemalelang)        | Assumed koKR                                                                                                                   |
| 41     | NameMale_3           | string | [Name_Male_Lang_frFR](chrclasses_dbc#namemalelang)        | Assumed frFR                                                                                                                   |
| 42     | NameMale_4           | string | [Name_Male_Lang_deDE](chrclasses_dbc#namemalelang)        | Assumed deDE                                                                                                                   |
| 43     | NameMale_5           | string | [Name_Male_Lang_enCN](chrclasses_dbc#namemalelang)        | Assumed enCN, not used in 3.3.5a                                                                                               |
| 44     | NameMale_6           | string | [Name_Male_Lang_zhCN](chrclasses_dbc#namemalelang)        | Assumed zhCN                                                                                                                   |
| 45     | NameMale_7           | string | [Name_Male_Lang_enTW](chrclasses_dbc#namemalelang)        | Assumed enTW, not used in 3.3.5a                                                                                               |
| 46     | NameMale_8           | string | [Name_Male_Lang_zhTW](chrclasses_dbc#namemalelang)        | Assumed zhTW                                                                                                                   |
| 47     | NameMale_9           | string | [Name_Male_Lang_esES](chrclasses_dbc#namemalelang)        | Assumed esES                                                                                                                   |
| 48     | NameMale_10          | string | [Name_Male_Lang_esMX](chrclasses_dbc#namemalelang)        | Assumed esMX                                                                                                                   |
| 49     | NameMale_11          | string | [Name_Male_Lang_ruRU](chrclasses_dbc#namemalelang)        | Assumed ruRU                                                                                                                   |
| 50     | NameMale_12          | string | [Name_Male_Lang_ptPT](chrclasses_dbc#namemalelang)        | Assumed ptPT, not used in 3.3.5a                                                                                               |
| 51     | NameMale_13          | string | [Name_Male_Lang_ptBR](chrclasses_dbc#namemalelang)        | Assumed ptBR, not used in 3.3.5a                                                                                               |
| 52     | NameMale_14          | string | [Name_Male_Lang_itIT](chrclasses_dbc#namemalelang)        | Assumed itIT, not used in 3.3.5a                                                                                               |
| 53     | NameMale_15          | string | [Name_Male_Lang_Unk](chrclasses_dbc#namemalelang)         | Unknown language, unsure of the usage in 3.3.5a                                                                                |
| 54     | NameMale_lang_mask   | uint32 | [Name_Male_Lang_Mask](chrclasses_dbc#namemalelang)        | String flags, unused. Assumed flags of the localized text                                                                      |
| 55     | Filename             | string | [Filename](chrclasses_dbc#filename)                       | Capitalized English name.                                                                                                      |
| 56     | SpellClassSet        | uint32 | [SpellClassSet](chrclasses_dbc#spellclassset)             | [spellClassSet](#spellclassset)                                                                                                |
| 57     | Flags                | uint32 | [Flags](chrclasses_dbc#flags)                             | [Flags](#flags): Unused                                                                                                        |
| 58     | CinematicSequenceID  | uint32 | [CinematicSequenceID](chrclasses_dbc#cinematicsequenceid) | Used for the opening cinematic. 165 for Death Knight, 0 for the others. ID in [CinematicSequences.dbc](dbc-cinematicsequences) |
| 59     | RequiredExpansion    | uint32 | [Required_Expansion](chrclasses_dbc#requiredexpansion)    | 0 = Classic, 1 = Burning Crusade, 3 = Wrath.                                                                                   |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

### Content

| Value | Hex      | Flag         | Class ID |
| :---- | :------: | :----------- | :------- |
| 1     | `0x0001` | Warrior      | 1        |
| 2     | `0x0002` | Paladin      | 2        |
| 4     | `0x0004` | Hunter       | 3        |
| 8     | `0x0008` | Rogue        | 4        |
| 16    | `0x0010` | Priest       | 5        |
| 32    | `0x0020` | Death Knight | 6        |
| 64    | `0x0040` | Shaman       | 7        |
| 128   | `0x0080` | Mage         | 8        |
| 256   | `0x0100` | Warlock      | 9        |
| 1024  | `0x0400` | Druid        | 11       |

### Flags

| Value | Hex    | Flag                        | Comment |
| :---- | :----: | :-------------------------- | :------ |
| 1     | `0x01` | Use loincloth               |         |
| 2     | `0x02` | Player class                |         |
| 4     | `0x04` | Display pet                 |         |
| 8     | `0x08` | Unused                      |         |
| 16    | `0x10` | Can wear mail               |         |
| 32    | `0x20` | Can wear scaling-stat plate |         |
| 64    | `0x40` | Bind starting area          |         |

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
