# ip\_banned

[<-Volver a:Auth](database-auth.md)

**Tabla \`ip\_banned\`**

Esta tabla contiene todas las IPs baneadas y la fecha en la que (en tal caso) el baneo expirase.

**Estructura**

| Field          | Type         | Attributes | Key | Null | Default   | Extra | Comment |
|----------------|--------------|------------|-----|------|-----------|-------|---------|
| [ip][1]        | VARCHAR(15)  |            | PRI | NO   | 127.0.0.1 |       |         |
| [bandate][2]   | INT          | UNSIGNED   | PRI | NO   |           |       |         |
| [unbandate][3] | INT          | UNSIGNED   |     | NO   |           |       |         |
| [bannedby][4]  | VARCHAR(50)  |            |     | NO   | [Console] |       |         |
| [banreason][5] | VARCHAR(255) |            |     | NO   | no reason |       |         |

[1]: #ip
[2]: #bandate
[3]: #unbandate
[4]: #bannedby
[5]: #banreason

**Descripción de los campos**

### ip

La dirección IP que está baneada.

### bandate

La fecha en que la IP fue baneada por primera vez, en tiempo Unix.

### unbandate

La fecha en que la IP será desbaneada en tiempo Unix. Cualquier fecha que se establezca por debajo de la fecha actual básicamente se clasifica como un baneo permanente ya que nunca expirará automáticamente.

### bannedby

El nombre del personaje que baneó la IP. El personaje debe pertenecer a una cuenta con los poderes sobre el comando .ban dentro del juego.

### banreason

La razón dada para el baneo de la IP.