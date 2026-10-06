# spell\_cone

[<-Back-to:World](database-world)

**The \`spell\_cone\` table**

This table stores cone-angle overrides used by cone target selection.
When a row exists, the value from `spell_cone.ConeDegrees` is used as the cone angle (in degrees).
If no override exists, the core falls back to legacy hardcoded spell handling.

**Table: spell\_cone's Structure**

| Field                       | Type     |          | Null | Key | Default | Extra | Comment               |
| :-------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :-------------------- |
| [ID](#id)                   | INT      | UNSIGNED | NO   | PRI |         |       | Spell ID              |
| [ConeDegrees](#conedegrees) | SMALLINT |          | NO   |     | 60      |       | Cone angle in degrees |

**Description of the table's fields**

### id

Spell identifier this row applies to.

### ConeDegrees

Cone angle in degrees used by cone target selection. Schema default is 60.
