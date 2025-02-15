# player_class_stats

[<-Back-to:World](database-world)

**The \`player_class_stats\` table**

This table holds information on what values are applied to stats for characters as they level up. All of the values in this table signify only the base stats of a class at a specific level.

**Table Structure**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Class][1]     | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [Level][2]     | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [BaseHP][3]    | INT     | UNSIGNED   |     | NO   | 1       |       |         |
| [BaseMana][4]  | INT     | UNSIGNED   |     | NO   | 1       |       |         |
| [Strength][5]  | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Agility][6]   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Stamina][7]   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Intellect][8] | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Spirit][9]    | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #Class
[2]: #Level
[3]: #BaseHP
[4]: #BaseMana
[5]: #Strength
[6]: #Agility
[7]: #Stamina
[8]: #Intellect
[9]: #Spirit

**Description of the fields**

### Class

The character class. This field defines what values to apply to the stats of a character. This value is taken from [`ChrClasses.dbc`](chrclasses).

### Level

The level at which the stats should be applied.

### BaseHP

The base health points to be applied to a character. Applied before stamina bonuses.

### BaseMana

The base mana to be applied to a character. Applied before intellect bonuses.

### Strength

The base strength to be applied to a character.

### Agility

The base agility to be applied to a character.

### Stamina

The base stamina to be applied to a character.

### Intellect

The base intellect to be applied to a character.

### Spirit

The base spirit to be applied to a character.

### Examples

| Class | Level | BaseHP | BaseMana | Strength | Agility | Stamina | Intellect | Spirit |
| ----- | ----- | ------ | -------- | -------- | ------- | ------- | --------- | ------ |
| 1     | 1     | 20     | 0        | 23       | 20      | 22      | 20        | 20     |
| 2     | 1     | 28     | 60       | 22       | 20      | 22      | 20        | 21     |
| 3     | 1     | 46     | 65       | 20       | 23      | 21      | 20        | 21     |
| 4     | 1     | 25     | 0        | 21       | 23      | 21      | 20        | 20     |
| 5     | 1     | 52     | 73       | 20       | 20      | 20      | 22        | 23     |
| 6     | 55    | 1359   | 0        | 108      | 73      | 99      | 29        | 42     |
| 7     | 1     | 40     | 85       | 21       | 20      | 21      | 21        | 22     |
| 8     | 1     | 32     | 100      | 20       | 20      | 20      | 23        | 22     |
| 9     | 1     | 23     | 90       | 20       | 20      | 21      | 22        | 22     |
| 11    | 1     | 44     | 60       | 21       | 20      | 20      | 22        | 22     |

**Relation to [\`player_race_stats\`](player_race_stats)**

This table alone does not define the stats of a character at any level. The values from this table are combined with the values found in the `player_race_stats` table to apply the final stats to a character at any level.

The way the final stat can be calculated is as follows: Take the base stat from this table and add the modifier for that stat from `player_race_stats`.

For example, a druid at level forty has a base strength stat of forty-six. Combining that with a night elf's strength modifier of negative four, you get a final value of forty-two.
