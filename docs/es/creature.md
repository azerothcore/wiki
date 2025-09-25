# creature

[<-Volver a:World](database-world)

**Estructura**

Contiene datos de generación de criaturas individuales para cada generación individual de cada criatura individual en el mundo del juego.

| Campo                 | Tipo     | Atributos | Llave | Nulo | Por defecto | Extra                 | Comentario                                                            |
| --------------------- | -------- | --------- | ----- | ---- | ----------- | --------------------- | --------------------------------------------------------------------- |
| [guid][1]             | INT      | UNSIGNED  | PRI   | NO   | NULL        | Incremento automático | Identificador único global                                            |
| [id1][2]              | INT      | UNSIGNED  |       | NO   | 0           |                       | Identificador de criatura                                             |
| [id2][3]              | INT      | UNSIGNED  |       | NO   | 0           |                       | Identificador de criatura                                             |
| [id3][4]              | INT      | UNSIGNED  |       | NO   | 0           |                       | Identificador de criatura                                             |
| [map][5]              | SMALLINT | UNSIGNED  |       | NO   | 0           |                       | Identificador de mapa                                                 |
| [zoneId][6]           | SMALLINT | UNSIGNED  |       | NO   | 0           |                       | Identificador de zona                                                 |
| [areaId][7]           | SMALLINT | UNSIGNED  |       | NO   | 0           |                       | Identificador de área                                                 |
| [spawnMask][8]        | TINYINT  | UNSIGNED  |       | NO   | 1           |                       |                                                                       |
| [phaseMask][9]        | SMALLINT | UNSIGNED  |       | NO   | 1           |                       |                                                                       |
| [equipment_id][10]    | TINYINT  | UNSIGNED  |       | NO   | 1           |                       |                                                                       |
| [position_x][11]      | FLOAT    | SIGNED    |       | NO   | 0           |                       |                                                                       |
| [position_y][12]      | FLOAT    | SIGNED    |       | NO   | 0           |                       |                                                                       |
| [position_z][13]      | FLOAT    | SIGNED    |       | NO   | 0           |                       |                                                                       |
| [orientation][14]     | FLOAT    | SIGNED    |       | NO   | 0           |                       |                                                                       |
| [spawntimesecs][15]   | INT      | UNSIGNED  |       | NO   | 120         |                       |                                                                       |
| [wander_distance][16] | FLOAT    | SIGNED    |       | NO   | 5           |                       | Dist en yardas para movimiento aleatorio.                             |
| [currentwaypoint][17] | INT      | UNSIGNED  |       | NO   | 0           |                       | Almacenamiento utilizado por el núcleo. "Siempre configurado como 0". |
| [curhealth][18]       | INT      | UNSIGNED  |       | NO   | 1           |                       | Almacenamiento utilizado por el núcleo. "Siempre establecido como 1"  |
| [curmana][19]         | INT      | UNSIGNED  |       | NO   | 0           |                       | Almacenamiento utilizado por el núcleo. "Siempre configurado como 0". |
| [MovementType][20]    | TINYINT  | UNSIGNED  |       | NO   | 0           |                       | 0 Sin movimiento, 1 aleatorio, 2 camino                               |
| [npcflag][21]         | INT      | UNSIGNED  |       | NO   | 0           |                       | creature_template anular                                              |
| [unit_flags][22]      | INT      | UNSIGNED  |       | NO   | 0           |                       | creature_template anular                                              |
| [dynamicflags][23]    | INT      | UNSIGNED  |       | NO   | 0           |                       | creature_template anular                                              |
| [ScriptName][24]      | CHAR     |           |       | SI   | NULL        |                       |                                                                       |
| [VerifiedBuild][25]   | INT      | SIGNED    |       | SI   | NULL        |                       | No utilizado por el núcleo                                            |
| [CreateObject][26]    | TINYINT  | UNSIGNED  |       | NO   | 0           |                       | No utilizado por el núcleo                                            |
| [Comment][27]         | TEXT     |           |       | SI   | NULL        |                       | No utilizado por el núcleo                                            |

[1]: #guid
[2]: #id1
[3]: #id2
[4]: #id3
[5]: #map
[6]: #zoneId
[7]: #areaId
[8]: #spawnmask
[9]: #phasemask
[10]: #equipmentid
[11]: #positionx
[12]: #positiony
[13]: #positionz
[14]: #orientation
[15]: #spawntimesecs
[16]: #wanderdistance
[17]: #currentwaypoint
[18]: #curhealth
[19]: #curmana
[20]: #movementtype
[21]: #npcflag
[22]: #unitflags
[23]: #dynamicflags
[24]: #scriptname
[25]: #verifiedbuild
[26]: #createobject
[27]: #comment

**Descripciones de campos**

### guid

Un identificador único asignado a cada criatura para distinguirla de otra. Dos criaturas no pueden tener el mismo GUID.

### id1

