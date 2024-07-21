# dungeon\_access\_requirements

[<-Back-to:World](database-world)

**The \`dungeon\_access\_requirements\` table**

**Table Structure**

| Field                  | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [dungeon_access_id][1] | TINYINT      | UNSIGNED   | PRI | NO   |         |       |         |
| [requirement_type][2]  | TINYINT      | UNSIGNED   | PRI | NO   |         |       |         |
| [requirement_id][3]    | MEDIUMINT    | UNSIGNED   | PRI | NO   |         |       |         |
| [requirement_note][4]  | VARCHAR(255) |            |     | YES  | NULL    |       |         |
| [faction][5]           | TINYINT      | UNSIGNED   |     | NO   | 2       |       |         |
| [priority][6]          | TINYINT      | UNSIGNED   |     | YES  | NULL    |       |         |
| [leader_only][7]       | TINYINT      | SIGNED     |     | NO   | 0       |       |         |
| [comment][8]           | VARCHAR(255) |            |     | YES  | NULL    |       |         |

[1]: #dungeon_access_id
[2]: #requirement_type
[3]: #requirement_id
[4]: #requirement_note
[5]: #faction
[6]: #priority
[7]: #leader_only
[8]: #comment

**Description of the fields**

### dungeon_access_id

ID from [dungeon_access_template.id](dungeon_access_template#id).

### requirement_type

| Value | Type        | Comment                         |
| :---- | :---------- | :------------------------------ |
| 0     | Achievement |                                 |
| 1     | Quest       |                                 |
| 2     | Item        | The item cannot be in the bank. |

### requirement_id

ID for Achievement, Quest or Item depending on chosen [requirement_type][2].

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
