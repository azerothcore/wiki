# arena\_team\_member

[<-Volver a:Characters](database-characters.md)

**Tabla \`arena\_team\_member\`**

La tabla alberga información acerca de los miembros específicos del Equipo de Arenas. Todos los miembros de [arena_team](arena_team) tienen un registro en esta tabla.

**Estructura**

| Field               | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [arenaTeamId][1]    | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [guid][2]           | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [weekGames][3]      | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [weekWins][4]       | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [seasonGames][5]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [seasonWins][6]     | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [personalRating][7] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #arenateamid
[2]: #guid
[3]: #weekgames
[4]: #weekwins
[5]: #seasongames
[6]: #seasonwins
[7]: #personalrating

**Descripción de los Campos**

### arenaTeamId

ID del Equipo de Arenas. Véase [arena\_team#arenateamid].

### guid

GUID o Identificador Global Único del personaje. Véase [characters.guid](characters#guid).

### weekGames

Número de juegos en esta **semana**.

### weekWins

Número de juegos ganados en esta esta **semana**.

### seasonGames

Número de juegos en la **temporada**.

### seasonWins

Número de juegos ganados en la **temporada**.

### personalrating

El índice personal del jugador.
