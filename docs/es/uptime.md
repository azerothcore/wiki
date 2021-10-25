# uptime

[<-Volver a:Auth](database-auth.md)

Leer en: [English :gb:](../uptime) [Spanish :es:](uptime)

**Tabla \`uptime\`**

Esta tabla contiene el tiempo de actividad del servidor. El núcleo actualizará automáticamente el valor de la última entrada hasta que se bloquee y se añada un nuevo registro.

**Estructura**

| Field           | Type         | Attributes | Key | Null | Default     | Extra | Comment |
| --------------- | ------------ | ---------- | --- | ---- | ----------- | ----- | ------- |
| [realmid][1]    | INT          | UNSIGNED   | PRI | NO   |             |       |         |
| [starttime][2]  | INT          | UNSIGNED   | PRI | NO   | 0           |       |         |
| [uptime][3]     | INT          | UNSIGNED   |     | NO   | 0           |       |         |
| [maxplayers][4] | SMALLINT     | UNSIGNED   |     | NO   | 0           |       |         |
| [revision][5]   | VARCHAR(255) | SIGNED     |     | NO   | AzerothCore |       |         |

[1]: #realmid
[2]: #starttime
[3]: #uptime
[4]: #maxplayers
[5]: #revision

**Descripción de los campos**

### realmid

El ID del reino. Ver [realmlist.id](realmlist#id).

### starttime

La hora de inicio del servidor, en tiempo Unix.

### uptime

El tiempo de actividad del servidor, en segundos.

### maxplayers

El número máximo de jugadores conectados.

### revision

La revisión detallada del WorldServer.
