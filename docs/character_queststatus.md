# character\_queststatus

[<-Back-to:Characters](database-characters.md)

**The \`character\_queststatus\` table**

Holds information on the quest status of each character.

**Structure**

| Field             | Type        | Attributes | Key | Null | Default | Extra | Comment                  |
|-------------------|-------------|------------|-----|------|---------|-------|--------------------------|
| [guid][1]         | INT     | UNSIGNED   | PRI | NO   |         |       | Global Unique Identifier |
| [quest][2]        | INT     | UNSIGNED   | PRI | NO   |         |       | Quest Identifier         |
| [status][3]       | TINYINT  | UNSIGNED   |     | NO   |         |       |                          |
| [explored][4]     | TINYINT  | UNSIGNED   |     | NO   |         |       |                          |
| [timer][5]        | INT     | UNSIGNED   |     | NO   |         |       |                          |
| [mobcount1][6]    | SMALLINT | UNSIGNED   |     | NO   |         |       |                          |
| [mobcount2][7]    | SMALLINT | UNSIGNED   |     | NO   |         |       |                          |
| [mobcount3][8]    | SMALLINT | UNSIGNED   |     | NO   |         |       |                          |
| [mobcount4][9]    | SMALLINT | UNSIGNED   |     | NO   |         |       |                          |
| [itemcount1][10]  | SMALLINT | UNSIGNED   |     | NO   |         |       |                          |
| [itemcount2][11]  | SMALLINT | UNSIGNED   |     | NO   |         |       |                          |
| [itemcount3][12]  | SMALLINT | UNSIGNED   |     | NO   |         |       |                          |
| [itemcount4][13]  | SMALLINT | UNSIGNED   |     | NO   |         |       |                          |
| [itemcount5][14]  | SMALLINT | UNSIGNED   |     | NO   |         |       |                          |
| [itemcount6][15]  | SMALLINT | UNSIGNED   |     | NO   |         |       |                          |
| [playercount][16] | SMALLINT | UNSIGNED   |     | NO   |         |       |                          |

[1]: #guid
[2]: #quest
[3]: #status
[4]: #explored
[5]: #timer
[6]: #mobcount1
[7]: #mobcount2
[8]: #mobcount3
[9]: #mobcount4
[10]: #itemcount1
[11]: #itemcount2
[12]: #itemcount3
[13]: #itemcount4
[14]: #itemcount5
[15]: #itemcount6
[16]: #playercount

**Description of the fields**

### guid

The GUID of the character. See characters.guid

### quest

The quest ID. See quest\_template.entry

### status

The current quest status.

**Possible values**

| Value | Status                     | Comments                                    |
|-------|----------------------------|---------------------------------------------|
| 0     | QUEST\_STATUS\_NONE        | Quest isn't shown in quest list; default    |
| 1     | QUEST\_STATUS\_COMPLETE    | Quest has been completed                    |
| 2     | QUEST\_STATUS\_UNAVAILABLE | NOT USED                                    |
| 3     | QUEST\_STATUS\_INCOMPLETE  | Quest is active in quest log but incomplete |
| 4     | QUEST\_STATUS\_AVAILABLE   | NOT USED                                    |
| 5     | QUEST\_STATUS\_FAILED      | Player failed to complete the quest         |

### explored

Boolean 1 or 0 representing if the character has explored what was needed to explore for the quest.

### timer

`field-no-description|5`

### mobcount1-4

Current count of the number of kills or casts on the first creature or gameobject, if any. Corresponds with quest\_template.ReqCreatureOrGOCount

### itemcount1-6

Current item count for the first item in a delivery quest, if any. Corresponds with quest\_template.ReqItemCount

### playercount

Current player slay count. Required in quest\_template.PlayersSlain
