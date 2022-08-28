# mail_server_character

[<-Volver a:Character](database-character.md)

**Tabla \`mail_server_character\`**

La tabla contiene identificadores del jugador que ha recibido un correo del servidor. Esto evita que el mismo correo sea enviado dos veces al mismo jugador.

**Estructura**

| Field       | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]   | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [mailId][2] | INT  | UNSIGNED   | PRI | NO   |         |       |         |

[1]: #guid
[2]: #mailId

## Descripción de los Campos

### guid

[characters.guid](characters#guid).

### mailId

[mail_server_template.id](mail_server_template#guid).
