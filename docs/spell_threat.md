# spell\_threat

[<-Back-to:World](database-world)

**The \`spell\_threat\` table**

This table holds threat values on all spells that should either give or take away threat.

**Table: spell\_threat's Structure**

| Field                 | Type  |          | Null | Key | Default | Extra | Comment                                   |
| :-------------------- | :---- | :------- | :--: | :-: | :-----: | :---: | :---------------------------------------- |
| [entry](#entry)       | INT   | UNSIGNED | NO   | PRI |         |       |                                           |
| [flatMod](#flatmod)   | INT   |          | YES  |     | NULL    |       |                                           |
| [pctMod](#pctmod)     | FLOAT |          | NO   |     | 1       |       | threat multiplier for damage/healing      |
| [apPctMod](#appctmod) | FLOAT |          | NO   |     | 0       |       | additional threat bonus from attack power |

**Description of the table's fields**

### entry

The spell ID. See [Spell.dbc](spell).

### flatMod

A flat amount of threat added by this spell (or removed if negative). `NULL` if no flat modifier applies.

### pctMod

Threat multiplier applied to the damage or healing done by this spell. Default `1`.

### apPctMod

Additional threat bonus derived from the caster's attack power. Default `0`.
