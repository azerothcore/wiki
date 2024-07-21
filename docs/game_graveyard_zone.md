# game_graveyard_zone

[<-Back-to:World](database-world)

**The \`game_graveyard_zone\` table**

| Field           | Type      | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]         | MEDIUMINT | unasigned  | PRI | NO   | 0       |       |         |
| [ghost_zone][2] | MEDIUMINT | unasigned  | PRI | NO   | 0       |       |         |
| [faction][3]    | SMALLINT  | unasigned  |     | NO   | 0       |       |         |

[1]: #id
[2]: #ghostzone
[3]: #faction

**Description of the fields**

### id
Graveyard's ID. See [WorldSafeLocs.dbc](WorldSafelocs)

### ghost_zone
Zone's ID of ghost position before teleportation to graveyard. See [AreaTable.dbc](AreaTable)

### faction
Graveyard's team.

0 - Any team accepted

469 - Alliance team only

67 - Horde team only
