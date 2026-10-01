# quest\_tracker

[<-返回至:Character](database-characters)

**`quest\_tracker` 表**

**表结构**

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

**字段说明**

### id

`field-no-description|1`

### character\_guid

请参阅 [characters.guid](characters#guid)。

### quest\_accept\_time

任务被接受的时间。

### quest\_complete\_time

任务完成的时间。

### quest\_abandon\_time

任务被放弃的时间。

### completed\_by\_gm

`field-no-description|6`

### core\_hash

`field-no-description|7`

### core\_revision

`field-no-description|8`
