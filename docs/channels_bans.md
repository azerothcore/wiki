# channels\_bans

[<-Back-to:Characters](database-characters.md)

**The \`channels\_bans\` table**

## Structure

| Field           | Type  | Attributes | Key | Null | Default | Extra  | Comment |
| --------------- | ----- | ---------- | --- | ---- | ------- | ------ | ------- |
| [channelId][1]  | INT   | UNSIGNED   | PRI | NO   |         |        |         |
| [playerGUID][2] | INT   | UNSIGNED   | PRI | NO   |         |        |         |
| [banTime][3]    | INT   | UNSIGNED   |     | NO   |         |        |         |

[1]: #channelId
[2]: #playerGUID
[3]: #banTime

**Description of the fields**

### channelId

The [channel id](channels#channelId).

### playerGUID

`field-no-description|2`

### banTime

The ban time of de [channel](channels#channelId).
