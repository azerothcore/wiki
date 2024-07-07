# game_graveyard

[<-Back-to:World](database-world)

**The \`game_graveyard\` table**

| Field               | Type         | Key | Null | Default |
| ------------------- | ------------ | --- | ---- | ------- |
| [ID](#id)           | INT          | PRI | NO   | 0       |
| [Map](#map)         | INT          |     | NO   | 0       |
| [x](#x)             | FLOAT        |     | NO   | 0       |
| [y](#y)             | FLOAT        |     | NO   | 0       |
| [z](#z)             | FLOAT        |     | NO   | 0       |
| [Comment](#omment) | VARCHAR(255) |     | YES  | NULL    |

**Description of the fields**

### ID
Graveyard's ID. See [WorldSafeLocs.dbc](WorldSafelocs)

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
