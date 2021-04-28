# spell\_group

[<-Back-to:World](database-world.md)

**The \`spell\_group\` table**

Table used to group spells for varius checks in the core. One spell may be added to many groups, but can occur in one group only once.

| Field         | Type    | Attributes | Key | Null | Default | Extra | Comment |
|---------------|---------|------------|-----|------|---------|-------|---------|
| [id][1]       | INT(11) | UNSIGNED   | PRI | NO   | 0       |       |         |
| [spell_id][2] | INT(11) | SIGNED     | PRI | NO   | 0       |       |         |

[1]: #id
[2]: #spell_id

**Description of the fields**

### id

Group identifier
Rules of assigning id:

-   if group is going to be used in core code, use first avalible entry below 1000 and add enum value to SpellGroup enum in SpellMgr.h
-   if group is not going to be used in core code, use lowest avalible entry higher than 1000

### spell\_id

SpellId from Spell.dbc or spell\_group id prefixed with "-". If spell is added to spell\_ranks, spell\_id has to be first rank of that spell.
