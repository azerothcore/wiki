# spell\_ranks

[<-Back-to:World](database-world)

**The \`spell\_ranks\` table**

Table used by the core to group different ranks of spells (the gray text seen on ranked spells) into one "spell stem". This partly involves checks for aura stacking (e.g. different levels of the same spell). One spell can not be linked to multiple rank chains (they are "unique").

**Table: spell\_ranks's Structure**

| Field                           | Type    |          | Null | Key | Default | Extra | Comment |
| :------------------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [first_spell_id](#firstspellid) | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [spell_id](#spellid)            | INT     | UNSIGNED | NO   | UNI | 0       |       |         |
| [rank](#rank)                   | TINYINT | UNSIGNED | NO   | PRI | 0       |       |         |

**Description of the table's fields**

### first\_spell\_id

SpellId from [Spell.dbc](spell) which is first rank of spell rank chain. It identifies the whole chain.

### spell\_id

SpellId from [Spell.dbc](spell).

### rank

An integer which ranks the spell within the chain of spell ranks for the given \`spell\_id\`. It can differ from the rank text in game (for example, some ranks in client start with level 0, while the server always starts from level 1 onward). Several conditions have to be fulfilled:

-   At least two levels are required
-   There can be no jumps between ranks (e.g. one spell being level 3 and one being level 5 while level 4 is missing altogether)
-   There can be no duplicates in ranks.
