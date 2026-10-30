# item\_soulbound\_trade\_data

[<-Back-to:Characters](database-characters)

**The \`item\_soulbound\_trade\_data\` table**

This table stores information about which players can trade soulbound items between each other.

**Table: item\_soulbound\_trade\_data's Structure**

| Field                             | Type |          | Null | Key | Default | Extra | Comment                                                                 |
| :-------------------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :---------------------------------------------------------------------- |
| [itemGuid](#itemguid)             | INT  | UNSIGNED | NO   | PRI |         |       | Item GUID                                                               |
| [allowedPlayers](#allowedplayers) | TEXT |          | NO   |     |         |       | Space separated GUID list of players who can receive this item in trade |

**Description of the table's fields**

### itemGuid

The GUID of the item that can be traded. See [item\_instance.guid](item_instance#guid).

### allowedPlayers

GUIDs of players eligible for the trade separated by space. See [characters.guid](characters#guid).
