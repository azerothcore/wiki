# arena\_team

[<-Volver a:Characters](database-characters)

**Tabla \`arena\_team\`**

La tabla aleberga información principal de los Equipos de Arenas existentes. Todos los equipos creados o en proceso de creación dentro del servidor tienen un registro en esta tabla.

**Estructura**

| Campo                 | Tipo        | Atributos | Llave | Nulo | Por defecto | Extra  | Comentario |
| --------------------- | ----------- | --------- | ----- | ---- | ----------- | ------ | ---------- |
| [arenaTeamId][1]      | INT         | UNSIGNED  | PRI   | NO   | 0           | Único  |            |
| [name][2]             | VARCHAR(24) | SIGNED    |       | NO   |             |        |            |
| [captainGuid][3]      | INT         | UNSIGNED  |       | NO   | 0           |        |            |
| [type][4]             | TINYINT     | UNSIGNED  |       | NO   | 0           |        |            |
| [rating][5]           | SMALLINT    | UNSIGNED  |       | NO   | 0           |        |            |
| [seasonGames][6]      | SMALLINT    | UNSIGNED  |       | NO   | 0           |        |            |
| [seasonWins][7]       | SMALLINT    | UNSIGNED  |       | NO   | 0           |        |            |
| [weekGames][8]        | SMALLINT    | UNSIGNED  |       | NO   | 0           |        |            |
| [weekWins][9]         | SMALLINT    | UNSIGNED  |       | NO   | 0           |        |            |
| [rank][10]            | INT         | UNSIGNED  |       | NO   | 0           |        |            |
| [BackgroundColor][11] | INT         | UNSIGNED  |       | NO   | 0           |        |            |
| [emblemStyle][12]     | TINYINT     | UNSIGNED  |       | NO   | 0           |        |            |
| [emblemColor][13]     | INT         | UNSIGNED  |       | NO   | 0           |        |            |
| [borderStyle][14]     | TINYINT     | UNSIGNED  |       | NO   | 0           |        |            |
| [borderColor][15]     | INT         | UNSIGNED  |       | NO   | 0           |        |            |

[1]: #arenateamid
[2]: #name
[3]: #captainguid
[4]: #type
[5]: #rating
[6]: #seasongames
[7]: #seasonwins
[8]: #weekgames
[9]: #weekwins
[10]: #rank
[11]: #backgroundcolor
[12]: #emblemstyle
[13]: #emblemcolor
[14]: #borderstyle
[15]: #bordercolor

**Descripción de los Campos**

### arenaTeamId

ID del Equipo de Arenas correspondiente. Este número debe ser único, ya que es el principal método para ser identificado del resto.

### name

Nombre del Equipo de Arena.

### captainGuid

GUID o Identificador Global Único del personaje quien creó el Equipo de Arenas. Véase [characters.guid](characters#guid).

### type

Define el tipo del Equipo de Arenas.

- 2 – Equipo 2vs2
- 3 – Equipo 3vs3
- 5 – Equipo 5vs5

### rating

Índice del Equipo.

### seasonGames

Número de juegos en la **temporada**.

### seasonWins

Número de juegos ganados en la **temporada**.

### weekGames

Número de juegos en esta **semana**.

### weekWins

Número de juegos ganados en esta **semana**.

### rank

Clasificación de los equipos dentro de la competición según su Índice.

### BackgroundColor

Color de fondo del tabardo de equipo (igual que el tabardo de hermandad).

### emblemStyle

Emblema del tabardo de equipo (igual que el tabardo de hermandad).

### emblemColor

Color de emblema del tabardo de equipo (igual que el tabardo de hermandad).

### borderStyle

Bordado del tabardo de equipo (igual que el tabardo de hermandad).

### borderColor

Color de bordado del tabardo de equipo (igual que el tabardo de hermandad).
