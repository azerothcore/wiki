# log\_money

[<-Back-to:Characters](database-characters)

**The \`log\_money\` table**

**Table Structure**

| Field              | Type      | Attributes | Key | Null | Default | Extra | Comment                                              |
| ------------------ | --------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------------------------- |
| [sender_acc][1]    | INT       | UNSIGNED   |     | NO   |         |       |                                                      |
| [sender_guid][2]   | INT       | UNSIGNED   |     | NO   |         |       |                                                      |
| [sender_name][3]   | CHAR(32)  | SIGNED     |     | NO   |         |       |                                                      |
| [sender_ip][4]     | CHAR(32)  | SIGNED     |     | NO   |         |       |                                                      |
| [receiver_acc][5]  | INT       | UNSIGNED   |     | NO   |         |       |                                                      |
| [receiver_name][6] | CHAR(32)  | SIGNED     |     | NO   |         |       |                                                      |
| [money][7]         | BIGINT    | UNSIGNED   |     | NO   |         |       |                                                      |
| [topic][8]         | CHAR(255) | SIGNED     |     | NO   |         |       |                                                      |
| [date][9]          | DATETIME  | SIGNED     |     | NO   |         |       |                                                      |
| [type][10]         | TINYINT   | SIGNED     |     | NO   |         |       | 1=COD,2=AH,3=GB DEPOSIT,4=GB WITHDRAW,5=MAIL,6=TRADE |

[1]: #senderacc
[2]: #senderguid
[3]: #sendername
[4]: #senderip
[5]: #receiveracc
[6]: #receivername
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

### type

| Name | Value       |
| ---- | ----------- |
| 1    | COD         |
| 2    | AH          |
| 3    | GB DEPOSIT  |
| 4    | GB WITHDRAW |
| 5    | MAIL        |
| 6    | TRADE       |
