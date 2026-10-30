# guild\_bank\_right

[<-Back-to:Characters](database-characters)

**The \`guild\_bank\_right\` table**

This table hold informations regarding the right guild member have to withdraw, deposit etc at the guild bank.

**Table: guild\_bank\_right's Structure**

| Field                     | Type    |          | Null | Key | Default | Extra | Comment |
| :------------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guildid](#guildid)       | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [TabId](#tabid)           | TINYINT | UNSIGNED | NO   | PRI | 0       |       |         |
| [rid](#rid)               | TINYINT | UNSIGNED | NO   | PRI | 0       |       |         |
| [gbright](#gbright)       | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [SlotPerDay](#slotperday) | INT     | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### guildid

The ID of the guild.

### TabId

The ID of the Tab you are setting the permissions for.

### rid

The rank you are setting the permissions for.

### gbright

The permissions you want to give to a player of that rank on the tab. This is a bitmask. To combine permissions, you must do the OR operation sum the flags.

FLAGS:

| Value | Hex    | Flag | Comment                                        |
| :---- | :----: | :--- | :--------------------------------------------- |
| 1     | `0x01` |      | view items                                     |
| 2     | `0x02` |      | deposit items                                  |
| 4     | `0x04` |      | update item name shown when navigating the tab |
| 8     | `0x08` |      | withdraw items                                 |
| 255   | `0xFF` |      | Has all rights                                 |

### SlotPerDay

The number of items that a player can withdraw per day (if permissions give him the right to withdraw items).
