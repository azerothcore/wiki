# game\_graveyard

[<-Back-to:World](database-world)

**The \`game\_graveyard\` table**

**Table: game\_graveyard's Structure**

| Field               | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)           | INT          | SIGNED     | PRI | NO   | 0       |       |         |
| [Map](#map)         | INT          | SIGNED     |     | NO   | 0       |       |         |
| [x](#x)             | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [y](#y)             | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [z](#z)             | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [Comment](#comment) | VARCHAR(255) |            |     | YES  | NULL    |       |         |

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
