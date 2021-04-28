# player\_classlevelstats

[<-Back-to:World](database-world.md)

**The \`player\_classlevelstats\` table**

This table holds information on the base health and mana of characters when they level up. Each class has different level stats. All of the values in this table signify only the base health and mana of the class at a specific level.

**Structure**

| Field         | Type        | Attributes | Key | Null | Default | Extra | Comment |
|---------------|-------------|------------|-----|------|---------|-------|---------|
| [class][1]    | TINYINT  | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [level][2]    | TINYINT  | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [basehp][3]   | SMALLINT | UNSIGNED   |     | NO   | NULL    |       |         |
| [basemana][4] | SMALLINT | UNSIGNED   |     | NO   | NULL    |       |         |

[1]: #class
[2]: #level
[3]: #basehp
[4]: #basemana

**Description of the fields**

### class

The character class. `ChrClasses.dbc`

### level

The level at which the stats should be applied.

### basehp

The base health of the character (before stamina bonuses).

### basemana

The base mana of the character (before intellect bonuses).
