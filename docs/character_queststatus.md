# character\_queststatus

[<-Back-to:Characters](database-characters)

**The \`character\_queststatus\` table**

Holds information on the quest status of each character.

**Table: character\_queststatus's Structure**

| Field                       | Type     |          | Null | Key | Default | Extra | Comment                  |
| :-------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)               | INT      | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [quest](#quest)             | INT      | UNSIGNED | NO   | PRI | 0       |       | Quest Identifier         |
| [status](#status)           | TINYINT  | UNSIGNED | NO   |     | 0       |       |                          |
| [explored](#explored)       | TINYINT  | UNSIGNED | NO   |     | 0       |       |                          |
| [timer](#timer)             | INT      | UNSIGNED | NO   |     | 0       |       |                          |
| [mobcount1](#mobcount)      | SMALLINT | UNSIGNED | NO   |     | 0       |       |                          |
| [mobcount2](#mobcount)      | SMALLINT | UNSIGNED | NO   |     | 0       |       |                          |
| [mobcount3](#mobcount)      | SMALLINT | UNSIGNED | NO   |     | 0       |       |                          |
| [mobcount4](#mobcount)      | SMALLINT | UNSIGNED | NO   |     | 0       |       |                          |
| [itemcount1](#itemcount)    | SMALLINT | UNSIGNED | NO   |     | 0       |       |                          |
| [itemcount2](#itemcount)    | SMALLINT | UNSIGNED | NO   |     | 0       |       |                          |
| [itemcount3](#itemcount)    | SMALLINT | UNSIGNED | NO   |     | 0       |       |                          |
| [itemcount4](#itemcount)    | SMALLINT | UNSIGNED | NO   |     | 0       |       |                          |
| [itemcount5](#itemcount)    | SMALLINT | UNSIGNED | NO   |     | 0       |       |                          |
| [itemcount6](#itemcount)    | SMALLINT | UNSIGNED | NO   |     | 0       |       |                          |
| [playercount](#playercount) | SMALLINT | UNSIGNED | NO   |     | 0       |       |                          |

**Description of the table's fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### quest

The quest ID. See [quest\_template.ID](quest_template#id).

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

The time remaining (in milliseconds) for the timed quest. Used only for quests with a time limit.

### mobcount

Current count of the number of kills or casts on the first creature or gameobject, if any. Corresponds with quest\_template.

### itemcount

Current item count for the first item in a delivery quest, if any. Corresponds with quest\_template.

### playercount

Current player slay count. Required in quest\_template.
