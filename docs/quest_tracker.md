# quest\_tracker

[<-Back-to:Characters](database-characters)

**The \`quest\_tracker\` table**

**Table: quest\_tracker's Structure**

| Field                    | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------ | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]                  | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [character_guid][2]      | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| [quest_accept_time][3]   | DATETIME     | SIGNED     |     | NO   |         |       |         |
| [quest_complete_time][4] | DATETIME     | SIGNED     |     | YES  |         |       |         |
| [quest_abandon_time][5]  | DATETIME     | SIGNED     |     | YES  |         |       |         |
| [completed_by_gm][6]     | TINYINT      | SIGNED     |     | NO   | 0       |       |         |
| [core_hash][7]           | VARCHAR(120) | SIGNED     |     | NO   | 0       |       |         |
| [core_revision][8]       | VARCHAR(120) | SIGNED     |     | NO   | 0       |       |         |

[1]: #id
[2]: #characterguid
[3]: #questaccepttime
[4]: #questcompletetime
[5]: #questabandontime
[6]: #completedbygm
[7]: #corehash
[8]: #corerevision

**Description of the table's fields**

### id

The quest. See [quest\_template.ID](quest_template#id).

### character\_guid

See [characters.guid](characters#guid).

### quest\_accept\_time

When the quest was accepted.

### quest\_complete\_time

When the quest was completed.

### quest\_abandon\_time

When the quest was abandoned.

### completed\_by\_gm

1 if the quest was completed with the `.quest complete` GM command.

### core\_hash

The commit hash of the core when the quest was accepted.

### core\_revision

The revision of the core when the quest was accepted.
