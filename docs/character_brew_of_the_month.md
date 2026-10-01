# character\_brew\_of\_the\_month

[<-Back-to:Characters](database-characters)

**The \`character\_brew\_of\_the\_month\` table**

**Table Structure**

| Field            | Type | Attributes | Key | Null | Default | Extra | Comment  |
| ---------------- | ---- | ---------- | --- | ---- | ------- | ----- | -------- |
| [guid][1]        | INT  | UNSIGNED   | PRI | NO   |         |       |          |
| [lastEventId][2] | INT  | UNSIGNED   |     | NO   | 0       |       |          |

[1]: #guid
[2]: #lasteventid

**Description of the fields**

### guid

GUID of the character. See [characters.guid](characters#guid).

### lastEventId

The Brew of the Month [game event](game_event) the character last got a mail for. Characters with the Brew of the Month achievement get one mail per month when they log in during that month's event.
