# spell\_script\_names

[<-Back-to:World](database-world)

**The \`spell\_script\_names\` table**

Holds the spell id to ScriptName pairings for use in spell scripts.

**Table: spell\_script\_names's Structure**

| Field                     | Type     |     | Null | Key | Default | Extra | Comment |
| :------------------------ | :------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [spell_id](#spellid)      | INT      |     | NO   | MUL |         |       |         |
| [ScriptName](#scriptname) | CHAR(64) |     | NO   |     |         |       |         |

**Description of the table's fields**

### spell\_id

The ID of the spell to link. If it is negative and the first rank of a spell, includes all ranks of the spell specified in spell\_ranks table.

One spell can have more than one script assigned.

### ScriptName

The script name for the given spell(s).
