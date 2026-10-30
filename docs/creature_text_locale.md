# creature\_text\_locale

[<-Back-to:World](database-world)

**The \`creature\_text\_locale\` table**

This table is used to provide to localized clients with localized string for creatures texts.

**Table: creature\_text\_locale's Structure**

| Field                     | Type       |          | Null | Key | Default | Extra | Comment |
| :------------------------ | :--------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [CreatureID](#creatureid) | INT        | UNSIGNED | NO   | PRI | 0       |       |         |
| [GroupID](#groupid)       | TINYINT    | UNSIGNED | NO   | PRI | 0       |       |         |
| [ID](#id)                 | TINYINT    | UNSIGNED | NO   | PRI | 0       |       |         |
| [Locale](#locale)         | VARCHAR(4) |          | NO   | PRI |         |       |         |
| [Text](#text)             | TEXT       |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### CreatureID

This is the [creature\_template.entry](creature_template#entry) to which the script is linked to.

### GroupID

If there is more than one of the same entry (more than one text the creature says), this column is used to choose if it is a random say or an ordered list. If a creature has got more than one say text to be shown in a given order, it must be incremented for each new matching entry (ex. 0, 1, 2, 3...). If there is only one entry or only one group, this value should be 0. If there are multiple groups of texts, this value stays the same within the group while the id increments within the same group.

### ID

Entry for each group of texts. This is the unique identifier when entry (creature) is the same and groupid is unchanged, it must be incremented (ex. 0, 1, 2, 3...). A creature say will be randomly selected from this list based on the groupid it belongs to.

### Locale

It is the language in which you want to make the translation.
You can choose from the following:

| ID | Language |
|----|----------|
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
