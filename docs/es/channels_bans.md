# channels\_bans

[<-Volver a:Characters](database-characters.md)

Leer en: [English :gb:](../channels_bans) [Spanish :es:](channels_bans)

**Tabla \`channels\_bans\`**

**Estructura**

| Field           | Type  | Attributes | Key | Null | Default | Extra  | Comment |
| --------------- | ----- | ---------- | --- | ---- | ------- | ------ | ------- |
| [channelId][1]  | INT   | UNSIGNED   | PRI | NO   |         |        |         |
| [playerGUID][2] | INT   | UNSIGNED   | PRI | NO   |         |        |         |
| [banTime][3]    | INT   | UNSIGNED   |     | NO   |         |        |         |

[1]: #channelid
[2]: #playerguid
[3]: #banTime

**Descripción de los campos**

### channelId

El [channel.id](channels#channelid).

### playerGUID

`campo-sin-descripción|2`

### banTime

El tiempo de baneo del [channel](channels#channelid).
