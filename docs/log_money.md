# log\_money

[<-Back-to:Characters](database-characters.md)

**The \`log\_money\` table**

**Structure**

| Field              | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [sender_acc][1]    | INT      | UNSIGNED   |     | NO   |         |       |         |
| [sender_guid][2]   | INT      | UNSIGNED   |     | NO   |         |       |         |
| [sender_name][3]   | CHAR(32) | SIGNED     |     | NO   |         |       |         |
| [sender_ip][4]     | CHAR(32) | SIGNED     |     | NO   |         |       |         |
| [receiver_acc][5]  | INT      | UNSIGNED   |     | NO   |         |       |         |
| [receiver_name][6] | CHAR(32) | SIGNED     |     | NO   |         |       |         |
| [money][7]         | BIGINT   | UNSIGNED   |     | NO   |         |       |         |
| [topic][8]         | CHAR(255)| SIGNED     |     | NO   |         |       |         |
| [date][9]          | DATETIME | SIGNED     |     | NO   |         |       |         |

[1]: #sender_acc
[2]: #sender_guid
[3]: #sender_name
[4]: #sender_ip
[5]: #receiver_acc
[6]: #receiver_name
[7]: #money
[8]: #topic
[9]: #date

**Description of the fields**

### sender\_acc

`field-no-description|1`

### sender\_guid

`field-no-description|2`

### sender\_name

`field-no-description|3`

### sender\_ip

`field-no-description|4`

### receiver\_acc

`field-no-description|5`

### receiver\_name

`field-no-description|6`

### money

`field-no-description|7`

### topic

`field-no-description|8`

### date

`field-no-description|9`