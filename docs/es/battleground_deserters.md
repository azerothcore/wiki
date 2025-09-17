# battleground\_deserters

[<-Volver a:Characters](database-characters)

**Tabla \`battleground\_deserters\`**

La tabla alberga datos acerca de los desertores en los Campos de Batalla. Para permitir el almacenamiento de este tipo de información en la Base de Datos, establezca **Battleground.TrackDeserters.Enable = 1** más especificamente en el archivo **worldserver.config o worldserver.config.dist**.

**Estructura**

| Campo         | Tipo     | Atributos | Llave | Nulo | Por defecto | Extra | Comentario                   |
| ------------- | -------- | --------- | ----- | ---- | ----------- | ----- | ---------------------------- |
| [guid][1]     | INT      | UNSIGNED  |       | NO   |             |       | characters.guid              |
| [type][2]     | TINYINT  | UNSIGNED  |       | NO   |             |       | tipo de deserción            |
| [datetime][3] | DATETIME | SIGNED    |       | NO   |             |       | fecha y hora de la deserción |

[1]: #guid
[2]: #type
[3]: #datetime

**Descripción de los Campos**

### guid

GUID o Identificador Global Único del personaje [characters.guid](characters#guid).

### type

| Valor | Descripción                                                                     |
| ----- | ------------------------------------------------------------------------------- |
| 0     | El jugador abandona el Campo de Batalla                                         |
| 1     | El jugador es expulsado del Campo de Batalla por inactividad                    |
| 2     | El jugador es invitado a ingresar pero se niega a hacerlo                       |
| 3     | El jugador es invitado a ingresar y no hacer nada (el tiempo de ingreso expira) |
| 4     | El jugador es invitado a ingresar y se desconecta                               |

### datetime

Fecha y hora del evento en cuestión.
