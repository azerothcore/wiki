# creature_template_movement

[<-Volver a:World](database-world)

Esta tabla contiene la descripción de los movimientos de las criaturas, dónde pueden moverse y atacar.

Esta tabla se puede anular mediante la función "anulación del movimiento de criaturas".

**Estructura**

| Campo                      | Tipo    | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| -------------------------- | ------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [CreatureId][1]            | INT     | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [Ground][2]                | TINYINT | UNSIGNED  |       | Si   | NULL        |       |            |
| [Swim][3]                  | TINYINT | UNSIGNED  |       | Si   | NULL        |       |            |
| [Flight][4]                | TINYINT | UNSIGNED  |       | Si   | NULL        |       |            |
| [Rooted][5]                | TINYINT | UNSIGNED  |       | Si   | NULL        |       |            |
| [Chase][6]                 | TINYINT | UNSIGNED  |       | Si   | NULL        |       |            |
| [Random][7]                | TINYINT | UNSIGNED  |       | Si   | NULL        |       |            |
| [InteractionPauseTimer][8] | TINYINT | UNSIGNED  |       | Si   | NULL        |       |            |

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

Esta es la [creature\_template.entry](creature_template#entry) a la que está vinculado el script.

#### Ground

| Estado  | Valor |
| ------- | ----- |
| Ninguno | 0     |
| Correr  | 1     |
| Flotar  | 2     |

#### Swim

| Estado  | Valor |
| ------- | ----- |
| Ninguno | 0     |
| Nadar   | 1     |

#### Flight

| Estado                 | Valor |
| ---------------------- | ----- |
| Ninguno                | 0     |
| Desactivar la gravedad | 1     |
| Puede volar            | 2     |

#### Rooted

| Estado    | Valor |
| --------- | ----- |
| Ninguno   | 0     |
| Arraigado | 1     |

Aviso:

La criatura enraizada que no cae una vez muerta debe usar \`Suelo\`=1, \`Nadar\`=0, \`Vuelo\`=0, \`Enraizada\`=1 (\`Nadar\`=1 si está sobre el agua)

La criatura enraizada que cae una vez muerta debe usar \`Tierra\`=0, \`Nadar\`=0, \`Vuelo\`=1, \`Enraizada\`=1

#### Chase

| Estado         | Valor |
| -------------- | ----- |
| Correr         | 0     |
| Puede caminar  | 1     |
| Camina siempre | 2     |

#### Random

| Estado        | Valor |
| ------------- | ----- |
| Caminar       | 0     |
| Puede correr  | 1     |
| Siempre corre | 2     |

#### InteractionPauseTimer

Tiempo (en milisegundos) durante el cual la criatura no se moverá después de la interacción con el jugador.
