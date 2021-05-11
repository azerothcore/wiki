# creature\_text\_locale

[<-Back-to:World](database-world.md)

**The \`creature\_text\_locale\` table**

This table is used to provide to localized clients with localized string for creatures texts.

**Structure**

| Field           | Type      | Attributes | Key | Null | Default | Extra | Comment |
|-----------------|-----------|------------|-----|------|---------|-------|---------|
| [CreatureID][1] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [GroupID][2]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [ID][3]         | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Locale][4]     | VARCHAR   |            | PRI | NO   |         |       |         |
| [Text][5]       | TEXT      |            |     | YES  |         |       |         |

[1]: #creatureid
[2]: #groupid
[3]: #id
[4]: #locale
[5]: #text

**Description of the fields**

### CreatureID

This is the [creature\_template.entry](creature_template#entry) to which the script is linked to.

### GroupID

If there is more than one of the same entry (more than one text the creature says), this column is used to choose if it is a random say or an ordered list. If a creature has got more than one say text to be shown in a given order, it must be incremented for each new matching entry (ex. 0, 1, 2, 3...). If there is only one entry or only one group, this value should be 0. If there are multiple groups of texts, this value stays the same within the group while the id increments within the same group.

Example from Stormwind City Guard, creature 68:

| CreatureID | GroupID | ID  | Text                                                                                                                       |
|------------|---------|-----|----------------------------------------------------------------------------------------------------------------------------|
| 68         | 0       | 0   | Taste blade, mongrel!                                                                                                      |
| 68         | 0       | 1   | Please tell me that you didn't just do what I think you just did. Please tell me that I'm not going to have to hurt you... |
| 68         | 0       | 2   | As if we don't have enough problems, you go and create more!                                                               |
| 68         | 2       | 0   | %s throws a rotten apple at $n.                                                                                            |
| 68         | 3       | 0   | %s throws rotten banana on $n.                                                                                             |
| 68         | 4       | 0   | %s spits on $n.                                                                                                            |
| 68         | 5       | 0   | Monster!                                                                                                                   |
| 68         | 5       | 1   | Murderer!                                                                                                                  |
| 68         | 5       | 2   | GET A ROPE!                                                                                                                |
| 68         | 5       | 3   | How dare you set foot in our city!                                                                                         |
| 68         | 5       | 4   | You disgust me.                                                                                                            |
| 68         | 5       | 5   | Looks like we're going to have ourselves an execution.                                                                     |
| 68         | 5       | 6   | Traitorous dog.                                                                                                            |
| 68         | 5       | 7   | My family was wiped out by the Scourge! MONSTER!                                                                           |

### ID

Entry for each group of texts. This is the unique identifier when entry (creature) is the same and groupid is unchanged, it must be incremented (ex. 0, 1, 2, 3...). A creature say will be randomly selected from this list based on the groupid it belongs to.

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
