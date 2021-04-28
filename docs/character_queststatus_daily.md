# character\_queststatus\_daily

[<-Back-to:Characters](database-characters.md)

**The \`character\_queststatus\_daily\` table**

Holds information on the daily quest status of every player. The quest must have type = 87 or the 4096 flag at QuestFlags.

**Structure**

| Field      | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
|------------|---------|------------|-----|------|---------|-------|--------------------------|
| [guid][1]  | INT(10) | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [quest][2] | INT(10) | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier         |
| [time][3]  | INT(10) | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #quest
[3]: #time

**Description of the fields**

### guid

The character GUID. See characters.guid

### quest

The quest ID of the daily quest. See quest\_template.entry

### time

The time when the quest was taken, in Unix time.
