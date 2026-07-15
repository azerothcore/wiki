# creature

[<-Volver a: World](database-world)

**Estructura**

Contiene los datos de generación de cada criatura individual para cada aparición individual de cada criatura del mundo de juego.

| Field                 | Type     | Attributes | Key | Null | Default | Extra          | Comment                                 |
| --------------------- | -------- | ---------- | --- | ---- | ------- | -------------- | --------------------------------------- |
| [guid][1]             | INT      | UNSIGNED   | PRI | NO   | NULL    | Auto Increment | Identificador único global              |
| [id1][2]              | INT      | UNSIGNED   |     | NO   | 0       |                | Identificador de criatura               |
| [id2][3]              | INT      | UNSIGNED   |     | NO   | 0       |                | Identificador de criatura               |
| [id3][4]              | INT      | UNSIGNED   |     | NO   | 0       |                | Identificador de criatura               |
| [map][5]              | SMALLINT | UNSIGNED   |     | NO   | 0       |                | Identificador de mapa                   |
| [zoneId][6]           | SMALLINT | UNSIGNED   |     | NO   | 0       |                | Identificador de zona                   |
| [areaId][7]           | SMALLINT | UNSIGNED   |     | NO   | 0       |                | Identificador de área                   |
| [spawnMask][8]        | TINYINT  | UNSIGNED   |     | NO   | 1       |                |                                         |
| [phaseMask][9]        | SMALLINT | UNSIGNED   |     | NO   | 1       |                |                                         |
| [equipment_id][10]    | TINYINT  | UNSIGNED   |     | NO   | 1       |                |                                         |
| [position_x][11]      | FLOAT    | SIGNED     |     | NO   | 0       |                |                                         |
| [position_y][12]      | FLOAT    | SIGNED     |     | NO   | 0       |                |                                         |
| [position_z][13]      | FLOAT    | SIGNED     |     | NO   | 0       |                |                                         |
| [orientation][14]     | FLOAT    | SIGNED     |     | NO   | 0       |                |                                         |
| [spawntimesecs][15]   | INT      | UNSIGNED   |     | NO   | 120     |                |                                         |
| [wander_distance][16] | FLOAT    | SIGNED     |     | NO   | 5       |                | Dist. en yardas para movimiento aleatorio. |
| [currentwaypoint][17] | INT      | UNSIGNED   |     | NO   | 0       |                | Almacenamiento usado por el core. "Siempre a 0" |
| [curhealth][18]       | INT      | UNSIGNED   |     | NO   | 1       |                | Almacenamiento usado por el core. "Siempre a 1" |
| [curmana][19]         | INT      | UNSIGNED   |     | NO   | 0       |                | Almacenamiento usado por el core. "Siempre a 0" |
| [MovementType][20]    | TINYINT  | UNSIGNED   |     | NO   | 0       |                | 0 sin movimiento, 1 aleatorio, 2 ruta   |
| [npcflag][21]         | INT      | UNSIGNED   |     | NO   | 0       |                | sobrescribe creature_template           |
| [unit_flags][22]      | INT      | UNSIGNED   |     | NO   | 0       |                | sobrescribe creature_template           |
| [dynamicflags][23]    | INT      | UNSIGNED   |     | NO   | 0       |                | sobrescribe creature_template           |
| [ScriptName][24]      | CHAR     |            |     | YES  | NULL    |                |                                         |
| [VerifiedBuild][25]   | INT      | SIGNED     |     | YES  | NULL    |                | No usado por el core.                   |
| [CreateObject][26]    | TINYINT  | UNSIGNED   |     | NO   | 0       |                | No usado por el core.                   |
| [Comment][27]         | TEXT     |            |     | YES  | NULL    |                | No usado por el core.                   |

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

**Descripción de los campos**

### guid

Un identificador único que se le da a cada criatura para distinguir una criatura de otra. Dos criaturas NO pueden tener el mismo GUID.

### id1

