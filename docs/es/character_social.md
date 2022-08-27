# character\_social

[<-Volver a:Characters](database-characters.md)

**Tabla \`character\_social\`**

Contiene datos acerca de la lista de amigos/ignorados del personaje dado.

**Estructura**

| Field       | Type        | Attributes | Key | Null | Default | Extra | Comment                            |
| ----------- | ----------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [guid][1]   | INT         | UNSIGNED   | PRI | NO   | 0       |       | Character Global Unique Identifier |
| [friend][2] | INT         | UNSIGNED   | PRI | NO   | 0       |       | Friend Global Unique Identifier    |
| [flags][3]  | TINYINT     | UNSIGNED   | PRI | NO   | 0       |       | Friend Flags                       |
| [note][4]   | VARCHAR(48) | SIGNED     |     | NO   | ''      |       | Friend Note                        |

[1]: #guid
[2]: #friend
[3]: #flags
[4]: #note

**Descripción de los Campos**

### guid

Globally Unique Identifier o Identificador Global Único del personaje. Véase [characters.guid](characters#guid).

### friend

El Identificador Global Único o GUID del amigo/ignorado. Véase [characters.guid](characters#guid).

### flags

| Value | Description                                                                                       |
|------ | ------------------------------------------------------------------------------------------------- |
| 0     | Identificador no usado - anteriormente funcionaba como amigo o bloqueado (eliminado/desbloqueado) |
| 1     | Añadido como amigo                                                                                |
| 2     | Añadido como usuario bloqueado                                                                    |
| 3     | Añadido como amigo, y en la lista de ignorados también                                            |

### note

Nota acerca del amigo (que aparece junto al nombre del amigo en la lista de amigos en el Cliente de juego).

Nota importante: Sólo puede haber 50 amigos y 50 personajes ignorados. Si tiene problemas con el no poder ver algún amigo en específico, intente eliminar algunos de ellos.
