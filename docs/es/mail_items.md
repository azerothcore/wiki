# mail\_items

[<-Volver a:Characters](database-character)

Leer en: [English :gb:](../mail_items) [Spanish :es:](mail_items)

**Tabla \`mail\_items\`**

Esta tabla contiene datos sobre los elementos de item\_instance que se envían por correo electrónico.

**Estructura**

| Field          | Type | Attributes | Key | Null | Default | Extra | Comment                            |
| -------------- | ---- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [mail_id][1]   | INT  | UNSIGNED   |     | NO   | 0       |       |                                    |
| [item_guid][2] | INT  | UNSIGNED   | PRI | NO   | 0       |       |                                    |
| [receiver][3]  | INT  | UNSIGNED   |     | NO   | 0       |       | Character Global Unique Identifier |

[1]: #mailid
[2]: #itemguid
[3]: #receiver

**Descripción de los campos**

### mail\_id

ID de correo al que está adjunto el artículo.

### item\_guid

Esta es la guid del elemento de [item\_instance.guid](item_instance#guid).

### receiver

Character guid que debería recibir este artículo.
