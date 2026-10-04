# calendar\_invites

[<-Back-to:Characters](database-characters)

**The \`calendar\_invites\` table**

Holds the invitations to the events in [calendar_events](calendar_events) and each invited player's response.

**Table: calendar\_invites's Structure**

| Field                     | Type         |          | Null | Key | Default | Extra | Comment |
| :------------------------ | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [id](#id)                 | BIGINT       | UNSIGNED | NO   | PRI | 0       |       |         |
| [event](#event)           | BIGINT       | UNSIGNED | NO   |     | 0       |       |         |
| [invitee](#invitee)       | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [sender](#sender)         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [status](#status)         | TINYINT      | UNSIGNED | NO   |     | 0       |       |         |
| [statustime](#statustime) | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [rank](#rank)             | TINYINT      | UNSIGNED | NO   |     | 0       |       |         |
| [text](#text)             | VARCHAR(255) |          | NO   |     | ''      |       |         |

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
