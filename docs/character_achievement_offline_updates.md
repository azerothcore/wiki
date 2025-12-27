# character_achievement_offline_updates

[<-Back-to:Characters](database-characters)

**The \`character_achievement_offline_updates\` table**

Stores updates to character achievements when the character was offline

**Table Structure**

| Field                       | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid](#guid)               | INT     | UNSIGNED   | IDX | NO   |         |       |         |
| [update_type](#update_type) | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [arg1](#arg1)               | INT     | UNSIGNED   |     | NO   |         |       |         |
| [arg2](#arg2)               | INT     | UNSIGNED   |     | YES  | NULL    |       |         |
| [arg3](#arg3)               | INT     | UNSIGNED   |     | YES  | NULL    |       |         |

**Description of the fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### update_type

Supported types: 1 - COMPLETE_ACHIEVEMENT; 2 - UPDATE_CRITERIA

### arg1

For type 1: achievement ID; for type 2: ACHIEVEMENT_CRITERIA_TYPE

### arg2

For type 2: miscValue1 for updating achievement criteria

### arg3

For type 2: miscValue1 for updating achievement criteria
