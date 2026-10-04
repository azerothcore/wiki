# warden\_action

[<-Back-to:Characters](database-characters)

**The \`warden\_action\` table**

Overrides the action taken when a player fails a [Warden check](warden_checks).

**Table: warden\_action's Structure**

| Field                 | Type     |          | Null | Key | Default | Extra | Comment |
| :-------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [wardenId](#wardenid) | SMALLINT | UNSIGNED | NO   | PRI |         |       |         |
| [action](#action)     | TINYINT  | UNSIGNED | YES  |     | NULL    |       |         |

**Description of the table's fields**

### wardenid

The check. See [warden\_checks.id](warden_checks#id).

### action

| Value | Action |
| ----- | ------ |
| 0     | Log    |
| 1     | Kick   |
| 2     | Ban    |
