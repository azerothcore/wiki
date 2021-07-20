# version\_db\_auth

[<-Back-to:Auth](database-auth.md)

Read in: [English :gb:](version_db_auth) [Spanish :es:](es/version_db_auth)

**The \`version\_db\_auth\` table**

| Field              | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [sql_rev][1]       | VARCHAR(100) | SIGNED     | PRI | NO   |         |       |         |
| [required_rev][2]  | VARCHAR(100) | SIGNED     | MUL | YES  |         |       |         |
| [date][3]          | VARCHAR(50)  | SIGNED     |     | YES  |         |       |         |
| [2021_06_17_00][4] | BIT(1)       | SIGNED     |     | YES  |         |       |         |

[1]: #sqlrev
[2]: #requiredrev
[3]: #date
[4]: #2021061700

**Description of the fields**

### sql\_rev

SQL review.

### required\_rev

### date 

Sql revisions date.

### 2021\_06\_17\_00

The date of the last update to the auth database.

**Note** this column changes automatically according to the last update of the auth database.
