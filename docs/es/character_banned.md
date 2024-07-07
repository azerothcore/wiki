# character\_banned

[<-Volver a:Characters](database-characters)

**Tabla \`character\_banned\`**

La tabla lista a todos aquellos personajes que han sido baneados, junto con la fecha en la que (en tal caso) expiraría el baneo.

**Estructura**

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment                  |
| -------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]      | INT          | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [bandate][2]   | INT          | UNSIGNED   | PRI | NO   | 0       |       |                          |
| [unbandate][3] | INT          | UNSIGNED   |     | NO   | 0       |       |                          |
| [bannedby][4]  | VARCHAR(50)  | SIGNED     |     | NO   |         |       |                          |
| [banreason][5] | VARCHAR(255) | SIGNED     |     | NO   |         |       |                          |
| [active][6]    | TINYINT      | UNSIGNED   |     | NO   | 1       |       |                          |

[1]: #guid
[2]: #bandate
[3]: #unbandate
[4]: #bannedby
[5]: #banreason
[6]: #active

**Descripción de los Campos**

### guid

GUID o Identificador Global Único del personaje. Véase [characters.guid](characters#guid).

### bandate

Fecha en la que el personaje correspondiente fue baneado, medido en Tiempo Unix.

### unbandate

Fecha en la cual el personaje en cuestión será automáticamente desbaneado, medido en Tiempo Unix. Un valor inferior a la fecha actual quiere decir, que el baneo es de tipo permanente.

### bannedby

Nombre del personaje con los privilegios necesarios para del comando '.ban', que en efecto fue el encargado en banear al personaje citado.

### banreason

Motivo del baneo (opcional).

### active

Booleano del 0 al 1 el cual controla sí el baneo se encuentra activo actualmente o no.
