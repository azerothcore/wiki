# mail\_server\_template\_items

[<-Back-to:Characters](database-characters)

**The \`mail\_server\_template\_items\` table**

Works together with [mail_server_template](mail_server_template).

Note: Entries in this table will be deleted automatically when the referenced entry in [mail_server_template.id](mail_server_template#id) is deleted. CONSTRAINT `fk_mail_template`

**Table: mail\_server\_template\_items's Structure**

| Field                     | Type |                | Null | Key | Default | Extra          | Comment |
| :------------------------ | :--- | :------------- | :--: | :-: | :-----: | :------------: | :------ |
| [id](#id)                 | INT  | UNSIGNED       | NO   | PRI |         | AUTO_INCREMENT |         |
| [templateID](#templateid) | INT  | UNSIGNED       | NO   | MUL |         |                |         |
| [faction](#faction)       | ENUM | Alliance,Horde | NO   |     |         |                |         |
| [item](#item)             | INT  | UNSIGNED       | NO   |     |         |                |         |
| [itemCount](#itemcount)   | INT  | UNSIGNED       | NO   |     |         |                |         |

**Description of the table's fields**

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
