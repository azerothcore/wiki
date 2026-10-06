# game\_graveyard

[<-Back-to:World](database-world)

**The \`game\_graveyard\` table**

Holds the graveyard locations: map and coordinates.

**Table: game\_graveyard's Structure**

| Field               | Type         |     | Null | Key | Default | Extra | Comment |
| :------------------ | :----------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)           | INT          |     | NO   | PRI | 0       |       |         |
| [Map](#map)         | INT          |     | NO   |     | 0       |       |         |
| [x](#x)             | FLOAT        |     | NO   |     | 0       |       |         |
| [y](#y)             | FLOAT        |     | NO   |     | 0       |       |         |
| [z](#z)             | FLOAT        |     | NO   |     | 0       |       |         |
| [Comment](#comment) | VARCHAR(255) |     | YES  |     | NULL    |       |         |

**Description of the table's fields**

### ID
Graveyard's ID. See [WorldSafeLocs.dbc](https://wowdev.wiki/DB/WorldSafeLocs)

### Map
Zone's ID of ghost position before teleportation to graveyard. See Map.dbc column 1

### x

The X position of graveyard where the character's ghost gets teleported to.

### y

The Y position of graveyard where the character's ghost gets teleported to.

### z

The Z position of graveyard where the character's ghost gets teleported to.

### Comment

Custom comment for this line.
