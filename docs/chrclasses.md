# ChrClasses.dbc

This DBC contains all possible player classes.

**Version is 3.3.5a**

### Structure

| Column | Name              | Type    | Notes                                      |
|--------|-------------------|---------|--------------------------------------------|
| 1      | ClassID           | Integer |                                            |
| 2      | Unk1              |         | Unused                                     |
| 3-4    | Unk2              |         | Unused                                     |
| 5-20   | Name              | String  | Unused                                     |
| 21     |                   | String  | Unused                                     |
| 22-36  | nameFemale        | String  | Unused, if different from base (male) case |
| 37     |                   | String  | Unused                                     |
| 38-53  | nameNeutralGender | String  | Unused, if different from base (male) case |
| 54     |                   |         | Unused                                     |
| 56     | spellfamily       | Integer |                                            |
| 57     |                   |         | Unused                                     |
| 58     | CinematicSequence | Integer | Id from CinematicSequence.dbc              |
| 59     | expansion         | Integer |                                            |

### Content

| ID | Value | Name               |
|----|-------|--------------------|
| 1  | 1     | Warrior            |
| 2  | 2     | Paladin            |
| 3  | 4     | Hunter             |
| 4  | 8     | Rogue              |
| 5  | 16    | Priest             |
| 6  | 32    | Death Knight (3.x) |
| 7  | 64    | Shaman             |
| 8  | 128   | Mage               |
| 9  | 256   | Warlock            |
| 10 | 512   | Monk (5.x)         |
| 11 | 1024  | Druid              |
| 12 | 2048  | Demon Hunter (7.x) |

### Description of the fields

> Value

Value designates the bitmask used in various places of the core and database (quest_template.RequiresClasses etc).

The formula for it is: **Value = 1 << (ID - 1);**
