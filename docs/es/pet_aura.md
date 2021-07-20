# pet\_aura

[<-Volver a:Characters](database-characters.md)

Leer en: [English :gb:](../pet_aura) [Spanish :es:](pet_aura)

**Tabla \`pet\_aura\`**

**Estructura**

| Field                | Type      | Attributes | Key | Null | Default | Extra | Comment                       |
| -------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ----------------------------- |
| [guid][1]            | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier      |
| [casterGuid][2]      | BIGINT    | UNSIGNED   | PRI | NO   | 0       |       | Full Global Unique Identifier |
| [spell][3]           | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [effectMask][4]      | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [recalculateMask][5] | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                               |
| [stackCount][6]      | TINYINT   | UNSIGNED   |     | NO   | 1       |       |                               |
| [amount0][7]         | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [amount1][8]         | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [amount2][9]         | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [base_amount0][10]   | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [base_amount1][11]   | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [base_amount2][12]   | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [maxDuration][13]    | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [remainTime][14]     | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [remainCharges][15]  | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                               |

[1]: #guid
[2]: #casterguid
[3]: #spell
[4]: #effectmask
[5]: #recalculatemask
[6]: #stackcount
[7]: #amount
[8]: #amount
[9]: #amount
[10]: #baseamount
[11]: #baseamount
[12]: #baseamount
[13]: #maxduration
[14]: #remaintime
[15]: #remaincharges

**Descripción de los campos**

### guid

El GUID del objetivo afectado por el aura. Ver [character\_pet.id](character_pet#id).

### casterGuid

El GUID del jugador que lanzó el aura. Ver [characters.guid](characters#guid).

### spell

El hechizo desde el que se aplicó el aura. Ver [Spell.dbc](spell) columna 1.

### effectMask

El índice de efecto del hechizo del que proviene el aura. Un hechizo tiene hasta tres efectos, siendo el índice 0, 1 o 2.

### recalculateMask

`campo-sin-descripción|5`

### stackCount

Determina cuántas acumulaciones del hechizo tiene el personaje.

### amount

El valor del modificador asociado con el aura.

### base\_amount

`campo-sin-descripción|10-12`

### maxDuration

La duración máxima del aura.

### remainTime

El tiempo restante en segundos en el aura. -1 significa que el aura es indefinida.

### remainCharges

El número de cargas que quedan en el aura.
