# spell\_threat

[<-Back-to:World](database-world)

**The \`spell\_threat\` table**

This table holds threat values on all spells that should either give or take away threat.

**Table Structure**

| Field       | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]    | MEDIUMINT | UNSIGNED   | PRI | NO   | NULL    |       |                                           |
| [flatMod][2]  | INT       | SIGNED     |     | YES  | NULL    |       |                                           |
| [pctMod][3]   | FLOAT     |            |     | NO   | 1       |       | threat multiplier for damage/healing      |
| [apPctMod][4] | FLOAT     |            |     | NO   | 0       |       | additional threat bonus from attack power |

[1]: #entry
[2]: #flatmod
[3]: #pctmod
[4]: #appctmod

**Description of the fields**

### entry

The spell ID. See [Spell.dbc](spell).

### flatMod

A flat amount of threat added by this spell (or removed if negative). `NULL` if no flat modifier applies.

### pctMod

Threat multiplier applied to the damage or healing done by this spell. Default `1`.

### apPctMod

Additional threat bonus derived from the caster's attack power. Default `0`.
