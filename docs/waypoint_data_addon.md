# waypoint\_data\_addon

[<-Back-to:World](database-world)

**The \`waypoint\_data\_addon\` table**

Provides custom intermediate spline interpolation points for waypoint paths that have `smoothTransition = 1` set in [waypoint\_data](waypoint_data). These points shape the catmullrom spline curve a creature follows between its main waypoints.

**Table: waypoint\_data\_addon's Structure**

| Field                                 | Type  |          | Null | Key | Default | Extra | Comment |
| :------------------------------------ | :---- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [PathID](#pathid)                     | INT   | UNSIGNED | NO   | PRI |         |       |         |
| [PointID](#pointid)                   | INT   | UNSIGNED | NO   | PRI |         |       |         |
| [SplinePointIndex](#splinepointindex) | INT   | UNSIGNED | NO   | PRI |         |       |         |
| [PositionX](#positionx)               | FLOAT |          | NO   |     | 0       |       |         |
| [PositionY](#positiony)               | FLOAT |          | NO   |     | 0       |       |         |
| [PositionZ](#positionz)               | FLOAT |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### PathID

The waypoint path ID. References [waypoint\_data.id](waypoint_data#id).

### PointID

The waypoint point number. References [waypoint\_data.point](waypoint_data#point).

### SplinePointIndex

The index of this intermediate spline point within the segment between the referenced waypoint and the next. Multiple intermediate points can be defined per waypoint segment by incrementing this index.

### PositionX

The X coordinate of the intermediate spline point.

### PositionY

The Y coordinate of the intermediate spline point.

### PositionZ

The Z coordinate of the intermediate spline point.