El ID principal de la [plantilla](creature_template#creature_template-entry) que se utiliza al crear una instancia de esta criatura.

### id2

El ID secundario de la [plantilla](creature_template#creature_template-entry) que se utiliza al crear una instancia de esta criatura.

### id3

El tercer ID de la [plantilla](creature_template#creature_template-entry) que se utiliza al crear una instancia de esta criatura.

### map

El ID del [mapa](Mapa) en el que se genera la criatura.

### zoneId

El ID de la zona en la que se genera la criatura (por ejemplo, Los Baldíos).

Esta columna la completa el servidor mundial al iniciarse si la opción `Calculate.Creature.Zone.Area.Data` está habilitada. Se origina en AreaTable.dbc.

### areaId

El ID del área donde se genera la criatura. Puedes pensar en un área como una "subzona" de una zona, por ejemplo, Oasis de Aguas Exuberantes dentro de Los Baldíos.

Esta columna la completa el servidor mundial al iniciarse si la opción `Calculate.Creature.Zone.Area.Data` está habilitada. Se origina en AreaTable.dbc.

### spawnMask

Controla las dificultades bajo las que se genera la criatura. Los valores están enmascarados, por lo que puedes sumarlos para combinar los efectos de dos o más valores.

Ejemplo:

4 + 8 = 12

La criatura aparecerá solo en las versiones heroicas de 10 y 25 jugadores del mapa en el que aparece la criatura.

| Valor | Comentario                                                                                     |
| ----- | ---------------------------------------------------------------------------------------------- |
| 0     | No generado                                                                                    |
| 1     | Aparece solo en versiones normales de mapas para 10 jugadores (incluye mapas sin modo heroico) |
| 2     | Aparece solo en versiones normales de mapas para 25 jugadores (o heroicas anteriores a la 3.2) |
| 4     | Aparece solo en versiones heroicas de mapas para 10 jugadores.                                 |
| 8     | Aparece solo en versiones heroicas de 25 jugadores de los mapas.                               |
| 15    | Aparece en todas las versiones de mapas.                                                       s|

### phaseMask

Este es un campo de máscara de bits que describe todas las fases en las que aparecerá una criatura. El aura 261 determina la fase que puedes ver. Por ejemplo, si tuvieras esta aura <http://www.wowhead.com/?spell=55782>, podrías ver criaturas en la fase 2. Si quisieras que la criatura fuera visible tanto en la fase 1 como en la fase 2, establecerías la máscara de fase en 3.

### equipment_id

El ID definido en [creature_equip_template](creature_equip_template) correspondiente a la [entry](creature_template). El valor "essential" define el equipamiento:

-   **-1**: Se elegirá un equipo aleatorio del conjunto de equipos en [creature_equip_template](creature_equip_template).
-   **0**: No hay ningún equipo definido.
-   **1+**: El ID individual dentro de creature_equip_template.

Si la criatura se generó con `.npc add`, este valor se establecerá automáticamente (0 si no hay nada en creature_equip_template).

### position_x

La posición X del punto de aparición de las criaturas.

### position_y

La posición Y del punto de aparición de las criaturas.

### position_z

La posición Z del punto de aparición de las criaturas.

### orientation

La orientación del punto de aparición de las criaturas. (Norte = 0,0; Sur = pi (3,14159))

### spawntimesecs

El tiempo de reaparición, en segundos, de la criatura.

### wander_distance

La distancia máxima que la criatura puede generar desde su punto de aparición. También controla la distancia que puede recorrer la criatura desde su punto de aparición si su [Tipo de Movimiento](#creature-Movement Type) = 1.

### currentwaypoint

El [waypoint](waypoint_data#waypoint_data-point) actual en el que se encuentra la criatura, si hay alguno.

### curhealth

La salud con la que aparecerá la criatura.

### curmana

El maná con el que aparecerá la criatura.

### MovementType

El tipo de movimiento asociado a la criatura. Generalmente es el mismo que su [MovementType](creature_template#creature_template-MovementType), pero puede ser diferente.

### npcflag

Igual que [creature_template.npcflag](creature_template#creature_template-npcflag).

NOTA: Un registro creature.npcflag anulará un registro [creature_template.npcflag](creature_template#creature_template-npcflag).

### unit_flags

Lo mismo que creature_template.unit_flags.

Nota:

Un registro creature.unit_flags anulará un registro [creature_template.unit_flags](creature_template#creature_template-unit_flags).

### dynamicflags

Lo mismo que creature_template.dynamicflags.

Nota:

Un registro creature.dynamicflags anulará un registro [creature_template.dynamicflags](creature_template#creature_template-dynamicflags).

### ScriptName

Lo mismo que creature_template.scriptname.

Un registro creature.scriptname anulará un registro [creature_template.scriptname](creature_template#creature_template-scriptname).

### VerifiedBuild

Este campo se utiliza para determinar si esta criatura proviene de olfateos verificados.

Si el valor es 0, entonces no se ha analizado todavía o se ha heredado de una base de datos más antigua u otro núcleo.

Si el valor es superior a 0, se ha analizado con rastreos de esa compilación de cliente específica.

Si el valor es -Client Build, entonces se analizó con archivos WDB de esa compilación de cliente específica y luego se editó manualmente para satisfacer alguna necesidad especial.

### CreateObject

Este campo es específico para las criaturas y se utiliza para determinar si las posiciones están perfeccionadas.

Una vez que se detecta una criatura, el paquete puede ser CreateObject1 o CreateObject2.
Una criatura CO1 generalmente ya ha aparecido, se ha movido y, por lo tanto, se desvía de su posición de aparición real.
Se olió una criatura de CO2 cuando apareció, por lo que, en la mayoría de los casos, es su posición de aparición real.

Se utiliza un tercer valor para casos especiales, es decir, criaturas que no reaparecen normalmente, sino mediante scripts. Funciona igual que CO2 y solo se utiliza para distinguir mejor estos casos especiales.

### comment

Este campo sirve para agregar contexto adicional a esta criatura, principalmente en el contexto de valores rastreados o notas de script.

Por ejemplo, si fuera necesario modificar la posición de una criatura, las posiciones originales se conservan en el campo de comentarios. O si las criaturas en cuestión forman parte de un script más amplio, el comentario sirve como contexto.
