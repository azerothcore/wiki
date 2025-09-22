# creature\_onkill\_reputation

[<-Volver a:World](database-world)

**Tabla \`creature\_onkill\_reputation\`**

Esta tabla controla la reputación que reciben las criaturas cuando son asesinadas por otros jugadores.

**Estructura**

| Campo                     | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentario                |
| ------------------------- | --------- | --------- | ----- | ---- | ----------- | ----- | ------------------------- |
| [creature_id][1]          | MEDIUMINT | UNSIGNED  | PRI   | NO   | 0           |       | Identificador de criatura |
| [RewOnKillRepFaction1][2] | SMALLINT  | SIGNED    |       | NO   | 0           |       |                           |
| [RewOnKillRepFaction2][3] | SMALLINT  | SIGNED    |       | NO   | 0           |       |                           |
| [MaxStanding1][4]         | TINYINT   | SIGNED    |       | NO   | 0           |       |                           |
| [IsTeamAward1][5]         | TINYINT   | SIGNED    |       | NO   | 0           |       |                           |
| [RewOnKillRepValue1][6]   | MEDIUMINT | SIGNED    |       | NO   | 0           |       |                           |
| [MaxStanding2][7]         | TINYINT   | SIGNED    |       | NO   | 0           |       |                           |
| [IsTeamAward2][8]         | TINYINT   | SIGNED    |       | NO   | 0           |       |                           |
| [RewOnKillRepValue2][9]   | MEDIUMINT | SIGNED    |       | NO   | 0           |       |                           |
| [TeamDependent][10]       | TINYINT   | UNSIGNED  |       | NO   | 0           |       |                           |

[1]: #creature_id
[2]: #rewonkillrepfaction1
[3]: #rewonkillrepfaction2
[4]: #maxstanding1
[5]: #isteamaward1
[6]: #rewonkillrepvalue1
[7]: #maxstanding2
[8]: #isteamaward2
[9]: #rewonkillrepvalue2
[10]: #teamdependent

**Descripción de los campos**

### creature\_id

El ID de plantilla de la criatura. Véase [creature\_template.entry](creature_template#creature_template-entry)

### RewOnKillRepFaction

El ID de la facción en la que el jugador ganará o perderá puntos. Ver Faction.dbc

### MaxStanding

El nivel máximo que la criatura otorgará en reputación. Si el jugador alcanza este nivel o uno superior, la criatura no otorgará reputación.

| ID  | Rango      |
| --- | ---------- |
| 0   | Odiado     |
| 1   | Hostil     |
| 2   | Antipático |
| 3   | Neutral    |
| 4   | Amistoso   |
| 5   | Honrado    |
| 6   | Venerado   |
| 7   | Exaltado   |

### IsTeamAward

Booleano 0 o 1 que controla si el jugador recibe la reputación no solo de la facción sino también del equipo de la facción.

-   0: El jugador recibe reputación solo por la facción
-   1: El jugador recibe reputación tanto para la facción como para el equipo de la facción.

NOTA: El valor de reputación que el jugador gana para el equipo (si el campo es 1) es la mitad del valor especificado en [RewOnKillRepValue](#creature_onkill_reputation-RewOnKillRepValue)

### RewOnKillRepValue

El valor de reputación que el jugador gana (o pierde si es negativo) al matar a la criatura.

### TeamDependent

Booleano 0 o 1.

-   0: La criatura otorgará reputación a cualquier jugador de ambos campos (RewOnKillRepFaction1 y RewOnKillRepFaction2) si ambos campos son distintos de cero.
-   1: La criatura otorgará a los jugadores de la alianza la reputación de RewOnKillRepFaction1 y otorgará a los jugadores de la Horda la reputación de RewOnKillRepFaction2
