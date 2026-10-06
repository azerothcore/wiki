# spell\_mixology

[<-Back-to:World](database-world)

**The \`spell\_mixology\` table**

Bonus the Alchemy talent Mixology gives to elixirs and flasks. Players with Mixology who know the recipe of the elixir or flask get a stronger effect and double duration.

**Table: spell\_mixology's Structure**

| Field             | Type  |          | Null | Key | Default | Extra | Comment          |
| :---------------- | :---- | :------- | :--: | :-: | :-----: | :---: | :--------------- |
| [entry](#entry)   | INT   | UNSIGNED | NO   | PRI |         |       |                  |
| [pctMod](#pctmod) | FLOAT |          | NO   |     | 30      |       | bonus multiplier |

**Description of the table's fields**

### entry

The spell ID of the elixir or flask effect.

### pctMod

Bonus in percent added to the effects of the spell, for example 30 makes them 30% stronger.
