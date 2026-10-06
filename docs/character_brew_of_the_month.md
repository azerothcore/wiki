# character\_brew\_of\_the\_month

[<-Back-to:Characters](database-characters)

**The \`character\_brew\_of\_the\_month\` table**

Stores, for each character, the last Brew of the Month event the core recorded for it.

**Table: character\_brew\_of\_the\_month's Structure**

| Field                       | Type |          | Null | Key | Default | Extra | Comment |
| :-------------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid)               | INT  | UNSIGNED | NO   | PRI |         |       |         |
| [lastEventId](#lasteventid) | INT  | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### guid

GUID of the character. See [characters.guid](characters#guid).

### lastEventId

The Brew of the Month [game event](game_event) the character last got a mail for. Characters with the Brew of the Month achievement get one mail per month when they log in during that month's event.
