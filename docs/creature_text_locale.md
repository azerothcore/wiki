# creature\_text\_locale

[<-Back-to:World](database-world.md)

**The \`creature\_text\_locale\` table**

This table is used to provide to localized clients with localized string for creatures texts.

**Structure**

| Field           | Type         | Attributes | Key      | Null     | Default | Extra | Comment |
|-----------------|--------------|------------|----------|----------|---------|-------|---------|
| [CreatureID][1] | mediumint(8) | unsigned   |  PRI     |  NO      | 0       |       |         |
| [GroupID][2]    | tinyint(3)   | unsigned   |  PRI     |  NO      | 0       |       |         |
| [ID][3]         | tinyint(3)   | unsigned   |  PRI     |  NO      | 0       |       |         |
| [Locale][4]     | varchar(4)   |            |  PRI     |  NO      |         |       |         |
| [Text][5]       | text         |            |          |  YES     |         |       |         |

[1]: #creatureid
[2]: #groupid
[3]: #id
[4]: #locale
[5]: #text

**Description of the fields**

### CreatureID
Creature ID, obtained from [creature_template.entry](creature_template#entry)

### GroupID
If there is more than one of the same entry (more than one text the creature says), this column is used to choose if it is a random say or an ordered list. If a creature has got more than one say text to be shown in a given order, it must be incremented for each new matching entry (ex. 0, 1, 2, 3...). If there is only one entry or only one group, this value should be 0. If there are multiple groups of texts, this value stays the same within the group while the id increments within the same group.

### ID
Entry for each group of texts. This is the unique identifier when entry (creature) is the same and groupid is unchanged, it must be incremented (ex. 0, 1, 2, 3...). A creature say will be randomly selected from this list based on the groupid it belongs to.

### Locale
It is the language in which you want to make the translation.
You can choose from the following:

| ID | Language |
|----|----------|
| 0  | enUS     |
| 1  | koKR     |
| 2  | frFR     |
| 3  | deDE     |
| 4  | zhCN     |
| 5  | zhTW     |
| 6  | esES     |
| 7  | esMX     |
| 8  | ruRU     |

### Text
The translated text the creature will say.
