# spell\_threat

[<-Back-to:World](database-world.md)

**The \`spell\_threat\` table**

This table holds threat values on all spells that should either give or take away threat.

**Structure**

| Field       | Type         | Attributes | Key | Null | Default | Extra | Comment |
|-------------|--------------|------------|-----|------|---------|-------|---------|
| [entry][1]  | MEDIUMINT(8) | unsigned   | PRI | NO   | NULL    |       |         |
| [Threat][2] | SMALLINT(6)  | signed     |     | NO   | NULL    |       |         |

[1]: #entry
[2]: #threat

**Description of the fields**

### entry

The spell ID. See [Spell.dbc](Spell).

### Threat

The threat value that this spells should add to the caster (or take away if it is negative).
