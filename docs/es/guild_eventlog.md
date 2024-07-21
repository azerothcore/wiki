# guild\_eventlog

[<-Volver a:Characters](database-characters)

**Tabla \`guild\_eventlog\`**

**Estructura**

| Field            | Type    | Attributes | Key | Null | Default | Extra | Comment                                     |
| ---------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------------------------------- |
| [guildid][1]     | INT     | UNSIGNED   | PRI | NO   |         |       | Guild Identificator                         |
| [LogGuid][2]     | INT     | UNSIGNED   | PRI | NO   |         |       | Log record identificator - auxiliary column |
| [EventType][3]   | TINYINT | UNSIGNED   |     | NO   |         |       | Event type                                  |
| [PlayerGuid1][4] | INT     | UNSIGNED   |     | NO   |         |       | Player 1                                    |
| [PlayerGuid2][5] | INT     | UNSIGNED   |     | NO   |         |       | Player 2                                    |
| [NewRank][6]     | TINYINT | UNSIGNED   |     | NO   |         |       | New rank(in case promotion/demotion)        |
| [timestamp][7]   | BIGINT  | UNSIGNED   |     | NO   |         |       | Event UNIX time                             |

[1]: #guildid
[2]: #logguid
[3]: #eventtype
[4]: #playerguid1
[5]: #playerguid2
[6]: #newrank
[7]: #timestamp

**Descripción de los Campos**

### guildid

ID de la hermandad correspondiente.

### LogGuid

GUID del registro - columna auxiliar.

### EventType

| Valor | Descripción                         | Comentarios              |
| ----- | ----------------------------------- | ------------------------ |
| 1     | GUILD\_EVENT\_LOG\_INVITE\_PLAYER   | Invitación al jugador    |
| 2     | GUILD\_EVENT\_LOG\_JOIN\_GUILD      | Ingreso a la hermandad   |
| 3     | GUILD\_EVENT\_LOG\_PROMOTE\_PLAYER  | Ascenso de jugador       |
| 4     | GUILD\_EVENT\_LOG\_DEMOTE\_PLAYER   | Degradación de jugador   |
| 5     | GUILD\_EVENT\_LOG\_UNINVITE\_PLAYER | Reachaza invitación      |
| 6     | GUILD\_EVENT\_LOG\_LEAVE\_GUILD     | Abandona la hermandad    |

### PlayerGuid1

GUID o Identificador Global Único del jugador número 1.

### PlayerGuid2

GUID o Identificador Global Único del jugador número 2.

### NewRank

Nuevo rango (en caso de ascenso/degradación).

### timestamp

Evento medido en tiempo UNIX.