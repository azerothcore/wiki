# guild\_bank\_right

[<-Volver a:Characters](database-characters)

**Tabla \`guild\_bank\_right\`**

La tabla alberga información sobre el privilegio que tienen los miembros de la hermandad para retirar, depositar, etc(...), cosas en el banco.

**Estructura**

| Field           | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guildid][1]    | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TabId][2]      | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [rid][3]        | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [gbright][4]    | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [SlotPerDay][5] | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guildid
[2]: #tabid
[3]: #rid
[4]: #gbright
[5]: #slotperday

**Descripción de los Campos**

### guildid

ID de la hermandad correspondiente.

### TabId

ID de la pestaña en la que están establecidos los permisos correspondientes.

### rid

El rango para el que está establecido los permisos.

### gbright

Los permisos que quieres otorgar al jugador con este rango en la pestaña. Lo que se muestra a continuación es una Máscara/Tabla de bits. Para combinar los privilegios, debes hacer la operación OR sumando los marcadores o 'flags'.

FLAGS (MARCADORES):

| Valor | Descripción                                                      |
|------ | ---------------------------------------------------------------- |
| 1     | Ver items                                                        |
| 2     | Depositar items                                                  |
| 4     | Actualizar el nombre del item mostrado al navegar por la pestaña |
| 8     | Retirar items                                                    |
| 255   | Todos los privilegios                                            |

### SlotPerDay

El número de items que un jugador puede retirar al día (si los permisos le otorgan los suficientes privilegios para retirar items).
