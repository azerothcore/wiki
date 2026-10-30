# log\_money

[<-Back-to:Characters](database-characters)

**The \`log\_money\` table**

Logs money moved through mail, trade, the auction house and the guild bank, with the sender, the receiver, the amount and the type of transfer.

**Table: log\_money's Structure**

| Field                          | Type     |          | Null | Key | Default | Extra | Comment                                              |
| :----------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :--------------------------------------------------- |
| [sender_acc](#senderacc)       | INT      | UNSIGNED | NO   |     |         |       |                                                      |
| [sender_guid](#senderguid)     | INT      | UNSIGNED | NO   |     |         |       |                                                      |
| [sender_name](#sendername)     | TEXT     |          | NO   |     |         |       |                                                      |
| [sender_ip](#senderip)         | TEXT     |          | NO   |     |         |       |                                                      |
| [receiver_acc](#receiveracc)   | INT      | UNSIGNED | NO   |     |         |       |                                                      |
| [receiver_name](#receivername) | TEXT     |          | NO   |     |         |       |                                                      |
| [money](#money)                | BIGINT   | UNSIGNED | NO   |     |         |       |                                                      |
| [topic](#topic)                | TEXT     |          | NO   |     |         |       |                                                      |
| [date](#date)                  | DATETIME |          | NO   |     |         |       |                                                      |
| [type](#type)                  | TINYINT  |          | NO   |     |         |       | 1=COD,2=AH,3=GB DEPOSIT,4=GB WITHDRAW,5=MAIL,6=TRADE |

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
