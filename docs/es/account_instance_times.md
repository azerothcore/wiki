# account\_instance\_times

[<-Volver a:Characters](database-characters.md)

**Tabla \`account\_instance\_times\`**

Esta tabla controla cuántas instancias han estado los personajes de la cuenta en la última hora. Si hay 5 registros por cuenta, el jugador no podrá ingresar a otra instancia.

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

Id de la cuenta del jugador. Consulte [account.id](account#id).

### instanceId

Este es el ID de instancia cuyos personajes de esta cuenta han pasado 5 horas.

### releaseTime

El tiempo en que las instancias deben volver a permitirse medido en tiempo Unix.
