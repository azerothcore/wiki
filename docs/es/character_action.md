# character\_action

[<-Volver a:Characters](database-characters.md)

**Tabla \`character\_action\`**

Alberga todos los datos de aquellos botones individuales para cada personaje. Un botón es considerado cualquiera de las casillas disponibles en la interfaz gráfica de usuario, por ejemplo, un hechizo, un elemento o una macro como acceso directo.

**Estructura**

| Field       | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]   | INT        | UNSIGNED   | PRI | NO   | 0       |       |         |
| [spec][2]   | TINYINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [button][3] | TINYINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [action][4] | INT        | UNSIGNED   |     | NO   | 0       |       |         |
| [type][5]   | TINYINT    | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #spec
[3]: #button
[4]: #action
[5]: #type

**Descripción de los Campos**

### guid

GUID o Identificador Global Único del personaje. Véase [characters.guid](characters#guid).

### spec

Especialización de Talentos: El número 0 es para la primera Especialización de Talentos, luego el número 1 es para la segunda.

### button

ID del botón en cuestión en la barra de acciones en donde se colocará el ícono de la acción correspondiente.

Las barras especiales se utilizan para aquellas habilidades especiales correspondientes de cada clase, ya sean auras (paladín), mascotas (Caballero de la Muerte, Cazador, Brujo o Mago), sigilo (Pícaro) y otras similares.

**Valores Posibles**

| Identificadores de los Botones | Fijar (Atajo)                          |
| ------------------------------ | -------------------------------------- |
| 1-11                           | 1 (SHIFT + 1)                          |
| 12-23                          | 2 (SHIFT + 2)                          |
| 24-35                          | 3 (SHIFT + 3) Barra lateral derecha    |
| 36-47                          | 4 (SHIFT + 4) Barra lateral derecha 2  |
| 48-59                          | 5 (SHIFT + 5) Barra inferior derecha   |
| 60-71                          | 6 (SHIFT + 6) Barra inferior izquierda |
| 72-83                          | 1 EspecialA                            |
| 84-95                          | 1 EspecialB                            |
| 96-107                         | 1 EspecialC                            |
| 108-119                        | 1 EspecialD                            |

### action

Dependiendo del tipo de valor, podría ser la ID del hechizo (Spell.dbc), el ID del Item o la de un macro en cuestión.

### type

Tipo de acción:

**Posibles tipos de acción**

| Valor | Descripción            |
| ----- | ---------------------- |
| 0     | Hechizo                |
| 1     | Clic                   |
| 32    | Gestor de Equipamiento |
| 64    | Macro                  |
| 65    | Clic Macro             |
| 128   | Item                   |
