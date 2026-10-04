# spell\_group

[<-Back-to:World](database-world)

**The \`spell\_group\` table**

Table used to group spells for varius checks in the core. One spell may be added to many groups, but can occur in one group only once.

**Table: spell\_group's Structure**

| Field                | Type |          | Null | Key | Default | Extra | Comment |
| :------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [id](#id)            | INT  | UNSIGNED | NO   | PRI | 0       |       |         |
| [spell_id](#spellid) | INT  |          | NO   | PRI |         |       |         |

**Description of the table's fields**

### id

Group identifier
Rules of assigning id:

-   if group is going to be used in core code, use first avalible entry below 1000 and add enum value to SpellGroup enum in [SpellMgr.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Spells/SpellMgr.h)
-   if group is not going to be used in core code, use lowest avalible entry higher than 1000

### spell\_id

SpellId from Spell.dbc or spell\_group id prefixed with "-". If spell is added to spell\_ranks, spell\_id has to be first rank of that spell.
