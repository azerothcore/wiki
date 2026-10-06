# mail\_items

[<-Back-to:Characters](database-characters)

**The \`mail\_items\` table**

This table contains data regarding items from item\_instance which are being sent via email.

**Table: mail\_items's Structure**

| Field                  | Type |          | Null | Key | Default | Extra | Comment                            |
| :--------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :--------------------------------- |
| [mail_id](#mailid)     | INT  | UNSIGNED | NO   | MUL | 0       |       |                                    |
| [item_guid](#itemguid) | INT  | UNSIGNED | NO   | PRI | 0       |       |                                    |
| [receiver](#receiver)  | INT  | UNSIGNED | NO   | MUL | 0       |       | Character Global Unique Identifier |

**Description of the table's fields**

### mail\_id

Mail ID the item is attached to.

### item\_guid

This is the guid of the item from [item\_instance.guid](item_instance#guid).

### receiver

Character guid which should receive this item.
