# waypoint\_data\_addon

[<-Volver a:World](database-world)

**Tabla \`waypoint\_data\_addon\`**

Proporciona puntos de interpolación spline intermedios personalizados para las rutas de waypoints que tienen `smoothTransition = 1` en [waypoint\_data](waypoint_data). Estos puntos dan forma a la curva spline catmullrom que sigue una creature entre sus waypoints principales.

**Estructura**

| Field                                   | Type | Attributes | Key | Null | Default |
| --------------------------------------- | ---- | ---------- | --- | ---- | ------- |
| [PathID](#pathid)                       | INT  | UNSIGNED   | PRI | NO   |         |
| [PointID](#pointid)                     | INT  | UNSIGNED   | PRI | NO   |         |
| [SplinePointIndex](#splinepointindex)   | INT  | UNSIGNED   | PRI | NO   |         |
| [PositionX](#positionx)                 | FLOAT |           |     | NO   | 0       |
| [PositionY](#positiony)                 | FLOAT |           |     | NO   | 0       |
| [PositionZ](#positionz)                 | FLOAT |           |     | NO   | 0       |

**Descripción de los campos**

### PathID

El ID de la ruta de waypoints. Referencia a [waypoint\_data.id](waypoint_data#id).

### PointID

El número de punto del waypoint. Referencia a [waypoint\_data.point](waypoint_data#point).

### SplinePointIndex

El índice de este punto spline intermedio dentro del segmento entre el waypoint referenciado y el siguiente. Se pueden definir varios puntos intermedios por segmento de waypoint incrementando este índice.

### PositionX

La coordenada X del punto spline intermedio.

### PositionY

La coordenada Y del punto spline intermedio.

### PositionZ

La coordenada Z del punto spline intermedio.
