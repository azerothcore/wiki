# game_graveyard

[<-Volver a:World](database-world)

**Tabla \`game_graveyard\`**

| Field               | Type         | Key | Null | Default |
| ------------------- | ------------ | --- | ---- | ------- |
| [ID](#id)           | INT          | PRI | NO   | 0       |
| [Map](#map)         | INT          |     | NO   | 0       |
| [x](#x)             | FLOAT        |     | NO   | 0       |
| [y](#y)             | FLOAT        |     | NO   | 0       |
| [z](#z)             | FLOAT        |     | NO   | 0       |
| [Comment](#omment) | VARCHAR(255) |     | YES  | NULL    |

**Descripción de los campos**

### ID
ID del cementerio. Ver [WorldSafeLocs.dbc](worldsafelocs)

### Map
ID de la zona de la posición del fantasma antes de la teletransportación al cementerio. Ver Map.dbc columna 1

### x

La posición X del cementerio a la que se teletransporta el fantasma del personaje.

### y

La posición Y del cementerio a la que se teletransporta el fantasma del personaje.

### z

La posición Z del cementerio a la que se teletransporta el fantasma del personaje.

### Comment

Comentario personalizado para esta línea.
