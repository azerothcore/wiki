# version_db_auth

[<-Back-to:Auth](database-auth.md)

**The \`version_db_auth\` table**

| Field              | Type         | Attributes | Key | Null | Default | Extra | Comment |
|--------------------|--------------|------------|-----|------|---------|-------|---------|
| [sql_rev][1]       | VARCHAR(100) |            | PRI | NO   |         |       |         |
| [required_rev][2]  | VARCHAR(100) |            | MUL | YES  |         |       |         |
| [date][3]          | VARCHAR(50)  |            |     | YES  |         |       |         |
| [2021_06_17_00][4] | bit(1)       |            |     | YES  |         |       |         |

[1]: #sql_rev
[2]: #required_rev
[3]: #2020_02_07_00
[4]: #2021_06_17_00

**Description of the fields**

### sql_rev

sql review

### required_rev

### date 

sql revisions date

### 2021_06_17_00

the date of the last update to the auth database

### Example

| sql_rev             | required_rev | date          | 2021_06_17_00 |
|---------------------|--------------|---------------|---------------|
| 1554142988374631100 |              |               |               |
| 1579213352894781043 |              |               |               |
| 1620146306002634000 |              | 2021_06_17_00 |               |
