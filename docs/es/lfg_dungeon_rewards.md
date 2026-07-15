# lfg\_dungeon\_rewards

[<-Volver a:World](database-world)

**Tabla \`lfg\_dungeon\_encounters\`**

`tabla-sin-descripción|0`

**Estructura**

| Field              | Type    | Attributes | Key | Null | Default | Extra | Comment                                                                                         |
| ------------------ | ------- | ---------- | --- | ---- | ------- | ----- | ----------------------------------------------------------------------------------------------- |
| [dungeonId][1]     | INT     | UNSIGNED   | PRI | NO   | 0       |       | Entry de la mazmorra del dbc                                                                    |
| [maxlevel][2]      | TINYINT | UNSIGNED   | PRI | NO   | 0       |       | Nivel máximo al que se otorga esta recompensa                                                    |
| [firstQuestId][3]  | INT     | UNSIGNED   |     | NO   | 0       |       | Id de quest con recompensas para la primera mazmorra de este día                                 |
| [firstMoneyVar][4] | INT     | UNSIGNED   |     | NO   | 0       |       | Multiplicador de dinero por completar la mazmorra por primera vez en un día con menos jugadores que el máximo |
| [firstXPVar][5]    | INT     | UNSIGNED   |     | NO   | 0       |       | Multiplicador de experiencia por completar la mazmorra por primera vez en un día con menos jugadores que el máximo |
| [otherQuestId][6]  | INT     | UNSIGNED   |     | NO   | 0       |       | Id de quest con recompensas para la N-ésima mazmorra de este día                                 |
| [otherMoneyVar][7] | INT     | UNSIGNED   |     | NO   | 0       |       | Multiplicador de dinero por completar la mazmorra la N-ésima vez en un día con menos jugadores que el máximo |
| [otherXPVar][8]    | INT     | UNSIGNED   |     | NO   | 0       |       | Multiplicador de experiencia por completar la mazmorra la N-ésima vez en un día con menos jugadores que el máximo |

[1]: #dungeonid
[2]: #maxlevel
[3]: #firstquestid
[4]: #firstmoneyvar
[5]: #firstxpvar
[6]: #otherquestid
[7]: #othermoneyvar
[8]: #otherxpvar

**Descripción de los campos**

### dungeonId

ID de la mazmorra de LFGDungeons.dbc

### maxlevel

Nivel máximo al que se otorga esta recompensa

### firstQuestId

Quest\_template.id con recompensas para la primera mazmorra de este día.

### firstMoneyVar

Multiplicador de dinero por completar la mazmorra por primera vez en un día con menos jugadores que el máximo.

### firstXPVar

Multiplicador de experiencia por completar la mazmorra por primera vez en un día con menos jugadores que el máximo.

### otherQuestId

Quest\_template.id con recompensas para la N-ésima mazmorra de este día

### otherMoneyVar

Multiplicador de dinero por completar la mazmorra la N-ésima vez en un día con menos jugadores que el máximo.

### otherXPVar

Multiplicador de experiencia por completar la mazmorra la N-ésima vez en un día con menos jugadores que el máximo.
