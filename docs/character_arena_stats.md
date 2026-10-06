# character\_arena\_stats

[<-Back-to:Characters](database-characters)

**The \`character\_arena\_stats\` table**

This table holds information about character's matchmaker rating in all team types.

**Table: character\_arena\_stats's Structure**

| Field                                 | Type     |          | Null | Key | Default | Extra | Comment |
| :------------------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid)                         | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [slot](#slot)                         | TINYINT  | UNSIGNED | NO   | PRI | 0       |       |         |
| [matchMakerRating](#matchmakerrating) | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |
| [maxMMR](#maxmmr)                     | SMALLINT |          | NO   |     |         |       |         |

**Description of the table's fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### slot

Arena slot index:

| Value | Description |
| ----- | ----------- |
| 0     | 2v2         |
| 1     | 3v3         |
| 2     | 5v5         |

### matchMakerRating

Player's matchmaker rating.

### maxMMR

The maximum matchmaker rating (MMR) this character has reached in this arena slot.
