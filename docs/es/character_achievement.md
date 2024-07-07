# character\_achievement

[<-Volver a:Characters](database-characters)

**Tabla \`character\_achievement\`**

La tabla alberga información sobre aquellos logros que un personaje ha obtenido/completado dentro del juego.

**Nota:** En caso de que eliminases un logro de "reino primero" (Ya sea Clase, Raza o de un modo general 'El Primero del Reino) dentro de la Base de Datos de los personajes (Characters), debes de reiniciar el servidor para que lo tenga en cuenta.

**Estructura**

| Field            | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]        | INT      | UNSIGNED   | PRI | NO   |         |       |         |
| [achievement][2] | SMALLINT | UNSIGNED   | PRI | NO   |         |       |         |
| [date][3]        | INT      | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #achievement
[3]: #date

**Descripción de los Campos**

### guid

GUID o Identificador Global Único del personaje. Véase [characters.guid](characters#guid).

### achievement

Identificador (ID) del logro en cuestión desde [Achievement.dbc](achievement).

### date

La Fecha/Hora en la que se obtuvo este logro, (Medido en Tiempo Unix). Véase [Marca de Tiempo Unix](https://www.unixtimestamp.com/es/index.php)
