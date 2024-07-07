# spell\_ranks

[<-Back-to:World](database-world)

**The \`spell\_ranks\` table**

Table used by the core to group different ranks of spells (the gray text seen on ranked spells) into one "spell stem". This partly involves checks for aura stacking (e.g. different levels of the same spell). One spell can not be linked to multiple rank chains (they are "unique").

**Table Structure**

| Field               | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [first_spell_id][1] | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [spell_id][2]       | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [rank][3]           | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #first_spell_id
[2]: #spell_id
[3]: #rank

**Description of the fields**

### first\_spell\_id

SpellId from [Spell.dbc](Spell) which is first rank of spell rank chain. It identifies the whole chain.

### spell\_id

SpellId from [Spell.dbc](Spell).

### rank

An integer which ranks the spell within the chain of spell ranks for the given \`spell\_id\`. It can differ from the rank text in game (for example, some ranks in client start with level 0, while the server always starts from level 1 onward). Several conditions have to be fulfilled:

-   At least two levels are required
-   There can be no jumps between ranks (e.g. one spell being level 3 and one being level 5 while level 4 is missing altogether)
-   There can be no duplicates in ranks.
