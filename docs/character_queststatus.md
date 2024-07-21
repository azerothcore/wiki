# character\_queststatus

[<-Back-to:Characters](database-characters)

**The \`character\_queststatus\` table**

Holds information on the quest status of each character.

**Table Structure**

| Field             | Type     | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------------- | -------- | ---------- | --- | ---- | ------- |------ | ------------------------ |
| [guid][1]         | INT      | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [quest][2]        | INT      | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier         |
| [status][3]       | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                          |
| [explored][4]     | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                          |
| [timer][5]        | INT      | UNSIGNED   |     | NO   | 0       |       |                          |
| [mobcount1][6]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [mobcount2][7]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [mobcount3][8]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [mobcount4][9]    | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount1][10]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount2][11]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount3][12]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount4][13]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount5][14]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [itemcount6][15]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [playercount][16] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #quest
[3]: #status
[4]: #explored
[5]: #timer
[6]: #mobcount
[7]: #mobcount
[8]: #mobcount
[9]: #mobcount
[10]: #itemcount
[11]: #itemcount
[12]: #itemcount
[13]: #itemcount
[14]: #itemcount
[15]: #itemcount
[16]: #playercount

**Description of the fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### quest

The quest ID. See [quest\_template.entry](quest_template#entry).

### status

The current quest status.

**Possible values**

| Value | Status                     | Comments                                    |
| ----- | -------------------------- | ------------------------------------------- |
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

### mobcount

Current count of the number of kills or casts on the first creature or gameobject, if any. Corresponds with quest\_template.

### itemcount

Current item count for the first item in a delivery quest, if any. Corresponds with quest\_template.

### playercount

Current player slay count. Required in quest\_template.
