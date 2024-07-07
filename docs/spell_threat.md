# spell\_threat

[<-Back-to:World](database-world)

**The \`spell\_threat\` table**

This table holds threat values on all spells that should either give or take away threat.

**Table Structure**

| Field       | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]  | MEDIUMINT | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [Threat][2] | SMALLINT  | SIGNED     |     | NO   | NULL    |       |         |

[1]: #entry
[2]: #threat

**Description of the fields**

### entry

The spell ID. See [Spell.dbc](Spell).

### Threat

The threat value that this spells should add to the caster (or take away if it is negative).
