# account\_tutorial

[<-Back-to:Characters](database-characters)

**The \`account\_tutorial\` table**

This table is used to store the tutorial state of all the accounts.

**Table Structure**

| Field          | Type | Attributes | Key | Null | Default | Extra  | Comment            |
| -------------- | ---- | ---------- | --- | ---- | ------- | ------ | ------------------ |
| [accountId][1] | INT  | UNSIGNED   | PRI | NO   | 0       | Unique | Account Identifier |
| [tut0][2]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |
| [tut1][3]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |
| [tut2][4]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |
| [tut3][5]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |
| [tut4][6]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |
| [tut5][7]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |
| [tut6][8]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |
| [tut7][9]      | INT  | UNSIGNED   |     | NO   | 0       |        |                    |

[1]: #accountid
[2]: #tut0
[3]: #tut1
[4]: #tut2
[5]: #tut3
[6]: #tut4
[7]: #tut5
[8]: #tut6
[9]: #tut7

**Description of the fields**

### guid

Account of the player. See [account.id](account#id).

### tut0

`field-no-description|2`

### tut1

`field-no-description|3`

### tut2

`field-no-description|4`

### tut3

`field-no-description|5`

### tut4

`field-no-description|6`

### tut5

`field-no-description|7`

### tut6

`field-no-description|8`

### tut7

These values 32bits flags. So 8 x 32bits values makes 256 bits available to store 256 tutorial messages status.

Each bit means:

- 0 - Not yet shown
- 1 - Shown

This is used to diplay only tutorial messages the character did not see before.

Unselecting the "Show tutorial" option in game, makes all bits to be set, so all tutX columns will contain then 11111111111111111111111111111111 binary = 4294967295 in decimal after this option is changed.
