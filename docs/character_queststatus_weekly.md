# character\_queststatus\_weekly

[<-Back-to:Characters](database-characters.md)

**The \`character\_queststatus\_weekly\` table**

Holds information on the weekly quest status of every player. The timers reset at the same time the Raids reset.

**Structure**

| Field      | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
|------------|---------|------------|-----|------|---------|-------|--------------------------|
| [guid][1]  | INT(10) | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [quest][2] | INT(10) | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier         |

[1]: #guid
[2]: #quest

**Description of the fields**

### guid

The guid of the character.

### quest

The id of the quest.
