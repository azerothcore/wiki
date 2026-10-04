# quest\_tracker

[<-Back-to:Characters](database-characters)

**The \`quest\_tracker\` table**

Records when characters accept, complete and abandon quests, to help find bugged quests. It is only filled when `Quests.EnableQuestTracker` is enabled in worldserver.conf.

**Table: quest\_tracker's Structure**

| Field                                     | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [id](#id)                                 | INT          | UNSIGNED | NO   | MUL | 0       |       |         |
| [character_guid](#characterguid)          | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [quest_accept_time](#questaccepttime)     | DATETIME     |          | NO   |     |         |       |         |
| [quest_complete_time](#questcompletetime) | DATETIME     |          | YES  |     | NULL    |       |         |
| [quest_abandon_time](#questabandontime)   | DATETIME     |          | YES  |     | NULL    |       |         |
| [completed_by_gm](#completedbygm)         | TINYINT      |          | NO   |     | 0       |       |         |
| [core_hash](#corehash)                    | VARCHAR(120) |          | NO   |     | 0       |       |         |
| [core_revision](#corerevision)            | VARCHAR(120) |          | NO   |     | 0       |       |         |

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
