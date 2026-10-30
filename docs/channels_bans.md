# channels\_bans

[<-Back-to:Characters](database-characters)

**The \`channels\_bans\` table**

Holds the players banned from chat channels, with the time each ban expires. The core removes expired bans.

**Table: channels\_bans's Structure**

| Field                     | Type |          | Null | Key | Default | Extra | Comment |
| :------------------------ | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [channelId](#channelid)   | INT  | UNSIGNED | NO   | PRI |         |       |         |
| [playerGUID](#playerguid) | INT  | UNSIGNED | NO   | PRI |         |       |         |
| [banTime](#bantime)       | INT  | UNSIGNED | NO   |     |         |       |         |

**Description of the table's fields**

### channelId

The [channel.id](channels#channelid).

### playerGUID

The GUID of the banned player. See [characters.guid](characters#guid).

### banTime

The ban time of de [channel](channels#channelid).
