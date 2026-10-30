# player\_race\_stats

[<-Back-to:World](database-world)

**The \`player\_race\_stats\` table**

This table holds information on modifiers for stat values applied to characters. All of the values in this table signify only the stat value modifiers based on the race of a character.

**Table: player\_race\_stats's Structure**

| Field                   | Type    |          | Null | Key | Default | Extra | Comment |
| :---------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [Race](#race)           | TINYINT | UNSIGNED | NO   | PRI |         |       |         |
| [Strength](#strength)   | INT     |          | NO   |     | 0       |       |         |
| [Agility](#agility)     | INT     |          | NO   |     | 0       |       |         |
| [Stamina](#stamina)     | INT     |          | NO   |     | 0       |       |         |
| [Intellect](#intellect) | INT     |          | NO   |     | 0       |       |         |
| [Spirit](#spirit)       | INT     |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### Race

The character race. This field defines what values to apply to the stats of a character. This value is taken from [`ChrRaces.dbc`](chrraces).

### Strength

The strength modifier to apply to a character's base stat.

### Agility

The agility modifier to apply to a character's base stat.

### Stamina

The stamina modifier to apply to a character's base stat.

### Intellect

The intellect modifier to apply to a character's base stat.

### Spirit

The spirit modifier to apply to a character's base stat.

**Relation to [\`player\_class\_stats\`](player_class_stats)**

This table alone does not define the stats of a character. The values from this table are combined with the values found in the `player\_class\_stats` table to apply the final stats to a character at any level.

The way the final stat can be calculated is as follows: Take the base stat from `player\_class\_stats` and add the modifier for that stat from this table.

For example, a druid at level forty has a base strength stat of forty-six. Combining that with a night elf's strength modifier of negative four, you get a final value of forty-two.
