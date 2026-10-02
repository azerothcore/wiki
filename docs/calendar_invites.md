# calendar\_invites

[<-Back-to:Characters](database-characters)

**The \`calendar\_invites\` table**

Holds the invitations to the events in [calendar_events](calendar_events) and each invited player's response.

**Table: calendar\_invites's Structure**

| Field           | Type         | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]         | BIGINT       | UNSIGNED   | PRI | NO   | 0       |       |         |
| [event][2]      | BIGINT       | UNSIGNED   |     | NO   | 0       |       |         |
| [invitee][3]    | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| [sender][4]     | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| [status][5]     | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [statustime][6] | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| [rank][7]       | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [text][8]       | VARCHAR(255) |            |     | NO   | ''      |       |         |

[1]: #id
[2]: #event
[3]: #invitee
[4]: #sender
[5]: #status
[6]: #statustime
[7]: #rank
[8]: #text

**Description of the table's fields**

### id

The unique ID of the invite.

### event

The calendar event the invite is for. See [calendar\_events.id](calendar_events#id).

### invitee

GUID of the invited character. See [characters.guid](characters#guid).

### sender

GUID of the character that sent the invite. See [characters.guid](characters#guid).

### status

| Value | Status        |
| ----- | ------------- |
| 0     | Invited       |
| 1     | Accepted      |
| 2     | Declined      |
| 3     | Confirmed     |
| 4     | Out           |
| 5     | Standby       |
| 6     | Signed up     |
| 7     | Not signed up |
| 8     | Tentative     |
| 9     | Removed       |

### statustime

The time the [status](#status) was last changed, in Unix time.

### rank

| Value | Rank      |
| ----- | --------- |
| 0     | Player    |
| 1     | Moderator |
| 2     | Owner     |

The owner and moderators can invite other characters and change the event.

### text

A note added to the invite.
