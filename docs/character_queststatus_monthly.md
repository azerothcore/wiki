# character\_queststatus\_monthly

[<-Back-to:Characters](database-characters)

**The \`character\_queststatus\_monthly\` table**

**Table Structure**

| Field       | Type | Attributes | Key | Null | Default | Extra  | Comment                  |
| ----------- | ---- | ---------- | --- | ---- | ------- | ------ | ------------------------ |
| [guid][1]   | INT  | UNSIGNED   | PRI | NO   | 0       |        | Global Unique Identifier |
| [quest][2]  | INT  | UNSIGNED   | PRI | NO   | 0       |        | Quest Identifier         |

[1]: #guid
[2]: #quest

**Description of the fields**

### guid

The character guid. See [characters.guid](characters#guid).

### quest

The quest ID of the rewarded quest. See [quest\_template.id](quest_template#id).
