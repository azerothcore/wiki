# guild\_rank

[<-Volver a:Characters](database-characters)

**Tabla \`guild\_rank\`**

La tabla alberga información de todos los rangos disponibles de una hermandad, junto con sus nombres y los privilegios que tiene una persona con ese rango.

**Estructura**

| Field                | Type        | Attributes | Key | Null | Default | Extra | Comment |
| -------------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guildid][1]         | INT         | UNSIGNED   | PRI | NO   | 0       |       |         |
| [rid][2]             | TINYINT     | UNSIGNED   | PRI | NO   |         |       |         |
| [rname][3]           | VARCHAR(20) | SIGNED     |     | NO   | "       |       |         |
| [rights][4]          | MEDIUMINT   | UNSIGNED   |     | NO   | 0       |       |         |
| [BankMoneyPerDay][5] | INT         | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guildid
[2]: #rid
[3]: #rname
[4]: #rights
[5]: #bankmoneyperday

**Descripción de los Campos**

### guildid

ID de la hermandad a la que pertenece el rango. Véase [guild.guildid](guild#guildid).

### rid

ID del rango particular. Este número debe ser único y difiere para cada rango en la hermandad.

### rname

El nombre del rango que se muestra en el juego.

### rights

Los privilegios que un jugador con este rango tiene en la hermandad. El cálculo o sumatoria de los privilegios múltiples es un tanto distinto en este caso, ya que no todos poseen los privilegios dados de tipo 2^n. Para combinar rangos, debes de hacer la operación OR (\|) con las flags/marcadores de aquellos privilegios que quieras combinar.

| flag    | Nombre                        | Comentarios                                                                     |
| ------- | ----------------------------- | ------------------------------------------------------------------------------- |
| 64      | GR_RIGHT_EMPTY                | Poseer sólo este marcador por sí mismo equivale a no tener ningún privilegio.   |
| 65      | GR_RIGHT_GCHATLISTEN          | El jugador puede leer mensajes en el canal de chat general de la hermandad.     |
| 66      | GR_RIGHT_GCHATSPEAK           | El jugador puede escribir mensajes en el canal de chat general de la hermandad. |
| 68      | GR_RIGHT_OFFCHATLISTEN        | El jugador puede leer mensajes en el canal de oficiales de la hermandad.        |
| 72      | GR_RIGHT_OFFCHATSPEAK         | El jugador puede escribir mensajes en el canal de oficiales de la hermandad.    |
| 80      | GR_RIGHT_INVITE               | Puede invitar a otros jugadores a la hermandad.                                 |
| 96      | GR_RIGHT_REMOVE               | Puede expulsar a otros jugadores a la hermandad.                                |
| 192     | GR_RIGHT_PROMOTE              | Puede promover a otros jugadores.                                               |
| 320     | GR_RIGHT_DEMOTE               | Puede degradar a otros jugadores.                                               |
| 4160    | GR_RIGHT_SETMOTD              | Puede modificar el mensaje diario de la hermandad.                              |
| 8256    | GR_RIGHT_EPNOTE               | Puede editar las notas de otros jugadores.                                      |
| 16448   | GR_RIGHT_VIEWOFFNOTE          | Puede ver las notas de los oficiales.                                           |
| 32832   | GR_RIGHT_EOFFNOTE             | Puede editar las notas de los oficiales.                                        |
| 65600   | GR_RIGHT_MODIFY_GUILD_INFO    | Puede editar la información de la hermandad.                                    |
| 131072  | GR_RIGHT_WITHDRAW_GOLD_LOCK   | Puede eliminar el límite de retirada de oro del banco.                          |
| 262144  | GR_RIGHT_WITHDRAW_REPAIR      | Puede retirar oro del banco para la reparación de sus Items.                    |
| 524288  | GR_RIGHT_WITHDRAW_GOLD        | Puede retirar oro.                                                              |
| 1048576 | GR_RIGHT_CREATE_GUILD_EVENT   | Puede crear un evento de hermandad.                                             |
| 1962495 | GR_RIGHT_ALL                  | Tiene todos los privilegios.                                                    |

### BankMoneyPerDay

El dinero diario total al cual tenga derecho el jugador que posea éste rango, medido en monedas de cobre. Use el valor máximo de un ENTERO NO ASIGNADO (4294967295) para especificar una cantidad ilimitada.
