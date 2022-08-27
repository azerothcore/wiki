# gm\_ticket

[<-Volver a:Characters](database-characters.md)

**Tabla \`gm\_tickets\` **

Esta tabla contiene todos los tickets del servidor.

Nota: no inserte información directamente en la mayoría de las columnas, de lo contrario el cliente no actualizará el estado del ticket hasta la recarga de la tabla y el cierre de la sesión.

**Estructura**

| Field                  | Type        | Attributes | Key | Null | Default | Extra          | Comment                                    |
| ---------------------- | ----------- | ---------- | --- | ---- | ------- | -------------- | ------------------------------------------ |
| [Id][1]                | INT         | UNSIGNED   | PRI | NO   |         | Auto increment |                                            |
| [type][2]              | TINYINT     | UNSIGNED   |     | NO   | 0       |                | 0 open, 1 closed, 2 character deleted      |
| [playerGuid][3]        | INT         | UNSIGNED   |     | NO   | 0       |                | Global Unique Identifier of ticket creator |
| [name][4]              | VARCHAR(12) | SIGNED     |     | NO   |         |                | Name of ticket creator                     |
| [description][5]       | text        | SIGNED     |     | NO   |         |                |                                            |
| [createTime][6]        | INT         | UNSIGNED   |     | NO   | 0       |                |                                            |
| [mapId][7]             | SMALLINT    | UNSIGNED   |     | NO   | 0       |                |                                            |
| [posX][8]              | FLOAT       | SIGNED     |     | NO   | 0       |                |                                            |
| [posY][9]              | FLOAT       | SIGNED     |     | NO   | 0       |                |                                            |
| [posZ][10]             | FLOAT       | SIGNED     |     | NO   | 0       |                |                                            |
| [lastModifiedTime][11] | INT         | UNSIGNED   |     | NO   | 0       |                |                                            |
| [closedBy][12]         | INT         | SIGNED     |     | NO   | 0       |                | -1 Closed by Console, >0 GUID of GM        |
| [assignedTo][13]       | INT         | UNSIGNED   |     | NO   | 0       |                | GUID of admin to whom ticket is assigned   |
| [comment][14]          | text        | SIGNED     |     | NO   |         |                |                                            |
| [response][15]         | text        | SIGNED     |     | NO   |         |                |                                            |
| [completed][16]        | TINYINT     | UNSIGNED   |     | NO   | 0       |                |                                            |
| [escalated][17]        | TINYINT     | UNSIGNED   |     | NO   | 0       |                |                                            |
| [viewed][18]           | TINYINT     | UNSIGNED   |     | NO   | 0       |                |                                            |
| [needMoreHelp][19]     | TINYINT     | UNSIGNED   |     | NO   | 0       |                |                                            |
| [resolvedBy][20]       | INT         | SIGNED     |     | NO   | 0       |                | -1 Resolved by Console, >0 GUID of GM      |

[1]: #id
[2]: #type
[3]: #playerguid
[4]: #name
[5]: #description
[6]: #createtime
[7]: #mapid
[8]: #posx
[9]: #posy
[10]: #posz
[11]: #lastmodifiedtime
[12]: #closedby
[13]: #assignedto
[14]: #comment
[15]: #response
[16]: #completed
[17]: #escalated
[18]: #viewed
[19]: #needmorehelp
[20]: #resolvedby

**Descripción de los Campos**

### Id

Globally Unique Identifier o Identificador Global único del ticket. Éste número debe de ser único, ya que se distingue por su propia cuenta de las demás casillas.

### type

Tipo de ticket. Variables: 
- 0 = Abierto
- 1 = Cerrado
- 2 = Personaje Eliminado

### playerGuid

GUID -Globally Unique Identifier o Identificador Global único- del jugador. Ver [characters.guid](characters#guid).

### name

Nombre del personaje del jugador el cual creó el ticket.

### description

El contenido del ticket como tal.

### createTime

La hora en la que fue creado el ticket -en marca de tiempo linux-.

### mapId

El mapa donde el ticket fue creado. Ver [Map.dbc](map).

### posX

Posición X donde el ticket fue creado.

### posY

Posición Y donde el ticket fue creado.

### posZ

Posición Z donde el ticket fue creado.

### lastModifiedTime

Hora en la que el ticket fue cerrado o eliminado por el jugador -en marca de tiempo linux-.

### closedBy

- 0 = Abierto
- ~-1 = Cerrado por la consola~ (No implementado aún en AzerothCore)
- > 0 = Jugador que abandonó el ticket o GM que eliminó el ticket

### assignedTo

Número de cuenta específica del Maestro del Juego al cual le fue asignado el ticket.

### comment

El comentario que fue añadido al ticket por medio del comando `.ticket comment`, sólo visible para Maestros del Juego. En caso de que el comando fuera utilizado dos veces, sobrescribe el comentario previamente agregado.
### response

Cadena en la que el Maestro de Juego inserta con el comando `.ticket response` la respuesta al ticket antes de completarlo. En caso de que el comando fuera utilizado dos veces, añade la nueva respuesta al final de la anterior.

### completed

- 0 = No resuelto
- 1 = Resuelto (informará al usuario y mostrará lo que hay escrito en `response`.)

### escalated

- 0 = El ticket no ha sido asignado.
- 1 = El ticket es asignado al Maestro de Juego actual.
- 2 = El ticket ha sido 'escalado' tras su finalización (Suponiendo que el Maestro de Juego se conactase con el jugador) 

### viewed

- 0 = Nadie ha visto el ticket.
- > 0 = Las veces que el ticket ha sido visto por Maestros del Juego.

### needMoreHelp

Solicita más interacción de Maestros del Juego sobre un ticket el cual ya ha sido solventado por otro Maestro de Juego. Básicamente significa "Hay un nuevo ticket".

### resolvedBy

- 0 = Abierto
- ~-1 = Resuelto por la Consola~ (Aún no es compatible con azerothcore debido al tipo de datos de la Base de Datos)
- > 0 = Identificador global único del personaje del Maestro de Juego que lo solventó (Cerrando o completando el ticket)
