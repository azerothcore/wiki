# exploration_basexp

[<-Back-to:World](database-world)

This table holds the base experience point information needed for when a player explores a new zone.

| Field       | Type      | Attributes | Key | Null | Default |
| ----------- | --------- | ---------- | --- | ---- | ------- |
| [level][1]  | TINYINT   | UNSIGNED   | PRI | NO   | 0       |
| [basexp][2] | MEDIUMINT | SIGNED     |     | NO   | 0       |

[1]: #level
[2]: #basexp

**Description of the fields**

### level
The player level.

### basexp
The base experience the player will recieve when he or she discovers a new zone at the level specified in the level field.
