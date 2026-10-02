# exploration\_basexp

[<-Back-to:World](database-world)

This table holds the base experience point information needed for when a player explores a new zone.

**Table: exploration\_basexp's Structure**

| Field       | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [level][1]  | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [basexp][2] | INT     | SIGNED     |     | NO   | 0       |       |         |

[1]: #level
[2]: #basexp

**Description of the table's fields**

### level
The player level.

### basexp
The base experience the player will receive when he or she discovers a new zone at the level specified in the level field.
