# quest_tracker

[<-Back-to:Character](database-character.md)

**The \`quest_tracker\` table**

**Structure**

| Field | Type | Attribute | Key | Null | Default | Extra | Comment
|:--- | :--- | :--- | :--- | :--- | :--- | :--- | :---
|[id][1] | MEDIUMINT | UNSIGNED | | NO | 0
|[character_guid][2] | INT | UNSIGNED | | NO | 0
|[quest_accept_time][3] | DATETIME | | | NO
|[quest_complete_time][4] | DATETIME | | | YES | NULL
|[quest_abandon_time][5] | DATETIME | | | YES | NULL
|[completed_by_gm][6] | TINYINT | SIGNED | | NO | 0
|[core_hash][7] | VARCHAR(120) | | | NO | 0
|[core_revision][8] | VARCHAR(120) | | | NO | 0

[1]: #id
[2]: #character_guid
[3]: #quest_accept_time
[4]: #quest_complete_time
[5]: #quest_abandon_time
[6]: #completed_by_gm
[7]: #core_hash
[8]: #core_revision

### id

`field-no-description|1`

### character_guid

[characters.guid](characters#guid).

### quest_accept_time

When the quest was accepted.

### quest_complete_time

When the quest was completed.

### quest_abandon_time

When the quest was abandoned.

### completed_by_gm

`field-no-description|6`

### core_hash

`field-no-description|7`

### core_revision

`field-no-description|8`
