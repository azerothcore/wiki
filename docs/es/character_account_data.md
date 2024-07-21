# character\_account\_data

[<-Volver a:Characters](database-characters)

**Tabla \`character\_account\_data\`**

Alberga información acerca de la configuración de los personajes del jugador.

**Estructura**

| Field     | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1] | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [type][2] | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [time][3] | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [data][4] | BLOB    | SIGNED     |     | NO   |         |       |         |

[1]: #guid
[2]: #type
[3]: #time
[4]: #data

**Descripción de los Campos**

### guid

GUID o Identificador Global Único del personaje. Véase [characters.guid](characters#guid).

### type

| Valor | Descripción                              |
|------ | ---------------------------------------- |
| 1     | Caché de Configuración por personaje     |
| 3     | Caché de Atajos de Teclado por personaje |
| 5     | Caché de Macros por personaje            |
| 6     | Caché de Interfaz por carácter           |
| 7     | Caché de Chat por personaje              |

### time

Hora de la última modificación en Tiempo Unix.

### data

No puede digitarse algún tipo de descripción para este campo en particular. Sólo debes entender que en cuestión son datos los que se encuentran aquí.
