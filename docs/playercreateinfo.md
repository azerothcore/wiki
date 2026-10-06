# playercreateinfo

[<-Back-to:World](database-world)

**The \`playercreateinfo\` table**

This table holds the start positions of each class-race combinations for all newly created characters.

**Table: playercreateinfo's Structure**

| Field                       | Type     |          | Null | Key | Default | Extra | Comment |
| :-------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [race](#race)               | TINYINT  | UNSIGNED | NO   | PRI | 0       |       |         |
| [class](#class)             | TINYINT  | UNSIGNED | NO   | PRI | 0       |       |         |
| [map](#map)                 | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |
| [zone](#zone)               | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [position_x](#positionx)    | FLOAT    |          | NO   |     | 0       |       |         |
| [position_y](#positiony)    | FLOAT    |          | NO   |     | 0       |       |         |
| [position_z](#positionz)    | FLOAT    |          | NO   |     | 0       |       |         |
| [orientation](#orientation) | FLOAT    |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### race

The character's race. `ChrRaces.dbc`

### class

The character's class. `ChrClasses.dbc`

### map

The map ID. See [Map.dbc](map)

### zone

The zone ID. See [AreaTable.dbc](areatable)

### position\_x

The X position.

### position\_y

The Y position.

### position\_z

The Z position.

### orientation

The orientation.
