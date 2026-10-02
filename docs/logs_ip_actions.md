# logs\_ip\_actions

[<-Back-to:Auth](database-auth)

**The \`logs\_ip\_actions\` table**

**Table: logs\_ip\_actions's Structure**

| Field               | Type        | Attributes | Key | Null | Default           | Extra          | Comment                       |
| ------------------- | ----------- | ---------- | --- | ---- | ----------------- | -------------- | ----------------------------- |
| [id][1]             | INT         | UNSIGNED   | PRI | NO   |                   | AUTO_INCREMENT | Unique Identifier             |
| [account_id][2]     | INT         | UNSIGNED   |     | NO   |                   |                | Account ID                    |
| [character_guid][3] | INT         | UNSIGNED   |     | NO   |                   |                | Character Guid                |
| [type][4]           | TINYINT     | UNSIGNED   |     | NO   |                   |                |                               |
| [ip][5]             | VARCHAR(15) |            |     | NO   | 127.0.0.1         |                |                               |
| [systemnote][6]     | TEXT        |            |     | YES  | NULL              |                | Notes inserted by system      |
| [unixtime][7]       | INT         | UNSIGNED   |     | NO   |                   |                | Unixtime                      |
| [time][8]           | TIMESTAMP   |            |     | NO   | CURRENT_TIMESTAMP |                | Timestamp                     |
| [comment][9]        | TEXT        |            |     | YES  | NULL              |                | Allows users to add a comment |

[1]: #id
[2]: #accountid
[3]: #characterguid
[4]: #type
[5]: #ip
[6]: #systemnote
[7]: #unixtime
[8]: #time
[9]: #comment

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
