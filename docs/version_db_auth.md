# version_db_auth

[<-Back-to:Auth](database-auth.md)

**The \`version_db_auth\` table**

| Field              | Type         | Attributes | Key | Null | Default | Extra | Comment |
|--------------------|--------------|------------|-----|------|---------|-------|---------|
| [sql_rev][1]       | VARCHAR(100) |            | PRI | NO   |         |       |         |
| [required_rev][2]  | VARCHAR(100) |            | MUL | YES  |         |       |         |
| [date][3]          | VARCHAR(50)  |            |     | YES  |         |       |         |
| [2021_06_17_00][4] | BIT(1)       |            |     | YES  |         |       |         |

[1]: #sql_rev
[2]: #required_rev
[3]: #date
[4]: #2021_06_17_00

**Description of the fields**

### sql_rev

SQL review.

### required_rev

### date 

Sql revisions date.

### 2021_06_17_00

The date of the last update to the auth database.

**Note** this column changes automatically according to the last update of the auth database.

