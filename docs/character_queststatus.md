# character\_queststatus

[<-Back-to:Characters](database-characters.md)

**The \`character\_queststatus\` table**

Holds information on the quest status of each character.

**Structure**

| Field             | Type        | Attributes | Key | Null | Default | Extra | Comment                  |
|-------------------|-------------|------------|-----|------|---------|-------|--------------------------|
| [guid][1]         | int(10)     | unsigned   | PRI | NO   |         |       | Global Unique Identifier |
| [quest][2]        | int(10)     | unsigned   | PRI | NO   |         |       | Quest Identifier         |
| [status][3]       | tinyint(3)  | unsigned   |     | NO   |         |       |                          |
| [explored][4]     | tinyint(3)  | unsigned   |     | NO   |         |       |                          |
| [timer][5]        | int(10)     | unsigned   |     | NO   |         |       |                          |
| [mobcount1][6]    | smallint(5) | unsigned   |     | NO   |         |       |                          |
| [mobcount2][7]    | smallint(5) | unsigned   |     | NO   |         |       |                          |
| [mobcount3][8]    | smallint(5) | unsigned   |     | NO   |         |       |                          |
| [mobcount4][9]    | smallint(5) | unsigned   |     | NO   |         |       |                          |
| [itemcount1][10]  | smallint(5) | unsigned   |     | NO   |         |       |                          |
| [itemcount2][11]  | smallint(5) | unsigned   |     | NO   |         |       |                          |
| [itemcount3][12]  | smallint(5) | unsigned   |     | NO   |         |       |                          |
| [itemcount4][13]  | smallint(5) | unsigned   |     | NO   |         |       |                          |
| [itemcount5][14]  | smallint(5) | unsigned   |     | NO   |         |       |                          |
| [itemcount6][15]  | smallint(5) | unsigned   |     | NO   |         |       |                          |
| [playercount][16] | smallint(5) | unsigned   |     | NO   |         |       |                          |

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
