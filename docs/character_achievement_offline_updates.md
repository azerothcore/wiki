# character\_achievement\_offline\_updates

[<-Back-to:Characters](database-characters)

**The \`character\_achievement\_offline\_updates\` table**

Stores updates to character achievements when the character was offline

**Table: character\_achievement\_offline\_updates's Structure**

| Field                      | Type    |          | Null | Key | Default | Extra | Comment                                                           |
| :------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :---------------------------------------------------------------- |
| [guid](#guid)              | INT     | UNSIGNED | NO   | MUL |         |       | Character's GUID                                                  |
| [update_type](#updatetype) | TINYINT | UNSIGNED | NO   |     |         |       | Supported types: 1 - COMPLETE_ACHIEVEMENT; 2 - UPDATE_CRITERIA    |
| [arg1](#arg1)              | INT     | UNSIGNED | NO   |     |         |       | For type 1: achievement ID; for type 2: ACHIEVEMENT_CRITERIA_TYPE |
| [arg2](#arg2)              | INT     | UNSIGNED | YES  |     | NULL    |       | For type 2: miscValue1 for updating achievement criteria          |
| [arg3](#arg3)              | INT     | UNSIGNED | YES  |     | NULL    |       | For type 2: miscValue2 for updating achievement criteria          |

**Description of the table's fields**

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
