# channels\_bans

[<-Back-to:Characters](database-characters)

**The \`channels\_bans\` table**

**Table Structure**

| Field           | Type  | Attributes | Key | Null | Default | Extra  | Comment |
| --------------- | ----- | ---------- | --- | ---- | ------- | ------ | ------- |
| [channelId][1]  | INT   | UNSIGNED   | PRI | NO   |         |        |         |
| [playerGUID][2] | INT   | UNSIGNED   | PRI | NO   |         |        |         |
| [banTime][3]    | INT   | UNSIGNED   |     | NO   |         |        |         |

[1]: #channelid
[2]: #playerguid
[3]: #banTime

**Description of the fields**

### channelId

The [channel.id](channels#channelid).

### playerGUID

`field-no-description|2`

### banTime

The ban time of de [channel](channels#channelId).
