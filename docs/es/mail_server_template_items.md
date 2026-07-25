# mail_server_template_items

[<-Volver a:Characters](database-characters)

**Tabla \`mail_server_template_items\`**

Funciona junto con [mail_server_template](mail_server_template).

Nota: Las entradas de esta tabla se borrarán automáticamente cuando se elimine la entrada referenciada en [mail_server_template.id](mail_server_template#id). CONSTRAINT `fk_mail_template`

**Estructura**

| Field                     | Type | Attributes | Key | Null | Default | Extra          | Comment |
| ------------------------- | ---- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [id](#id)                 | INT  | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [templateID](#templateid) | INT  | UNSIGNED   |     | NO   |         |                |         |
| [faction](#moneyh)        | ENUM |            |     | NO   |         |                |         |
| [item](#item)             | INT  | UNSIGNED   |     | NO   |         |                |         |
| [itemCount](#itemcount)   | INT  | UNSIGNED   |     | NO   |         |                |         |

**Descripción de los campos**

### id

ID único.

### templateID

[mail_server_template.id](mail_server_template#id).

### faction

- Alliance
- Horde

### item

Entry del item. Ver [item_template.entry](item_template#entry).

### itemCount

Número de copias a enviar.
