# areatrigger

[<-Back-to:World](database-world.md)

**The \`areatrigger\` table**

This table contains trigger points for events in certain coordinates in the maps.

**Structure**

| Field             | Type     | Attributes | Key | Null | Default | Extra          | Comment |
|-------------------|----------|------------|-----|------|---------|----------------|---------|
| [entry][1]        | int (10) | unsigned   | PRI | NO   | NULL    | auto_increment |         |
| [map][2]          | int(10)  | unsigned   | PRI | NO   | 0       |                |         |
| [x][3]            | FLOAT    |            |     | NO   | 0       |                |         |
| [y][4]            | FLOAT    |            |     | NO   | 0       |                |         |
| [z][5]            | FLOAT    |            |     | NO   | 0       |                |         |
| [radius][6]       | FLOAT    |            |     | NO   | 0       |                |         |
| [length][7]       | FLOAT    |            |     | NO   | 0       |                |         |
| [width][8]        | FLOAT    |            |     | NO   | 0       |                |         |
| [height][9]       | FLOAT    |            |     | NO   | 0       |                |         |
| [orientation][10] | FLOAT    |            |     | NO   | 0       |                |         |

[1]: #entry
[2]: #map
[3]: #x
[4]: #y
[5]: #z
[6]: #radius
[7]: #length
[8]: #width
[9]: #height
[10]: #orientation

**Description of the fields**

### Entry

This is just a automatic counter that assigns a value to each trigger to list it.

### Map

This field recall a certain map based on the ID (for example, ID 30 recalls Elwynn Forest)

### X, Y and Z

Contains the coordinates of the three 3d dimensions.

### Radius

This contains the radius of activation of the trigger.

### Length, Width, Height and Orientation

these fields contain the values for the physics and behavior of a given trigger.
