# spell\_target\_position

[<-Back-to:World](database-world)

**The \`spell\_target\_position\` table**

This table holds coordinate information on where the player should be teleported to when a spell with target type: TARGET\_DST\_DB(17).

**Table Structure**

| Field                   | Type      | Attributes | Key | Null | Default | Extra | Comment    |
| ----------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------- |
| [id][1]                 | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Identifier |
| [target_map][2]         | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |            |
| [target_position_x][3]  | FLOAT     | SIGNED     |     | NO   | 0       |       |            |
| [target_position_y][4]  | FLOAT     | SIGNED     |     | NO   | 0       |       |            |
| [target_position_z][5]  | FLOAT     | SIGNED     |     | NO   | 0       |       |            |
| [target_orientation][6] | FLOAT     | SIGNED     |     | NO   | 0       |       |            |

[1]: #id
[2]: #targetmap
[3]: #targetpositionx
[4]: #targetpositiony
[5]: #targetpositionz
[6]: #targetorientation

**Description of the fields**

### id

The spell ID. See [Spell.dbc](Spell)

### target\_map

Map where the player should be teleported to. See [Map.dbc](Map).

### target\_position\_x

X coordinate for the target destination of the spell.

### target\_position\_y

Y coordinate for the target destination of the spell.

### target\_position\_z

Z coordinate for the target destination of the spell.

### target\_orientation

Orientation the player will get when appearing at this location
