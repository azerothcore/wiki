# mail_server_template_items

[<-Back-to:Characters](database-characters)

**The \`mail_server_template_items\` table**

Works together with [mail_server_template](mail_server_template).

Note: Entries in this table will be deleted automatically when the referenced entry in [mail_server_template.id](mail_server_template#id) is deleted. CONSTRAINT `fk_mail_template`

**Table Structure**

| Field                     | Type | Attributes | Key | Null | Default | Extra          | Comment |
| ------------------------- | ---- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [id](#id)                 | INT  | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [templateID](#templateid) | INT  | UNSIGNED   |     | NO   |         |                |         |
| [faction](#moneyh)        | ENUM |            |     | NO   |         |                |         |
| [item](#item)             | INT  | UNSIGNED   |     | NO   |         |                |         |
| [itemCount](#itemcount)   | INT  | UNSIGNED   |     | NO   |         |                |         |

**Description of the fields**

### id

Unique ID.

### templateID

[mail_server_template.id](mail_server_template#id).

### faction

- Alliance
- Horde

### item

Item entry. See [item_template.entry](item_template#entry).

### itemCount

Number of copies to send.
