# character\_arena\_stats

[<-Volver a:Characters](database-characters)

**Tabla \`character\_arena\_stats\`**

Esta tabla contiene información sobre la calificación de emparejamiento del personaje en todos los tipos de equipo.

**Estructura**

| Campo                 | Tipo        | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| --------------------- | ----------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [guid][1]             | INT         | UNSIGNED  | PRI   | NO   |             |       |            |
| [slot][2]             | TINYINT     | UNSIGNED  | PRI   | NO   |             |       |            |
| [matchmakerRating][3] | SMALLINT    | UNSIGNED  |       | NO   |             |       |            |
| [maxMMR][4]           | SMALLINT    | SIGNED    |       | NO   |             |       |            |

[1]: #guid
[2]: #slot
[3]: #matchmakerrating
[4]: #maxmmr

**Descripción de los Campos**

### guid

GUID o Identificador Global Único del personaje. Véase [characters.guid](characters#guid).

### slot

Índice del tipo de Arena:

| Valor | Descripción |
| ----- | ----------- |
| 0     | 2v2         |
| 1     | 3v3         |
| 2     | 5v5         |

### matchmakerRating

Calificación del emparejador del jugador.

### maxMMR

`field-no-description|4` (¿MMR máximo?)
