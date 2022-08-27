# mail_server_template

[<-Volver a:Character](database-character.md)

**Tabla \`mail_server_template\`**

La tabla contiene información del correo del servidor que se enviará a los jugadores que cumplan con el requisito. Los correos son enviados al iniciar sesión.

**Estructura**

| Field            | Type    | Attributes | Key | Null | Default | Extra          | Comment |
| ---------------- | ------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [id][1]          | INT     | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [reqLevel][2]    | TINYINT | UNSIGNED   |     | NO   | 0       |                |         |
| [reqPlayTime][3] | INT     | UNSIGNED   |     | NO   | 0       |                |         |
| [moneyA][4]      | INT     | UNSIGNED   |     | NO   | 0       |                |         |
| [moneyH][5]      | INT     | UNSIGNED   |     | NO   | 0       |                |         |
| [itemA][6]       | INT     | UNSIGNED   |     | NO   | 0       |                |         |
| [itemCountA][7]  | INT     | UNSIGNED   |     | NO   | 0       |                |         |
| [itemH][8]       | INT     | UNSIGNED   |     | NO   | 0       |                |         |
| [itemCountH][9]  | INT     | UNSIGNED   |     | NO   | 0       |                |         |
| [subject][10]    | TEXT    |            |     | NO   |         |                |         |
| [body][11]       | TEXT    |            |     | NO   |         |                |         |
| [active][12]     | TINYINT | UNSIGNED   |     | NO   | 1       |                |         |

[1]: #id
[2]: #reqlevel
[3]: #reqplaytime
[4]: #moneya
[5]: #moneyh
[6]: #itema
[7]: #itemcounta
[8]: #itemh
[9]: #itemcounth
[10]: #subject
[11]: #body
[12]: #active

## Descripción de los Campos

### id

Identificador único.

### reqLevel

Nivel requerido del jugador para recibir el correo.

### reqPlayTime

Tiempo de juego necesario en milisegundos para recibir el correo.

### moneyA

Dinero en monedas de cobre que será enviado al jugador de la Alianza.

### moneyH

Dinero en monedas de cobre que será enviado al jugador de la Horda.

### itemA

[item_template.entry](item_template#entry) Item que será enviado al jugador de la Alianza.

### itemCountA

Cuántos de los items especificados previamente en [itemA](#itema) serán enviados.

### itemH

[item_template.entry](item_template#entry) Item que será enviado al jugador de la Alianza.

### itemCountH

Cuántos de los items especificados previamente en [itemH](#itemh) serán enviados.

### subject

El título/asunto del correo.

### body

El cuerpo de texto del correo.

### active

En booleanos:

- 1 = El correo estará activo y será enviado al jugador sí cumple el requisito.
- 0 = Inhabilitado.