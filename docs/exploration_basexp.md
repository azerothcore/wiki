# exploration\_basexp

[<-Back-to:World](database-world)

This table holds the base experience point information needed for when a player explores a new zone.

**Table: exploration\_basexp's Structure**

| Field             | Type    |          | Null | Key | Default | Extra | Comment |
| :---------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [level](#level)   | TINYINT | UNSIGNED | NO   | PRI | 0       |       |         |
| [basexp](#basexp) | INT     |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### level
The player level.

### basexp
The base experience the player will receive when he or she discovers a new zone at the level specified in the level field.
