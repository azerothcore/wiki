# account\_muted

[<-Volver a:Auth](database-auth.md)

**Tabla \`account\_muted\`**

Esta tabla contiene los ID de cuentas cuyos personajes tienen asignado un baneo de chat (mute).

GM-Command: **.mute [$NombreDelJugador] $TiempoEnMinutos [$motivo]**.

Desactiva la mensajería de chat para cualquier personaje de la cuenta $NombreDelJugador (o actualmente seleccionado) en $TiempoEnMinutos (minutos). El jugador puede estar desconectado.

**Structure**

| Field           | Type         | Attributes | Key | Null | Default | Extra | Comment                  |
| --------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]       | INT          | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [mutedate][2]   | INT          | UNSIGNED   | PRI | NO   | 0       |       |                          |
| [mutetime][3]   | INT          | UNSIGNED   |     | NO   | 0       |       |                          |
| [mutedby][4]    | VARCHAR(50)  |            |     | NO   |         |       |                          |
| [mutereason][5] | VARCHAR(255) |            |     | NO   |         |       |                          |

[1]: #guid
[2]: #mutedate
[3]: #mutetime
[4]: #mutedby
[5]: #mutereason

### Descripción de los campos

### guid

ID de la cuenta silenciada, tomada del personaje muteado. Todos los personajes de esta cuenta serán silenciados durante [mutetime](#mutetime).

### mutedate

La fecha en la que comenzó el mute. Se utiliza la marca de tiempo UNIX.

### mutetime

Duración del mute en minutos.

### mutedby

Apodo del GM/moderador que emitió el mute.

#### mutereason

Campo de texto con la descripción del motivo del mute.