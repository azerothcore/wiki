# playercreateinfo

[<-Back-to:World](database-world.md)

**The \`playercreateinfo\` table**

This table holds the start positions of each class-race combinations for all newly created characters.

**Structure**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment |
|------------------|--------------|------------|-----|------|---------|-------|---------|
| [race][1]        | tinyint(3)   | unsigned   | PRI | NO   | 0       |       |         |
| [class][2]       | tinyint(3)   | unsigned   | PRI | NO   | 0       |       |         |
| [map][3]         | smallint(5)  | unsigned   |     | NO   | 0       |       |         |
| [zone][4]        | mediumint(8) | unsigned   |     | NO   | 0       |       |         |
| [position_x][5]  | float        | signed     |     | NO   | 0       |       |         |
| [position_y][6]  | float        | signed     |     | NO   | 0       |       |         |
| [position_z][7]  | float        | signed     |     | NO   | 0       |       |         |
| [orientation][8] | float        | signed     |     | NO   | 0       |       |         |

[1]: #race
[2]: #class
[3]: #map
[4]: #zone
[5]: #position_x
[6]: #position_y
[7]: #position_z
[8]: #orientation

**Description of the fields**

### race

The character's race. `ChrRaces.dbc`

### class

The character's class. `ChrClasses.dbc`

### map

The map ID. See [Map.dbc](Map)

### zone

The zone ID. See [AreaTable.dbc](AreaTable)

### position\_x

The X position.

### position\_y

The Y position.

### position\_z

The Z position.

### orientation

The orientation.
