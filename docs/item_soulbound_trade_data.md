# item\_soulbound\_trade\_data

[<-Back-to:Characters](database-characters.md)

**The \`item\_soulbound\_trade\_data**

This table stores information about which players can trade soulbound items between each other.

**Structure**

| Field              | Type    | Attributes | Key | Null | Default | Extra  | Comment                                                                 |
|--------------------|---------|------------|-----|------|---------|--------|-------------------------------------------------------------------------|
| [itemGuid][1]      | INT(10) | UNSIGNED   | PRI | NO   |         | Unique | Item GUID                                                               |
| [alowedplayers][2] | text    | SIGNED     | PRI | NO   |         |        | Space separated GUID list of players who can receive this item in trade |

[1]: #itemguid
[2]: #alowedplayers

**Description of the fields**

### itemGuid

The GUID of the item that can be traded. See item\_instance.guid.

### alowedplayers

GUIDs of players eligible for the trade separated by space. See characters.guid.
