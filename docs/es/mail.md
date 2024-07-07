# mail

[<-Volver a:Characters](database-characters)

Leer en: [English :gb:](../mail) [Spanish :es:](mail)

**Tabla \`mail\`**

Esta tabla contiene datos principales sobre todos los correos del juego.

**Estructura**

| Field               | Type     | Attributes | Key | Null | Default | Extra | Comment                            |
| ------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [id][1]             | INT      | UNSIGNED   | PRI | NO   | 0       |       | Identifier                         |
| [messageType][2]    | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                    |
| [stationery][3]     | TINYINT  | UNSIGNED   |     | NO   | 41      |       |                                    |
| [mailTemplateId][4] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                    |
| [sender][5]         | INT      | UNSIGNED   |     | NO   | 0       |       | Character Global Unique Identifier |
| [receiver][6]       | INT      | UNSIGNED   |     | NO   | 0       |       | Character Global Unique Identifier |
| [subject][7]        | LONGTEXT | SIGNED     |     | YES  |         |       |                                    |
| [body][8]           | LONGTEXT | SIGNED     |     | YES  |         |       |                                    |
| [has_items][9]      | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                    |
| [expire_time][10]   | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [deliver_time][11]  | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [money][12]         | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [cod][13]           | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [checked][14]       | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                    |
| [auctionId][14]     | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |

[1]: #id
[2]: #messagetype
[3]: #stationery
[4]: #mailtemplateid
[5]: #sender
[6]: #receiver
[7]: #subject
[8]: #body
[9]: #hasitems
[10]: #expiretime
[11]: #delivertime
[12]: #money
[13]: #cod
[14]: #checked
[15]: #auctionid

**Descripción de los campos**

### id

Este campo contiene una ID único de cualquier mensaje.

¡No tengas autoincremento!

### messageType

-   0 = Normal
-   1 = doesn't exist
-   2 = Auction
-   3 = Creature
-   4 = Gameobject
-   5 = Item

### stationery

Este campo puede contener estos valores:

-   1 = Test
-   41 = Normal mail layout
-   61 = GM (Blizzard)
-   62 = Auction
-   64 = VAL (???)
-   65 = CHR (???)

### mailTemplateId

Id de MailTemplate.dbc

### sender

En este campo se contiene el remitente [character.guid](character#guid).

### receiver

Aquí está el [character.guid](character#guid) del receptor.

### subject

Aquí está el asunto del correo almacenado.

### body

El texto contenido en el correo. La longitud máxima es de 8000 caracteres.

### has_items

Predeterminado: 0,

Cuando se establece en 1, ese correo puede contener elementos.

Para ver los elementos, consulte la tabla [mail\_items](mail_items).

### expire\_time

Aquí hay una marca de tiempo que almacena la fecha para el correo de retorno automático al remitente.

### deliver\_time

Aquí hay una marca de tiempo que almacena la fecha de envío del correo.

### money

La cantidad de dinero en el correo, o dinero para pagar cuando es contra reembolso.

### cod

Predeterminado: 0 - Sin COD,

cuando se establece en 1, ese campo \`money\` almacena oro para contra reembolso.

### checked

| Flag | Comment                     |
| ---- | --------------------------- |
| 0    | MAIL_CHECK_MASK_NONE        |
| 1    | MAIL_CHECK_MASK_READ        |
| 2    | MAIL_CHECK_MASK_RETURNED    |
| 4    | MAIL_CHECK_MASK_COPIED      |
| 8    | MAIL_CHECK_MASK_COD_PAYMENT |
| 16   | MAIL_CHECK_MASK_HAS_BODY    |

### auctionId

`campo-sin-descripción|14`
