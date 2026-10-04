# dungeon\_access\_requirements

[<-Back-to:World](database-world)

**The \`dungeon\_access\_requirements\` table**

Holds the requirements a player must meet to enter a dungeon listed in [dungeon_access_template](dungeon_access_template).

**Table: dungeon\_access\_requirements's Structure**

| Field                                 | Type         |          | Null | Key | Default | Extra | Comment                                                                                                  |
| :------------------------------------ | :----------- | :------- | :--: | :-: | :-----: | :---: | :------------------------------------------------------------------------------------------------------- |
| [dungeon_access_id](#dungeonaccessid) | TINYINT      | UNSIGNED | NO   | PRI |         |       | ID from dungeon_access_template                                                                          |
| [requirement_type](#requirementtype)  | TINYINT      | UNSIGNED | NO   | PRI |         |       | 0 = achiev, 1 = quest, 2 = item                                                                          |
| [requirement_id](#requirementid)      | INT          | UNSIGNED | NO   | PRI |         |       | Achiev/quest/item ID                                                                                     |
| [requirement_note](#requirementnote)  | VARCHAR(255) |          | YES  |     | NULL    |       | Optional msg shown ingame to player if he cannot enter. You can add extra info                           |
| [faction](#faction)                   | TINYINT      | UNSIGNED | NO   |     | 2       |       | 0 = Alliance, 1 = Horde, 2 = Both factions                                                               |
| [priority](#priority)                 | TINYINT      | UNSIGNED | YES  |     | NULL    |       | Priority order for the requirement, sorted by type. 0 is the highest priority                            |
| [leader_only](#leaderonly)            | TINYINT      |          | NO   |     | 0       |       | 0 = check the requirement for the player trying to enter, 1 = check the requirement for the party leader |
| [comment](#comment)                   | VARCHAR(255) |          | YES  |     | NULL    |       |                                                                                                          |

**Description of the table's fields**

### dungeon_access_id

ID from [dungeon_access_template.id](dungeon_access_template#id).

### requirement_type

| Value | Type        | Comment                         |
| :---- | :---------- | :------------------------------ |
| 0     | Achievement |                                 |
| 1     | Quest       |                                 |
| 2     | Item        | The item cannot be in the bank. |

### requirement_id

ID for Achievement, Quest or Item depending on chosen [requirement_type](#requirementtype).

### requirement_note

The text that is shown if you try and enter the instance without meeting the requirements.

### faction

| Value | Comment  |
| :---- | :------- |
| 0     | Alliance |
| 1     | Horde    |
| 2     | Both     |

### priority

Priority order for the requirement, sorted by type. 0 is the highest priority.

### leader_only

0 = Check the requirement for each player trying to enter.

1 = Only check the requirement for the party leader.

### comment

A description of the row. Not used by the core.
