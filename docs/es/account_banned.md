# account\_banned

[<-Volver a: Auth](database-auth)

**Tabla \`account\_banned\`**

Esta tabla enumera todas las cuentas que han sido baneadas junto con la fecha en la que (en tal caso) expirase el baneo.

**Estructura**

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment    |
| -------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ---------- |
| [id][1]        | INT          | UNSIGNED   | PRI | NO   | 0       |       | Account id |
| [bandate][2]   | INT          | UNSIGNED   | PRI | NO   | 0       |       |            |
| [unbandate][3] | INT          | UNSIGNED   |     | NO   | 0       |       |            |
| [bannedby][4]  | VARCHAR(50)  | SIGNED     |     | NO   |         |       |            |
| [banreason][5] | VARCHAR(255) | SIGNED     |     | NO   |         |       |            |
| [active][6]    | TINYINT      | UNSIGNED   |     | NO   | 1       |       |            |

[1]: #id
[2]: #bandate
[3]: #unbandate
[4]: #bannedby
[5]: #banreason
[6]: #active

**Descripción de los campos**

### id

El ID de la cuenta. Véase [account.id](account#id).

### bandate

La fecha en que la cuenta fue baneada, en tiempo Unix.

### unbandate

La fecha en que la cuenta será automáticamente desbaneada, en tiempo Unix. Un valor inferior en negativo a la fecha actual significa, en efecto, un baneo permanente.

### bannedby

El nombre del personaje del GM que baneó esa cuenta. Si se banea desde la consola, entonces estará vacía (hasta que se cambie).

### banreason

La razón del ban.

### active

Booleano 0 o 1 que controla si el baneo está activo o no.
