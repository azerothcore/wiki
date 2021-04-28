# spell\_script\_names

[<-Back-to:World](database-world.md)

**The \`spell\_script\_names\` table**

Holds the spell id to ScriptName pairings for use in spell scripts.

**Structure**

| Field           | Type     | Attributes | Key    | Null | Default | Extra | Comment |
|-----------------|----------|------------|--------|------|---------|-------|---------|
| [spell_id][1]   | INT(11)  | signed     | UNIQUE | NO   | NONE    |       |         |
| [ScriptName][2] | char(64) | unsigned   | UNIQUE | NO   | NONE    |       |         |

[1]: #spell_id
[2]: #scriptname

**Description of the fields**

### spell\_id

The ID of the spell to link. If it is negative and the first rank of a spell, includes all ranks of the spell specified in spell\_ranks table.

One spell can have more than one script assigned.

### ScriptName

The script name for the given spell(s).
