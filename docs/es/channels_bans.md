# channels\_bans

[<-Volver a:Characters](database-characters)

**Tabla \`channels\_bans\`**

**Estructura**

| Campo           | Tipo  | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| --------------- | ----- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [channelId][1]  | INT   | UNSIGNED  | PRI   | NO   |             |       |            |
| [playerGUID][2] | INT   | UNSIGNED  | PRI   | NO   |             |       |            |
| [banTime][3]    | INT   | UNSIGNED  |       | NO   |             |       |            |

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
