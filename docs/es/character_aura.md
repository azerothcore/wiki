# character\_aura

[<-Volver a:Characters](database-characters)

**Tabla \`character\_aura\`**

Alberga información del aura que es cargada cuando un personaje ingresa al mundo, por lo cual aquellas auras que tenía el personaje antes de desconectarse siguen manteniéndose, aún cuando el jugador ingresa pasado cierto tiempo. Un hechizo, por ejemplo, puede tener hasta tres auras al tiempo, una en cada uno de sus efectos.

**Estructura**

| Campo                 | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentario                          |
| --------------------- | --------- | --------- | ----- | ---- | ----------- | ----- | ----------------------------------- |
| [guid][1]             | INT       | UNSIGNED  | PRI   | NO   | 0           |       | Identificador único global          |
| [casterGuid][2]       | BIGINT    | UNSIGNED  | PRI   | NO   | 0           |       | Identificador único global completo |
| [itemGuid][3]         | BIGINT    | UNSIGNED  | PRI   | NO   | 0           |       |                                     |
| [spell][4]            | MEDIUMINT | UNSIGNED  | PRI   | NO   | 0           |       |                                     |
| [effectMask][5]       | TINYINT   | UNSIGNED  | PRI   | NO   | 0           |       |                                     |
| [recalculateMask][6]  | TINYINT   | UNSIGNED  |       | NO   | 0           |       |                                     |
| [stackCount][7]       | TINYINT   | UNSIGNED  |       | NO   | 1           |       |                                     |
| [amount0][8]          | INT       | SIGNED    |       | NO   | 0           |       |                                     |
| [amount1][9]          | INT       | SIGNED    |       | NO   | 0           |       |                                     |
| [amount2][10]         | INT       | SIGNED    |       | NO   | 0           |       |                                     |
| [base_amount0][11]    | INT       | SIGNED    |       | NO   | 0           |       |                                     |
| [base_amount1][12]    | INT       | SIGNED    |       | NO   | 0           |       |                                     |
| [base_amount2][13]    | INT       | SIGNED    |       | NO   | 0           |       |                                     |
| [maxDuration][14]     | INT       | SIGNED    |       | NO   | 0           |       |                                     |
| [remainTime][15]      | INT       | SIGNED    |       | NO   | 0           |       |                                     |
| [remainCharges][16]   | TINYINT   | UNSIGNED  |       | NO   | 0           |       |                                     |

[1]: #guid
[2]: #casterguid
[3]: #itemguid
[4]: #spell
[5]: #effectmask
[6]: #recalculatemask
[7]: #stackcount
[8]: #amount
[9]: #amount
[10]: #amount
[11]: #baseamount0
[12]: #baseamount1
[13]: #baseamount2
[14]: #maxduration
[15]: #remaintime
[16]: #remaincharges

**Descripción de los Campos**

### guid

GUID o Identificador Global Único del personaje afectado por el aura. Véase [characters.guid](characters#guid).

### casterGuid

GUID del personaje que lanzó el aura al primer personaje citado. Véase [characters.guid](characters#guid).

### itemGuid

GUID del Item que lanzó el aura al primer personaje citado. Véase [item\_instance.guid](item\_instance#guid).

### spell

El hechizo a partir del cual se aplicó el aura. Véase [Spell.dbc](spell) columna número 1.

### effectMask

El índice de efecto del hechizo del que proviene el aura. Un hechizo tiene hasta tres efectos, con un índice de 0, 1 o 2.

### recalculateMask

`field-no-description|5`

### stackcount

Determina cuántas cargas del hechizo (aura) tiene el personaje.

### amount

Modificador del valor asociado con el aura.

### base\_amount0

`field-no-description|11`

### base\_amount1

`field-no-description|12`

### base\_amount2

`field-no-description|13`

### maxduration

Duración máxima del aura en milisegundos.

### remaintime

El tiempo restante en milisegundos del aura. El valor -1 significa que el aura es indefinida.

### remaincharges

El número de cargas restantes del aura.
