# mail\_items

[<-Back-to:Characters](database-characters)

**The \`mail\_items\` table**

This table contains data regarding items from item\_instance which are being sent via email.

**Table Structure**

| Field          | Type | Attributes | Key | Null | Default | Extra | Comment                            |
| -------------- | ---- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [mail_id][1]   | INT  | UNSIGNED   |     | NO   | 0       |       |                                    |
| [item_guid][2] | INT  | UNSIGNED   | PRI | NO   | 0       |       |                                    |
| [receiver][3]  | INT  | UNSIGNED   |     | NO   | 0       |       | Character Global Unique Identifier |

[1]: #mailid
[2]: #itemguid
[3]: #receiver

**Description of the fields**

### mail\_id

Mail ID the item is attached to.

### item\_guid

This is the guid of the item from [item\_instance.guid](item_instance#guid).

### receiver

Character guid which should receive this item.
