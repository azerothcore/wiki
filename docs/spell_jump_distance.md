# spell\_jump\_distance

[<-Back-to:World](database-world)


**The \`spell\_jump\_distance\` table**

This table stores per-spell chain hop distance overrides. When present, the server loads `JumpDistance` and assigns it to `SpellInfo::JumpDistance`; `Spell::SearchChainTargets()` then uses this value to constrain chain-target hop radius.

**Table: spell\_jump\_distance's Structure**

| Field                         | Type  |          | Null | Key | Default | Extra | Comment                   |
| :---------------------------- | :---- | :------- | :--: | :-: | :-----: | :---: | :------------------------ |
| [ID](#id)                     | INT   | UNSIGNED | NO   | PRI |         |       | spell id                  |
| [JumpDistance](#jumpdistance) | FLOAT |          | NO   |     | 0       |       | max hop distance in yards |

**Description of the table's fields**

### ID

Spell identifier this row applies to. See [Spell.dbc](spell).

### JumpDistance

Maximum chain-hop distance (in yards) for the spell. When > 0 the server will use this value instead of the default jump radius when searching chain targets.
