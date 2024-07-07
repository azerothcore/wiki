# account\_instance\_times

[<-Volver a: Characters](database-characters)

**La tabla \`account\_instance\_times\`**

Esta tabla controla en que tantas instancias han estado los personajes de la cuenta por una hora. Si hay 5 registros por cuenta, el jugador no podrá entrar a otra instancia.

**Estructura**

| Field            | Type   | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [accountId][1]   | INT    | UNSIGNED   | PRI | NO   |         |       |         |
| [instanceId][2]  | INT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [releaseTime][3] | BIGINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #accountid
[2]: #instanceid
[3]: #releasetime

**Descripción de los campos**

### accountId

Cuenta del jugador. Véase [account.id](account#id).

### instanceId

Estas son las id de las instancias en las que el jugador ha pasado 5 horas.

### releaseTime

Cuando las instancias deberán estar disponibles de nuevo, medido en Unixtime.
