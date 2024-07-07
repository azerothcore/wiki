# guild\_bank\_right

[<-Back-to:Characters](database-characters)

**The \`guild\_bank\_right\` table**

This table hold informations regarding the right guild member have to withdraw, deposit etc at the guild bank.

**Table Structure**

| Field           | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guildid][1]    | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TabId][2]      | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [rid][3]        | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [gbright][4]    | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [SlotPerDay][5] | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guildid
[2]: #tabid
[3]: #rid
[4]: #gbright
[5]: #slotperday

**Description of the fields**

### guildid

The ID of the guild.

### TabId

The ID of the Tab you are setting the permissions for.

### rid

The rank you are setting the permissions for.

### gbright

The permissions you want to give to a player of that rank on the tab. This is a bitmask. To combine permissions, you must do the OR operation sum the flags.

FLAGS:

| Value | Description                                    |
| ----- | ---------------------------------------------- |
| 1     | view items                                     |
| 2     | deposit items                                  |
| 4     | update item name shown when navigating the tab |
| 8     | withdraw items                                 |
| 255   | Has all rights                                 |

### SlotPerDay

The number of items that a player can withdraw per day (if permissions give him the right to withdraw items).
