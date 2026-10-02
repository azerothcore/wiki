# account\_tutorial

[<-Back-to:Characters](database-characters)

**The \`account\_tutorial\` table**

This table is used to store the tutorial state of all the accounts.

**Table: account\_tutorial's Structure**

| Field          | Type | Attributes | Key | Null | Default | Extra | Comment            |
| -------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------------------ |
| [accountId][1] | INT  | UNSIGNED   | PRI | NO   | 0       |       | Account Identifier |
| [tut0][2]      | INT  | UNSIGNED   |     | NO   | 0       |       |                    |
| [tut1][3]      | INT  | UNSIGNED   |     | NO   | 0       |       |                    |
| [tut2][4]      | INT  | UNSIGNED   |     | NO   | 0       |       |                    |
| [tut3][5]      | INT  | UNSIGNED   |     | NO   | 0       |       |                    |
| [tut4][6]      | INT  | UNSIGNED   |     | NO   | 0       |       |                    |
| [tut5][7]      | INT  | UNSIGNED   |     | NO   | 0       |       |                    |
| [tut6][8]      | INT  | UNSIGNED   |     | NO   | 0       |       |                    |
| [tut7][9]      | INT  | UNSIGNED   |     | NO   | 0       |       |                    |

[1]: #accountid
[2]: #tut0-7
[3]: #tut0-7
[4]: #tut0-7
[5]: #tut0-7
[6]: #tut0-7
[7]: #tut0-7
[8]: #tut0-7
[9]: #tut0-7

**Description of the table's fields**

### accountId

Account of the player. See [account.id](account#id).

### tut0-7

These values 32bits flags. So 8 x 32bits values makes 256 bits available to store 256 tutorial messages status.

Each bit means:

- 0 - Not yet shown
- 1 - Shown

This is used to diplay only tutorial messages the character did not see before.

Unselecting the "Show tutorial" option in game, makes all bits to be set, so all tutX columns will contain then 11111111111111111111111111111111 binary = 4294967295 in decimal after this option is changed.
