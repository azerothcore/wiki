# log\_money

[<-Back-to:Characters](database-characters)

**The \`log\_money\` table**

**Table: log\_money's Structure**

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

**Description of the table's fields**

### sender\_acc

Account of the player who gave the money. See [account.id](account#id).

### sender\_guid

GUID of the character who gave the money. See [characters.guid](characters#guid).

### sender\_name

Name of the character who gave the money.

### sender\_ip

IP of the player who gave the money.

### receiver\_acc

Account of the player who got the money. See [account.id](account#id).

### receiver\_name

Name of the character who got the money.

### money

The amount of money in copper.

### topic

Details of the transfer, for example the mail subject, the auction or the guild bank.

### date

The date and time of the transfer.

### type

| Name | Value       |
| ---- | ----------- |
| 1    | COD         |
| 2    | AH          |
| 3    | GB DEPOSIT  |
| 4    | GB WITHDRAW |
| 5    | MAIL        |
| 6    | TRADE       |
