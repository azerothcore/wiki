# character\_queststatus

[<-Volver a:Characters](database-characters)

**Tabla \`character\_queststatus\`**

Contiene información sobre el estado de misiones de cada personaje.

**Estructura**

| Field             | Type     | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------------- | -------- | ---------- | --- | ---- | ------- |------ | ------------------------ |
| [guid][1]         | INT      | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [quest][2]        | INT      | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier         |
| [status][3]       | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                          |
| [explored][4]     | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                          |
| [timer][5]        | INT      | UNSIGNED   |     | NO   | 0       |       |                          |
| [mobcount1][6]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [mobcount2][7]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [mobcount3][8]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [mobcount4][9]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount1][10]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount2][11]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount3][12]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount4][13]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount5][14]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount6][15]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [playercount][16] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #quest
[3]: #status
[4]: #explored
[5]: #timer
[6]: #mobcount
[7]: #mobcount
[8]: #mobcount
[9]: #mobcount
[10]: #itemcount
[11]: #itemcount
[12]: #itemcount
[13]: #itemcount
[14]: #itemcount
[15]: #itemcount
[16]: #playercount

**Descripción de los Campos**

### guid

Globally Unique Identifier o Identificador Global Único del personaje. Ver [characters.guid](characters#guid).

### quest

Identificador o ID de la misión. Ver [quest\_template.entry](quest_template#entry).

### status

El estado actual de la misión.

**Valores posibles**

| Value | Status                     | Comments                                                              |
| ----- | -------------------------- | --------------------------------------------------------------------- |
| 0     | QUEST\_STATUS\_NONE        | La misión no se muestra en la lista de misiones; por defecto          |
| 1     | QUEST\_STATUS\_COMPLETE    | La misión no ha sido completada todavía                               |
| 2     | QUEST\_STATUS\_UNAVAILABLE | NO USADO                                                              |
| 3     | QUEST\_STATUS\_INCOMPLETE  | La misión está activa en el registro de misiones pero está incompleta |
| 4     | QUEST\_STATUS\_AVAILABLE   | NO USADO                                                              |
| 5     | QUEST\_STATUS\_FAILED      | El jugador falló al intentar completar la misión                      |

### explored

Booleano del 0 al 1 que representa si el personaje ha explorado lo necesario para completar la misión.

### timer

Contador de tiempo o temporizador.

### mobcount

Recuento actual del número de muertes o lanzamiento de hechizos sobre la primera criatura u objeto de juego (si los hay). Es correspondiente con quest\template.

Recordemos que son 4 casillas con el nombre 'mobcount'

### itemcount

Recuento actual de Items para el primer Item de una misión de entrega (si los hay). Es correspondiente con quest\template.

Recordemos que son 4 casillas con el nombre 'itemcount'

### playercount

Recuento actual de muertes de jugadores para completar la misión. Requerido en quest\template.
