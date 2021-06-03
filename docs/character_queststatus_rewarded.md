# character\_queststatus\_rewarded

[<-Back-to:Characters](database-characters.md)

**The \`character\_queststatus\_rewarded\` table**

This table holds information of **every** rewarded quest to a player.

**Structure**

| Field       | Type       | Attributes | Key | Null | Default | Extra | Comment                  |
|-------------|------------|------------|-----|------|---------|-------|--------------------------|
| [guid][1]   | INT    | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [quest][2]  | INT    | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier         |
| [active][3] | TINYINT | UNSIGNED   |     | NO   | 1       |       |                          |

[1]: #guid
[2]: #quest
[3]: #active

**Description of the fields**

### guid

The character GUID. See characters.guid

### quest

The quest ID of the rewarded quest. See quest\_template.id

### active

`field-no-description`
