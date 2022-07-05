# Waypoints y rutas

### Diferentes tipos de rutas de waypoints

- Las rutas de los puntos de ruta adjuntadas directamente a una criatura a través de [creature_addon.path_id](creature_addon#path_id) utilizan las tablas [waypoint_data](waypoint_data) y [waypoint_scripts](waypoint_scripts). Se pueden añadir utilizando el comando de GM `.wp`.
- [SmartAI](smart_scripts) utilizan rutas de waypoints definidas en la tabla [waypoints](waypoints).
- La tabla [script_waypoint](script_waypoint) contiene rutas de waypoints para [CreatureAI](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/AI/ScriptedAI/ScriptedCreature.h#L159).

### Resumen de los comandos GM `.wp`.

- ```.wp add``` [waypoint_data.id](waypoint_data#id): Añade un nuevo punto para el id de ruta especificado. Se recomienda utilizar el GUID de la criatura * 10 o el GUID * 100 como id de la ruta, pero puede ser cualquier número aleatorio.
- ```.wp reload``` [waypoint_data.id](waypoint_data#id): Recarga el id de camino especificado (para nuevos caminos tiene que ser ejecutado antes de `.wp load`).
- ```.wp load``` [waypoint_data.id](waypoint_data#id): Carga el id de camino especificado para la criatura seleccionada.
- ```.wp unload```: Elimina la trayectoria de la criatura seleccionada.
- ```.wp show on``` [waypoint_data.id](waypoint_data#id): Muestra todos los waypoints de la ruta especificada (se requiere GM on para verlos realmente). Si no se especifica ningún id de ruta muestra los waypoints de la criatura seleccionada.
- ```.wp show off```: Ocultar todos los waypoints visuales.
- ```.wp show info```: Mostrar información sobre el waypoint seleccionado.
- ```.wp modify```: Modificar el waypoint seleccionado, opciones:
  - ```del```: Eliminar el waypoint seleccionado.
  - ```move```: Mueve el waypoint seleccionado a la posición del GM.
  - ```delay```: Cambia el [retraso](waypoint_data#delay) del waypoint seleccionado.
  - ```action```: Cambiar la [acción](scripts#id) del waypoint seleccionado.
  - ```action_chance```: Cambia la [action_chance](waypoint_data#action_chance) del waypoint seleccionado.
  - ```move_type```: Cambia el [tipo de movimiento](waypoint_data#move_type) del waypoint seleccionado (0: caminar, 1: correr, 2: volar).
- ```.wp event```: Modificar el waypoint [acciones](scripts#id), opciones:
  - ```add``` [guid](scripts#guid): Añade una nueva acción con el GUID especificado (¡no confundir con el GUID de la criatura!). Si no se especifica un GUID, se genera uno nuevo automáticamente.
  - ```listid``` [acción](scripts#id): Muestra información sobre el id de la acción especificada.
  - ```del``` [guid](scripts#guid): Elimina la acción con el GUID especificado.
  - ```mod``` [guid](scripts#guid): Modifica la acción con el GUID especificado, más opciones:
    - ```setid``` [acción](scripts#id): Establece un nuevo id de acción.
    - ```delay``` [retraso](scripts#delay): Establece un retardo específico antes de que el script se active.
    - ```command``` [comando](scripts#command): Establece el comando para este script.
    - ```datalong``` [datalong](scripts#datalong): Establece el datalong para este script.
    - ```datalong2``` [datalong2](scripts#datalong2): Establece el datalong2 para este script.
    - ```dataint``` [dataint](scripts#dataint): Establece el dataint para este script.
    - ```posx``` [posx](scripts#posx): Establece la posición en x para este script.
    - ```posy``` [posy](scripts#posy): Establece la posición en y para este script.
    - ```posz``` [posz](scripts#posz): Establece la posición en z para este script.
    - ```orientation``` [orientation](scripts#orientation): Establece la orientación para este script.

### Ejemplo de creación de una ruta con los comandos GM `.wp`

Ejemplo de criatura GUID: `1234567`, ejemplo de ruta de acceso: `123456700`

- Crea un macro `wp1` con este comando:

```
.wp add 123456700
```

- Crea un macro `wp2` con estos comandos:

```
.wp reload 123456700
.wp load 123456700
```

- Crea un macro `wp3` con este comando:

```
.wp show on 123456700
```

- Crea un macro `wp4` con este comando:

```
.wp show off 123456700
```

- Teletransporte a la criatura:

```
.go creature 1234567
```

- Utilizar la macro `wp1`
- Crea el camino:
  - Ve a la posición donde debería estar el siguiente waypoint y utiliza la macro 'wp1'
  - Repita la operación hasta que todos los puntos de ruta estén fijados (no olvide crear también una ruta de vuelta a la posición inicial)
  - Utilizar las macros 'wp3' y 'wp4' para mostrar/ocultar la ruta (se requiere GM on para ver realmente la ruta)
  - Asegúrese de que los puntos de ruta no están demasiado lejos unos de otros, especialmente si la criatura está caminando sobre colinas, etc., ya que tratará de moverse directamente al siguiente punto de ruta, incluso si esto significa pasar por el suelo.
- Selecciona la criatura y utiliza la macro `wp2`. Ahora debería empezar a moverse

### Algunas sentencias SQL útiles

#### Borrar ruta

- Selecciona la criatura y elimina el camino:

```
.wp unload
```

- Borre la ruta de la base de datos, por ejemplo 123456700:

```sql
DELETE FROM `waypoint_data` WHERE `id` = 123456700;
```

#### Trasladar los waypoints de 'waypoint_data' a 'waypoints' (SmartAI)

Si necesita los waypoints para SmartAI tiene que copiar los waypoints de la tabla [waypoint_data](waypoint_data) en la tabla [waypoints](waypoints) y luego borrar los waypoints originales (elimine la ruta para la criatura a través de `.wp unload` si estaba cargada antes). Aquí un ejemplo para la ruta 123456700:

```sql
INSERT INTO `waypoints` (`entry`,`pointid`,`position_x`,`position_y`,`position_z`)

SELECT `id`,`point`,`position_x`,`position_y`,`position_z` FROM `waypoint_data` WHERE `id` = 123456700;

DELETE FROM `waypoint_data` WHERE `id` = 123456700;
```

#### Trasladar los waypoints de 'waypoint_data' a 'script_waypoint' (CreatureAI)

Lo mismo que arriba, pero ahora para [script_waypoint](script_waypoint) en lugar de [waypoints](waypoints). La entrada de [script_waypoint](script_waypoint) tiene que ser la [creature_template.entry](creature_template#entry), aquí por ejemplo 1234567:

```sql
INSERT INTO `script_waypoint` (`entry`,`pointid`,`location_x`,`location_y`,`location_z`)

SELECT 1234567 AS `entry`,`point`,`position_x`,`position_y`,`position_z` FROM `waypoint_data` WHERE `id` = 123456700;

DELETE FROM `waypoint_data` WHERE `id` = 123456700;
```

No te olvides de eliminar el camino de la criatura si se cargó antes.


### Mejores prácticas de trazado de rutas

Cuando se crean trayectorias a lo largo de una pendiente, se puede minimizar el recorte del terreno manteniendo la línea de visión.

![waypoints](https://i.imgur.com/s045BKp.png)