El ID principal de la [plantilla](creature_template#creature_template-entry) que se usa al instanciar esta criatura.

### id2

El ID secundario de la [plantilla](creature_template#creature_template-entry) que se usa al instanciar esta criatura.

### id3

El tercer ID de la [plantilla](creature_template#creature_template-entry) que se usa al instanciar esta criatura.

### map

El ID del [mapa](map) en el que se genera la criatura.

### zoneId

El ID de la zona en la que se genera la criatura. (p. ej. Los Baldíos)

Esta columna la rellena el worldserver al arrancar si la opción `Calculate.Creature.Zone.Area.Data` está habilitada. Proviene de AreaTable.dbc.

### areaId

El ID del área en la que se genera la criatura. Puedes pensar en un área como una "subzona" de una zona, p. ej. el Oasis Aguacristalina dentro de Los Baldíos.

Esta columna la rellena el worldserver al arrancar si la opción `Calculate.Creature.Zone.Area.Data` está habilitada. Proviene de AreaTable.dbc.

### spawnMask

Controla en qué dificultades se genera la criatura. Los valores son bit-mask, así que puedes sumarlos para combinar los efectos de dos o más valores.

Ejemplo:

4 + 8 = 12

La criatura solo se generará en las versiones heroicas de 10 y 25 jugadores del mapa en el que se genera.

| Value | Comment                                                                              |
| ----- | ------------------------------------------------------------------------------------ |
| 0     | No generada                                                                          |
| 1     | Generada solo en versiones normales de 10 jugadores de los mapas (incluye mapas sin modo heroico) |
| 2     | Generada solo en versiones normales de 25 jugadores de los mapas (o heroicas anteriores a 3.2) |
| 4     | Generada solo en versiones heroicas de 10 jugadores de los mapas                    |
| 8     | Generada solo en versiones heroicas de 25 jugadores de los mapas                    |
| 15    | Generada en todas las versiones de los mapas                                         |

### phaseMask

Este es un campo bit-mask que describe todas las fases en las que aparecerá una criatura. El Aura 261 determina la fase que puedes ver. Por ejemplo, si tuvieras esta aura <http://www.wowhead.com/?spell=55782>, podrías ver criaturas en la fase 2. Si quisieras que la criatura fuera visible tanto en la fase 1 como en la fase 2, pondrías la phase-mask a 3.

### equipment_id

El ID definido en [creature_equip_template](creature_equip_template) correspondiente al [entry](creature_template). El valor básicamente define el equipamiento:

-   **-1**: Se elegirá un equipamiento aleatorio del conjunto de equipamientos de [creature_equip_template](creature_equip_template).
-   **0**: Sin equipamiento definido.
-   **1+**: El id individual dentro de creature_equip_template.

Si la criatura se genera con `.npc add`, este valor se establecerá automáticamente (0 si no hay nada en creature_equip_template).

### position_x

La posición X del punto de generación de la criatura.

### position_y

La posición Y del punto de generación de la criatura.

### position_z

La posición Z del punto de generación de la criatura.

### orientation

La orientación del punto de generación de la criatura. (Norte = 0.0; Sur = pi (3.14159))

### spawntimesecs

El tiempo de reaparición, en segundos, de la criatura.

### wander_distance

La distancia máxima a la que la criatura puede generarse desde su punto de generación. También controla cuán lejos puede caminar la criatura desde su punto de generación si su [MovementType](#creature-MovementType) = 1.

### currentwaypoint

El [waypoint](waypoint_data#waypoint_data-point) actual en el que está la criatura, si lo hay.

### curhealth

La salud con la que se generará la criatura.

### curmana

El maná con el que se generará la criatura.

### MovementType

El tipo de movimiento asociado a la criatura. Normalmente el mismo que su [MovementType](creature_template#creature_template-MovementType), pero puede ser diferente.

### npcflag

Igual que [creature_template.npcflag](creature_template#creature_template-npcflag) .

NOTA: Un registro de creature.npcflag sobrescribirá a un registro de [creature_template.npcflag](creature_template#creature_template-npcflag).

### unit_flags

Igual que creature_template.unit_flags.

Nota:

Un registro de creature.unit_flags sobrescribirá a un registro de [creature_template.unit_flags](creature_template#creature_template-unit_flags).

### dynamicflags

Igual que creature_template.dynamicflags.

Nota:

Un registro de creature.dynamicflags sobrescribirá a un registro de [creature_template.dynamicflags](creature_template#creature_template-dynamicflags).

### ScriptName

Igual que creature_template.scriptname.

Un registro de creature.scriptname sobrescribirá a un registro de [creature_template.scriptname](creature_template#creature_template-scriptname).

### VerifiedBuild

Este campo se usa para determinar si esta criatura proviene de sniffs verificados.

Si el valor es 0, entonces aún no ha sido parseada o ha sido heredada de una BD más antigua u otro Core.

Si el valor es mayor que 0, entonces ha sido parseada con sniffs de esa build de cliente específica.

Si el valor es -Client Build, entonces fue parseada con archivos WDB de esa build de cliente específica y editada manualmente después por alguna necesidad especial.

### CreateObject

Este campo es específico de las criaturas y se usa para determinar si las posiciones están perfeccionadas.

Una vez que una criatura es sniffeada, el paquete puede ser CreateObject1 o CreateObject2.
Una criatura CO1 normalmente ya ha aparecido, se ha movido y por tanto se desvía de su posición de generación real.
Una criatura CO2 fue sniffeada cuando había aparecido, así que es, en la mayoría de casos, su posición de generación real.

Se usa un 3.er valor para casos especiales, que son criaturas que no reaparecen normalmente sino mediante scripts. Es funcionalmente igual que CO2 y solo se usa para distinguir mejor estos casos especiales.

### comment

Este campo sirve para añadir contexto adicional a esta criatura, principalmente en el contexto de valores sniffeados o notas de script.

Por ejemplo, si fue necesario modificar la posición de una criatura, las posiciones originales se guardan en el campo comment. O si las criaturas en cuestión forman parte de un script mayor, el comment sirve de contexto.
