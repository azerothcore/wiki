# account\_tutorial

[<-Back-to:Characters](database-characters)

**The \`account\_tutorial\` table**

This table is used to store the tutorial state of all the accounts.

**Table: account\_tutorial's Structure**

| Field                   | Type |          | Null | Key | Default | Extra | Comment            |
| :---------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :----------------- |
| [accountId](#accountid) | INT  | UNSIGNED | NO   | PRI | 0       |       | Account Identifier |
| [tut0](#tut0-7)         | INT  | UNSIGNED | NO   |     | 0       |       |                    |
| [tut1](#tut0-7)         | INT  | UNSIGNED | NO   |     | 0       |       |                    |
| [tut2](#tut0-7)         | INT  | UNSIGNED | NO   |     | 0       |       |                    |
| [tut3](#tut0-7)         | INT  | UNSIGNED | NO   |     | 0       |       |                    |
| [tut4](#tut0-7)         | INT  | UNSIGNED | NO   |     | 0       |       |                    |
| [tut5](#tut0-7)         | INT  | UNSIGNED | NO   |     | 0       |       |                    |
| [tut6](#tut0-7)         | INT  | UNSIGNED | NO   |     | 0       |       |                    |
| [tut7](#tut0-7)         | INT  | UNSIGNED | NO   |     | 0       |       |                    |

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
