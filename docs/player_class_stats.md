# player\_levelstats

[<-Back-to:World](database-world.md)

**The \`player\_levelstats\` table**

This table holds information on what values are applied to stats for characters as they level up. All of the values in this table signify only the base stats of a class at a specific level.

**Structure**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment |
|----------------|---------|------------|-----|------|---------|-------|---------|
| [Class][1]     | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [Level][2]     | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [Strength][3]  | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Agility][4]   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Stamina][5]   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Intellect][6] | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Spirit][7]    | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #Class
[2]: #Level
[3]: #Strength
[4]: #Agility
[5]: #Stamina
[6]: #Intellect
[7]: #Spirit

**Description of the fields**

### Class

The character class. This field defines what values to apply to the stats of a character. This value is taken from [`ChrClasses.dbc`](chrclasses).

### Level

The level at which the stats should be applied.

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

| Class | Level | Strength | Agility | Stamina | Intellect | Spirit |
|-------|-------|----------|---------|---------|-----------|--------|
| 1     | 1     | 23       | 20      | 22      | 20        | 20     |
| 2     | 1     | 22       | 20      | 22      | 20        | 21     |
| 3     | 1     | 20       | 23      | 21      | 20        | 21     |
| 4     | 1     | 21       | 23      | 21      | 20        | 20     |
| 5     | 1     | 20       | 20      | 20      | 22        | 23     |
| 6     | 55    | 108      | 73      | 99      | 29        | 42     |
| 7     | 1     | 21       | 20      | 21      | 21        | 22     |
| 8     | 1     | 20       | 20      | 20      | 23        | 22     |
| 9     | 1     | 20       | 20      | 21      | 22        | 22     |
| 11    | 1     | 21       | 20      | 20      | 22        | 22     |

**Relation to [\`player\_race\_stats\`](player_race_stats)**

This table alone does not define the stats of a character at any level. The values from this table are combined with the values found in the \`player\_race\_stats\` table to apply the final stats to a character at any level.