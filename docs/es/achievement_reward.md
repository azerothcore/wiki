# achievement\_reward

[<-Voler a: World](database-world.md)

**La tabla \`achievement\_reward\`**

Esta tabla describe al recompensa que recibirá cuando alcance determinado logro.

**Estructura**

| Field               | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]             | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TitleA][2]         | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [TitleH][3]         | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [ItemID][4]         | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [Sender][5]         | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [Subject][6]        | VARCHAR(255) |            |     | YES  |         |       |         |
| [Body][7]           | text         |            |     | YES  |         |       |         |
| [MailTemplateID][8] | MEDIUMINT    | UNSIGNED   |     | YES  | 0       |       |         |

[1]: #id
[2]: #titlea
[3]: #titleh
[4]: #itemid
[5]: #sender
[6]: #subject
[7]: #body
[8]: #mailtemplateid

**Descripción de los campos**

### ID

Este es el ID del logro, tomado de `Achievement.dbc`.

### TitleA

Este es el ID del título para la Alianza, tomado de `CharTitles.dbc` si el logro recompensa con un title.

### TitleH

Este es el ID del título para la Horda, tomado de `CharTitles.dbc` si el logro recompensa con un title.

### ItemID

Este es el item que el jugador recibirá si el logro recompensa con un item. El jugador lo recibirá por correo.

### Sender

Este es el remitente del correo que el jugador recibirá.

### Subject

Este es el asunto del correo que el jugador recibirá.

### Body

Este es el cuerpo (texto) del correo que el jugador recibirá. This is the body (text) of the mail that the player will receive.

### MailTemplateID

ID de la plantilla de `MailTemplate.dbc` del correo que el jugador recibirá. Para usar esta columna, `Subject` y `Body` debe estar vacio ya que serán tomadas del archivo DBC.

### Ejemplo

| ID  | TitleA | TitleH | ItemID | Sender | Subject             |
| --- | ------ | ------ | ------ | ------ | ------------------- |
| 13  | 0      | 0      | 41426  | 16128  | Level 80            |
| 45  | 0      | 0      | 43348  | 28070  | You've Been Around! |
