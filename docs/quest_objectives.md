# quest\_objectives

[<-Back-to:World](database-world)

Table: quest\_objectives

This table provides answer for a very important question. What do I need to do in order to finish a quest?

**Table Structure**

| Field                  | Type      | Attributes | Null | Key | Default | Comment |
| ---------------------- | --------- | ---------- | ---- | --- | ------- | ------- |
| [ID][1]                | MEDIUMINT | UNSIGNED   | NO   | PRI | 0       |         |
| [QuestID][2]           | MEDIUMINT | UNSIGNED   | NO   |     | 0       |         |
| [Type][3]              | TINYINT   | UNSIGNED   | NO   |     | 0       |         |
| [StorageIndex][4]      | TINYINT   | SIGNED     | NO   |     | 0       |         |
| [ObjectID][5]          | INT       | SIGNED     | NO   |     | 0       |         |
| [Amount][6]            | INT       | SIGNED     | NO   |     | 0       |         |
| [Flags][7]             | INT       | UNSIGNED   | NO   |     | 0       |         |
| [Flags2][8]            | INT       | UNSIGNED   | NO   |     | 0       |         |
| [ProgressBarWeight][9] | FLOAT     |            | NO   |     | 0       |         |
| [Description][10]      | text      |            | YES  |     | NULL    |         |
| [VerifiedBuild][11]    | SMALLINT  | SIGNED     | NO   |     | 0       |         |

[1]: #id
[2]: #questid
[3]: #type
[4]: #storageindex
[5]: #objectid
[6]: #amount
[7]: #flags
[8]: #flags2
[9]: #progressbarweight
[10]: #description
[11]: #verifiedbuild

**Description of the fields**

### ID

Unique ObjectiveId

### QuestID

The Quest Id from quest\_template.id

### Type

| Type                                   | ID  | ObjectID                  |
| -------------------------------------- | --- | ------------------------- |
| QUEST_OBJECTIVE_MONSTER                | 0   | creature_template.entry   |
| QUEST_OBJECTIVE_ITEM                   | 1   | itemID from Item.db2      |
| QUEST_OBJECTIVE_GAMEOBJECT             | 2   | gameobject_template.entry |
| QUEST_OBJECTIVE_TALKTO                 | 3   | creature_template.entry   |
| QUEST_OBJECTIVE_CURRENCY               | 4   |                           |
| QUEST_OBJECTIVE_LEARNSPELL             | 5   | SpellId Spell.db2         |
| QUEST_OBJECTIVE_MIN_REPUTATION         | 6   | Faction                   |
| QUEST_OBJECTIVE_MAX_REPUTATION         | 7   | Faction                   |
| QUEST_OBJECTIVE_MONEY                  | 8   | Money                     |
| QUEST_OBJECTIVE_PLAYERKILLS            | 9   |                           |
| QUEST_OBJECTIVE_AREATRIGGER            | 10  |                           |
| QUEST_OBJECTIVE_WINPETBATTLEAGAINSTNPC | 11  |                           |
| QUEST_OBJECTIVE_DEFEATBATTLEPET        | 12  |                           |
| QUEST_OBJECTIVE_WINPVPPETBATTLES       | 13  |                           |
| QUEST_OBJECTIVE_CRITERIA_TREE          | 14  |                           |
| QUEST_OBJECTIVE_PROGRESS_BAR           | 15  |                           |
| QUEST_OBJECTIVE_HAVE_CURRENCY          | 16  |                           |
| QUEST_OBJECTIVE_OBTAIN_CURRENCY        | 17  |                           |

### StorageIndex

### ObjectID

See above

### Amount

Displays how much players you need to kill before completing the quest.

### Flags

This flag field defines more specifically the type of objective it is.

| Flag | Name                                                           | Description                                                                                                     |
| ---- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 0    | QUEST\_OBJECTIVE\_FLAG\_NONE                                   | No flags                                                                                                        |
| 1    | QUEST\_OBJECTIVE\_FLAG\_TRACKED\_ON\_MINIMAP                   | Client displays large yellow blob on minimap for creature/gameobject                                            |
| 2    | QUEST\_OBJECTIVE\_FLAG\_SEQUENCED                              | Client will not see the objective displayed until all previous objectives are completed                         |
| 4    | QUEST\_OBJECTIVE\_FLAG\_OPTIONAL                               | Not required to complete the quest                                                                              |
| 8    | QUEST\_OBJECTIVE\_FLAG\_HIDDEN                                 | Never displayed in quest log                                                                                    |
| 16   | QUEST\_OBJECTIVE\_FLAG\_HIDE\_ITEM\_GAINS                      | Skip showing item objective progress                                                                            |
| 32   | QUEST\_OBJECTIVE\_FLAG\_PROGRESS\_COUNTS\_ITEMS\_IN\_INVENTORY | Item objective progress counts items in inventory instead of reading it from updatefields                       |
| 64   | QUEST\_OBJECTIVE\_FLAG\_PART\_OF\_PROGRESS\_BAR                | Hidden objective used to calculate progress bar percent (quests are limited to a single progress bar objective) |

Like all flag based fields, **QuestObjectiveFlags** can be added for the different types of objective.

### Flags2

### ProgressBarWeight

### Description

### VerifiedBuild
