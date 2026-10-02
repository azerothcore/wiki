# item\_soulbound\_trade\_data

[<-Back-to:Characters](database-characters)

**The \`item\_soulbound\_trade\_data\` table**

This table stores information about which players can trade soulbound items between each other.

**Table: item\_soulbound\_trade\_data's Structure**

| Field               | Type | Attributes | Key | Null | Default | Extra | Comment                                                                 |
| ------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ----------------------------------------------------------------------- |
| [itemGuid][1]       | INT  | UNSIGNED   | PRI | NO   |         |       | Item GUID                                                               |
| [allowedPlayers][2] | TEXT |            |     | NO   |         |       | Space separated GUID list of players who can receive this item in trade |

[1]: #itemguid
[2]: #allowedplayers

**Description of the table's fields**

### itemGuid

The GUID of the item that can be traded. See [item\_instance.guid](item_instance#guid).

### allowedPlayers

GUIDs of players eligible for the trade separated by space. See [characters.guid](characters#guid).
