# graveyard\_zone

[<-Back-to:World](database-world)

**The \`graveyard\_zone\` table**

Contains information about zones connected to world's graveyards.

This table is used to set what factions a given graveyard will accept, and also to specify the nearest graveyard to a given zone.

For a list of all existing graveyard zones and their respective IDs, check out WorldSafeLocs.dbc

**Table: graveyard\_zone's Structure**

| Field                   | Type     |          | Null | Key | Default | Extra | Comment |
| :---------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)               | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [GhostZone](#ghostzone) | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [Faction](#faction)     | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |
| [Comment](#comment)     | TEXT     |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### ID

Graveyard's ID. See WorldSafeLocs.dbc

### GhostZone

Zone's Id of ghost position before teleportation to graveyard. See AreaTable.dbc

### Faction

Graveyard's team.

0 - Any team accepted

469 - Alliance team only

67 - Horde team only

### Comment

A human-readable comment describing this graveyard zone entry.
