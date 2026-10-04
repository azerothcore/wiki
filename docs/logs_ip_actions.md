# logs\_ip\_actions

[<-Back-to:Auth](database-auth)

**The \`logs\_ip\_actions\` table**

Logs the IP address used for account and character actions. It is only filled when `Allow.IP.Based.Action.Logging` is enabled in worldserver.conf.

**Table: logs\_ip\_actions's Structure**

| Field                            | Type        |          | Null | Key | Default           | Extra          | Comment                       |
| :------------------------------- | :---------- | :------- | :--: | :-: | :---------------: | :------------: | :---------------------------- |
| [id](#id)                        | INT         | UNSIGNED | NO   | PRI |                   | AUTO_INCREMENT | Unique Identifier             |
| [account_id](#accountid)         | INT         | UNSIGNED | NO   |     |                   |                | Account ID                    |
| [character_guid](#characterguid) | INT         | UNSIGNED | NO   |     |                   |                | Character Guid                |
| [type](#type)                    | TINYINT     | UNSIGNED | NO   |     |                   |                |                               |
| [ip](#ip)                        | VARCHAR(15) |          | NO   |     | 127.0.0.1         |                |                               |
| [systemnote](#systemnote)        | TEXT        |          | YES  |     | NULL              |                | Notes inserted by system      |
| [unixtime](#unixtime)            | INT         | UNSIGNED | NO   |     |                   |                | Unixtime                      |
| [time](#time)                    | TIMESTAMP   |          | NO   |     | CURRENT_TIMESTAMP |                | Timestamp                     |
| [comment](#comment)              | TEXT        |          | YES  |     | NULL              |                | Allows users to add a comment |

**Description of the table's fields**

### id

The unique ID of the entry.

### account\_id

The account. See [account.id](account#id).

### character\_guid

GUID of the character, 0 for account actions. See [characters.guid](characters#guid).

### type

| Value | Action                     |
| ----- | -------------------------- |
| 0     | Account login              |
| 1     | Failed account login       |
| 2     | Password change            |
| 3     | Failed password change     |
| 4     | Email change               |
| 5     | Failed email change        |
| 7     | Character created          |
| 8     | Character login            |
| 9     | Character logout           |
| 10    | Character deleted          |
| 11    | Failed character delete    |
| 12    | Unknown action             |

### ip

IP the action came from.

### systemnote

Note added by the core, for example the account and character names.

### unixtime

The time of the action, in Unix time.

### time

The time of the action.

### comment

A comment that can be added by hand. Not used by the core.
