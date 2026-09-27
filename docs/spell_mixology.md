# spell_mixology

[<-Back-to:World](database-world)

**The \`spell_mixology\` table**

Bonus the Alchemy talent Mixology gives to elixirs and flasks. Players with Mixology who know the recipe of the elixir or flask get a stronger effect and double duration.

**Table Structure**

| Field             | Type  | Attributes | Key | Null | Default | Extra | Comment          |
| ----------------- | ----- | ---------- | --- | ---- | ------- | ----- | ---------------- |
| [entry](#entry)   | INT   | UNSIGNED   | PRI | NO   |         |       |                  |
| [pctMod](#pctmod) | FLOAT |            |     | NO   | 30      |       | bonus multiplier |

**Description of the fields**

### entry

The spell ID of the elixir or flask effect.

### pctMod

Bonus in percent added to the effects of the spell, for example 30 makes them 30% stronger.
