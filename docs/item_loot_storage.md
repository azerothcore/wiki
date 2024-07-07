# item\_loot_\storage

[<-Back-to:Characters](database-characters)

**The \`item\_loot_\storage\` table**

**Table Structure**

| Field                   | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [containerGUID][1]      | INT     | UNSIGNED   |     | NO   |         |       |         |
| [itemid][2]             | INT     | UNSIGNED   |     | NO   |         |       |         |
| [count][3]              | INT     | UNSIGNED   |     | NO   |         |       |         |
| [randomPropertyId][4]   | INT     | SIGNED     |     | NO   |         |       |         |
| [randomSuffix][5]       | INT     | UNSIGNED   |     | NO   |         |       |         |
| [follow_loot_rules][6]  | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [freeforall][7]         | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [is_blocked][8]         | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [is_counted][9]         | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [is_underthreshold][10] | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [needs_quest][11]       | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [conditionLootId][12]   | INT     | SIGNED     |     | NO   | 0       |       |         |

[1]: #containerguid
[2]: #itemid
[3]: #count
[4]: #randompropertyid
[5]: #randomsuffix
[6]: #followlootrules
[7]: #freeforall
[8]: #isblocked
[9]: #iscounted
[10]: #isunderthreshold
[11]: #needsquest
[12]: #conditionlootid

**Description of the fields**

### containerGUID

`field-no-description|1`

### itemid

`field-no-description|2`

### count

`field-no-description|3`

### randomPropertyId

`field-no-description|4`

### randomSuffix

`field-no-description|5`

### follow\_loot\_rules

`field-no-description|6`

### freeforall

`field-no-description|7`

### is\_blocked

`field-no-description|8`

### is\_counted

`field-no-description|9`

### is\_underthreshold

`field-no-description|10`

### needs\_quest

`field-no-description|11`

### conditionLootId

`field-no-description|12`
