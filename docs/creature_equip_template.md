# creature\_equip\_template

[<-Back-to:World](database-world)

## **Table: creature\_equip\_template**

This table contains all the equipment combinations that can be sent for each creature.

**Table: creature\_equip\_template's Structure**

| Field                           | Type    |          | Null | Key | Default | Extra | Comment      |
| :------------------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :----------- |
| [CreatureID](#creatureid)       | INT     | UNSIGNED | NO   | PRI | 0       |       | Unique entry |
| [ID](#id)                       | TINYINT | UNSIGNED | NO   | PRI | 1       |       | Unique entry |
| [ItemID1](#itemid1)             | INT     | UNSIGNED | NO   |     | 0       |       |              |
| [ItemID2](#itemid2)             | INT     | UNSIGNED | NO   |     | 0       |       |              |
| [ItemID3](#itemid3)             | INT     | UNSIGNED | NO   |     | 0       |       |              |
| [VerifiedBuild](#verifiedbuild) | INT     |          | YES  |     | NULL    |       |              |

**Description of the table's fields**

### CreatureID

The direct corresponding [id](http://www.azerothcore.org/wiki/creature#id) in [creature](creature) table or [entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry) in [creature\_template](creature_template) table.

### ID

An additional identifier for each individual entry, enabling multiple equipment for one creature entry. Counter **must** start with 1 and grow accordingly.

### ItemID1

This is the item number of the equipment used in the right hand from [Item.dbc](https://wowdev.wiki/DB/Item).

### ItemID2

This is the item number of the equipment used in the left hand from [Item.dbc](https://wowdev.wiki/DB/Item).

### ItemID3

This is the item number of the equipment used in the ranged slot from [Item.dbc](https://wowdev.wiki/DB/Item).

### VerifiedBuild

Client build this row was verified against (from WDB/ADB extraction). `NULL` if not applicable.
