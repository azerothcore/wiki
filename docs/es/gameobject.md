# gameobject

[<-Volver a: World](database-world)

**Tabla \`gameobject\`**

Esta tabla contiene los datos individuales de cada objeto de juego generado en el mundo. Estos datos, junto con los datos de plantilla del objeto, se leen y se usan para instanciar los objetos en el mundo.

**Estructura**

| Field               | Type     | Attributes | Key | Null | Default | Extra          | Comment                  |
| ------------------- | -------- | ---------- | --- | ---- | ------- | -------------- | ------------------------ |
| [guid][1]           | INT      | UNSIGNED   | PRI | NO   | NULL    | Auto increment | Global Unique Identifier |
| [id][2]             | INT      | UNSIGNED   |     | NO   | 0       |                | Gameobject Identifier    |
| [map][3]            | SMALLINT | UNSIGNED   |     | NO   | 0       |                | Map Identifier           |
| [zoneId][4]         | SMALLINT | UNSIGNED   |     | NO   | 0       |                | Zone Identifier          |
| [areaId][5]         | SMALLINT | UNSIGNED   |     | NO   | 0       |                | Area Identifier          |
| [spawnMask][6]      | TINYINT  | UNSIGNED   |     | NO   | 1       |                |                          |
| [phaseMask][7]      | SMALLINT | UNSIGNED   |     | NO   | 1       |                |                          |
| [position_x][8]     | FLOAT    | SIGNED     |     | NO   | 0       |                |                          |
| [position_y][9]     | FLOAT    | SIGNED     |     | NO   | 0       |                |                          |
| [position_z][10]    | FLOAT    | SIGNED     |     | NO   | 0       |                |                          |
| [orientation][11]   | FLOAT    | SIGNED     |     | NO   | 0       |                |                          |
| [rotation0][12]     | FLOAT    | SIGNED     |     | NO   | 0       |                |                          |
| [rotation1][13]     | FLOAT    | SIGNED     |     | NO   | 0       |                |                          |
| [rotation2][14]     | FLOAT    | SIGNED     |     | NO   | 0       |                |                          |
| [rotation3][15]     | FLOAT    | SIGNED     |     | NO   | 0       |                |                          |
| [spawntimesecs][16] | INT      | SIGNED     |     | NO   | 0       |                |                          |
| [animprogress][17]  | TINYINT  | UNSIGNED   |     | NO   | 0       |                |                          |
| [state][18]         | TINYINT  | UNSIGNED   |     | NO   | 1       |                |                          |
| [ScriptName][19]    | CHAR     |            |     | YES  | ''      |                |                          |
| [VerifiedBuild][20] | INT      | SIGNED     |     | YES  | NULL    |                | Not used by the core.    |
| [Comment][21]       | TEXT     |            |     | YES  | NULL    |                |                          |

[1]: #guid
[2]: #id
[3]: #map
[4]: #zoneId
[5]: #areaId
[6]: #spawnmask
[7]: #phasemask
[8]: #position_x
[9]: #position_y
[10]: #position_z
[11]: #orientation
[12]: #rotation0
[13]: #rotation1
[14]: #rotation2
[15]: #rotation3
[16]: #spawntimesecs
[17]: #animprogress
[18]: #state
[19]: #scriptname
[20]: #verifiedbuild
[21]: #comment

**Descripción de los campos**

### guid

El identificador único global del objeto de juego. Este campo debe ser único entre todos los objetos de juego.

### id

El ID de plantilla del gameobject. Ver [gameobject_template.entry](http://www.azerothcore.org/wiki/gameobject_template#entry)

### map

El ID del mapa donde se genera este objeto. Ver Maps.dbc

### zoneId

El ID de la zona en la que se genera este objeto. (p. ej. Los Baldíos)

Esta columna la rellena el worldserver al arrancar si la opción `Calculate.Gameoject.Zone.Area.Data` está habilitada. Proviene de AreaTable.dbc.

### areaId

El ID del área en la que se genera este objeto. Puedes pensar en un área como una "subzona" de una zona, p. ej. el Oasis Aguacristalina dentro de Los Baldíos.

Esta columna la rellena el worldserver al arrancar si la opción `Calculate.Gameoject.Zone.Area.Data` está habilitada. Proviene de AreaTable.dbc.

### spawnMask

Controla en qué dificultades se genera el objeto.

Igual que los flags, puedes sumarlos como quieras, así que 3 sería: generado en las versiones normales de 10/25 jugadores de los mapas (antes de 3.2, todos los mapas)

| Value | Comment                                                                              |
| ----- | ------------------------------------------------------------------------------------ |
| 0     | No generado                                                                          |
| 1     | Generado solo en versiones normales de 10 jugadores de los mapas (incluye mapas sin modo heroico) |
| 2     | Generado solo en versiones normales de 25 jugadores de los mapas (o heroicas anteriores a 3.2) |
| 4     | Generado solo en versiones heroicas de 10 jugadores de los mapas                    |
| 8     | Generado solo en versiones heroicas de 25 jugadores de los mapas                    |
| 15    | Generado en todas las versiones de los mapas                                         |

### phaseMask

Este es un campo bitmask que describe todas las fases en las que aparecerá este gameobject. El Aura 261 determina la fase que puedes ver. Por ejemplo, si tuvieras esta aura <http://www.wowhead.com/?spell=55782>, podrías ver gameobjects en la fase 2. Si quisieras que el gameobject fuera visible tanto en la fase 1 como en la fase 2, pondrías la phaseMask a 3.

### position_x

La posición X.

### position_y

La posición Y.

### position_z

La posición Z.

### orientation

La orientación. (Norte = 0, Sur = 3.14159)

### rotation0

### rotation1

### rotation2

### rotation3

### spawntimesecs

Tiempo en segundos para que este objeto reaparezca.

Usar 0 hará que el objeto no desaparezca al usarlo.

Usar un valor negativo hará que el objeto empiece estando "desaparecido" hasta que un script lo genere. Entonces desaparecerá tras pasar la cantidad de tiempo especificada aquí.

### animprogress

No se sabe muy bien para qué se usa esto por ahora. No obstante, ponlo siempre a 100 para los cofres.

### state

Para cofres o puertas.

-   1 = cerrado
-   0 = abierto

### ScriptName

Igual que gameobject_template.scriptname.

Un registro de gameobject.scriptname sobrescribirá a un registro de [gameobject_template.scriptname](gameobject_template#gameobject_template-scriptname).

### VerifiedBuild

Este campo se usa para determinar si este gameobject proviene de sniffs verificados.

Si el valor es 0, entonces aún no ha sido parseado o ha sido heredado de una BD más antigua u otro Core.

Si el valor es mayor que 0, entonces ha sido parseado con sniffs de esa build de cliente específica.

Si el valor es -Client Build, entonces fue parseado con archivos WDB de esa build de cliente específica y editado manualmente después por alguna necesidad especial.

### comment

Este campo sirve para añadir contexto adicional a este gameobject, principalmente en el contexto de valores sniffeados o notas de script.

Por ejemplo, si fue necesario modificar la posición de un gameobject, las posiciones originales se guardan en el campo comment. O si los gobs en cuestión forman parte de un script mayor, el comment sirve de contexto.
