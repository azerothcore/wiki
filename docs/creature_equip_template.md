# creature\_equip\_template

[<-Back-to:World](database-world)

## **Table: creature\_equip\_template**

This table contains all the equipment combinations that can be sent for each creature.

## Structure

| Field           | Type      | Attributes | Key | Null | Default | Extra | Comment      |
| --------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------ |
| [CreatureID][1] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Unique entry |
| [ID][2]         | TINYINT   | UNSIGNED   | PRI | NO   | 1       |       | Unique entry |
| [ItemID1][3]    | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |              |
| [ItemID2][4]    | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |              |
| [ItemID3][5]    | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |              |

[1]: #creatureid
[2]: #id
[3]: #itemid1
[4]: #itemid2
[5]: #itemid3

## Description of the fields

### CreatureID

The direct corresponding [id](http://www.azerothcore.org/wiki/creature#id) in [creature](creature) table or [entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry) in [creature\_template](creature_template) table.

### ID

An additional identifier for each individual entry, enabling multiple equipment for one creature entry. Counter **must** start with 1 and grow accordingly.

### ItemID1

This is the item number of the equipment used in the right hand from [Item.dbc](Item).

### ItemID2

This is the item number of the equipment used in the left hand from [Item.dbc](Item).

### ItemID3

This is the item number of the equipment used in the ranged slot from [Item.dbc](Item).
