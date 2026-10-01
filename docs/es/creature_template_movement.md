# creature_template_movement

[<-Volver a: World](database-world)

Esta tabla contiene la descripción de los movimientos de las criaturas: dónde puede moverse y atacar la criatura.

Esta tabla puede ser sobrescrita por \`creature_movement_override\`

**Estructura**

| Field                      | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [CreatureId][1]            | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Ground][2]                | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Swim][3]                  | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Flight][4]                | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Rooted][5]                | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Chase][6]                 | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Random][7]                | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [InteractionPauseTimer][8] | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |

[1]: #creatureid
[2]: #ground
[3]: #swim
[4]: #flight
[5]: #rooted
[6]: #chase
[7]: #random
[8]: #interactionpausetimer

**Descripción de los campos**

#### CreatureId

Este es el [creature\_template.entry](creature_template#entry) al que está enlazado el script.

#### Ground

| State | Value |
| ----- | ----- |
| None  | 0     |
| Run   | 1     |
| Hover | 2     |

#### Swim

| State | Value |
| ----- | ----- |
| None  | 0     |
| Swim  | 1     |

#### Flight

| State          | Value |
| -------------- | ----- |
| None           | 0     |
| DisableGravity | 1     |
| CanFly         | 2     |

#### Rooted

| State  | Value |
| ------ | ----- |
| None   | 0     |
| Rooted | 1     |

Aviso:

Una criatura enraizada (rooted) que no cae al morir debe usar \`Ground\`=1, \`Swim\`=0, \`Flight\`=0, \`Rooted\`=1 (\`Swim\`=1 si está sobre el agua)

Una criatura enraizada que sí cae al morir debe usar \`Ground\`=0, \`Swim\`=0, \`Flight\`=1, \`Rooted\`=1

#### Chase

| State      | Value |
| ---------- | ----- |
| Run        | 0     |
| CanWalk    | 1     |
| AlwaysWalk | 2     |

#### Random

| State     | Value |
| --------- | ----- |
| Walk      | 0     |
| CanRun    | 1     |
| AlwaysRun | 2     |

#### InteractionPauseTimer

Tiempo (en milisegundos) durante el cual la criatura no se moverá tras interactuar con un jugador.
