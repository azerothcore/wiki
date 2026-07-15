# waypoints

[<-Volver a:World](database-world)

**Tabla \`waypoints\`**

Usada por [SAI](smart_scripts)

Contiene datos de waypoints, permitiendo a las creatures moverse a ciertas coordenadas X, Y y Z. Consulta también [Waypoints-Information](Waypoints-Information) para información general sobre waypoints.

**Estructura**

| Field                            | Type      | Attributes | Key | Null | Default |
| -------------------------------- | --------- | ---------- | --- | ---- | ------- |
| [entry](#entry)                  | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |
| [pointid](#pointid)              | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |
| [position\_x](#positionx)        | FLOAT     |            |     | NO   | 0       |
| [position\_y](#positiony)        | FLOAT     |            |     | NO   | 0       |
| [position\_z](#positionz)        | FLOAT     |            |     | NO   | 0       |
| [orientation](#orientation)      | FLOAT     |            |     | YES  | NULL    |
| [point\_comment](#point_comment) | text      |            |     | YES  | NULL    |

**Descripción de los campos**

#### entry

ID de la ruta. La forma estándar de asignar un ID es [creature\_template.entry](creature_template#entry) * 100, pero aquí se puede usar cualquier número aleatorio.

#### pointid

ID único para cada waypoint. Empieza en 1 y aumenta con cada waypoint.

#### position\_x

La coordenada X del waypoint de destino.

#### position\_y

La coordenada Y del waypoint de destino.

#### position\_z

La coordenada Z del waypoint de destino.

#### orientation

#### point\_comment

Comentario de texto.

### Example Rows

| entry | pointid | position\_x | position\_y | position\_z | point\_comment           |
| ----- | ------- | ----------- | ----------- | ----------- | ------------------------ |
| 16208 | 1       | 6647.83     | -6344.92    | 9.13345     | Apothecary Enith point 1 |
| 16208 | 2       | 6657.92     | -6345.96    | 15.3468     | Apothecary Enith point 2 |

La creature con ID 16208 tendrá ahora 2 waypoints; primero se moverá al pointid 1, y cuando alcance la posición XYZ, se moverá al pointid 2. El comentario ayuda a aclarar a qué creature pertenece el ID.
