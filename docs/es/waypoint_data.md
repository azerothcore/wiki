# waypoint\_data

[<-Volver a:World](database-world)

**Tabla \`waypoint\_data\`**

Esta tabla contiene todos los datos de rutas para las creatures que usan waypoints y scripts de waypoint directamente en la definición de su creature addon. Consulta también [Waypoints-Information](Waypoints-Information) para información general sobre waypoints.

**Estructura**

| Field                                 | Type      | Attributes | Key | Null | Default |
| ------------------------------------- | --------- | ---------- | --- | ---- | ------- |
| [id](#id)                             | INT       | UNSIGNED   | PRI | NO   | 0       |
| [point](#point)                       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |
| [position\_x](#positionx)             | FLOAT     |            |     | NO   | 0       |
| [position\_y](#positiony)             | FLOAT     |            |     | NO   | 0       |
| [position\_z](#positionz)             | FLOAT     |            |     | NO   | 0       |
| [orientation](#orientation)           | FLOAT     |            |     | YES  | NULL    |
| [velocity](#velocity)                 | FLOAT     |            |     | NO   | 0       |
| [delay](#delay)                       | INT       | UNSIGNED   |     | NO   | 0       |
| [smoothTransition](#smoothtransition) | TINYINT   |            |     | NO   | 0       |
| [move\_type](#movetype)               | INT       |            |     | NO   | 0       |
| [action](#action)                     | INT       |            |     | NO   | 0       |
| [action\_chance](#actionchance)       | SMALLINT  |            |     | NO   | 100     |
| [wpguid](#wpguid)                     | INT       | UNSIGNED   |     | NO   | 0       |

**Descripción de los campos**

### id

ID único de cada ruta.

*La forma estándar de TDB de asignar un ID es multiplicar el GUID de la creature por 10.*

*Así que para una creature con un GUID de 1234 el ID de la ruta sería 12340. Cualquier waypoint enviado a TDB debería seguir este estándar.*

*Sin embargo, esto es solo una sugerencia al crear tus propios waypoints. Este ID puede ser lo que quieras siempre que creature\_addon.path\_id esté fijado al ID que elijas aquí para la creature a la que le estás creando un waypoint.*

### point

ID de punto único para cada punto de una ruta. Empieza en 1 y aumenta con cada ruta.

### position\_x

La coordenada X del waypoint de destino.

### position\_y

La coordenada Y del waypoint de destino.

### position\_z

La coordenada Z del waypoint de destino.

### orientation

La orientación de la creature. (Norte = 0.0; Sur = π (3.14159))

### velocity

Sobrescribe la velocidad de movimiento por defecto de la creature para este waypoint. Ponlo a `0` para usar la velocidad por defecto.

### delay

Tiempo de espera (en ms) entre cada punto.

### smoothTransition

Cuando está activado, la creature sigue una curva spline catmullrom suave a través de los waypoints en lugar de detenerse y girar bruscamente en cada punto. Se pueden añadir puntos spline intermedios personalizados a través de la tabla [waypoint\_data\_addon](waypoint_data_addon).

| Value | Description                                          |
| ----- | ---------------------------------------------------- |
| 0     | Desactivado (por defecto) — la creature se detiene en cada waypoint |
| 1     | Activado — curva spline suave entre waypoints        |

### move\_type

| Value | Name    | Description                                                    |
| ----- | ------- | -------------------------------------------------------------- |
| 0     | Walk    | La creature se mueve a velocidad de caminata.                  |
| 1     | Run     | La creature se mueve a velocidad de carrera (por defecto).     |
| 2     | Land    | Fija el nivel de animación a Ground (usado al aterrizar desde el vuelo). |
| 3     | Takeoff | Fija el nivel de animación a Hover (usado al despegar).        |

### action

ID de la acción a realizar. Ver [waypoint\_scripts.id](waypoint_scripts).

### action\_chance

Porcentaje de que la acción ocurra (0-100%).

### wpguid

Este campo lo usa el core y **NO** debe fijarse a mano.

Este campo contiene el GUID del visual del waypoint cuando activas el modo visual para los waypoints.

### Example Rows

| Id    | Point | Position\_x | Position\_y | Position\_z | Orientation | Velocity | Delay | SmoothTransition | Move\_type | Action | Action\_chance | wpguid |
| ----- | ----- | ----------- | ----------- | ----------- | ----------- | -------- | ----- | ---------------- | ---------- | ------ | -------------- | ------ |
| 20160 | 1     | -4998       | -1167       | 501657      | 0           | 0        | 10000 | 0                | 0          | 0      | 100            | 0      |
| 20160 | 2     | -4958.38    | -1199.34    | 501659      | 0           | 0        | 0     | 0                | 0          | 0      | 100            | 0      |
